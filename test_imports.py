#!/usr/bin/env python3
"""
Simple test to debug the library import issues.
"""

# Test 1: Try importing utils first
try:
    from bluesky_util.utils import format_date, validate_username
    print("✓ Utils import successful")
except Exception as e:
    print(f"✗ Utils import failed: {e}")

# Test 2: Try importing followers module directly
try:
    import bluesky_util.followers
    print("✓ Followers module import successful")
except Exception as e:
    print(f"✗ Followers module import failed: {e}")

# Test 3: Try accessing the class
try:
    from bluesky_util.followers import BlueSkyFollowers
    print("✓ BlueSkyFollowers class import successful")
except Exception as e:
    print(f"✗ BlueSkyFollowers class import failed: {e}")

# Test 4: Try creating an instance
try:
    from bluesky_util.followers import BlueSkyFollowers
    client = BlueSkyFollowers()
    print("✓ BlueSkyFollowers instance creation successful")
except Exception as e:
    print(f"✗ BlueSkyFollowers instance creation failed: {e}")
