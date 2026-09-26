"""Streamlit UI for BobNairaAssist — offline DEMO_MODE judge path."""

from __future__ import annotations

import os

import streamlit as st

from bob_naira_assist.agent import (
    run_alert_scenario,
    run_fx_wait_scenario,
    run_quiet_scenario,
    run_send_later_scenario,
    run_send_now_scenario,
)
from bob_naira_assist.bills import format_bill_line, sample_bills, total_due, urgent_bills
from bob_naira_assist.decisions import evaluate_buffer
from bob_naira_assist.fx import mock_quote
from bob_naira_assist.models import ActionKind, AgentDecision, CashBuffer

os.environ.setdefault("DEMO_MODE", "1")

st.set_page_config(
    page_title="BobNairaAssist",
    page_icon="₦",
    layout="centered",
)

ACTION_STYLE = {
    ActionKind.QUIET: ("success", "🟢"),
    ActionKind.PING_SHORTFALL: ("error", "🔴"),
    ActionKind.PING_FX_WATCH: ("warning", "🟡"),
    ActionKind.SUGGEST_WAIT: ("warning", "🟠"),
    ActionKind.SUGGEST_SEND_NOW: ("info", "🔵"),
    ActionKind.SUGGEST_SEND_LATER: ("warning", "🟣"),
}


def fmt_ngn(amount: float) -> str:
    return f"₦{amount:,.0f}"


def render_decision(decision: AgentDecision, lines: list[str] | None = None) -> None:
    kind, emoji = ACTION_STYLE.get(decision.action, ("info", "⚪"))
    badge = f"{emoji} `{decision.action.value}`"
    if kind == "success":
        st.success(badge)
    elif kind == "error":
        st.error(badge)
    elif kind == "warning":
        st.warning(badge)
    else:
        st.info(badge)

    st.write(decision.message)
    m1, m2, m3 = st.columns(3)
    m1.metric("Buffer", fmt_ngn(decision.buffer_ngn))
    m2.metric("Bills total", fmt_ngn(decision.bills_total_ngn))
    shortfall_label = fmt_ngn(decision.shortfall_ngn) if decision.shortfall_ngn else "—"
    m3.metric("Shortfall", shortfall_label)
    st.caption(f"FX change: {decision.fx_pct_change:+.2f}%")
    if lines:
        with st.expander("Raw scenario log"):
            st.code("\n".join(lines), language="text")


st.title("BobNairaAssist")
st.warning(
    "**DEMO_MODE is ON** (default). Offline mock bills + FX only — "
    "no IBM / watsonx / cloud LLM credentials required."
)
st.caption(
    "Nigeria remittance + everyday money assistant · IBM Bob 2.0 LabLab demo · "
    "builder Joshua Jubelo (Quantumwoof)"
)

st.markdown(
    """
**Story:** Help a Nigeria-based household cover rent, DSTV, MTN data, and generator fuel,
watch NGN cash buffer vs bills, and time a USD→NGN remittance using mock FX — built to
showcase **IBM Bob IDE** as the core development partner.
"""
)

tab_demo, tab_play, tab_about = st.tabs(["Judge demo", "Playground", "About Bob"])

