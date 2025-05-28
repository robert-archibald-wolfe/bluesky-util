# Development Notes

## v1.0.0 Release Notes

### What Works
- ✅ Retrieves followers using BlueSky public API
- ✅ Shows follower join dates (when they created their BlueSky account)
- ✅ Rich table formatting with handle, display name, description, join date
- ✅ Chronological sorting by join date
- ✅ No authentication required
- ✅ Automatic username formatting (.bsky.social)
- ✅ Error handling and user-friendly messages

### Known Limitations
- ❌ Cannot get actual "followed on" dates (not available in public API)
- ❌ Limited to 100 followers per request (API limitation)
- ❌ No pagination support yet
- ❌ No export functionality

### Technical Details
- Uses atproto library for BlueSky API access
- Public API endpoint: https://public.api.bsky.app
- No rate limiting implemented yet
- Handles both username and username.bsky.social formats

### Future Development Ideas

#### v1.1 Features
- [ ] Export to CSV/JSON
- [ ] Pagination support for large follower lists
- [ ] Rate limiting and retry logic
- [ ] Progress bars for large requests

#### v2.0 Features  
- [ ] Following/followers comparison
- [ ] Follower analytics (join date trends, etc.)
- [ ] Batch processing for multiple users
- [ ] Interactive mode with user selection
- [ ] Web interface option

#### v3.0+ Features
- [ ] Follow/unfollow tracking over time
- [ ] Notification system for new followers
- [ ] Database storage for historical data
- [ ] API server mode
- [ ] Dashboard with charts and graphs

### Development Setup
```bash
# Install dependencies
uv sync

# Run tests
uv run python bluesky_followers.py --version

# Test with sample user
uv run python bluesky_followers.py jack 10
```

### Code Structure
- `bluesky_followers.py` - Main script
- `get_followers()` - Core function to retrieve and format data
- `format_date()` - Date formatting utility
- `main()` - CLI interface and argument parsing

### API Notes
- BlueSky public API is used (no auth required)
- indexed_at timestamps are NOT reliable for follow dates
- created_at is the user's account creation date (reliable)
- Profile descriptions are truncated to 35 chars for table display
