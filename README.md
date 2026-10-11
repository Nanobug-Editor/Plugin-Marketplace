# Nanobug Plugin Marketplace

[简体中文](README.zh-CN.md)

The official registry and delivery project for Nanobug plugins.

Tickets 01–04 are implemented and verified: reviewed native installation, version history and safe upgrades, seven independently released official plugins, and unbundled Windows delivery. The [ticket index](docs/tickets/README.md) links the delivery records and actual GitHub states; the [final Windows record](docs/verification/04-unbundled-delivery-2026-10-11.md) states the tested scope and remaining platform limitations.

## Scope

- An in-editor marketplace for discovery, downloads, download counts, version history and compatible-version installation.
- Public, open-source plugins submitted through reviewed pull requests.
- Static registry data on GitHub Pages; plugin ZIPs on each author's GitHub Releases.
- Seven independently maintained official plugins; no bundled plugins in the final editor distribution.
- No separate marketplace website, ratings, payments, private plugin sources or extra backend.

## Documentation

- [Documentation index](docs/README.md)
- [Execution specification](docs/specs/plugin-marketplace.md)
- [Four tickets and testing plan](docs/tickets/README.md)
- [Publication records](docs/tickets/publication.json)
- [Agent instructions](AGENTS.md)

The Nanobug editor implements the native UI and installation runtime. Individual plugin repositories own plugin source and release assets. This repository owns registry data, review and publication workflows, statistics, and this project's planning records.

## Build and contribute

Python 3.11+ is sufficient for the catalog builder and its tests:

```powershell
# Validate registry invariants using deterministic ZIP and GitHub fixtures.
python -m unittest discover -s tests -v
# Build an empty catalog, or add --validator <inspect_package.exe> for registered plugins.
python marketplace.py --output dist
# Measure only reviewed Release ZIP assets; retain prior counts during an API outage.
python market_statistics.py --catalog dist/catalog.json --previous-url https://t-miracle.github.io/Nanobug-Plugin-Marketplace/stats.json --output dist/stats.json
```

Submit a [registry record](registry/README.md) through a pull request. Every version requires human review. Ownership transfers use a [separate review](transfers/README.md). PR validation uses the trusted base builder and a pinned Nanobug `Package` validator; it never runs guest code. Build that validator from the revision in `.github/validator.json` with `cargo build --locked -p plugin-runtime --example inspect_package` in the Nanobug repository.

Actions gives the trusted builder a read-only `GH_TOKEN` for public metadata on `https://api.github.com`. API redirects must stay on that origin; Release ZIP requests never carry this token. Local validation also works without a token, subject to GitHub's unauthenticated API limit.

The `Reviewed catalog` workflow publishes only main-branch data to [catalog.json](https://t-miracle.github.io/Nanobug-Plugin-Marketplace/catalog.json). Pages must use **GitHub Actions** as its source. Only `dist/` is uploaded; there is no separate website. The registry starts empty until a real plugin passes review; controlled test packages are not published.

The native client keeps an inert catalog cache with its last successful fetch time. A failed refresh disables market installations and upgrades until a refresh succeeds. Details never fetch embedded Markdown images or resolve SVG file/network references. Explicit source and feedback controls open the reviewed GitHub repository. First installation requires consent, a matching SHA-256 and manifest, compatibility and workspace trust. Installed plugins can only advance to a newer compatible stable version; new permissions require confirmation. Checks run asynchronously at startup and approximately every six hours, without downloading updates. The title-bar dot remains until no available upgrade remains.

The workflow measures downloads approximately every six hours and publishes [stats.json](https://t-miracle.github.io/Nanobug-Plugin-Marketplace/stats.json) separately from the reviewed catalog. Counts include repeated and outside-market downloads, not installation numbers. API failures retain the last measurement and time; an unmeasured count is unavailable. Statistics failures do not block installation. See the [static data contract](docs/specs/static-data-contract.md).
