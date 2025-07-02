# BlueSky Followers Utility — Current Capabilities (as of July 2025)

## Overview

The BlueSky Followers Utility is a Python library and CLI tool for retrieving, analyzing, and exporting follower data from the BlueSky social network. It is designed for both programmatic use (as a library) and direct use via the command line.

---

## Core Features

- **Library Architecture**: Import and use `BlueSkyFollowers` and `BlueSkyClient` classes in your own projects.
- **Custom Domain Support**: Fully supports BlueSky's custom domains (requires fully qualified usernames, e.g., `user.example.com`).
- **Enhanced CLI**: Modern argparse-based interface with flags:
  - `--limit` to control number of results
  - `--no-description` to hide profile descriptions
  - `--version` to show version info
- **Rich Output**: Beautiful table formatting using the Rich library.
- **No Authentication Required**: Uses public BlueSky API endpoints.
- **Structured Data Export**: Methods return structured data for further processing or export.
- **Comprehensive Documentation**: Sphinx-based docs, migration guides, and real-world usage examples.
- **Error Handling**: Specific exception types with detailed error messages and graceful fallback behavior.
- **Type Hints**: Full type annotation support throughout the codebase.

---

## Main Classes

- `BlueSkyClient`: General-purpose client for BlueSky operations (profile lookups, etc.)
- `BlueSkyFollowers`: Inherits from `BlueSkyClient`, adds follower-specific methods (fetch, sort, display, etc.)

---

## CLI Usage

Retrieve followers for a user:

```bash
python cli.py jack.bsky.social --limit 50
```

Show version:

```bash
python cli.py --version
```

---

## Library Usage Example

```python
from bluesky_util import BlueSkyFollowers
bf = BlueSkyFollowers()
data = bf.get_followers_data('jack.bsky.social', limit=50)
```

---

## Current Limitations

- Follower join dates are based on account creation (not actual follow date; API limitation)
- Limited to 100 followers per request (API limitation)
- No pagination or batch processing yet (planned)
- No export to CSV/JSON yet (planned)
- No web interface or interactive mode yet (planned)

---

## Recent Changes (v2.1.0, May 2025)

- Added `BlueSkyClient` for general profile operations
- `BlueSkyFollowers` now inherits from `BlueSkyClient`
- Modularized code for easier extension
- Enhanced examples and documentation

---

## Planned/Roadmap Features

- Batch user processing
- Export formats (CSV, JSON)
- Following/followers relationship analysis
- Rate limiting and retry logic
- AsyncIO support
- Web interface and dashboard

---

*This document is auto-generated and should be updated as features are added or changed.*
