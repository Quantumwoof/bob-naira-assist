"""Streamlit UI for BobNairaAssist — offline DEMO_MODE judge path."""

from __future__ import annotations

import os

import streamlit as st

from bob_naira_assist.agent import (
    run_alert_scenario,
    run_fx_watch_scenario,
    run_quiet_scenario,
)
from bob_naira_assist.bills import format_bill_line, sample_bills
from bob_naira_assist.decisions import evaluate_buffer
from bob_naira_assist.fx import mock_quote
from bob_naira_assist.models import CashBuffer

os.environ.setdefault("DEMO_MODE", "1")

st.set_page_config(
    page_title="BobNairaAssist",
    page_icon="₦",
    layout="centered",
)

st.title("BobNairaAssist")
st.caption(
    "Nigeria remittance + everyday money assistant · IBM Bob 2.0 LabLab demo · "
    "DEMO_MODE (no cloud LLM)"
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
    st.write("Three fixed scenarios — same logic as `python -m bob_naira_assist`.")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("1 · Quiet / healthy", use_container_width=True):
            lines, decision = run_quiet_scenario()
            st.code("\n".join(lines), language="text")
            st.success(decision.action.value)
    with col2:
        if st.button("2 · Shortfall alert", use_container_width=True):
            lines, decision = run_alert_scenario()
            st.code("\n".join(lines), language="text")
            st.warning(decision.action.value)
    with col3:
        if st.button("3 · FX wait", use_container_width=True):
            lines, decision = run_fx_watch_scenario()
            st.code("\n".join(lines), language="text")
            st.info(decision.action.value)

with tab_play:
    st.subheader("Adjust buffer & FX")
    bills = sample_bills()
    st.markdown("**Sample bills**")
    for b in bills:
        st.text(format_bill_line(b))

    buffer_ngn = st.slider("NGN cash buffer", 100_000, 600_000, 400_000, 10_000)
    fx_scenario = st.selectbox("Mock FX", ["stable", "spike"])
    remit_usd = st.number_input("Planned remittance (USD)", min_value=0, value=200, step=50)

    if st.button("Evaluate", type="primary"):
        decision = evaluate_buffer(
            bills,
            CashBuffer(balance_ngn=float(buffer_ngn)),
            mock_quote(fx_scenario),
            remittance_planned_usd=float(remit_usd) if remit_usd else None,
        )
        st.metric("Action", decision.action.value)
        st.write(decision.message)
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
