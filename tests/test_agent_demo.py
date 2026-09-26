"""DEMO_MODE agent script smoke tests."""

from bob_naira_assist.agent import (
    run_alert_scenario,
    run_demo_script,
    run_fx_send_now_scenario,
    run_fx_wait_scenario,  # back-compat alias
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


def test_fx_send_now_scenario_is_suggest_send_now():
    """Beat 3: FX spike (naira weaker) + remittance → suggest_send_now (favourable rate)."""
    _, d = run_fx_send_now_scenario()
    assert d.action == ActionKind.SUGGEST_SEND_NOW
    assert d.fx_pct_change >= 3.0
    assert d.action != ActionKind.SUGGEST_WAIT


def test_fx_wait_scenario_alias_is_suggest_send_now():
    """Back-compat alias run_fx_wait_scenario must also return suggest_send_now now."""
    _, d = run_fx_wait_scenario()
    assert d.action == ActionKind.SUGGEST_SEND_NOW


def test_send_now_scenario_optional():
    _, d = run_send_now_scenario()
    assert d.action == ActionKind.SUGGEST_SEND_NOW


def test_demo_script_three_judge_beats():
    text = run_demo_script()
    assert "quiet" in text.lower()
    assert "shortfall" in text.lower()
    # Beat 3 is now "FX spike → send now"
    assert "send now" in text.lower() or "favourable" in text.lower()
    assert "Decision: quiet" in text
    assert "Decision: ping_shortfall" in text
    assert "Decision: suggest_send_now" in text
    assert "DEMO_MODE=1" in text
    # suggest_wait must not appear in the judge beat output
    assert "Decision: suggest_wait" not in text
