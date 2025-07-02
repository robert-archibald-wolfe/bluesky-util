# TODO List for BlueSky Followers Utility API

This file tracks outstanding tasks and features to implement in the API and related code.

## API Endpoints

- [ ] Replace mocked logic in `/profile/{handle}` with real BlueSkyClient.get_user_profile
- [ ] Replace mocked logic in `/followers/{handle}` with real BlueSkyFollowers.get_followers
- [ ] Replace mocked logic in `/blocked/{handle}` with real BlueSkyClient.get_blocked_accounts
- [ ] Implement real authentication/session in `/login`
- [ ] Implement export logic (CSV, JSON, etc.) in `/export/followers/{handle}`
- [ ] Add pagination and filtering to follower/block endpoints
- [ ] Add endpoints for following/unfollowing, blocking/unblocking
- [ ] Add endpoints for importing data
- [ ] Add user/session management endpoints
- [ ] Add error handling and validation improvements

## General

- [ ] Remove unused imports (e.g., `Depends` in api_server.py)
- [ ] Add OpenAPI docs and examples
- [ ] Add automated tests for API endpoints
- [ ] Integrate with frontend dashboard when ready

---

Add new TODOs here as you discover them!
