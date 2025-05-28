#!/usr/bin/env python3
"""
Example: Using BlueSky Utility as a Library

This example shows how to use the BlueSky utility library
programmatically in your own applications.
"""

from bluesky_util import BlueSkyFollowers
import json


def example_basic_usage():
    """Basic example of getting follower data."""
    print("=== Basic Library Usage Example ===")
    
    # Initialize the client
    client = BlueSkyFollowers()
    
    # Get follower data for a user (using fully qualified username)
    data = client.get_followers_data("jack.bsky.social", limit=5)
    
    if data["success"]:
        target = data["target_user"]
        followers = data["followers"]
        
        print(f"\nTarget User: {target['display_name']} (@{target['handle']})")
        print(f"Joined: {target['joined_date']}")
        print(f"Followers: {target['follower_count']}, Following: {target['following_count']}")
        
        print(f"\nFirst {len(followers)} followers:")
        for i, follower in enumerate(followers, 1):
            print(f"{i}. @{follower['handle']} - joined {follower['joined_date']}")
    else:
        print(f"Error: {data['error']}")


def example_data_export():
    """Example of exporting data to JSON."""
    print("\n=== Data Export Example ===")
    
    client = BlueSkyFollowers()
    data = client.get_followers_data("jack.bsky.social", limit=10)
    
    if data["success"]:
        # Export to JSON
        with open("followers_data.json", "w") as f:
            json.dump(data, f, indent=2)
        print("✓ Exported follower data to followers_data.json")
        
        # Show summary statistics
        followers = data["followers"]
        join_years = {}
        
        for follower in followers:
            if follower["joined_date"]:
                year = follower["joined_date"][:4]
                join_years[year] = join_years.get(year, 0) + 1
        
        print("\nJoin date distribution:")
        for year, count in sorted(join_years.items()):
            print(f"  {year}: {count} followers")
    else:
        print(f"Error: {data['error']}")


def example_profile_lookup():
    """Example of getting just profile information."""
    print("\n=== Profile Lookup Example ===")
    
    client = BlueSkyFollowers()
    profile = client.get_user_profile("jack.bsky.social")
    
    if profile:
        print(f"User: {profile.display_name or 'No display name'}")
        print(f"Handle: {profile.handle}")
        print(f"Description: {profile.description or 'No description'}")
        print(f"Followers: {getattr(profile, 'followers_count', 'Unknown')}")
        print(f"Following: {getattr(profile, 'follows_count', 'Unknown')}")
    else:
        print("User not found")


if __name__ == "__main__":
    example_basic_usage()
    example_data_export()
    example_profile_lookup()
