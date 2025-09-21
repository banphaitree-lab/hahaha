#!/usr/bin/env bash
# verify_omega_ledger.sh
set -euo pipefail
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 /path/to/ledger.json"
  exit 1
fi
LEDGER="$1"
if command -v python3 >/dev/null 2>&1; then
  python3 verify_omega_ledger.py "$LEDGER"
  exit 0
fi
if ! command -v jq >/dev/null 2>&1 || ! command -v openssl >/dev/null 2>&1; then
  echo "Need python3 or (jq and openssl) installed to verify."
  exit 1
fi
roots=$(jq -r '.exhibits[].merkle_root' "$LEDGER" | sort | tr -d '\n')
printf "%s" "$roots" | openssl dgst -sha256
