"""Unit tests for pure decision logic (no network)."""

from bob_naira_assist.bills import sample_bills, total_due
from bob_naira_assist.decisions import (
    FX_WAIT_PCT,
    FX_WATCH_PCT,
    SHORTFALL_PING_THRESHOLD_NGN,
    evaluate_buffer,
)
from bob_naira_assist.fx import (
    DEMO_FX_SPIKE,
    DEMO_FX_STABLE,
    DEMO_FX_WATCH,
    mock_quote,
)
from bob_naira_assist.models import ActionKind, CashBuffer, FxQuote


def test_sample_bills_total():
    bills = sample_bills()
    assert len(bills) == 4
    assert total_due(bills) == 250_000 + 24_500 + 8_000 + 45_000


def test_quiet_when_buffer_covers_and_fx_stable_no_remittance():
    bills = sample_bills()
    buffer = CashBuffer(400_000.0)
    d = evaluate_buffer(bills, buffer, DEMO_FX_STABLE)
    assert d.action == ActionKind.QUIET
    assert d.shortfall_ngn == 0.0


def test_quiet_without_remittance_even_if_buffer_healthy():
    """Regression: remittance_planned must be absent for true quiet."""
    bills = sample_bills()
    buffer = CashBuffer(400_000.0)
    d = evaluate_buffer(bills, buffer, DEMO_FX_STABLE, remittance_planned_usd=None)
    assert d.action == ActionKind.QUIET


def test_shortfall_ping():
    bills = sample_bills()
    buffer = CashBuffer(280_000.0)
    d = evaluate_buffer(bills, buffer, DEMO_FX_STABLE)
    assert d.action == ActionKind.PING_SHORTFALL
    assert d.shortfall_ngn == total_due(bills) - 280_000.0


def test_boundary_exact_bills_total_is_quiet():
    bills = sample_bills()
    total = total_due(bills)
    d = evaluate_buffer(bills, CashBuffer(total), DEMO_FX_STABLE)
    assert d.action == ActionKind.QUIET
    assert d.shortfall_ngn == 0.0


def test_boundary_one_naira_under_triggers_shortfall():
    bills = sample_bills()
    total = total_due(bills)
    under = total - SHORTFALL_PING_THRESHOLD_NGN
    d = evaluate_buffer(bills, CashBuffer(under), DEMO_FX_STABLE)
    assert d.action == ActionKind.PING_SHORTFALL
    assert d.shortfall_ngn == SHORTFALL_PING_THRESHOLD_NGN


def test_fx_spike_suggests_send_now_when_buffer_ok():
    """Sharp naira weakening with planned remittance → suggest_send_now.

    A weakening naira is FAVOURABLE for the USD sender: each dollar buys more NGN.
    The correct advice is to consider sending now, not to wait.
    """
    bills = sample_bills()
    buffer = CashBuffer(500_000.0)
    d = evaluate_buffer(bills, buffer, DEMO_FX_SPIKE, remittance_planned_usd=500.0)
    assert d.action == ActionKind.SUGGEST_SEND_NOW
    assert d.fx_pct_change > FX_WAIT_PCT


def test_fx_spike_with_remittance_never_returns_suggest_wait():
    """Regression: a sharp naira-weakening spike + remittance must NEVER return suggest_wait."""
    bills = sample_bills()
    buffer = CashBuffer(500_000.0)
    d = evaluate_buffer(bills, buffer, DEMO_FX_SPIKE, remittance_planned_usd=500.0)
    assert d.action != ActionKind.SUGGEST_WAIT


def test_fx_watch_between_two_and_three_percent():
    bills = sample_bills()
    buffer = CashBuffer(500_000.0)
    assert FX_WATCH_PCT <= abs(DEMO_FX_WATCH.pct_change) < FX_WAIT_PCT
    d = evaluate_buffer(bills, buffer, DEMO_FX_WATCH, remittance_planned_usd=500.0)
    assert d.action == ActionKind.PING_FX_WATCH


def test_fx_watch_custom_quote():
    """Explicit mock between 2–3% adverse."""
    bills = sample_bills()
    fx = FxQuote(usd_ngn=1632.0, previous_usd_ngn=1600.0, as_of_label="custom-2pct")
    assert abs(fx.pct_change - 2.0) < 0.01
    d = evaluate_buffer(bills, CashBuffer(500_000.0), fx, remittance_planned_usd=200.0)
    assert d.action == ActionKind.PING_FX_WATCH


def test_send_now_on_stable_with_remittance():
    bills = sample_bills()
    buffer = CashBuffer(400_000.0)
    d = evaluate_buffer(bills, buffer, DEMO_FX_STABLE, remittance_planned_usd=200.0)
    assert d.action == ActionKind.SUGGEST_SEND_NOW


def test_mock_quote_scenarios():
    assert mock_quote("stable").usd_ngn == 1600.0
    assert mock_quote("watch").usd_ngn == 1640.0
    assert mock_quote("spike").usd_ngn == 1680.0


def test_fx_spike_without_remittance_is_watch_not_send_now():
    """Spike alone (no remittance) must give ping_fx_watch, not suggest_send_now."""
    bills = sample_bills()
    buffer = CashBuffer(500_000.0)
    d = evaluate_buffer(bills, buffer, DEMO_FX_SPIKE, remittance_planned_usd=None)
    assert d.action == ActionKind.PING_FX_WATCH
    assert d.action != ActionKind.SUGGEST_WAIT
    assert d.action != ActionKind.SUGGEST_SEND_NOW
    assert d.action != ActionKind.QUIET


def test_shortfall_beats_fx_spike_and_remittance():
    """Cash shortfall wins over FX send-now even when remittance + spike are set."""
    bills = sample_bills()
    buffer = CashBuffer(280_000.0)
    d = evaluate_buffer(bills, buffer, DEMO_FX_SPIKE, remittance_planned_usd=500.0)
    assert d.action == ActionKind.PING_SHORTFALL


def test_naira_strengthening_stays_quiet_without_remittance():
    """Stronger naira (negative pct) is not adverse — stay quiet if buffer OK."""
    bills = sample_bills()
    fx = FxQuote(usd_ngn=1550.0, previous_usd_ngn=1600.0, as_of_label="stronger")
    assert fx.pct_change < 0
    assert not fx.naira_weakened
    d = evaluate_buffer(bills, CashBuffer(400_000.0), fx, remittance_planned_usd=None)
    assert d.action == ActionKind.QUIET
