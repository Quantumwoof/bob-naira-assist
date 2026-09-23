"""DEMO_MODE agent script smoke tests."""

from bob_naira_assist.agent import run_alert_scenario, run_demo_script, run_quiet_scenario
from bob_naira_assist.models import ActionKind


def test_quiet_scenario_action():
    _, d = run_quiet_scenario()
    assert d.action in {ActionKind.QUIET, ActionKind.SUGGEST_SEND_NOW}


def test_alert_scenario_is_shortfall():
    _, d = run_alert_scenario()
    assert d.action == ActionKind.PING_SHORTFALL


def test_demo_script_mentions_both_runs():
    text = run_demo_script()
    assert "quiet" in text.lower()
    assert "alert" in text.lower()
    assert "DEMO_MODE=1" in text
