"""
BlueSky client functionality - v2.1.0
"""

from typing import Optional, Any
from atproto import Client

from .utils import validate_username

AUTHENTICATED_API_URL = "https://bsky.social/xrpc"

class BlueSkyClient:
    """A general-purpose client for BlueSky social network operations."""
    
    def __init__(self, base_url: str = "https://public.api.bsky.app"):
        """Initialize the BlueSky client."""
        self.base_url = base_url
        self.client = Client(base_url=base_url)
        self.is_authenticated = False
        self.authenticated_user = None
        self.authenticated_at = None
    
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
        
    def get_user_posts(self, username: str, limit: int = 20) -> list:
        """
        Fetch recent posts for a user using the BlueSky API.
        
        Args:
            username: Fully qualified BlueSky username (e.g., 'user.bsky.social')
            limit: Maximum number of posts to retrieve
            
        Returns:
            List of post objects (dicts)
        """
        try:
            username = validate_username(username)
            profile = self.get_user_profile(username)
            if not profile:
                return []
            # The atproto Client has a get_author_feed method for posts
            feed = self.client.get_author_feed(profile.did, limit=limit)
            # Return the list of posts (feed.feed is a list of post objects)
            return [post.to_dict() if hasattr(post, 'to_dict') else dict(post) for post in getattr(feed, 'feed', [])]
        except Exception as e:
            print(f"[ERROR] Failed to fetch posts for {username}: {e}")
            return []

    def login(self, username: str, app_password: str) -> bool:
        """
        Authenticate the client with a Bluesky handle and app password.
        Returns True if successful, False otherwise.
        Automatically switches to the authenticated API endpoint if needed.
        """
        import datetime
        # Switch to authenticated endpoint if not already set
        if self.base_url != AUTHENTICATED_API_URL:
            self.base_url = AUTHENTICATED_API_URL
            self.client = Client(base_url=AUTHENTICATED_API_URL)
        try:
            self.client.login(username, app_password)
            self.is_authenticated = True
            self.authenticated_user = username
            self.authenticated_at = datetime.datetime.now()
            return True
        except Exception as e:
            print(f"[ERROR] Login failed: {e}")
            self.is_authenticated = False
            self.authenticated_user = None
            self.authenticated_at = None
            return False

    @property
    def auth_status(self) -> str:
        """
        Returns a string describing the authentication status, user, and timestamp.
        """
        if self.is_authenticated:
            return f"Authenticated as {self.authenticated_user} at {self.authenticated_at}"
        else:
            return "Not authenticated"

    def get_blocked_accounts(self) -> list:
        """
        Fetch the list of accounts blocked by the authenticated user using a direct HTTP XRPC call.
        Returns a list of dicts with handle and did.
        Raises RuntimeError if not authenticated.
        Enhanced with detailed HTTP error handling.
        """
        if not self.is_authenticated:
            raise RuntimeError("Client is not authenticated. Please log in first.")
        import requests
        try:
            session = getattr(self.client, "_session", None)
            access_jwt = getattr(session, "access_jwt", None)
            if not access_jwt:
                raise RuntimeError("No access token found in client session. Please log in again.")
            headers = {"Authorization": f"Bearer {access_jwt}"}
            url = f"{AUTHENTICATED_API_URL}/app.bsky.graph.getBlocks"
            resp = requests.get(url, headers=headers, params={"limit": 100})
            if resp.status_code == 401:
                print("[ERROR] Unauthorized: Invalid or expired token. Please log in again.")
                return []
            elif resp.status_code == 403:
                print("[ERROR] Forbidden: You do not have permission to access this resource.")
                return []
            elif resp.status_code == 404:
                print("[ERROR] Not Found: The blocklist endpoint does not exist or is unavailable.")
                return []
            elif resp.status_code >= 500:
                print(f"[ERROR] Server error ({resp.status_code}): {resp.reason}")
                return []
            elif resp.status_code != 200:
                print(f"[ERROR] Unexpected HTTP status {resp.status_code}: {resp.reason}")
                return []
            data = resp.json()
            return [
                {"handle": block.get("handle"), "did": block.get("did")}
                for block in data.get("blocks", [])
            ]
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Network or HTTP error: {e}")
            return []
        except Exception as e:
            print(f"[ERROR] Failed to fetch block list: {e}")
            return []
