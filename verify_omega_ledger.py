#!/usr/bin/env python3
# verify_omega_ledger.py
import json, sys, hashlib

def merkle_pairwise(leaf_hexes):
    leaves = [h.lower() for h in leaf_hexes]
    norm = []
    for h in leaves:
        try:
            bytes.fromhex(h)
            norm.append(h)
        except Exception:
            norm.append(hashlib.sha256(h.encode("utf-8")).hexdigest())
    current = norm
    if not current:
        return None
    while len(current) > 1:
        nxt = []
        i = 0
        while i < len(current):
            left = current[i]
            right = current[i+1] if i+1 < len(current) else current[i]
            h = hashlib.sha256(bytes.fromhex(left) + bytes.fromhex(right)).hexdigest()
            nxt.append(h)
            i += 2
        current = nxt
    return current[0]

def sorted_concat_root(leaf_hexes):
    roots = sorted([h.lower() for h in leaf_hexes])
    concat = "".join(roots).encode("utf-8")
    return hashlib.sha256(concat).hexdigest()

def main(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    leaves = [e["merkle_root"] for e in data.get("exhibits", [])]
    r_sorted = sorted_concat_root(leaves)
    r_merkle = merkle_pairwise(leaves)
    print("Sorted-concat root:", r_sorted)
    print("Pairwise Merkle root:", r_merkle)
    stored_sorted = data.get("master_merkle_root", {}).get("value")
    stored_pair = data.get("pairwise_merkle_root", {}).get("value")
    if stored_sorted:
        print("Matches stored sorted-concat root?:", "YES" if stored_sorted == r_sorted else "NO")
    if stored_pair:
        print("Matches stored pairwise Merkle root?:", "YES" if stored_pair == r_merkle else "NO")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 verify_omega_ledger.py /path/to/ledger.json")
        sys.exit(1)
    main(sys.argv[1])
