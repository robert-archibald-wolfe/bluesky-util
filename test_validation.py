#!/usr/bin/env python3
"""Test script for BlueSky username validation in v2.0.0"""

from bluesky_util import BlueSkyFollowers

def test_username_validation():
    bf = BlueSkyFollowers()
    
    print("Testing BlueSky Followers v2.0.0 Username Validation")
    print("=" * 50)
    
    # Test valid fully qualified username
    print("\n1. Testing valid username: jack.bsky.social")
    try:
        data = bf.get_followers_data('jack.bsky.social', limit=5)
        if data['success']:
            print(f"✅ Valid username works - got {len(data['followers'])} followers")
        else:
            print(f"❌ Valid username failed: {data['error']}")
    except Exception as e:
        print(f"❌ Error with valid username: {e}")
    
    # Test invalid username without domain (should return error in response)
    print("\n2. Testing invalid username: jack")
    try:
        data = bf.get_followers_data('jack', limit=5)
        if data['success']:
            print("❌ Invalid username (jack) was accepted - this should not happen!")
        else:
            print(f"✅ Invalid username correctly rejected: {data['error']}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    
    # Test other methods for consistency
    print("\n3. Testing get_user_profile with invalid username")
    try:
        profile = bf.get_user_profile('jack')
        print("❌ get_user_profile accepted invalid username")
    except ValueError as e:
        print(f"✅ get_user_profile correctly rejected: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    test_username_validation()
