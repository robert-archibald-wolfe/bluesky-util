"""
BlueSky client functionality - v2.1.0
"""

from typing import Optional, Any
from atproto import Client

from .utils import validate_username


class BlueSkyClient:
    """A general-purpose client for BlueSky social network operations."""
    
    def __init__(self, base_url: str = "https://public.api.bsky.app"):
        """Initialize the BlueSky client."""
        self.client = Client(base_url=base_url)
    
    def get_user_profile(self, username: str) -> Optional[Any]:
        """
        Get a user's profile information.
        
        Args:
            username: Fully qualified BlueSky username (e.g., 'user.bsky.social')
            
        Returns:
            User profile object or None if not found
            
        Raises:
            ValueError: If username format is invalid
        """
        try:
            username = validate_username(username)
            return self.client.get_profile(username)
        except ValueError as e:
            # Username validation error - let it bubble up
            raise e
        except Exception:
            return None
