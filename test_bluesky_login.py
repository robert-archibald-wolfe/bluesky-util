import getpass
from bluesky_util.client import BlueSkyClient

if __name__ == "__main__":
    print("BlueSky Login Test")
    username = input("Enter your Bluesky handle (e.g., user.bsky.social): ")
    password = getpass.getpass("Enter your app password: ")

    client = BlueSkyClient()
    if client.login(username, password):
        print(f"[SUCCESS] Logged in as {client.authenticated_user} at {client.authenticated_at}")
    else:
        print("[FAILURE] Login failed. Please check your credentials.")
