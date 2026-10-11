"""Check public Release-asset counts without treating statistics as install authority."""

import unittest
from unittest.mock import patch
from pathlib import Path
import json
import tempfile
import urllib.error

from market_statistics import build_statistics, main


class StatisticsTests(unittest.TestCase):
    """Use a reviewed catalog and controlled GitHub API replies at the network seam."""

    def setUp(self):
        """Keep unrelated ZIP/source assets out of the reviewed input set."""
        self.catalog = {"schema": 1, "plugins": [
            {"id": "test.notes", "repository": "author/notes", "versions": [
                {"version": "1.0.0", "asset_id": 12,
                 "url": "https://github.com/author/notes/releases/download/v1.0.0/notes.zip"},
                {"version": "1.1.0", "asset_id": 34,
                 "url": "https://github.com/author/notes/releases/download/v1.1.0/notes.zip"},
            ]},
        ]}
        self.replies = {
            "https://api.github.com/repos/author/notes/releases/assets/12":
                {"id": 12, "name": "notes.zip", "state": "uploaded", "download_count": 7,
                 "browser_download_url": self.catalog["plugins"][0]["versions"][0]["url"]},
            "https://api.github.com/repos/author/notes/releases/assets/34":
                {"id": 34, "name": "notes.zip", "state": "uploaded", "download_count": 11,
                 "browser_download_url": self.catalog["plugins"][0]["versions"][1]["url"]},
        }

    def test_only_reviewed_zip_assets_are_summed_with_measurement_time(self):
        """Published totals and per-version counts come from the same API snapshot."""
        result = build_statistics(self.catalog, None, self.replies.__getitem__, "2026-10-11T01:00:00Z")
        self.assertEqual(result["measured_at"], "2026-10-11T01:00:00Z")
        self.assertEqual(result["plugins"][0]["total"], 18)
        self.assertEqual(result["plugins"][0]["versions"],
                         [{"version": "1.0.0", "downloads": 7},
                          {"version": "1.1.0", "downloads": 11}])

    def test_api_failure_preserves_prior_counts_and_timestamp(self):
        """A broken count source must not fabricate a new zero or block catalog publication."""
        previous = build_statistics(self.catalog, None, self.replies.__getitem__, "2026-10-11T01:00:00Z")

        def unavailable(_url):
            raise OSError("GitHub unavailable")

        self.assertEqual(build_statistics(self.catalog, previous, unavailable,
                                          "2026-10-11T07:00:00Z"), previous)
        no_previous = build_statistics(self.catalog, None, unavailable, "2026-10-11T07:00:00Z")
        self.assertIsNone(no_previous["measured_at"])
        self.assertIsNone(no_previous["plugins"][0]["total"])
        self.assertIsNone(no_previous["plugins"][0]["versions"][0]["downloads"])

    def test_mismatched_asset_response_cannot_be_counted(self):
        """An asset ID alone is insufficient if the API points to another ZIP."""
        previous = build_statistics(self.catalog, None, self.replies.__getitem__, "2026-10-11T01:00:00Z")
        self.replies[next(iter(self.replies))]["browser_download_url"] = "https://example.org/other.zip"
        self.assertEqual(build_statistics(self.catalog, previous, self.replies.__getitem__,
                                          "2026-10-11T07:00:00Z"), previous)


    def test_unreadable_previous_snapshot_cannot_publish_unknown_counts(self):
        """The production CLI distinguishes transient baseline failure from a confirmed first deployment."""
        with tempfile.TemporaryDirectory() as folder:
            catalog = Path(folder) / "catalog.json"
            output = Path(folder) / "stats.json"
            catalog.write_text(json.dumps(self.catalog), encoding="utf-8")
            arguments = ["market_statistics.py", "--catalog", str(catalog),
                         "--previous-url", "https://market.example/stats.json", "--output", str(output)]
            with patch("sys.argv", arguments), patch("market_statistics.fetch_json", side_effect=OSError("temporary outage")):
                with self.assertRaisesRegex(RuntimeError, "Cannot retain"):
                    main()
            self.assertFalse(output.exists(), "must not replace previously published measurements")
            missing = urllib.error.HTTPError("https://market.example/stats.json", 404, "not found", {}, None)
            with patch("sys.argv", arguments), patch("market_statistics.fetch_json", side_effect=[missing, OSError("API outage")]):
                main()
            self.assertIsNone(json.loads(output.read_text(encoding="utf-8"))["measured_at"])


if __name__ == "__main__":
    unittest.main()
