"""Unit tests for pure decision logic (no network)."""

from bob_naira_assist.bills import sample_bills, total_due
from bob_naira_assist.decisions import evaluate_buffer
from bob_naira_assist.fx import DEMO_FX_SPIKE, DEMO_FX_STABLE, mock_quote
from bob_naira_assist.models import ActionKind, CashBuffer


def test_sample_bills_total():
    bills = sample_bills()
    assert len(bills) == 4
    assert total_due(bills) == 250_000 + 24_500 + 8_000 + 45_000


def test_quiet_when_buffer_covers_and_fx_stable():
    bills = sample_bills()
    buffer = CashBuffer(400_000.0)
    d = evaluate_buffer(bills, buffer, DEMO_FX_STABLE)
    assert d.action == ActionKind.QUIET
    assert d.shortfall_ngn == 0.0


def test_shortfall_ping():
    bills = sample_bills()
    buffer = CashBuffer(280_000.0)
    d = evaluate_buffer(bills, buffer, DEMO_FX_STABLE)
    assert d.action == ActionKind.PING_SHORTFALL
    assert d.shortfall_ngn == total_due(bills) - 280_000.0


def test_fx_spike_suggests_wait_when_buffer_ok():
    bills = sample_bills()
    buffer = CashBuffer(500_000.0)
    d = evaluate_buffer(bills, buffer, DEMO_FX_SPIKE, remittance_planned_usd=500.0)
    assert d.action == ActionKind.SUGGEST_WAIT
    assert d.fx_pct_change > 3.0


def test_send_now_on_stable_with_remittance():
    bills = sample_bills()
    buffer = CashBuffer(400_000.0)
    d = evaluate_buffer(bills, buffer, DEMO_FX_STABLE, remittance_planned_usd=200.0)
    assert d.action == ActionKind.SUGGEST_SEND_NOW


def test_mock_quote_scenarios():
    assert mock_quote("stable").usd_ngn == 1600.0
    assert mock_quote("spike").usd_ngn == 1680.0
