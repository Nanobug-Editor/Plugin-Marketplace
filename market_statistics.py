"""Publish optional GitHub Release download statistics beside the reviewed catalog.

The catalog is the sole source of countable ZIP assets. A failed GitHub statistics
request never changes catalog freshness or replaces a previously measured count.
"""

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sys
import urllib.request
import urllib.error


class StatisticsRedirect(urllib.request.HTTPRedirectHandler):
    """Reject insecure redirects and never forward API credentials to another host."""

    def redirect_request(self, request, response, code, message, headers, new_url):
        """Permit public HTTPS redirects; authenticated API reads must keep their original URL."""
        if not new_url.startswith("https://") or request.has_header("Authorization"):
            raise ValueError("Statistics redirect would escape its credential/source boundary")
        return super().redirect_request(request, response, code, message, headers, new_url)


def unavailable_statistics(catalog):
    """Represent never-measured counts as unavailable, not as zero downloads."""
    return {"schema": 1, "measured_at": None, "plugins": [
        {"id": plugin["id"], "total": None,
         "versions": [{"version": version["version"], "downloads": None}
                      for version in plugin["versions"]]}
        for plugin in catalog["plugins"]]}


def build_statistics(catalog, previous, fetch, measured_at):
    """Sum only reviewed package assets; preserve the last snapshot on any API error.

    `fetch` obtains one GitHub Release-asset JSON document. The function verifies
    both its immutable asset ID and its download URL before accepting its count.
    A complete measurement is atomic so a partial API outage cannot show a mix of
    old and new timestamps under one total.
    """
    fallback = previous if previous and previous.get("schema") == 1 else unavailable_statistics(catalog)
    try:
        plugins = []
        for plugin in catalog["plugins"]:
            versions = []
            for version in plugin["versions"]:
                url = ("https://api.github.com/repos/" + plugin["repository"]
                       + "/releases/assets/" + str(version["asset_id"]))
                asset = fetch(url)
                if (asset["id"] != version["asset_id"] or asset["state"] != "uploaded"
                        or asset["browser_download_url"] != version["url"]
                        or not asset["name"].endswith(".zip")
                        or not isinstance(asset["download_count"], int)
                        or isinstance(asset["download_count"], bool)
                        or not 0 <= asset["download_count"] <= 2**64 - 1):
                    raise ValueError("Release asset does not match reviewed ZIP")
                versions.append({"version": version["version"],
                                 "downloads": asset["download_count"]})
            total = sum(v["downloads"] for v in versions)
            if total > 2**64 - 1:
                raise ValueError("Plugin download total exceeds the public u64 contract")
            plugins.append({"id": plugin["id"], "total": total,
                            "versions": versions})
        return {"schema": 1, "measured_at": measured_at, "plugins": plugins}
    except (KeyError, TypeError, ValueError, OSError) as error:
        # Statistics are advisory; availability never turns a reviewed catalog into a failure.
        print(f"Statistics unavailable; retaining previous measurement: {error}", file=sys.stderr)
        return fallback


def fetch_json(url, token=None):
    """Read bounded HTTPS JSON; credentials go only to the GitHub API endpoint."""
    if not url.startswith("https://"):
        raise ValueError("Statistics source requires HTTPS")
    headers = {"User-Agent": "Nanobug-Plugin-Marketplace",
               "Accept": "application/vnd.github+json"}
    if token and url.startswith("https://api.github.com/"):
        headers["Authorization"] = "Bearer " + token
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.build_opener(StatisticsRedirect()).open(request, timeout=30) as response:
        if not response.url.startswith("https://"):
            raise ValueError("Statistics redirect requires HTTPS")
        body = response.read(1024 * 1024 + 1)
    if len(body) > 1024 * 1024:
        raise ValueError("Statistics response quota exceeded")
    return json.loads(body)


def main():
    """Publish one complete measurement or an explicit/stale unavailable snapshot."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--previous-url")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    catalog = json.loads(args.catalog.read_text(encoding="utf-8"))
    previous = None
    baseline_unavailable = False
    if args.previous_url:
        try:
            previous = fetch_json(args.previous_url)
        except urllib.error.HTTPError as error:
            # Only a confirmed missing resource identifies the first publication.
            baseline_unavailable = error.code != 404
        except (OSError, ValueError):
            baseline_unavailable = True
    at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    result = build_statistics(catalog, previous,
                              lambda url: fetch_json(url, os.environ.get("GH_TOKEN")), at)
    if baseline_unavailable and result["measured_at"] is None:
        # Pages replaces the whole artifact. Abort this deployment rather than erase
        # a measurement we could not retrieve; the existing catalog still serves installs.
        raise RuntimeError("Cannot retain published statistics: previous snapshot and API are unavailable")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
