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


def run_quiet_scenario() -> Tuple[List[str], AgentDecision]:
    """Healthy buffer + stable FX → quiet (or mild send-now)."""
    bills = sample_bills()
    buffer = CashBuffer(balance_ngn=400_000.0)
    fx = mock_quote("stable")
    decision = evaluate_buffer(bills, buffer, fx, remittance_planned_usd=200.0)
    lines = [
        "=== BobNairaAssist DEMO — quiet / healthy run ===",
        "Bills:",
        *[format_bill_line(b) for b in bills],
        f"Buffer: ₦{buffer.balance_ngn:,.0f}",
        f"Decision: {decision.action.value}",
        f"Message: {decision.message}",
    ]
    return lines, decision


def run_alert_scenario() -> Tuple[List[str], AgentDecision]:
    """Tight buffer + FX spike → shortfall or FX wait ping."""
    bills = sample_bills()
    buffer = CashBuffer(balance_ngn=280_000.0)  # shortfall vs ~327.5k bills
    fx = mock_quote("spike")
    decision = evaluate_buffer(bills, buffer, fx, remittance_planned_usd=500.0)
    lines = [
        "=== BobNairaAssist DEMO — alert / shortfall run ===",
        "Bills:",
        *[format_bill_line(b) for b in bills],
        f"Buffer: ₦{buffer.balance_ngn:,.0f}",
        f"Decision: {decision.action.value}",
        f"Message: {decision.message}",
    ]
    return lines, decision


def run_fx_watch_scenario() -> Tuple[List[str], AgentDecision]:
    """Buffer OK but FX spiked → wait / FX watch."""
    bills = sample_bills()
    buffer = CashBuffer(balance_ngn=500_000.0)
    fx = mock_quote("spike")
    decision = evaluate_buffer(bills, buffer, fx, remittance_planned_usd=500.0)
    lines = [
        "=== BobNairaAssist DEMO — FX watch / wait run ===",
        "Bills:",
        *[format_bill_line(b) for b in bills],
        f"Buffer: ₦{buffer.balance_ngn:,.0f}",
        f"Decision: {decision.action.value}",
        f"Message: {decision.message}",
    ]
    return lines, decision


def run_demo_script() -> str:
    """Print quiet + alert story for CLI judges (deterministic)."""
    chunks: List[str] = []
    for runner in (run_quiet_scenario, run_alert_scenario, run_fx_watch_scenario):
        lines, _ = runner()
        chunks.append("\n".join(lines))
    footer = (
        "\n---\n"
        "DEMO_MODE=1: no IBM/watsonx credentials required.\n"
        "IBM Bob IDE is the planned core build partner (see AGENTS.md, bob_sessions/)."
    )
    return "\n\n".join(chunks) + footer
