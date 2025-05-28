# BlueSky Followers Utility

A command-line utility to retrieve and display followers of a BlueSky user with timeline information.

## Features

- Get followers for any BlueSky user using just their username
- Display when each follower joined BlueSky
- Show follower profiles with handle, display name, and description
- Sort followers chronologically by join date
- Beautiful table output with Rich formatting
- No authentication required (uses public API)

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

```bash
# Using uv (recommended)
uv run python bluesky_followers.py <username> [limit]

# Or if you have activated the virtual environment
python bluesky_followers.py <username> [limit]
```

### Examples

```bash
# Get followers for a user (default limit: 100)
uv run python bluesky_followers.py jack

# Get followers with custom limit
uv run python bluesky_followers.py jack.bsky.social 50

# The script automatically adds .bsky.social if not present
uv run python bluesky_followers.py someuser
```

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

### v1.0.0 (Current)
- Initial release
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

## Future Features

Additional functionality planned for future versions:
- Export to CSV/JSON
- Follow/unfollow tracking
- Follower analytics
- Batch user processing
- Interactive mode

## License

MIT License - see LICENSE file for details.