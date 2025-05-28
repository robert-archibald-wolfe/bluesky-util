#!/usr/bin/env python3
"""
BlueSky Followers Utility v1.0.0
Get followers of a BlueSky user and show timeline information.

Features:
- Retrieve followers for any BlueSky user
- Display join dates and profile information  
- Sort chronologically by join date
- Rich table formatting
- No authentication required

Usage:
    python bluesky_followers.py <username> [limit]
    
Examples:
    python bluesky_followers.py jack
    python bluesky_followers.py jack.bsky.social 50
"""

import sys
from datetime import datetime
from atproto import Client
from rich.console import Console
from rich.table import Table

__version__ = "1.0.0"


def format_date(date_string):
    """Format an ISO date string to YYYY-MM-DD"""
    if not date_string:
        return ""
    try:
        dt = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d')
    except Exception:
        return date_string[:10] if len(date_string) >= 10 else date_string


def get_followers(username, limit=100):
    """Get followers for a BlueSky user"""
    console = Console()
    
    # Ensure username has proper format
    if not username.endswith('.bsky.social') and '.' not in username:
        username = f"{username}.bsky.social"
    
    console.print(f"[blue]Fetching followers for: {username}[/blue]")
    
    try:
        # Create client
        client = Client(base_url="https://public.api.bsky.app")
        
        # Get user profile
        profile = client.get_profile(username)
        console.print(f"[green]Found user: {profile.display_name or profile.handle}[/green]")
        
        # Get target user's join date
        target_joined = format_date(getattr(profile, 'created_at', None))
        
        # Get followers
        followers_response = client.get_followers(profile.did, limit=limit)
        followers = followers_response.followers
        
        console.print(f"[green]Found {len(followers)} followers[/green]")
        
        if not followers:
            console.print("[yellow]No followers found[/yellow]")
            return []
        
        # Sort by join date (oldest first)
        followers.sort(key=lambda f: getattr(f, 'created_at', '') or '')
        
        # Create table
        table_title = f"Followers of @{username}"
        if target_joined:
            table_title += f" (joined {target_joined})"
        
        table = Table(title=table_title)
        table.add_column("Handle", style="cyan")
        table.add_column("Display Name", style="magenta")
        table.add_column("Description", style="green", max_width=35)
        table.add_column("Joined BlueSky", style="blue")
        
        # Add rows
        for follower in followers:
            description = (follower.description or "")[:32]
            if len(follower.description or "") > 32:
                description += "..."
            
            joined_date = format_date(getattr(follower, 'created_at', None))
            
            table.add_row(
                follower.handle,
                follower.display_name or "",
                description,
                joined_date
            )
        
        console.print(table)
        return followers
        
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        return []


def main():
    console = Console()
    
    # Handle version flag
    if len(sys.argv) > 1 and sys.argv[1] in ['--version', '-v']:
        console.print(f"[blue]BlueSky Followers Utility v{__version__}[/blue]")
        return
    
    if len(sys.argv) < 2:
        console.print(f"[blue]BlueSky Followers Utility v{__version__}[/blue]")
        console.print("[yellow]Usage: python bluesky_followers.py <username> [limit][/yellow]")
        console.print("[yellow]       python bluesky_followers.py --version[/yellow]")
        console.print("[yellow]Example: python bluesky_followers.py jack[/yellow]")
        console.print("[yellow]Example: python bluesky_followers.py jack.bsky.social 50[/yellow]")
        return
    
    username = sys.argv[1]
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    
    console.print(f"[blue]Getting followers for {username} (limit: {limit})[/blue]")
    followers = get_followers(username, limit)
    
    if followers:
        console.print(f"\n[green]✓ Retrieved {len(followers)} followers[/green]")
    else:
        console.print(f"\n[red]✗ No followers retrieved[/red]")


if __name__ == "__main__":
    main()
