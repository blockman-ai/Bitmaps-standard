import requests, json

url = "https://ordiscan.com/api/v1/inscriptions?q=bitmap-claim"
res = requests.get(url)
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

with open("explorer/claims.json", "w") as f:
    json.dump(bitmap_claims, f, indent=2)
