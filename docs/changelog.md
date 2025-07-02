# Changelog

All notable changes to the BlueSky Followers Utility will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2025-05-28

### Added (v2.1.0)

- **New `BlueSkyClient` class:** General-purpose client for BlueSky operations
- **Modular Architecture:** Separated general BlueSky functionality from followers-specific functionality
- **Enhanced Examples:** Updated library usage examples to showcase new architecture

### Changed (v2.1.0)

- **Code Organization:** Moved `get_user_profile` method from `BlueSkyFollowers` to the new `BlueSkyClient` class
- **Inheritance:** `BlueSkyFollowers` now inherits from `BlueSkyClient` for better code reuse
- **Library Structure:** Added `bluesky_util.client` module for general BlueSky operations

### Implementation Details

- `BlueSkyClient` provides base functionality for user profile operations
- `BlueSkyFollowers` extends `BlueSkyClient` with follower-specific functionality
- Backward compatibility maintained - all existing `BlueSkyFollowers` methods work unchanged
- New import available: `from bluesky_util import BlueSkyClient`

### Migration from v2.0.0

No breaking changes. Existing code continues to work as before. Optionally:

```python
# NEW: Use BlueSkyClient for general profile operations
from bluesky_util import BlueSkyClient
client = BlueSkyClient()
profile = client.get_user_profile("user.bsky.social")

# EXISTING: BlueSkyFollowers still has all the same methods
from bluesky_util import BlueSkyFollowers
bf = BlueSkyFollowers()
profile = bf.get_user_profile("user.bsky.social")  # Still works via inheritance
```

## [2.0.0] - 2024-12-19

### ⚠️ BREAKING CHANGES

- **Username Validation:** Removed automatic `.bsky.social` suffix addition. All usernames must now be fully qualified (e.g., `jack.bsky.social` instead of `jack`).
- **API Changes:** Converted from script-based to library-based architecture with class-based interface.
- **CLI Interface:** New command-line interface with different argument structure.

### Added (v2.0.0)

- **Library Architecture:** Converted to importable Python library with `BlueSkyFollowers` class
- **Custom Domain Support:** Full support for BlueSky custom domains (e.g., `user.custom-domain.com`)
- **Enhanced CLI:** New `cli.py` with argparse-based interface
  - `--limit` flag to control number of results
  - `--no-description` flag to hide descriptions  
  - `--version` flag to show version information
- **Comprehensive Documentation:**
  - Sphinx documentation setup with RTD theme
  - Migration guide from v1.0.0 to v2.0.0
  - API reference documentation
  - Comprehensive examples and usage patterns
- **Better Error Handling:** Specific exception types with detailed error messages
- **Type Hints:** Full type annotation support throughout the codebase
- **Examples:** Updated examples demonstrating library and CLI usage patterns

### Changed (v2.0.0)

- **Username Validation:** `validate_username()` now requires fully qualified usernames and raises `ValueError` for invalid formats
- **Project Structure:** Reorganized into proper Python package structure with `bluesky_util/` directory
- **Dependencies:** Updated `pyproject.toml` with proper library configuration and optional dependency groups
- **Version Management:** Semantic versioning with proper Git tagging (v2.0.0, v2.0.0-release)

### Removed

- **Automatic Domain Addition:** No longer automatically appends `.bsky.social` to usernames
- **Direct Script Execution:** Replaced with library import and separate CLI interface
- **Legacy CLI Arguments:** Old positional argument structure replaced with flag-based interface

### Fixed

- **Domain Flexibility:** Now properly supports any BlueSky domain, not just `.bsky.social`
- **Error Messages:** More descriptive error messages for invalid usernames and API failures
- **Code Organization:** Better separation of concerns with modular architecture

### Technical Details

- **Package Structure:**

  ```text
  bluesky_util/
  ├── __init__.py      # Library exports and version
  ├── followers.py     # BlueSkyFollowers class
  └── utils.py         # Utility functions
  ```

