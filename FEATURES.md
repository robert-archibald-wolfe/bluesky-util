# BlueSky Followers Utility: Feature List

## Last updated: 2025-06-30

## Implemented Features

### Core Functionality

- **BlueSkyClient**: General-purpose client for BlueSky API operations
  - `get_user_profile`: Fetch a user's profile information
- **BlueSkyFollowers**: Follower-specific operations
  - Fetch followers for a given user
  - Load, process, and validate follower data
  - Data migration and cleaning utilities
- **Command-Line Interface (CLI)**
  - Run follower operations from the command line
  - Arguments for fetching, cleaning, and validating data
  - Version and help output
- **Data Validation & Cleaning**
  - Scripts for cleaning follower data
  - Validation scripts for data integrity
- **Testing & Debugging**
  - Test scripts for import, migration, and core functionality
  - Debugging utilities
- **Documentation & Examples**
  - Sphinx-based documentation (API reference, changelog, migration guide, usage examples)
  - Example scripts for library usage
- **Backward Compatibility**
  - All follower-related features from previous versions remain available

## Planned / Not Yet Implemented Features

- **Automated Testing Suite**
  - Full pytest-based test coverage and CI integration
- **Error Handling Improvements**
  - More robust error messages and exception management
- **Async API Support**
  - Asynchronous methods for improved performance
- **Rate Limiting & Retry Logic**
  - Automatic handling of API rate limits and retries
- **OAuth & Advanced Authentication**
  - Support for OAuth and other authentication flows
- **Export/Import Utilities**
  - Tools for exporting and importing follower data in various formats (CSV, JSON, etc.)
- **Web UI / Dashboard**
  - Optional web-based dashboard for managing and visualizing followers
- **PyPI Release Automation**
  - Automated packaging and publishing to PyPI
- **Configuration File Support**
  - Use of config files for CLI and library settings
- **Extensive Logging**
  - Configurable logging for debugging and monitoring
- **API Rate Usage Reporting**
  - Tools to report and visualize API usage and limits

---

If you want to update this list or add/remove features, just let me know!
