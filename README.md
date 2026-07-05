# plugin-quantum

Quantum-safe posture helpers for the Decision OS / AuthGate stack.

> Part of the Decision OS — governed by the Legitimacy ⊥ Authority pipeline
> (FDK legitimacy → AuthGate authority). Plugins are advisory only and hold
> **no authority**; the kernel remains the single authority.

**Status: experimental — advisory + interface-only. Weakest plugin in the set.**

## What it does

Two deliberately modest pieces:

- `quantum_risk_advisor(action)` — advisory only: flags `"suspicious"` when an
  action asserts long-lived secrecy under classical crypto (a "harvest-now,
  decrypt-later" exposure).
- `QRNG` / `StubQRNG` — an interface for a hardware quantum RNG, stubbed until such
  hardware is actually available.

This is **not** real quantum computing. That has no practical use for this project
today, and adding it would be theater.

## Authority

This plugin holds **no authority**. The advisor can only return `"suspicious"` or
`None`; the kernel decides.

## Install

```bash
pip install "decision-os-min @ git+https://github.com/Aliipou/decision-os-min.git"
pip install -e . --no-deps
pytest -q          # AUTHGATE_BACKEND=python
```

## Usage

```python
from dos_plugin_quantum import quantum_risk_advisor
quantum_risk_advisor({"data_labels": ["long_term_secret"]})   # -> "suspicious"
quantum_risk_advisor({"data_labels": []})                      # -> None
```

## Status and limitations

- The advisor is a **one-line label check**, not real cryptographic analysis.
- The QRNG is a stub only.
- Honest note: the useful post-quantum work lives in `plugin-pqcrypto`. This
  plugin is a candidate for pruning if it does not earn its keep.