- **API Changes:**

  ```python
  # v1.0.0 (OLD)
  # Direct script execution only
  
  # v2.0.0 (NEW)
  from bluesky_util import BlueSkyFollowers
  bf = BlueSkyFollowers()
  data = bf.get_followers_data('jack.bsky.social', limit=50)
  ```

- **CLI Changes:**

  ```bash
  # v1.0.0 (OLD)
  python bluesky_followers.py jack 50
  
  # v2.0.0 (NEW)  
  python cli.py jack.bsky.social --limit 50
  ```

### Migration Notes

- **Backup Available:** Original v1.0.0 script preserved as `bluesky_followers_v1.0.0.py`
- **Breaking Change Impact:** All existing code using the utility must be updated to use fully qualified usernames
- **Migration Guide:** Comprehensive migration documentation available in `docs/migration.md`

### Documentation

- **Sphinx Setup:** Professional documentation generation with Read the Docs theme
- **API Reference:** Complete API documentation with examples
- **Migration Guide:** Step-by-step migration instructions from v1.0.0
- **Contributing Guide:** Guidelines for contributors and development setup
- **Examples:** Comprehensive usage examples for both library and CLI interfaces

---

## [1.0.0] - 2024-12-18

### Added

- **Initial Release:** Basic BlueSky followers retrieval functionality
- **Core Features:**
  - Retrieve followers for any BlueSky user
  - Beautiful tabular display with Rich library
  - Configurable follower limits
  - Basic error handling
- **Username Handling:** Automatic `.bsky.social` suffix addition for convenience
- **CLI Interface:** Simple positional arguments (username, limit)
- **Dependencies:**
  - `requests` for API communication
  - `rich` for beautiful terminal output
  - `python-dotenv` for environment configuration

### Technical Implementation

- **Single Script:** Monolithic `bluesky_followers.py` script
- **Direct Execution:** `python bluesky_followers.py username limit`
- **API Integration:** BlueSky AT Protocol API integration
- **Output Format:** Rich table with follower handle, display name, and description

### Known Limitations

- **Domain Limitation:** Only supported `.bsky.social` usernames
- **Script-Only:** No library import capability  
- **Basic Error Handling:** Limited error recovery and reporting
- **No Custom Domains:** Couldn't handle BlueSky custom domains

---

## [0.2.0] - 2025-06-30

### Changed

- Reset versioning to 0.2.0 for pre-release development status.

## Development Notes

### Versioning Strategy

- **Major (X.0.0):** Breaking changes, significant architecture changes
- **Minor (x.Y.0):** New features, backward compatible additions  
- **Patch (x.y.Z):** Bug fixes, documentation updates, minor improvements

### Release Channels

- **Stable:** Tagged releases (v2.0.0, v1.0.0)
- **Development:** Main branch with latest changes
- **Feature Branches:** Individual feature development

### Contribution Guidelines

All changes should:

1. Follow semantic versioning principles
2. Include appropriate tests when possible
3. Update documentation for user-facing changes
4. Include changelog entries
5. Use conventional commit messages

### Future Roadmap

Planned for future releases:

- **v2.1.0 (Minor):**
  - Enhanced filtering and sorting options
  - Batch processing for multiple users
  - Export formats (CSV, JSON)
  - Performance optimizations

- **v2.2.0 (Minor):**
  - Following/followers relationship analysis
  - User profile information retrieval
  - Rate limiting and retry logic improvements

- **v3.0.0 (Major):**
  - AsyncIO support for better performance
  - Plugin architecture for extensibility
  - REST API server mode
  - Advanced analytics and insights

### Support Policy

- **Current Release (2.0.0):** Full support with bug fixes and security updates
- **Previous Release (1.0.0):** Security updates only, deprecated features
- **Pre-1.0.0:** No longer supported

---

*For detailed technical information about each release, see the [API Reference](api-reference.md) and [Migration Guide](migration.md).*
