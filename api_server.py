"""
FastAPI starter API for BlueSky Followers Utility

- This is a minimal API scaffold with mocked endpoints for follower management.
- Replace mock logic with real BlueSkyClient/BlueSkyFollowers calls as you build out features.
"""

from fastapi import FastAPI, HTTPException  # TODO: Remove unused imports (e.g., Depends)
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="BlueSky Followers API", description="API for managing and visualizing BlueSky followers.")

# --- Models ---
class UserProfile(BaseModel):
    handle: str
    did: str
    display_name: Optional[str] = None
    followers_count: Optional[int] = None
    following_count: Optional[int] = None

class Follower(BaseModel):
    handle: str
    did: str
    display_name: Optional[str] = None

class BlockedAccount(BaseModel):
    handle: str
    did: str

# --- Mocked Data ---
MOCK_PROFILE = UserProfile(handle="alice.bsky.social", did="did:plc:123", display_name="Alice", followers_count=42, following_count=10)
MOCK_FOLLOWERS = [
    Follower(handle="bob.bsky.social", did="did:plc:456", display_name="Bob"),
    Follower(handle="carol.bsky.social", did="did:plc:789", display_name="Carol"),
]
MOCK_BLOCKED = [
    BlockedAccount(handle="spam.bsky.social", did="did:plc:999"),
]

# --- Endpoints ---
@app.get("/profile/{handle}", response_model=UserProfile)
def get_profile(handle: str):
    # TODO: Replace with BlueSkyClient.get_user_profile
    if handle == MOCK_PROFILE.handle:
        return MOCK_PROFILE
    raise HTTPException(status_code=404, detail="User not found")

@app.get("/followers/{handle}", response_model=List[Follower])
def get_followers(handle: str):
    # TODO: Replace with BlueSkyFollowers.get_followers
    if handle == MOCK_PROFILE.handle:
        return MOCK_FOLLOWERS
    raise HTTPException(status_code=404, detail="User not found")

@app.get("/blocked/{handle}", response_model=List[BlockedAccount])
def get_blocked_accounts(handle: str):
    # TODO: Replace with BlueSkyClient.get_blocked_accounts
    if handle == MOCK_PROFILE.handle:
        return MOCK_BLOCKED
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/login")
def login(username: str, password: str):
    # TODO: Implement real authentication/session
    if username == "alice.bsky.social" and password == "password":
        return {"message": "Login successful", "token": "mock-token"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/export/followers/{handle}")
def export_followers(handle: str, format: str = "json"):
    # TODO: Implement export logic (CSV, JSON, etc.)
    if handle == MOCK_PROFILE.handle:
        if format == "json":
            return {"followers": [f.dict() for f in MOCK_FOLLOWERS]}
        elif format == "csv":
            csv_data = "handle,did,display_name\n" + "\n".join(f"{f.handle},{f.did},{f.display_name or ''}" for f in MOCK_FOLLOWERS)
            return {"csv": csv_data}
        else:
            raise HTTPException(status_code=400, detail="Unsupported format")
    raise HTTPException(status_code=404, detail="User not found")

@app.get("/health")
def health():
    return {"status": "ok"}
