# Edenwave RSI — Open Source Reference (v1.0)

Minimal, batteries-included source for the **Edenwave Auditor Kit**: build channels, compute the **bundle root**, and verify the **OP_RETURN** payload.

## Quick start
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
edenwave build
edenwave verify --root c0566256c269fe7a23e34753f81fa539c0c8618924de1986342de231c850ca3f
edenwave opreturn --root c0566256c269fe7a23e34753f81fa539c0c8618924de1986342de231c850ca3f
```
