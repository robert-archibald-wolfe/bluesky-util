"""
BlueSky followers functionality - v2.0.0
"""

from typing import List, Optional, Dict, Any
from atproto import Client
from rich.console import Console
from rich.table import Table

from .utils import format_date, validate_username, truncate_text


class BlueSkyFollowers:
    """A class for retrieving and analyzing BlueSky follower data."""
    
    def __init__(self, base_url: str = "https://public.api.bsky.app"):
        """Initialize the BlueSky followers client."""
        self.client = Client(base_url=base_url)
        self.console = Console()
    
    def get_user_profile(self, username: str) -> Optional[Any]:
        """Get a user's profile information."""
        try:
            username = validate_username(username)
            return self.client.get_profile(username)
        except Exception:
            return None
    
    def get_followers_raw(self, username: str, limit: int = 100) -> List[Any]:
        """Get raw follower data for a user."""
        try:
            username = validate_username(username)
            profile = self.client.get_profile(username)
            followers_response = self.client.get_followers(profile.did, limit=limit)
            return followers_response.followers
        except Exception:
            return []
    
    def get_followers_data(self, username: str, limit: int = 100) -> Dict[str, Any]:
        """Get formatted follower data with metadata."""
        username = validate_username(username)
        
        # Get user profile
        profile = self.get_user_profile(username)
        if not profile:
            return {
                "success": False,
                "error": "User not found",
                "username": username,
                "followers": [],
                "metadata": {}
            }
        
        # Get followers
        followers = self.get_followers_raw(username, limit)
        
        # Sort by join date
        followers.sort(key=lambda f: getattr(f, 'created_at', '') or '')
        
        # Format data
        formatted_followers = []
        for follower in followers:
            formatted_followers.append({
                "handle": follower.handle,
                "display_name": follower.display_name or "",
                "description": follower.description or "",
                "description_truncated": truncate_text(follower.description),
                "joined_date": format_date(getattr(follower, 'created_at', None)),
                "joined_date_raw": getattr(follower, 'created_at', None),
                "avatar": getattr(follower, 'avatar', None),
                "did": getattr(follower, 'did', None)
            })
        
        return {
            "success": True,
            "username": username,
            "target_user": {
                "handle": profile.handle,
                "display_name": profile.display_name or "",
                "description": profile.description or "",
                "joined_date": format_date(getattr(profile, 'created_at', None)),
                "joined_date_raw": getattr(profile, 'created_at', None),
                "follower_count": getattr(profile, 'followers_count', 0),
                "following_count": getattr(profile, 'follows_count', 0)
            },
            "followers": formatted_followers,
            "metadata": {
                "total_retrieved": len(followers),
                "limit_requested": limit
            }
        }
    
    def display_followers_table(self, username: str, limit: int = 100, 
                              show_description: bool = True) -> bool:
        """Display followers in a Rich table format."""
        data = self.get_followers_data(username, limit)
        
        if not data["success"]:
            self.console.print(f"[red]Error: {data['error']}[/red]")
            return False
        
        target = data["target_user"]
        followers = data["followers"]
        
        self.console.print(f"[green]Found {len(followers)} followers[/green]")
        
        # Create table
        table_title = f"Followers of @{username}"
        if target["joined_date"]:
            table_title += f" (joined {target['joined_date']})"
        
        table = Table(title=table_title)
        table.add_column("Handle", style="cyan")
        table.add_column("Display Name", style="magenta")
        
        if show_description:
            table.add_column("Description", style="green", max_width=35)
        
        table.add_column("Joined BlueSky", style="blue")
        
        # Add rows
        for follower in followers:
            row_data = [
                follower["handle"],
                follower["display_name"],
            ]
            
            if show_description:
                row_data.append(follower["description_truncated"])
            
            row_data.append(follower["joined_date"])
            table.add_row(*row_data)
        
        self.console.print(table)
        return True
