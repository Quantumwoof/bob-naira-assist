"""Tests for the three decision-logic fixes (architecture review task-01).

Fix 1 – evaluate_buffer must return SUGGEST_SEND_LATER (not SUGGEST_SEND_NOW)
         when the naira is strengthening sharply (USD/NGN falling >= 3%).

Fix 2 – total_due respects a horizon_days parameter; bills past the horizon are
         excluded.  Shortfall messages name bills that are due within 3 days.

Fix 3 – remittance_planned_usd=0.0 is treated the same as None.
"""

from __future__ import annotations

import pytest

from bob_naira_assist.bills import (
    URGENT_DAYS,
    sample_bills,
    total_due,
    urgent_bills,
)
from bob_naira_assist.decisions import (
    FX_STRENGTHENING_PCT,
    FX_WAIT_PCT,
    evaluate_buffer,
)
from bob_naira_assist.fx import DEMO_FX_STABLE
from bob_naira_assist.models import ActionKind, Bill, BillCategory, CashBuffer, FxQuote


# ---------------------------------------------------------------------------
# Fix 1: strengthening naira (USD/NGN falling >= FX_STRENGTHENING_PCT)
# ---------------------------------------------------------------------------

def _strengthening_fx(pct: float = FX_STRENGTHENING_PCT) -> FxQuote:
    """Return an FxQuote where naira has strengthened by exactly *pct* percent."""
    prev = 1600.0
    now = prev * (1.0 - pct / 100.0)
    return FxQuote(usd_ngn=now, previous_usd_ngn=prev, as_of_label=f"strengthening-{pct}pct")


def test_strengthening_naira_with_remittance_returns_suggest_send_later():
    """Sharp naira strengthening + planned remittance → SUGGEST_SEND_LATER."""
    bills = sample_bills()
    buffer = CashBuffer(500_000.0)
    fx = _strengthening_fx(FX_STRENGTHENING_PCT)  # exactly at threshold
    assert fx.pct_change <= -FX_STRENGTHENING_PCT + 0.001  # naira stronger
    d = evaluate_buffer(bills, buffer, fx, remittance_planned_usd=300.0)
    assert d.action == ActionKind.SUGGEST_SEND_LATER


def test_strengthening_naira_message_explains_fewer_naira():
    """SUGGEST_SEND_LATER message must explain the fewer-naira consequence."""
    bills = sample_bills()
    buffer = CashBuffer(500_000.0)
    fx = _strengthening_fx(5.0)  # well above threshold
    d = evaluate_buffer(bills, buffer, fx, remittance_planned_usd=200.0)
    assert d.action == ActionKind.SUGGEST_SEND_LATER
    assert "naira" in d.message.lower()
    assert "waiting" in d.message.lower() or "wait" in d.message.lower()


def test_strengthening_naira_without_remittance_stays_quiet():
    """No remittance planned → strengthening naira should not surface SUGGEST_SEND_LATER."""
    bills = sample_bills()
    buffer = CashBuffer(500_000.0)
    fx = _strengthening_fx(5.0)
    d = evaluate_buffer(bills, buffer, fx, remittance_planned_usd=None)
    assert d.action == ActionKind.QUIET


def test_strengthening_naira_below_threshold_stays_send_now():
    """Mild strengthening (<3%) with stable flag → falls through to SUGGEST_SEND_NOW."""
    bills = sample_bills()
    buffer = CashBuffer(500_000.0)
    # 1% strengthening — naira slightly stronger but under FX_STRENGTHENING_PCT
    fx = FxQuote(usd_ngn=1584.0, previous_usd_ngn=1600.0, as_of_label="mild-strengthen")
    assert abs(fx.pct_change) < FX_STRENGTHENING_PCT
    # pct_change is ~-1%, so <= 0.5 check passes → SUGGEST_SEND_NOW
    d = evaluate_buffer(bills, buffer, fx, remittance_planned_usd=200.0)
    assert d.action == ActionKind.SUGGEST_SEND_NOW


