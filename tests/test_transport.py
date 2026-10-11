"""Verify credential boundaries for trusted metadata and public Release ZIP transport."""
import io
import os
import unittest
from unittest.mock import Mock, patch
import urllib.request

from marketplace import _GitHubApiRedirect, fetch_github


class TransportTests(unittest.TestCase):
    """Check observable outgoing headers and redirect decisions without real credentials."""

    def response(self, url, payload):
        """Provide a bounded response at the HTTP boundary, preserving its final public URL."""
        response = io.BytesIO(payload)
        response.url = url
        return response

    def test_readonly_token_authenticates_metadata(self):
        """Metadata avoids the unauthenticated API limit while preserving JSON decoding."""
        url = "https://api.github.com/repos/author/plugin"
        opener = Mock()
        opener.open.return_value = self.response(url, b'{"private":false}')
        with patch.dict(os.environ, {"GH_TOKEN": "test-readonly-token"}), \
                patch("marketplace.urllib.request.build_opener", return_value=opener):
            self.assertEqual(fetch_github(url), {"private": False})
        request = opener.open.call_args.args[0]
        self.assertEqual(request.get_header("Authorization"), "Bearer test-readonly-token")

    def test_public_assets_and_lookalike_origins_never_receive_token(self):
        """Release downloads remain unauthenticated, including redirectable asset requests."""
        urls = ["https://github.com/author/plugin/releases/download/v1/plugin.zip",
                "https://api.github.com.example/plugin.zip"]
        with patch.dict(os.environ, {"GH_TOKEN": "test-readonly-token"}):
            for url in urls:
                with self.subTest(url=url), patch("marketplace.urllib.request.urlopen") as open_request:
                    open_request.return_value = self.response("https://release-assets.githubusercontent.com/file", b"zip")
                    self.assertEqual(fetch_github(url), b"zip")
                    self.assertIsNone(open_request.call_args.args[0].get_header("Authorization"))

    def test_metadata_without_token_remains_public(self):
        """Local validation does not require account credentials."""
        url = "https://api.github.com/repos/author/plugin"
        opener = Mock()
        opener.open.return_value = self.response(url, b"{}")
        with patch.dict(os.environ, {}, clear=True), \
                patch("marketplace.urllib.request.build_opener", return_value=opener):
            self.assertEqual(fetch_github(url), {})
        self.assertIsNone(opener.open.call_args.args[0].get_header("Authorization"))

    def test_authenticated_redirects_reject_new_origins_and_downgrades(self):
        """Reject credential forwarding before a foreign, userinfo, or HTTP destination is contacted."""
        request = urllib.request.Request("https://api.github.com/repos/old/plugin",
                                         headers={"Authorization": "Bearer test-readonly-token"})
        redirect = _GitHubApiRedirect()
        for target in ["https://example.com/file", "http://api.github.com/repos/new/plugin",
                       "https://api.github.com.example/file", "https://user@api.github.com/file"]:
            with self.subTest(target=target), self.assertRaisesRegex(ValueError, "trusted origin"):
                redirect.redirect_request(request, None, 301, "Moved", {}, target)
        moved = redirect.redirect_request(request, None, 301, "Moved", {},
                                           "https://api.github.com/repos/new/plugin")
        self.assertEqual(moved.get_header("Authorization"), "Bearer test-readonly-token")
