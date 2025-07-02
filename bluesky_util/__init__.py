"""
BlueSky Utility Library v2.1.0

A Python library for interacting with BlueSky social network data.

Main modules:
- client: General BlueSky client operations
- followers: Get and analyze follower data
- following: Get and analyze following data  
- analytics: Generate insights and statistics
- utils: Common utilities and helpers
"""

__version__ = "0.2.1"

from .client import BlueSkyClient
from .followers import BlueSkyFollowers
from .utils import format_date, validate_username

__all__ = [
    "BlueSkyClient",
    "BlueSkyFollowers",
    "format_date", 
    "validate_username",
    "__version__"
]
