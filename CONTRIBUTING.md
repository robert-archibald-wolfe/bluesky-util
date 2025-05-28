# Contributing to BlueSky Followers Utility

Thank you for your interest in contributing to the BlueSky Followers Utility! This document provides guidelines for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contributing Guidelines](#contributing-guidelines)
- [Submitting Changes](#submitting-changes)
- [Reporting Issues](#reporting-issues)

## Code of Conduct

This project adheres to a code of conduct that promotes a welcoming and inclusive environment. Please be respectful and professional in all interactions.

## Getting Started

### Prerequisites

- Python 3.13 or higher
- Git
- `uv` package manager (recommended) or `pip`

### Development Setup

1. **Fork and Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/bluesky-util.git
   cd bluesky-util
   ```

2. **Set Up Development Environment**
   ```bash
   # Using uv (recommended)
   uv sync
   
   # Or using pip
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Verify Installation**
   ```bash
   # Test library import
   python -c "from bluesky_util import BlueSkyFollowers; print('Import successful')"
   
   # Test CLI
   python cli.py --version
   ```

## Contributing Guidelines

### Code Style

- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to all public functions and classes
- Keep functions focused and single-purpose
- Use type hints where appropriate

### Example Code Style

```python
def get_followers_data(self, username: str, limit: int = 100) -> Dict[str, Any]:
    """
    Retrieve formatted follower data with metadata.
    
    Args:
        username: Fully qualified BlueSky username (e.g., 'user.bsky.social')
        limit: Maximum number of followers to retrieve
        
    Returns:
        Dictionary containing success status, followers list, and metadata
        
    Raises:
        ValueError: If username doesn't include a domain
    """
    # Implementation here
```

### Testing

Before submitting changes, please test your code:

1. **Manual Testing**
   ```bash
   # Test library functionality
   python test_imports.py
   
   # Test CLI functionality
   python cli.py jack.bsky.social --limit 5
   ```

2. **Username Validation**
   ```bash
   python test_validation.py
   ```

3. **Migration Testing**
   ```bash
   python test_migration.py
   ```

### Documentation

- Update relevant documentation for any changes
- Add examples for new features
- Update API documentation if method signatures change
- Keep the CHANGELOG.md updated

## Submitting Changes

### Pull Request Process

1. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Your Changes**
   - Write clean, well-documented code
   - Follow the existing code style
   - Add tests if applicable
   - Update documentation

3. **Test Your Changes**
   ```bash
   # Run basic tests
   python test_imports.py
   python cli.py --version
   
   # Test with real data (optional, requires internet)
   python cli.py jack.bsky.social --limit 5
   ```

4. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

   Use conventional commit messages:
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation changes
   - `refactor:` for code refactoring
   - `test:` for adding tests

5. **Push and Create Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

### Pull Request Guidelines

- Provide a clear description of the changes
- Reference any related issues
- Include examples of how to use new features
- Ensure all existing functionality still works
- Update documentation if needed

## Reporting Issues

### Bug Reports

When reporting bugs, please include:

1. **Environment Information**
   - Python version
   - Operating system
   - Package versions (`pip list`)

2. **Steps to Reproduce**
   - Exact commands used
   - Expected behavior
   - Actual behavior

3. **Error Messages**
   - Full error traceback
   - Any relevant log output

### Feature Requests

For feature requests:

1. Describe the feature and its use case
2. Explain why it would be valuable
3. Provide examples of how it would be used
4. Consider if it fits the project's scope

### Example Issue Template

```markdown
## Bug Report

**Environment:**
- Python: 3.13
- OS: Windows 11
- atproto: 0.0.61

**Steps to Reproduce:**
1. Run `python cli.py invalid-username`
2. ...

**Expected Behavior:**
Should show helpful error message

**Actual Behavior:**
Shows confusing traceback

**Error Message:**
```
[paste error here]
```

## Development Guidelines

### Project Structure

```
bluesky-util/
├── bluesky_util/          # Main library package
│   ├── __init__.py        # Package exports
│   ├── followers.py       # BlueSkyFollowers class
│   └── utils.py          # Utility functions
├── docs/                  # Documentation
│   ├── API.md            # API documentation
│   ├── EXAMPLES.md       # Usage examples
│   └── TROUBLESHOOTING.md # Common issues
├── examples/             # Example scripts
├── cli.py               # Command-line interface
├── README.md            # Main documentation
├── CHANGELOG.md         # Version history
└── pyproject.toml       # Package configuration
```

### Adding New Features

1. **Library Features**: Add to appropriate module in `bluesky_util/`
2. **CLI Features**: Update `cli.py` with new arguments
3. **Documentation**: Update relevant docs in `docs/`
4. **Examples**: Add usage examples to `docs/EXAMPLES.md`

### Version Management

- Follow semantic versioning (MAJOR.MINOR.PATCH)
- Update version in `pyproject.toml`
- Update `bluesky_util/__init__.py` version
- Add entry to `CHANGELOG.md`

## Questions?

If you have questions about contributing:

1. Check existing issues and documentation
2. Create a new issue with the "question" label
3. Be specific about what you're trying to accomplish

Thank you for contributing to the BlueSky Followers Utility! 🚀
