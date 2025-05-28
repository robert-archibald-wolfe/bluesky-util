# Contributing to BlueSky Followers Utility

Thank you for your interest in contributing to the BlueSky Followers Utility! This guide will help you get started.

## Table of Contents

1. [Development Setup](#development-setup)
2. [Project Structure](#project-structure)
3. [Making Changes](#making-changes)
4. [Testing](#testing)
5. [Documentation](#documentation)
6. [Submitting Changes](#submitting-changes)
7. [Code Style](#code-style)
8. [Release Process](#release-process)

## Development Setup

### Prerequisites

- Python 3.9 or higher
- Git
- uv (recommended) or pip

### Initial Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/bluesky-util.git
   cd bluesky-util
   ```

2. **Create Virtual Environment**
   ```bash
   # Using uv (recommended)
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   
   # Or using Python venv
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   # Install all dependencies including dev tools
   uv sync --extra dev --extra docs
   
   # Or with pip
   pip install -e ".[dev,docs]"
   ```

4. **Verify Installation**
   ```bash
   # Test library import
   python -c "from bluesky_util import BlueSkyFollowers; print('✓ Library import works')"
   
   # Test CLI
   python cli.py --version
   
   # Test docs build
   cd docs && sphinx-build -b html . _build
   ```

## Project Structure

```
bluesky-util/
├── bluesky_util/           # Main library package
│   ├── __init__.py         # Package initialization and exports
│   ├── followers.py        # BlueSkyFollowers class
│   └── utils.py            # Utility functions
├── docs/                   # Sphinx documentation
│   ├── conf.py             # Sphinx configuration
│   ├── *.md                # Documentation files
│   └── _build/             # Built documentation (generated)
├── examples/               # Usage examples
│   └── library_usage.py    # Library usage examples
├── tests/                  # Test files (create as needed)
├── cli.py                  # Command-line interface
├── pyproject.toml          # Project configuration
├── README.md               # Main project readme
└── MIGRATION_COMPLETE.md   # Migration documentation
```

## Making Changes

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-description
```

### 2. Types of Contributions

**Bug Fixes:**
- Fix existing functionality
- Add tests to prevent regression
- Update documentation if needed

**New Features:**
- Add new functionality to the library
- Include comprehensive tests
- Update documentation and examples
- Ensure backward compatibility when possible

**Documentation:**
- Improve existing docs
- Add new examples
- Fix typos or unclear instructions

**Performance:**
- Optimize existing code
- Add benchmarks to verify improvements
- Document performance changes

### 3. Development Workflow

```bash
# Make your changes
# Test your changes
python cli.py jack.bsky.social --limit 5

# Run tests (when available)
python -m pytest tests/

# Build documentation
cd docs && sphinx-build -b html . _build

# Check your changes
git status
git diff
```

## Testing

### Manual Testing

Test core functionality:

```bash
# Test username validation
python -c "
from bluesky_util import validate_username
try:
    validate_username('jack')
    print('❌ Should have failed')
except ValueError:
    print('✓ Validation works')

validate_username('jack.bsky.social')
print('✓ Valid username accepted')
"

# Test library usage
python -c "
from bluesky_util import BlueSkyFollowers
bf = BlueSkyFollowers()
print('✓ Library import and instantiation works')
"

# Test CLI
python cli.py --version
python cli.py jack.bsky.social --limit 5 --no-description
```

### Unit Tests (Future)

When adding tests, use pytest:

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_followers.py

# Run with coverage
python -m pytest --cov=bluesky_util
```

### Integration Testing

Test with real BlueSky API:

```bash
# Test with real account (use a test account)
python cli.py test.bsky.social --limit 3
```

## Documentation

### Building Documentation

```bash
cd docs
sphinx-build -b html . _build
```

### Adding Documentation

1. **API Documentation:** Update `docs/api-reference.md`
2. **Examples:** Add to `docs/EXAMPLES.md`
3. **Migration Info:** Update `docs/migration.md`

### Documentation Style

- Use clear, concise language
- Include code examples for all features
- Add screenshots when helpful
- Keep examples up-to-date with current API

## Submitting Changes

### 1. Commit Guidelines

Use conventional commit format:

```bash
# Features
git commit -m "feat: add support for custom timeout settings"

# Bug fixes
git commit -m "fix: handle rate limiting correctly"

# Documentation
git commit -m "docs: update migration guide with new examples"

# Breaking changes
git commit -m "feat!: require fully qualified usernames"
```

### 2. Push and Create PR

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub with:
- Clear description of changes
- Link to any related issues
- Screenshots if UI changes
- Testing notes

### 3. PR Review Process

1. Automated checks will run
2. Maintainer review
3. Address feedback
4. Merge after approval

## Code Style

### Python Style Guide

- Follow PEP 8
- Use type hints where appropriate
- Write docstrings for all public functions
- Keep functions focused and small
- Use meaningful variable names

### Example Code Style

```python
def get_followers_data(
    self, 
    username: str, 
    limit: int = 100
) -> Dict[str, Any]:
    """
    Retrieve followers data for a BlueSky user.
    
    Args:
        username: Fully qualified BlueSky username (e.g., 'user.bsky.social')
        limit: Maximum number of followers to retrieve (default: 100)
        
    Returns:
        Dictionary containing success status, followers list, and metadata
        
    Raises:
        ValueError: If username format is invalid
        ConnectionError: If API request fails
    """
    validate_username(username)
    # ... implementation
```

### Documentation Style

- Use Markdown format
- Include code examples
- Keep line length reasonable
- Use proper headings hierarchy

## Release Process

### Version Management

We use semantic versioning (MAJOR.MINOR.PATCH):

- **MAJOR:** Breaking changes
- **MINOR:** New features, backward compatible
- **PATCH:** Bug fixes, backward compatible

### Creating a Release

1. **Update Version**
   ```bash
   # Update version in pyproject.toml
   version = "2.1.0"
   ```

2. **Update Changelog**
   - Document all changes
   - Follow Keep a Changelog format

3. **Create Tag**
   ```bash
   git tag -a v2.1.0 -m "Release v2.1.0: Add custom timeout support"
   git push origin v2.1.0
   ```

4. **Build and Test**
   ```bash
   # Test build
   python -m build
   
   # Test installation
   pip install dist/bluesky_util-2.1.0-py3-none-any.whl
   ```

## Getting Help

- **Questions:** Open a GitHub Discussion
- **Bugs:** Open a GitHub Issue
- **Chat:** Join our community channel (if available)

## Recognition

Contributors will be:
- Listed in the project's contributors section
- Mentioned in release notes for significant contributions
- Given appropriate credit in documentation

Thank you for contributing to BlueSky Followers Utility! 🎉