with tab_demo:
    st.subheader("Deterministic demo script")
    st.write(
        "Three judge beats (same as `python -m bob_naira_assist`). "
        "Optional extras: send-now and send-later (also in Playground)."
    )
    st.info(
        "Click a beat below to evaluate. Order for judges: "
        "**1 · Quiet** → **2 · Shortfall ping** → **3 · FX wait**. "
        "Quiet is never faked as a remittance decision."
    )
    if "judge_decision" not in st.session_state:
        st.session_state.judge_decision = None
        st.session_state.judge_lines = None
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("1 · Quiet", use_container_width=True, help="Buffer OK, stable FX, no remittance → quiet"):
            lines, decision = run_quiet_scenario()
            st.session_state.judge_decision = decision
            st.session_state.judge_lines = lines
    with c2:
        if st.button("2 · Shortfall ping", use_container_width=True, help="Buffer below bills → ping_shortfall (urgent bills named ≤3 days)"):
            lines, decision = run_alert_scenario()
            st.session_state.judge_decision = decision
            st.session_state.judge_lines = lines
    with c3:
        if st.button("3 · FX wait", use_container_width=True, help="Buffer OK, FX spike ≥3%, remittance planned → suggest_wait"):
            lines, decision = run_fx_wait_scenario()
            st.session_state.judge_decision = decision
            st.session_state.judge_lines = lines

    st.divider()
    co1, co2 = st.columns(2)
    with co1:
        if st.button("Optional · Send now", use_container_width=True, help="Buffer OK + stable FX + remittance → suggest_send_now"):
            lines, decision = run_send_now_scenario()
            st.session_state.judge_decision = decision
            st.session_state.judge_lines = lines
    with co2:
        if st.button("Optional · Send later", use_container_width=True, help="Naira strengthening ≥3% + remittance planned → suggest_send_later"):
            lines, decision = run_send_later_scenario()
            st.session_state.judge_decision = decision
            st.session_state.judge_lines = lines

    if st.session_state.judge_decision is None:
        st.caption("Empty state — pick a judge beat to see buffer, bills, and action.")
    else:
        dec = st.session_state.judge_decision
        render_decision(dec, st.session_state.judge_lines)
        if dec.action == ActionKind.PING_SHORTFALL:
            ub = urgent_bills(sample_bills())
            if ub:
                st.warning(
                    "**Urgent bills (due ≤ 3 days):** "
                    + ", ".join(f"{b.name} (₦{b.amount_ngn:,.0f}, {b.due_in_days}d)" for b in ub)
                )

with tab_play:
    st.subheader("Adjust buffer & FX")
    st.caption("DEMO_MODE playground — explore thresholds; not part of the three-beat judge story.")
    bills = sample_bills()
    st.markdown(f"**Sample bills** (total {fmt_ngn(total_due(bills))})")
    for b in bills:
        st.text(format_bill_line(b))

    buffer_ngn = st.slider("NGN cash buffer", 100_000, 600_000, 400_000, 10_000)
    fx_scenario = st.selectbox(
        "Mock FX scenario",
        ["stable", "watch", "spike", "strengthen"],
        help=(
            "stable: mild move · watch: naira weaker ~2.5% · "
            "spike: naira weaker 5% (suggest_wait with remittance) · "
            "strengthen: naira stronger ≥3% (suggest_send_later with remittance)"
        ),
    )
    remit_usd = st.number_input("Planned remittance (USD)", min_value=0, value=0, step=50)

    if st.button("Evaluate", type="primary"):
        decision = evaluate_buffer(
            bills,
            CashBuffer(balance_ngn=float(buffer_ngn)),
            mock_quote(fx_scenario),
            remittance_planned_usd=float(remit_usd) if remit_usd else None,
        )
        render_decision(decision)
        if decision.action == ActionKind.PING_SHORTFALL:
            ub = urgent_bills(bills)
            if ub:
                st.warning(
                    "**Urgent bills (due ≤ 3 days):** "
                    + ", ".join(f"{b.name} (₦{b.amount_ngn:,.0f}, {b.due_in_days}d)" for b in ub)
                )
        for d in decision.details:
            st.caption(d)

with tab_about:
    st.markdown(
        """
### IBM Bob IDE as core component
This MVP is scaffolded so **Bob** can own multi-step build tasks once hackathon access
lands (Enterprise invite ~40 Bobcoins at kickoff; personal trial usable now).

- See **AGENTS.md** and **docs/bob-workflow.md** for planned Bob sessions.
- Before final submit, export Bob task reports + screenshots into **bob_sessions/**.
- Session reports are **pending** until Bob IDE access — we do not claim they exist yet.

### Links
- Team: [BobNairaAssist on LabLab](https://lablab.ai/ai-hackathons/ibm-bob-2-hackathon/bobnairaassist)
- Builder: Joshua Jubelo (Quantumwoof) · Nigeria (Lokoja / Abuja)
- Contact: caughtsight007@gmail.com
"""
    )
