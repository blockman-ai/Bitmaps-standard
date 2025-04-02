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
