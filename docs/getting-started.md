# Getting Started

## Installation

### Prerequisites

- Python 3.13 or higher
- Git (for cloning the repository)

### Installing the Package

#### Option 1: Clone and Install with uv (Recommended)

```bash
# Clone the repository
git clone https://github.com/your-username/bluesky-util.git
cd bluesky-util

# Install dependencies with uv
uv sync

# Install with optional documentation dependencies
uv sync --extra docs

# Install with development dependencies
uv sync --extra dev
```

#### Option 2: Install with pip

```bash
# Clone the repository
git clone https://github.com/your-username/bluesky-util.git
cd bluesky-util

# Install dependencies
pip install -r requirements.txt

# Install with documentation dependencies
pip install -e ".[docs]"
```

## Quick Start Guide

### 1. Basic CLI Usage

The simplest way to get started is using the command-line interface:

```bash
# Get followers for a BlueSky user
python cli.py jack.bsky.social

# Get a limited number of followers
python cli.py jack.bsky.social --limit 25

# Hide description column for cleaner output
python cli.py jack.bsky.social --no-description

# Get help
python cli.py --help
```

### 2. Library Usage

For programmatic access, import the BlueSkyFollowers class:

```python
from bluesky_util import BlueSkyFollowers

# Initialize the client
bf = BlueSkyFollowers()

# Get structured follower data
data = bf.get_followers_data('jack.bsky.social', limit=50)

if data['success']:
    print(f"Target user: {data['target_user']['display_name']}")
    print(f"Found {len(data['followers'])} followers")
    
    # Process followers
    for follower in data['followers']:
        print(f"  @{follower['handle']} - joined {follower['joined_date']}")
else:
    print(f"Error: {data['error']}")
```

### 3. Display Options

You can display followers in a formatted table:

```python
# Display in a Rich table (default: show descriptions)
bf.display_followers_table('jack.bsky.social', limit=25)

# Hide descriptions for cleaner output
bf.display_followers_table('jack.bsky.social', limit=25, show_description=False)
```

## Username Requirements (v2.0.0)

**Important**: BlueSky now supports custom domains, so you must provide fully qualified usernames:

- ✅ **Correct**: `jack.bsky.social`, `user.example.com`, `someone.custom-domain.org`
- ❌ **Incorrect**: `jack`, `user`, `someone`

This is a breaking change from v1.0.0 where `.bsky.social` was automatically appended.

## Configuration

### API Endpoint

By default, the library uses BlueSky's public API endpoint (`https://public.api.bsky.app`). You can customize this:

```python
# Use a different API endpoint
bf = BlueSkyFollowers(base_url="https://custom.api.endpoint")
```

### Rate Limiting

The library handles rate limiting gracefully, but for large requests, consider:

- Using smaller batch sizes (`limit` parameter)
- Adding delays between requests in your own code
- Monitoring API response times

## Troubleshooting

### Common Issues

1. **"Username must include a domain" error**
   - Make sure to use fully qualified usernames (e.g., `user.bsky.social`)

2. **"User not found" error**
   - Verify the username is correct and the user exists
   - Check that the domain is correct (`.bsky.social` vs custom domain)

3. **Import errors**
   - Ensure you're in the correct virtual environment
   - Run `uv sync` or `pip install -r requirements.txt`

### Getting Help

- Check the [Examples](examples.md) page for more usage patterns
- Review the [API Reference](api-reference.md) for detailed method documentation
- See [Migration Guide](migration.md) if upgrading from v1.0.0

## Next Steps

- Explore the [API Reference](api-reference.md) for detailed method documentation
- Check out [Examples](examples.md) for more usage patterns
- Learn about [Contributing](contributing.md) if you want to help improve the project
