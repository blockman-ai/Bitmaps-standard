import requests
import json

# Insert your Ordiscan API Key here
api_key = "9cd23c3c-a965-4a27-90f2-ce84848d83eb"

headers = {
    "Authorization": f"Bearer {api_key}"
}

url = "https://api.ordiscan.com/v1/inscriptions?q=bitmap-claim"

res = requests.get(url, headers=headers)

if res.status_code != 200:
    print("Error fetching data:", res.status_code)
    print(res.text)
    exit()

data = res.json()
bitmap_claims = {}

for item in data.get("results", []):
    content = item.get("content", "")
    inscription_id = item.get("inscription_id")
    block = item.get("block_number")

    if block is None or inscription_id is None:
        continue

    if "bitmap-claim" in content:
        bitmap_claims[str(block)] = {
            "name": "Unknown",
            "theme": "Undiscovered",
            "coordinates": [0, 0],
            "artist": "Unknown",
            "inscription": inscription_id
        }

# Save to explorer/claims.json
with open("explorer/claims.json", "w") as f:
    json.dump(bitmap_claims, f, indent=2)

print(f"Updated {len(bitmap_claims)} bitmap claims.")
