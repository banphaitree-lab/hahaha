import json, hashlib
from typing import Dict, List
from .canonical import canonical_bytes
from .triad import B
from .rotor import rotor_R

def hash_hex(obj) -> str:
    return hashlib.sha256(canonical_bytes(obj)).hexdigest()

def build_channels(xi: complex = 1+1j, vectors: List[complex] = None, N: int = 40) -> Dict[str, dict]:
    if vectors is None:
        vectors = [2+0j, 1.1+0j, 1+1e-6+0j]
    B_records = []
    R_records = []
    for x in vectors:
        Bz = B(x, xi, N)
        Rz = rotor_R(x, xi, N)
        rec = {
            "x": {"re": x.real, "im": x.imag},
            "xi": {"re": xi.real, "im": xi.imag},
            "B": {"re": Bz.real, "im": Bz.imag},
        }
        B_records.append(rec)
        R_records.append({**rec, "R": Rz})
    hb = {"equation": "Omega * F(x)^(3/2) = C", "Omega": 164888.512, "C": 164888.512, "solution": {"F": 1}}
    payout = {"derivation_contract": "PAYOUT = (Omega*A/E)*(T/C)^2*Scale", "target_payout": 5000000000}
    return {
        "B_channel": {"rsi_version": "1.1", "records": B_records},
        "rotor_channel": {"rsi_version": "1.1", "records": R_records},
        "HB_equilibrium": hb,
        "payout_derived_v1_1": payout,
    }

def bundle_root_from_channels(ch: Dict[str, dict]) -> str:
    order = ["B_channel", "rotor_channel", "HB_equilibrium", "payout_derived_v1_1"]
    hexes = [hash_hex(ch[name]) for name in order]
    concat = bytes.fromhex("".join(hexes))
    return hashlib.sha256(concat).hexdigest()


def build_bundle(ch: Dict[str, dict]) -> dict:
    shas = {k: hash_hex(v) for k, v in ch.items()}
    root = bundle_root_from_channels(ch)
    return {
        "rsi_bundle_version": "1.5",
        "channel_shas": shas,
        "ordering": "SHA256(B) || SHA256(Rotor) || SHA256(HB) || SHA256(payout_derived v1.1)",
        "bundle_root_sha256": root,
    }