def test_strengthening_naira_shortfall_beats_strengthening():
    """Cash shortfall must still win even when naira is strengthening sharply."""
    bills = sample_bills()
    buffer = CashBuffer(100_000.0)  # well short of ~327,500
    fx = _strengthening_fx(5.0)
    d = evaluate_buffer(bills, buffer, fx, remittance_planned_usd=300.0)
    assert d.action == ActionKind.PING_SHORTFALL


# ---------------------------------------------------------------------------
# Fix 2: horizon_days in total_due + urgent bills in shortfall reason
# ---------------------------------------------------------------------------

def test_total_due_default_horizon_includes_all_sample_bills():
    """Default horizon=30 days must include every sample bill (max due_in_days=5)."""
    bills = sample_bills()
    assert total_due(bills) == total_due(bills, horizon_days=30)
    assert total_due(bills) == 250_000 + 24_500 + 8_000 + 45_000


def test_total_due_horizon_excludes_far_bills():
    """Bills past the horizon are excluded from the total."""
    bills = [
        Bill("Soon", 10_000.0, BillCategory.OTHER, due_in_days=2),
        Bill("Later", 20_000.0, BillCategory.OTHER, due_in_days=31),
    ]
    assert total_due(bills, horizon_days=30) == 10_000.0


def test_total_due_horizon_zero_excludes_all_bills_except_due_today():
    """horizon_days=0 includes only bills where due_in_days == 0."""
    bills = [
        Bill("Due today", 5_000.0, BillCategory.OTHER, due_in_days=0),
        Bill("Tomorrow", 3_000.0, BillCategory.OTHER, due_in_days=1),
    ]
    assert total_due(bills, horizon_days=0) == 5_000.0


def test_total_due_horizon_exactly_on_boundary():
    """A bill due exactly on the horizon boundary is included."""
    bills = [Bill("Boundary", 7_500.0, BillCategory.OTHER, due_in_days=5)]
    assert total_due(bills, horizon_days=5) == 7_500.0
    assert total_due(bills, horizon_days=4) == 0.0


def test_urgent_bills_returns_only_bills_within_urgent_days():
    """urgent_bills() returns only bills due within URGENT_DAYS."""
    bills = sample_bills()
    urgent = urgent_bills(bills)
    # All returned bills must be within threshold
    assert all(b.due_in_days <= URGENT_DAYS for b in urgent)
    # Must NOT include rent (due_in_days=5) or DSTV (due_in_days=3 == URGENT_DAYS exactly)
    # DSTV is at exactly 3 which equals URGENT_DAYS → included
    names = {b.name for b in urgent}
    assert "MTN data (15GB)" in names       # due_in_days=1
    assert "Generator fuel" in names        # due_in_days=2
    assert "DSTV Compact" in names          # due_in_days=3 (== URGENT_DAYS)
    assert "Rent (monthly share)" not in names  # due_in_days=5


def test_urgent_bills_sorted_soonest_first():
    bills = sample_bills()
    urgent = urgent_bills(bills)
    days = [b.due_in_days for b in urgent]
    assert days == sorted(days)


def test_shortfall_message_names_urgent_bills():
    """When there is a shortfall, the message must mention urgent bills."""
    bills = sample_bills()
    buffer = CashBuffer(100_000.0)  # guaranteed shortfall
    d = evaluate_buffer(bills, buffer, DEMO_FX_STABLE)
    assert d.action == ActionKind.PING_SHORTFALL
    # At least one urgent bill name must appear in the message
    urgent = urgent_bills(bills)
    assert any(b.name in d.message for b in urgent)


def test_shortfall_message_contains_urgent_label():
    """URGENT label must be present in the shortfall message when bills are urgent."""
    bills = sample_bills()
    buffer = CashBuffer(100_000.0)
    d = evaluate_buffer(bills, buffer, DEMO_FX_STABLE)
    assert "URGENT" in d.message or "urgent" in d.message.lower()


