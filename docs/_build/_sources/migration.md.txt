# Migration Guide: v1.0.0 to v2.0.0

This guide helps you migrate from BlueSky Followers Utility v1.0.0 to v2.0.0.

## Overview

Version 2.0.0 introduces significant changes that improve the library's flexibility and usability. The most important change is the removal of automatic `.bsky.social` suffix addition to support BlueSky's custom domain feature.

## Breaking Changes

### 1. Username Format Requirements

**v1.0.0 (OLD):**
```python
# Automatically added .bsky.social
get_followers('jack')  # Became jack.bsky.social
```

**v2.0.0 (NEW):**
```python
# Must provide fully qualified username
from bluesky_util import BlueSkyFollowers

bf = BlueSkyFollowers()
bf.get_followers_data('jack.bsky.social')  # Required
bf.get_followers_data('custom.domain.com')  # Now supported!
```

### 2. Library vs Script Usage

**v1.0.0 (OLD):**
```bash
# Direct script execution
python bluesky_followers.py jack 50
```

**v2.0.0 (NEW):**
```bash
# CLI interface
python cli.py jack.bsky.social --limit 50

# OR library usage
python -c "from bluesky_util import BlueSkyFollowers; ..."
```

## Migration Steps

### Step 1: Update Username Calls

Search your code for any hardcoded usernames and add the appropriate domain:

```python
# OLD
usernames = ['jack', 'alice', 'bob']

# NEW
usernames = ['jack.bsky.social', 'alice.bsky.social', 'bob.custom-domain.com']
```

### Step 2: Update Import Statements

```python
# OLD - Script import not supported

# NEW - Library import
from bluesky_util import BlueSkyFollowers, validate_username
```

### Step 3: Update Function Calls

```python
# OLD - Direct function calls not available

# NEW - Class-based approach
bf = BlueSkyFollowers()
data = bf.get_followers_data('jack.bsky.social', limit=50)
```

### Step 4: Handle Validation Errors

The new version raises `ValueError` for invalid usernames:

```python
from bluesky_util import validate_username

try:
    validate_username('jack')  # Will raise ValueError
except ValueError as e:
    print(f"Invalid username: {e}")
    # Fix by adding domain
    validate_username('jack.bsky.social')  # OK
```

## New Features in v2.0.0

### 1. Library Architecture
- Import as `from bluesky_util import BlueSkyFollowers`
- Reusable class-based interface
- Proper error handling with exceptions

### 2. Custom Domain Support
- Support for any BlueSky domain
- No automatic domain suffix addition
- Full username validation

### 3. Enhanced CLI Interface
- `--limit` flag for controlling output
- `--no-description` flag to hide descriptions
- `--version` flag to show version info
- Better error messages

### 4. Improved Error Handling
- Specific error types (`ValueError`, `ConnectionError`, etc.)
- Detailed error messages
- Graceful fallback behavior

## Common Migration Issues

### Issue 1: "Invalid username format"
**Cause:** Passing username without domain (e.g., `'jack'` instead of `'jack.bsky.social'`)

**Solution:**
```python
# Wrong
bf.get_followers_data('jack')

# Correct
bf.get_followers_data('jack.bsky.social')
```

### Issue 2: Import errors
**Cause:** Trying to import from old script location

**Solution:**
```python
# Wrong
from bluesky_followers import get_followers

# Correct
from bluesky_util import BlueSkyFollowers
```

### Issue 3: CLI argument format
**Cause:** Using old CLI argument format

**Solution:**
```bash
# Wrong
python bluesky_followers.py jack 50

# Correct
python cli.py jack.bsky.social --limit 50
```

## Testing Your Migration

Use this checklist to verify your migration:

1. **Username Validation:**
   ```python
   from bluesky_util import validate_username
   
   # Should work
   validate_username('jack.bsky.social')
   validate_username('custom.domain.com')
   
   # Should raise ValueError
   try:
       validate_username('jack')
       assert False, "Should have raised ValueError"
   except ValueError:
       pass  # Expected
   ```

2. **Library Import:**
   ```python
   from bluesky_util import BlueSkyFollowers
   bf = BlueSkyFollowers()
   assert bf is not None
   ```

3. **CLI Interface:**
   ```bash
   python cli.py --version  # Should show v2.0.0
   python cli.py invalid-username  # Should show error
   python cli.py jack.bsky.social --limit 5  # Should work
   ```

## Support

If you encounter issues during migration:

1. Check the [API Reference](api-reference.md) for detailed function signatures
2. Review [Examples](EXAMPLES.md) for usage patterns
3. Check the [Changelog](changelog.md) for all changes
4. Open an issue on GitHub with your specific migration problem

## Rollback Plan

If you need to rollback to v1.0.0:

1. The original v1.0.0 script is preserved as `bluesky_followers_v1.0.0.py`
2. Use: `python bluesky_followers_v1.0.0.py jack 50`
3. Note: v1.0.0 won't support custom domains

## Performance Notes

v2.0.0 includes several performance improvements:

- Better connection handling and reuse
- Optimized data structures
- Reduced memory usage for large follower lists
- Improved error recovery

Expect similar or better performance compared to v1.0.0.
