# API Reference

This page provides detailed documentation for all classes and methods in the BlueSky Followers Utility v2.1.0.

## Core Classes

```{eval-rst}
.. automodule:: bluesky_util
   :members:
   :undoc-members:
   :show-inheritance:
```

## BlueSkyClient Class (New in v2.1.0)

The general-purpose BlueSky client for basic operations.

```{eval-rst}
.. autoclass:: bluesky_util.BlueSkyClient
   :members:
   :undoc-members:
   :show-inheritance:
```

### Constructor

```{eval-rst}
.. automethod:: bluesky_util.BlueSkyClient.__init__
```

### Profile Methods

```{eval-rst}
.. automethod:: bluesky_util.BlueSkyClient.get_user_profile
```

## BlueSkyFollowers Class

Specialized class for follower operations. Inherits from `BlueSkyClient` (v2.1.0+).

```{eval-rst}
.. autoclass:: bluesky_util.BlueSkyFollowers
   :members:
   :undoc-members:
   :show-inheritance:
```

### Constructor

```{eval-rst}
.. automethod:: bluesky_util.BlueSkyFollowers.__init__
```

### Data Retrieval Methods

```{eval-rst}
.. automethod:: bluesky_util.BlueSkyFollowers.get_followers_raw
.. automethod:: bluesky_util.BlueSkyFollowers.get_followers_data
```

**Note:** `get_user_profile` is inherited from `BlueSkyClient` as of v2.1.0.

### Display Methods

```{eval-rst}
.. automethod:: bluesky_util.BlueSkyFollowers.display_followers_table
```

## Utility Functions

```{eval-rst}
.. automodule:: bluesky_util.utils
   :members:
   :undoc-members:
   :show-inheritance:
```

### Username Validation

```{eval-rst}
.. autofunction:: bluesky_util.utils.validate_username
```

### Date and Text Formatting

```{eval-rst}
.. autofunction:: bluesky_util.utils.format_date
.. autofunction:: bluesky_util.utils.truncate_text
```

## Data Structures

### Follower Data Response

The `get_followers_data()` method returns a structured dictionary with the following format:

```python
{
    "success": bool,          # Whether the request was successful
    "username": str,          # The requested username
    "target_user": {          # Information about the target user
        "handle": str,
        "display_name": str,
        "description": str,
        "joined_date": str,
        "joined_date_raw": str,
        "follower_count": int,
        "following_count": int
    },
    "followers": [            # List of follower objects
        {
            "handle": str,
            "display_name": str,
            "description": str,
            "description_truncated": str,
            "joined_date": str,
            "joined_date_raw": str,
            "avatar": str,
            "did": str
        }
    ],
    "metadata": {             # Request metadata
        "total_retrieved": int,
        "limit_requested": int
    }
}
```

### Error Response

When `success` is `False`, the response includes an error message:

```python
{
    "success": False,
    "error": str,             # Description of the error
    "username": str,          # The requested username
    "followers": [],          # Empty list
    "metadata": {}            # Empty metadata
}
```

## Exception Handling

### ValueError

Raised by utility functions for invalid input:

- `validate_username()` raises `ValueError` for usernames without domains
- Other validation functions may raise `ValueError` for invalid input

### Network Exceptions

The library uses the `atproto` library which may raise various network-related exceptions:

- Connection errors
- Timeout errors
- API rate limiting errors

These are generally caught and handled gracefully, returning error responses instead of raising exceptions.

## Type Hints

The library uses Python type hints throughout. Key types:

```python
from typing import List, Optional, Dict, Any

# Common return types
UserProfile = Optional[Any]                    # atproto profile object
FollowerList = List[Any]                      # List of atproto follower objects
FollowerData = Dict[str, Any]                 # Structured response dict
```

## Constants

### Default Values

```python
DEFAULT_BASE_URL = "https://public.api.bsky.app"
DEFAULT_LIMIT = 100
MAX_DESCRIPTION_LENGTH = 35
```

### Date Formats

```python
OUTPUT_DATE_FORMAT = "%Y-%m-%d"              # Used in formatted output
INPUT_DATE_FORMATS = [                       # Accepted input formats
    "%Y-%m-%dT%H:%M:%S.%fZ",
    "%Y-%m-%dT%H:%M:%SZ",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d"
]
```
