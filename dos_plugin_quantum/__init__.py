"""Quantum-adjacent helpers — EXPERIMENTAL, and deliberately modest.

This is NOT real quantum computing (that has no practical use for this project
today; adding it would be theater). It provides: (1) a quantum-RISK advisor that
flags actions relying on classical crypto that a future quantum adversary could
break, and (2) a QRNG interface stub for hardware entropy if ever available.
Everything here is advisory / interface-only.
"""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable


def quantum_risk_advisor(action: dict[str, Any]) -> str | None:
    """Advisory only: flag 'suspicious' if the action asserts long-lived secrecy
    under classical crypto (harvest-now-decrypt-later exposure)."""
    if action.get("data_labels") and "long_term_secret" in action["data_labels"]:
        return "suspicious"
    return None


@runtime_checkable
class QRNG(Protocol):
    def random_bytes(self, n: int) -> bytes: ...


class StubQRNG:
    def random_bytes(self, n: int) -> bytes:  # pragma: no cover
        raise NotImplementedError("Wire a hardware QRNG here if/when available.")
