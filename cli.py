#!/usr/bin/env python3
"""
BlueSky Followers CLI - v2.1.0
Command line interface for retrieving BlueSky follower data.
Now uses library architecture with separate BlueSkyClient for better reusability.
"""

import argparse
import sys
from rich.console import Console

from bluesky_util import BlueSkyFollowers, __version__


def main():
    """Main CLI function."""
    console = Console()
    
    parser = argparse.ArgumentParser(
        description="Get BlueSky followers for a user",
        epilog="Examples:\n"
               "  python cli.py jack.bsky.social\n"
               "  python cli.py jack.bsky.social --limit 50\n"
               "  python cli.py someone.custom-domain.org --limit 100 --no-description",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('username', 
                       help='BlueSky username (must include domain, e.g., user.bsky.social)')
    parser.add_argument('--limit', '-l', 
                       type=int, 
                       default=100, 
                       help='Maximum number of followers to retrieve (default: 100)')
    parser.add_argument('--no-description', 
                       action='store_true', 
                       help='Hide description column in output')
    parser.add_argument('--version', '-v', 
                       action='version', 
                       version=f'BlueSky Followers Utility v{__version__}\nNow using library architecture for better reusability')
    
    args = parser.parse_args()
    
    console.print(f"[blue]Getting followers for {args.username} (limit: {args.limit})[/blue]")
    
    # Use the library
    followers_client = BlueSkyFollowers()
    
    try:
        success = followers_client.display_followers_table(
            args.username, 
            args.limit, 
            show_description=not args.no_description
        )
        if not success:
            sys.exit(1)
    except KeyboardInterrupt:
        console.print("\n[yellow]Operation cancelled by user[/yellow]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]Unexpected error: {e}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()
