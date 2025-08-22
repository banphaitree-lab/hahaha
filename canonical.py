import json, hashlib
from typing import Any

def canonical_bytes(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()

def sha256_hex_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def sha256_hex(obj: Any) -> str:
    return sha256_hex_bytes(canonical_bytes(obj))
