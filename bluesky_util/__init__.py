"""
BlueSky Utility Library v2.0.0

A Python library for interacting with BlueSky social network data.

Main modules:
- followers: Get and analyze follower data
- following: Get and analyze following data  
- analytics: Generate insights and statistics
- utils: Common utilities and helpers
"""

__version__ = "2.0.0"

from .followers import BlueSkyFollowers
from .utils import format_date, validate_username

__all__ = [
    "BlueSkyFollowers",
    "format_date", 
    "validate_username",
    "__version__"
]
