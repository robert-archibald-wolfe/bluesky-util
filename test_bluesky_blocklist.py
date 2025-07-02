import getpass
from bluesky_util.client import BlueSkyClient

if __name__ == "__main__":
    print("BlueSky Blocklist Test")
    username = input("Enter your Bluesky handle (e.g., user.bsky.social): ")
    password = getpass.getpass("Enter your app password: ")

    client = BlueSkyClient()
    if client.login(username, password):
        print(f"[SUCCESS] Logged in as {client.authenticated_user} at {client.authenticated_at}")
        try:
            blocks = client.get_blocked_accounts()
            if blocks:
                print(f"Blocked accounts ({len(blocks)}):")
                for block in blocks:
                    print(f"- {block['handle']} ({block['did']})")
            else:
                print("No blocked accounts found.")
        except Exception as e:
            print(f"[ERROR] Could not fetch block list: {e}")
    else:
        print("[FAILURE] Login failed. Please check your credentials.")
