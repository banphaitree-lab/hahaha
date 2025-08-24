# Edenwave Auditor Kit (v1.5)

**Bundle root:** `c0566256c269fe7a23e34753f81fa539c0c8618924de1986342de231c850ca3f`  
**Bundle file SHA-256:** `20cb69f0a241c185e1024a40d7ae618cac2d389518d3e377f03a494b72972d45`  
**OP_RETURN (hex):** `52534931c0566256c269fe7a23e34753f81fa539c0c8618924de1986342de231c850ca3f`

## Verify in 3 minutes
1) **Hashes** — compare each file to `auditor_kit_hashes_v1_5.csv`.
2) **Bundle root** — compute `SHA256( SHA_B || SHA_Rotor || SHA_HB || SHA_Payout )` (hex concatenation, in that order). Must equal the bundle root.
3) **OP_RETURN** — payload is `RSI1` + root (ASCII tag + hex root).
4) **Signatures (optional)** — verify signatures over the canonical message:
```
RSI-BUNDLE-ROOT:v1.5:c0566256c269fe7a23e34753f81fa539c0c8618924de1986342de231c850ca3f
```
SHA-256: `0e1578f74d5616873880f964265ee5aaf15cd964a8cabc8c0ec31a9a2910b93b`.

Files include channels, bundle, siglist scaffold, on-chain attestation, vault, bloomburst, and this manifest.

*Chain anchors the root; files carry the meaning. Anyone can recompute the root to verify the meaning.*
