# Demo script (≈2–3 minutes for judges)

**Prep:** `DEMO_MODE=1`, no API keys.

```bash
cd bob-naira-assist
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python -m bob_naira_assist
streamlit run app.py
```

## Minute 0:30 — Problem

Nigerian households juggle rent, DSTV, airtime/data, and generator fuel while watching
USD→NGN remittance timing. Noise is costly; an agent should stay **quiet** when safe and
**ping** on shortfall or FX stress.

## Minute 1:00 — CLI story

Run `python -m bob_naira_assist`. Point to the three judge beats:

1. **Quiet** — buffer covers bills, stable FX, **no** remittance planned → `quiet`
2. **Shortfall ping** — buffer too low → `ping_shortfall`
3. **FX spike → send now** — buffer OK, FX spiked ≥3% (naira weaker, **favourable for the sender**),
   remittance planned → `suggest_send_now`.
   Key insight: a weakening naira means each USD buys *more* NGN — the agent tells you to act
   before the rate reverts, not to wait.

Optional (Playground / UI button): **Send later** — naira strengthening ≥3% + remittance → `suggest_send_later`.

## Minute 2:00 — Streamlit

Open **Judge demo** tab → click **1 · Quiet**, **2 · Shortfall ping**, **3 · FX spike → send now**.
Optionally **Optional · Send later** or use **Playground** (buffer slider, FX `stable` / `watch` / `spike` / `strengthen`).

Banner confirms **DEMO_MODE is ON**.

## Minute 2:30 — Bob as core component

Open `bob_sessions/README.md`. Show the four real Bob tasks: task-01 Bob reviewed the
architecture and found three decision-logic gaps; task-02 Bob fixed them with new tests;
task-03 Bob wired the new `suggest_send_later` outcome into the Streamlit UI and refreshed docs;
task-04 Bob fixed the backwards FX-wait logic (naira weakening now favours sending).
Show one consumption screenshot (about 5.3 Bobcoins used across all four).

## Minute 3:00 — Links

- Team page: https://lablab.ai/ai-hackathons/ibm-bob-2-hackathon/bobnairaassist
- Builder: Joshua Jubelo · Quantumwoof · Independent
- Checklist: `docs/submission-checklist.md`
