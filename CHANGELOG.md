# Changelog

All notable changes to the BlueSky Followers Utility will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2024-12-19

### 🚀 Added
- **Library Architecture**: Complete refactor to importable Python library
- **Custom Domain Support**: Full support for BlueSky custom domains
- **Enhanced CLI**: New argparse-based command-line interface with proper option handling
- **Structured Data Export**: Methods return structured data for programmatic use
- **Comprehensive API**: `BlueSkyFollowers` class with multiple methods for different use cases
- **Rich Documentation**: Complete API documentation, examples, and migration guide
- **Error Handling**: Proper exception handling with meaningful error messages
- **Package Distribution**: Configured for PyPI distribution with proper `pyproject.toml`

### 🔄 Changed
- **BREAKING**: `validate_username()` now requires fully qualified usernames (e.g., `user.bsky.social`)
- **BREAKING**: No longer auto-appends `.bsky.social` to usernames
- **BREAKING**: CLI arguments changed to use argparse instead of sys.argv
- **BREAKING**: Function signatures updated for library usage
- **Enhanced**: Better error messages and validation
- **Improved**: Code organization with proper module structure

### 🗑️ Removed
- **BREAKING**: Automatic `.bsky.social` suffix addition
- **BREAKING**: Legacy command-line argument parsing
- **BREAKING**: Global script execution model

### 🔧 Fixed
- Username validation now properly handles custom domains
- Better error handling for network issues
- Improved table formatting edge cases

### 📚 Documentation
- Added comprehensive `README.md` with library usage examples
- Created detailed `docs/API.md` with method signatures and parameters
- Added extensive `docs/EXAMPLES.md` with real-world usage patterns
- Created migration guide for v1.0.0 users
- Added troubleshooting documentation

### 🧹 Technical
- Converted monolithic script to proper Python package structure
- Added proper `__init__.py` with exports
- Implemented proper class-based architecture
- Added comprehensive error handling
- Improved code organization and modularity

## [1.0.0] - 2024-12-18

### 🚀 Added
- Initial release of BlueSky Followers Utility
- Command-line tool to retrieve BlueSky follower information
- Rich table formatting for follower display
- Timeline information showing when followers joined
- Automatic `.bsky.social` domain handling
- Basic error handling and user feedback

### ✨ Features
- Retrieve followers for any public BlueSky user
- Display follower handles, names, and descriptions
- Show join dates in human-readable format
- Sort followers chronologically by join date
- Beautiful table output using Rich library
- No authentication required

---

## Migration Guide v1.0.0 → v2.0.0

### Breaking Changes

1. **Username Format**: Must now use fully qualified usernames
   ```python
   # v1.0.0
   python bluesky_followers.py jack
   
   # v2.0.0
   python cli.py jack.bsky.social
   ```

2. **Library Import**: Now available as importable library
   ```python
   # v2.0.0
   from bluesky_util import BlueSkyFollowers
   bf = BlueSkyFollowers()
   data = bf.get_followers_data('jack.bsky.social')
   ```

3. **CLI Arguments**: New argparse-based CLI
   ```bash
   # v1.0.0
   python bluesky_followers.py username
   
   # v2.0.0
   python cli.py username --limit 50 --no-description
   ```

### Upgrade Steps

1. Update username references to include full domain
2. Update CLI calls to use new argument format
3. Consider migrating to library usage for programmatic access
4. Update any automation scripts to use new CLI syntax

For detailed migration instructions, see the [Migration Guide](README.md#migration-from-v100) in the README.
