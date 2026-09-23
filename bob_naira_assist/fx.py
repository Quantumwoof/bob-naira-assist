"""Mock USD/NGN FX helpers (no network)."""

from __future__ import annotations

from bob_naira_assist.models import FxQuote

# Stable demo fixtures — not live rates.
DEMO_FX_STABLE = FxQuote(usd_ngn=1600.0, previous_usd_ngn=1595.0, as_of_label="demo-stable")
DEMO_FX_SPIKE = FxQuote(usd_ngn=1680.0, previous_usd_ngn=1600.0, as_of_label="demo-spike")


def mock_quote(scenario: str = "stable") -> FxQuote:
    """Return a deterministic FX quote for demo/tests."""
    key = (scenario or "stable").strip().lower()
    if key in {"spike", "volatile", "alert"}:
        return DEMO_FX_SPIKE
    return DEMO_FX_STABLE
