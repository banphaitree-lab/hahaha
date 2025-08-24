import hashlib
EXPECTED = "c0566256c269fe7a23e34753f81fa539c0c8618924de1986342de231c850ca3f"
SHAS = {
  "B":    "edbfde4660f7924a5e3094ce14beed7258962cc8b76085255c427299300b3da4",
  "Rotor":"2e3f618d0cb8f6a258db9f98e984c7d49b16a4efe514bd38b02be2b428ecf598",
  "HB":   "beeedf4d7f5234f8f0b038b51d2dad3b08f927b752822058ba427c21c475607b",
  "Payout":"c4b3125859d3378aad30ea2ea81463fc986bb29af4b520976617dac5259b762b"
}
def hex_to_bytes(h): return bytes.fromhex(h)
root = hashlib.sha256(hex_to_bytes(SHAS["B"]) + hex_to_bytes(SHAS["Rotor"]) + hex_to_bytes(SHAS["HB"]) + hex_to_bytes(SHAS["Payout"])).hexdigest()
print("Recomputed bundle root:", root)
print("Matches expected:", root == EXPECTED)
