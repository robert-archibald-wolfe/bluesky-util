# BlueSky Followers Utility v2.0.0

A Python library and command-line utility to retrieve and display followers of a BlueSky user with timeline information. Now with library architecture for better reusability and full custom domain support.

## Features

- **Library Architecture**: Import and use `BlueSkyFollowers` class in your own projects
- **Custom Domain Support**: Full support for BlueSky's custom domains (requires fully qualified usernames)
- **Command-Line Interface**: Enhanced CLI with proper argument parsing
- Display when each follower joined BlueSky
- Show follower profiles with handle, display name, and description
- Sort followers chronologically by join date
- Beautiful table output with Rich formatting
- No authentication required (uses public API)
- Structured data export capabilities

## Installation

1. Clone or download this repository
2. Install dependencies using uv (recommended) or pip:

```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install -r requirements.txt
```

## Usage

### Library Usage (New in v2.0.0)

You can now import and use the BlueSky Followers utility as a library in your own projects:

```python
from bluesky_util import BlueSkyFollowers

# Initialize the client
bf = BlueSkyFollowers()

# Get followers data for a user (returns structured data)
data = bf.get_followers_data('jack.bsky.social', limit=50)

if data['success']:
    print(f"Found {len(data['followers'])} followers for {data['username']}")
    
    # Access follower information
    for follower in data['followers']:
        print(f"@{follower['handle']} - joined {follower['joined_date']}")
    
    # Access target user info
    target = data['target_user']
    print(f"Target user: {target['display_name']} (@{target['handle']})")
    print(f"Followers: {target['follower_count']}, Following: {target['following_count']}")
else:
    print(f"Error: {data['error']}")

# Display followers in a formatted table
bf.display_followers_table('jack.bsky.social', limit=25, show_description=True)

# Get just the raw follower data
followers = bf.get_followers_raw('jack.bsky.social', limit=10)

# Get user profile information
profile = bf.get_user_profile('jack.bsky.social')
```

### Command Line Usage

```bash
# Using the new CLI (v2.0.0)
python cli.py <username> [options]

# Using uv
uv run python cli.py <username> [options]
```

### CLI Examples

```bash
# Get followers for a user (default limit: 100)
python cli.py jack.bsky.social

# Get followers with custom limit
python cli.py jack.bsky.social --limit 50

# Hide description column for cleaner output
python cli.py jack.bsky.social --limit 25 --no-description

# Works with custom domains too
python cli.py user.example.com
python cli.py someone.custom-domain.org --limit 100

# Get help and see all options
python cli.py --help

# Check version
python cli.py --version
```

**⚠️ Breaking Change in v2.0.0:** BlueSky now supports custom domains, so you **must** provide the full username including the domain (e.g., `user.bsky.social` or `user.custom-domain.com`). Usernames without domains (like just `jack`) are no longer accepted.

### Output

The utility displays a formatted table with:
- **Handle**: The follower's BlueSky handle
- **Display Name**: Their chosen display name
- **Description**: Profile bio (truncated to fit)
- **Joined BlueSky**: When they created their account

The table title shows the target user's handle and join date.

## Requirements

- Python 3.13+
- atproto >= 0.0.61
- rich >= 14.0.0

## Version History

### v2.0.0 (Current)

**🎉 Major Release - Library Architecture & Custom Domain Support**

- **Breaking Change**: Now requires fully qualified usernames (e.g., `jack.bsky.social` instead of `jack`)
- **New**: Library architecture - import and use `BlueSkyFollowers` class in your projects
- **New**: Enhanced CLI with argparse (`--limit`, `--no-description`, `--help`, `--version`)
- **New**: Full custom domain support (e.g., `user.example.com`)
- **New**: Structured data export capabilities
- **Improved**: Better error handling and user feedback
- **Improved**: More robust username validation

### v1.0.0

- Initial release
- Basic command-line interface
- Get followers with join date information
- Rich table formatting
- Chronological sorting
- Public API access (no auth required)

## Technical Notes

- Uses BlueSky's public API endpoint
- No authentication required
- The "followed on" date is not available through the public API
- Followers are sorted by their BlueSky join date (oldest first)
- Handles rate limiting gracefully
- Library architecture allows for easy integration into other projects
- Supports both `.bsky.social` and custom domain usernames

## Migration from v1.0.0

If you're upgrading from v1.0.0, please note these breaking changes:

1. **Username Format**: You must now include the full domain
   - ❌ Old: `jack`
   - ✅ New: `jack.bsky.social`

2. **Import Path**: If using as a library
   - ❌ Old: `import bluesky_followers`
   - ✅ New: `from bluesky_util import BlueSkyFollowers`

3. **CLI Interface**: New options available
   - ❌ Old: `python bluesky_followers.py jack 50`
   - ✅ New: `python cli.py jack.bsky.social --limit 50`

## Future Features

Additional functionality planned for future versions:

- Enhanced analytics and reporting
- Follow/unfollow tracking over time
- Batch user processing
- Interactive mode
- Web interface
- Database integration options

## License

MIT License - see LICENSE file for details.