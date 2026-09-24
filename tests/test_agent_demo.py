"""DEMO_MODE agent script smoke tests."""

from bob_naira_assist.agent import (
    run_alert_scenario,
    run_demo_script,
    run_fx_wait_scenario,
    run_quiet_scenario,
    run_send_now_scenario,
)
from bob_naira_assist.models import ActionKind


def test_quiet_scenario_is_quiet():
    lines, d = run_quiet_scenario()
    assert d.action == ActionKind.QUIET
    assert d.shortfall_ngn == 0.0
    assert "no remittance" in "\n".join(lines).lower()


def test_alert_scenario_is_shortfall():
    _, d = run_alert_scenario()
    assert d.action == ActionKind.PING_SHORTFALL


def test_fx_wait_scenario_is_suggest_wait():
    _, d = run_fx_wait_scenario()
    assert d.action == ActionKind.SUGGEST_WAIT
    assert d.fx_pct_change >= 3.0


def test_send_now_scenario_optional():
    _, d = run_send_now_scenario()
    assert d.action == ActionKind.SUGGEST_SEND_NOW


def test_demo_script_three_judge_beats():
    text = run_demo_script()
    assert "quiet" in text.lower()
    assert "shortfall" in text.lower()
    assert "FX wait" in text or "fx wait" in text.lower()
    assert "Decision: quiet" in text
    assert "Decision: ping_shortfall" in text
    assert "Decision: suggest_wait" in text
    assert "DEMO_MODE=1" in text
    # send-now is optional; not a core CLI beat
    assert "Decision: suggest_send_now" not in text
