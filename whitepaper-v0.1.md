# Bitmaps v0.1 – The Whitepaper  
*A New Standard for a Bitcoin Metaverse*

---

## Abstract  
**Bitmaps** is an experimental indexing protocol that assigns virtual parcels to individual Bitcoin blocks.  
Each block becomes a unique “coordinate” in a decentralized metaverse.  
Anyone can claim a block by inscribing metadata to it, allowing for endless layers of interpretation — from art and games to historical archives and digital real estate.

---

## 1. Motivation  
Bitcoin is the most decentralized, secure, and immutable network on Earth.  
Bitmaps aims to bring a metaverse to Bitcoin not by building on top of it — but by revealing what’s already there.  
Each block is a story, a space, a dimension. Bitmaps unlock that potential.

---

## 2. Core Concepts

- **Parcel = Block Height**  
  Every block on Bitcoin is a unique, fixed coordinate in Bitmap space.

- **Claiming a Parcel**  
  A user claims a block by inscribing metadata (e.g., title, description, visuals) with a standardized tag.

- **Metadata**  
  Metadata is open. A claimed block can include descriptions, traits, coordinates in a 2D/3D grid, or artistic meaning.

- **Interpretation Layers**  
  Bitmaps does not enforce a single worldview. Developers and communities are free to interpret blocks however they wish: voxel land, pixel grid, storyline map, timeline museum — all views are valid.

---

## 3. Claiming Logic

- Claim is made via Ordinal inscription using a tag like `bitmap-claim:<block_height>`  
- Only blocks mined before the inscription timestamp are eligible  
- First valid inscription for a block is recognized as canonical by the indexer  
- Optional: Include metadata in JSON format within the inscription  
- Example:
```json
{
  "type": "bitmap-claim",
  "block": 840000,
  "name": "Genesis Tower",
  "theme": "Post-halving monument",
  "coordinates": [0, 0]
}
```

---

## 4. Rules & Integrity

- One block = One parcel = One canonical claim  
- Metadata is optional and flexible  
- All data is permanently on-chain via inscriptions  
- Indexing is community-driven and experimental — always **DYOR**

---

## 5. Use Cases

- **Virtual Land**: Claim, trade, and build visual layers on parcels  
- **Games**: Design mechanics based on time (block height) or rarity (early blocks)  
- **Art**: Turn blocks into generative art canvases or curated galleries  
- **Lore**: Build timelines, temples, or ruins on historical block events  
- **Collectibles**: Display collections that evolve per block/era

---

## 6. Ecosystem Stack

- **Indexer**: Parses the chain for valid `bitmap-claim` inscriptions  
- **Explorer**: UI for browsing parcels, viewing claims, and visualizing blocks  
- **Renderer**: Optional community-built tools to visualize Bitmaps in 2D/3D  
- **Toolkit**: Open-source repo for building on Bitmap data

---

## 7. Community Growth

- Launch initial claiming guide + indexer  
- Drop Genesis Blocks (milestone parcels)  
- Offer dev bounties to expand renderers, games, or integrations  
- Onboard artists, devs, lore masters, and collectors  
- Host quests/challenges using Bitmap coordinates

---

## 8. Final Notes

- **This is experimental.** Indexing rules may evolve as the community builds.  
- No central server, no admin key — just inscriptions and interpretations.  
- A metaverse truly **on Bitcoin**, not around it.

```
