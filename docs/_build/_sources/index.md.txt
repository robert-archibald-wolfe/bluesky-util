# BlueSky Followers Utility Documentation

Welcome to the BlueSky Followers Utility documentation!

```{toctree}
:maxdepth: 2
:caption: Contents:

getting-started
api-reference
EXAMPLES
migration
contributing
changelog
```

## Quick Start

The BlueSky Followers Utility is a Python library and command-line tool for retrieving and analyzing BlueSky follower data.

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/bluesky-util.git
cd bluesky-util

# Install dependencies
uv sync

# Or install with documentation dependencies
uv sync --extra docs
```

### Basic Usage

#### Library Usage

```python
from bluesky_util import BlueSkyFollowers

# Initialize the client
bf = BlueSkyFollowers()

# Get followers data
data = bf.get_followers_data('jack.bsky.social', limit=50)

if data['success']:
    print(f"Found {len(data['followers'])} followers")
    for follower in data['followers']:
        print(f"@{follower['handle']} - joined {follower['joined_date']}")
```

#### Command Line Usage

```bash
# Get followers for a user
python cli.py jack.bsky.social

# With options
python cli.py jack.bsky.social --limit 50 --no-description
```

## Key Features

- **Library Architecture**: Import and use `BlueSkyFollowers` class in your projects
- **Custom Domain Support**: Full support for BlueSky's custom domains
- **Enhanced CLI**: Modern argparse-based interface
- **Rich Output**: Beautiful table formatting with Rich
- **No Authentication**: Uses public API endpoints

## Indices and tables

- {ref}`genindex`
- {ref}`modindex`
- {ref}`search`
