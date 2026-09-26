"""Mock USD/NGN FX helpers (no network)."""

from __future__ import annotations

from bob_naira_assist.models import FxQuote

# Deterministic demo fixtures — not live rates.
DEMO_FX_STABLE = FxQuote(usd_ngn=1600.0, previous_usd_ngn=1595.0, as_of_label="demo-stable")
# ~2.5% adverse — between FX_WATCH_PCT (2%) and FX_WAIT_PCT (3%).
DEMO_FX_WATCH = FxQuote(usd_ngn=1640.0, previous_usd_ngn=1600.0, as_of_label="demo-watch")
# 5% adverse — triggers suggest_wait when remittance is planned.
DEMO_FX_SPIKE = FxQuote(usd_ngn=1680.0, previous_usd_ngn=1600.0, as_of_label="demo-spike")
# ~3.1% naira strengthening — triggers suggest_send_later when remittance is planned.
DEMO_FX_STRENGTHEN = FxQuote(usd_ngn=1550.0, previous_usd_ngn=1600.0, as_of_label="demo-strengthen")


def mock_quote(scenario: str = "stable") -> FxQuote:
    """Return a deterministic FX quote for demo/tests.

    Scenarios:
    - stable: mild move (~0.3%), not adverse enough for FX watch
    - watch: ~2.5% naira weaker → ping_fx_watch (not wait)
    - spike: 5% naira weaker → suggest_wait when remittance planned
    - strengthen: ~3.1% naira stronger → suggest_send_later when remittance planned
    """
    key = (scenario or "stable").strip().lower()
    if key in {"spike", "volatile", "alert"}:
        return DEMO_FX_SPIKE
    if key in {"watch", "mild", "fx_watch"}:
        return DEMO_FX_WATCH
    if key in {"strengthen", "strengthening"}:
        return DEMO_FX_STRENGTHEN
    return DEMO_FX_STABLE
