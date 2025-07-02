import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from bluesky_util.account import BlueSkyAccount
from bluesky_util import BlueSkyFollowers

import asyncio
import time
from typing import List

async def main():
    bf = BlueSkyFollowers()
    profile = bf.get_user_profile('robtalksnonsense.com')
    account = BlueSkyAccount(
        handle=profile.handle,
        display_name=profile.display_name or "",
        description=profile.description or "",
        joined_date=getattr(profile, 'created_at', ""),
        follower_count=getattr(profile, 'followers_count', 0),
        following_count=getattr(profile, 'follows_count', 0),
        avatar=getattr(profile, 'avatar', ""),
        did=getattr(profile, 'did', ""),
        posts=[]  # Optionally, fetch posts if needed
    )
    await account.save_to_postgresql()
    print("Account saved for robtalksnonsense.com.")

    loaded = await BlueSkyAccount.load_from_postgresql(handle=profile.handle)
    print("Loaded:", loaded)

async def batch_import_accounts(handles: List[str], delay: float = 2.0, retry_delay: float = 30.0, posts_limit: int = 20):
    bf = BlueSkyFollowers()
    for handle in handles:
        print(f"Fetching profile for {handle}...")
        try:
            profile = bf.get_user_profile(handle)
            if not profile:
                print(f"[WARN] No profile found for {handle}. Skipping.")
                continue
            posts = bf.get_user_posts(handle, limit=posts_limit)
            account = BlueSkyAccount(
                handle=profile.handle,
                display_name=profile.display_name or "",
                description=profile.description or "",
                joined_date=getattr(profile, 'created_at', ""),
                follower_count=getattr(profile, 'followers_count', 0),
                following_count=getattr(profile, 'follows_count', 0),
                avatar=getattr(profile, 'avatar', ""),
                did=getattr(profile, 'did', ""),
                posts=posts or []
            )
            await account.save_to_postgresql()
            print(f"[OK] Saved {handle} to database with {len(posts)} posts.")
            time.sleep(delay)
        except Exception as e:
            msg = str(e).lower()
            if 'throttle' in msg or 'rate limit' in msg or '429' in msg:
                print(f"[THROTTLED] Detected throttling for {handle}. Waiting {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print(f"[ERROR] Failed for {handle}: {e}")

# Example usage:
# if __name__ == "__main__":
#     handles = ["jack.bsky.social", "robtalksnonsense.com", ...]
#     asyncio.run(batch_import_accounts(handles))

if __name__ == "__main__":
    handles = ["rob-wolfe.com", "robtalksnonsense.com"]
    asyncio.run(batch_import_accounts(handles))
