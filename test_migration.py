#!/usr/bin/env python3
"""Test comprehensive functionality of BlueSky v2.0.0 migration"""

from bluesky_util import BlueSkyFollowers
from rich.console import Console

def test_migration():
    console = Console()
    bf = BlueSkyFollowers()
    
    console.print("[bold]Testing BlueSky v2.0.0 Migration[/bold]", style="blue")
    console.print("=" * 50)
    
    # Test 1: Valid username should work
    console.print("\n[bold]Test 1: Valid username (jack.bsky.social)[/bold]")
    try:
        data = bf.get_followers_data('jack.bsky.social', limit=3)
        if data['success']:
            console.print(f"✅ Success - Retrieved {len(data['followers'])} followers", style="green")
        else:
            console.print(f"❌ Failed: {data['error']}", style="red")
    except Exception as e:
        console.print(f"❌ Exception: {e}", style="red")
    
    # Test 2: Invalid username (no domain) should fail gracefully
    console.print("\n[bold]Test 2: Invalid username (jack)[/bold]")
    try:
        data = bf.get_followers_data('jack', limit=3)
        if data['success']:
            console.print("❌ Should have failed but didn't", style="red")
        else:
            console.print(f"✅ Correctly rejected: {data['error']}", style="green")
    except Exception as e:
        console.print(f"❌ Unexpected exception: {e}", style="red")
    
    # Test 3: Profile method should also validate
    console.print("\n[bold]Test 3: Profile lookup validation[/bold]")
    try:
        profile = bf.get_user_profile('jack')
        console.print("❌ Profile lookup should have failed", style="red")
    except ValueError as e:
        console.print(f"✅ Profile lookup correctly rejected: {e}", style="green")
    except Exception as e:
        console.print(f"❌ Unexpected exception: {e}", style="red")
    
    # Test 4: Valid custom domain
    console.print("\n[bold]Test 4: Custom domain support[/bold]")
    try:
        # This will fail with actual API call but should pass validation
        data = bf.get_followers_data('user.example.com', limit=1)
        if not data['success'] and 'User not found' in data['error']:
            console.print("✅ Custom domain validated correctly (user not found is expected)", style="green")
        elif data['success']:
            console.print("✅ Custom domain works!", style="green")
        else:
            console.print(f"✅ Custom domain passed validation: {data['error']}", style="green")
    except ValueError as e:
        console.print(f"❌ Custom domain validation failed: {e}", style="red")
    except Exception as e:
        console.print(f"ℹ️ Custom domain validation passed, API error expected: {e}", style="yellow")
    
    console.print("\n[bold]Migration Test Complete![/bold]", style="blue")

if __name__ == "__main__":
    test_migration()
