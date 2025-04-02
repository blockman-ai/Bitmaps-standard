# Bitmap Claim Specification v0.1

---

## Purpose  
Defines the standard for claiming a Bitcoin block as a Bitmap parcel using Ordinal inscriptions.

---

## Claim Format (Tag-based)

Each claim must include the keyword:  
```
bitmap-claim:<block_height>
```

### Example:
```
bitmap-claim:840000
```

This tag can be included:
- In plaintext inscription body
- OR in metadata JSON with `"type": "bitmap-claim"`

---

## Metadata (Optional)

Inscriptions can include metadata in JSON format to describe the parcel.

### Example JSON:
```json
{
  "type": "bitmap-claim",
  "block": 840000,
  "name": "Genesis Tower",
  "theme": "Post-halving monument",
  "coordinates": [0, 0],
  "artist": "blockman-ai"
}
```

---

## Canonical Claim Rules

- **Block height must be in the past** (can't claim future blocks).
- **First valid inscription** for a block is canonical.
- **One parcel per block** — no duplicates.
- **Claim must be on Bitcoin mainnet.**
- **All claims are final** (unless soft-consensus rules change later).

---

## Parsing Logic (Indexer Pseudocode)

```python
if "bitmap-claim" in inscription_text:
    block_height = extract_block_number(inscription_text)
    if block_height < current_block:
        if block_height not in claimed_blocks:
            claimed_blocks[block_height] = inscription_id
```

---

## Rendering Notes

Interpretation of metadata (e.g. `coordinates`, `theme`) is open to developers.  
Bitmaps encourages creative layers — voxel worlds, pixel maps, lore overlays, etc.

---

## DYOR

This is an experimental protocol.  
All indexers must cross-verify data and interpret rules openly.
```