# ---------------------------------------------------------------------------
# Fix 3: remittance_planned_usd=0.0 treated same as None
# ---------------------------------------------------------------------------

def test_zero_remittance_is_quiet_not_send_now():
    """0.0 must not trigger SUGGEST_SEND_NOW — same as passing None."""
    bills = sample_bills()
    buffer = CashBuffer(400_000.0)
    d_zero = evaluate_buffer(bills, buffer, DEMO_FX_STABLE, remittance_planned_usd=0.0)
    d_none = evaluate_buffer(bills, buffer, DEMO_FX_STABLE, remittance_planned_usd=None)
    assert d_zero.action == ActionKind.QUIET
    assert d_none.action == ActionKind.QUIET
    assert d_zero.action == d_none.action


def test_zero_remittance_does_not_trigger_suggest_wait_on_spike():
    """0.0 must not trigger SUGGEST_WAIT — falls through to PING_FX_WATCH like None."""
    from bob_naira_assist.fx import DEMO_FX_SPIKE

    bills = sample_bills()
    buffer = CashBuffer(500_000.0)
    d_zero = evaluate_buffer(bills, buffer, DEMO_FX_SPIKE, remittance_planned_usd=0.0)
    d_none = evaluate_buffer(bills, buffer, DEMO_FX_SPIKE, remittance_planned_usd=None)
    assert d_zero.action == ActionKind.PING_FX_WATCH
    assert d_none.action == ActionKind.PING_FX_WATCH


def test_zero_remittance_does_not_trigger_suggest_send_later():
    """0.0 must not trigger SUGGEST_SEND_LATER when naira strengthens sharply."""
    bills = sample_bills()
    buffer = CashBuffer(500_000.0)
    fx = _strengthening_fx(5.0)
    d = evaluate_buffer(bills, buffer, fx, remittance_planned_usd=0.0)
    assert d.action == ActionKind.QUIET


def test_positive_small_remittance_still_triggers_send_now():
    """Any positive amount (even very small) is treated as a real planned remittance."""
    bills = sample_bills()
    buffer = CashBuffer(400_000.0)
    d = evaluate_buffer(bills, buffer, DEMO_FX_STABLE, remittance_planned_usd=0.01)
    assert d.action == ActionKind.SUGGEST_SEND_NOW


# ---------------------------------------------------------------------------
# run_send_later_scenario helper
# ---------------------------------------------------------------------------

def test_run_send_later_scenario_returns_suggest_send_later():
    """run_send_later_scenario must produce (lines, decision) with SUGGEST_SEND_LATER."""
    from bob_naira_assist.agent import run_send_later_scenario

    lines, decision = run_send_later_scenario()
    assert decision.action == ActionKind.SUGGEST_SEND_LATER


def test_run_send_later_scenario_lines_non_empty():
    """Scenario log lines must be a non-empty list of strings."""
    from bob_naira_assist.agent import run_send_later_scenario

    lines, _ = run_send_later_scenario()
    assert isinstance(lines, list)
    assert len(lines) > 0
    assert all(isinstance(line, str) for line in lines)


def test_run_send_later_scenario_decision_fields():
    """Decision must have a non-empty message, zero shortfall, and positive buffer."""
    from bob_naira_assist.agent import run_send_later_scenario

    _, decision = run_send_later_scenario()
    assert decision.message
    assert decision.shortfall_ngn == 0.0
    assert decision.buffer_ngn > 0.0


def test_run_send_later_scenario_fx_is_strengthening():
    """FX pct_change must be negative (naira strengthened) in the send-later scenario."""
    from bob_naira_assist.agent import run_send_later_scenario

    _, decision = run_send_later_scenario()
    assert decision.fx_pct_change < 0.0
