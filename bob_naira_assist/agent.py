"""BobNairaAssist agent — DEMO_MODE deterministic runs (no cloud LLM)."""

from __future__ import annotations

import os
from typing import List, Tuple

from bob_naira_assist.bills import format_bill_line, sample_bills
from bob_naira_assist.decisions import evaluate_buffer
from bob_naira_assist.fx import mock_quote
from bob_naira_assist.models import AgentDecision, CashBuffer


def demo_mode_enabled() -> bool:
    return os.environ.get("DEMO_MODE", "1").strip() not in {"0", "false", "False", "no"}


def _scenario_lines(title: str, buffer: CashBuffer, decision: AgentDecision, bills) -> List[str]:
    return [
        f"=== BobNairaAssist DEMO — {title} ===",
        "Bills:",
        *[format_bill_line(b) for b in bills],
        f"Buffer: ₦{buffer.balance_ngn:,.0f}",
        f"Decision: {decision.action.value}",
        f"Message: {decision.message}",
    ]


def run_quiet_scenario() -> Tuple[List[str], AgentDecision]:
    """True quiet: buffer covers bills, stable FX, no remittance planned → quiet."""
    bills = sample_bills()
    buffer = CashBuffer(balance_ngn=400_000.0)
    fx = mock_quote("stable")
    decision = evaluate_buffer(bills, buffer, fx, remittance_planned_usd=None)
    return _scenario_lines("quiet (no remittance)", buffer, decision, bills), decision


def run_alert_scenario() -> Tuple[List[str], AgentDecision]:
    """Tight buffer → ping_shortfall (FX irrelevant once shortfall wins)."""
    bills = sample_bills()
    buffer = CashBuffer(balance_ngn=280_000.0)  # shortfall vs ₦327,500 bills
    fx = mock_quote("spike")
    decision = evaluate_buffer(bills, buffer, fx, remittance_planned_usd=500.0)
    return _scenario_lines("shortfall ping", buffer, decision, bills), decision


def run_fx_send_now_scenario() -> Tuple[List[str], AgentDecision]:
    """Buffer OK, FX spiked ≥3% (naira weaker) with remittance planned → suggest_send_now.

    A weakening naira is FAVOURABLE for the USD sender: each dollar now buys more NGN.
    The agent advises sending now (or splitting) before the rate potentially reverts.
    """
    bills = sample_bills()
    buffer = CashBuffer(balance_ngn=500_000.0)
    fx = mock_quote("spike")
    decision = evaluate_buffer(bills, buffer, fx, remittance_planned_usd=500.0)
    return _scenario_lines("FX spike → send now (favourable rate)", buffer, decision, bills), decision


# Back-compat aliases — old name pointed to the wrong economic story; kept so
# any existing imports or older docs do not break.
run_fx_wait_scenario = run_fx_send_now_scenario
run_fx_watch_scenario = run_fx_send_now_scenario


def run_send_now_scenario() -> Tuple[List[str], AgentDecision]:
    """Optional 4th beat: buffer OK + stable FX + remittance planned → suggest_send_now."""
    bills = sample_bills()
    buffer = CashBuffer(balance_ngn=400_000.0)
    fx = mock_quote("stable")
    decision = evaluate_buffer(bills, buffer, fx, remittance_planned_usd=200.0)
    return _scenario_lines("send now (optional)", buffer, decision, bills), decision


def run_send_later_scenario() -> Tuple[List[str], AgentDecision]:
    """Optional 5th beat: naira strengthening ≥3% + remittance planned → suggest_send_later.

    Buffer covers bills. USD/NGN has fallen ~3.1% (naira stronger), so sending now
    yields fewer naira per dollar than waiting might. The outcome is advisory only.
    """
    bills = sample_bills()
    buffer = CashBuffer(balance_ngn=500_000.0)
    fx = mock_quote("strengthen")  # ~3.1% naira strengthening
    decision = evaluate_buffer(bills, buffer, fx, remittance_planned_usd=300.0)
    return _scenario_lines("send later (optional)", buffer, decision, bills), decision


def run_demo_script() -> str:
    """Judge CLI story: quiet → shortfall → FX spike → send now (send-later is optional/playground)."""
    chunks: List[str] = []
    for runner in (run_quiet_scenario, run_alert_scenario, run_fx_send_now_scenario):
        lines, _ = runner()
        chunks.append("\n".join(lines))
    footer = (
        "\n---\n"
        "Judge beats: quiet → shortfall ping → FX spike → send now (favourable rate).\n"
        "Optional: send-later (run_send_later_scenario).\n"
        "DEMO_MODE=1: no IBM/watsonx credentials required.\n"
        "Built with IBM Bob IDE: exported task reports in bob_sessions/ (see AGENTS.md)."
    )
    return "\n\n".join(chunks) + footer
