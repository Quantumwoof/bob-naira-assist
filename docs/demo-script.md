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
3. **FX wait** — buffer OK but spiked FX + remittance planned → `suggest_wait`

Optional (Playground / UI button): **Send now** — healthy buffer + stable FX + remittance → `suggest_send_now`.

## Minute 2:00 — Streamlit

Open **Judge demo** tab → click **1 · Quiet**, **2 · Shortfall ping**, **3 · FX wait**.
Optionally **Optional · Send now** or use **Playground** (buffer slider, FX `stable` / `watch` / `spike`).

Banner confirms **DEMO_MODE is ON**.

## Minute 2:30 — Bob as core component

Open `bob_sessions/README.md`. Show the three real Bob tasks: task-01 Bob reviewed the
architecture and found three decision-logic gaps; task-02 Bob fixed them with new tests;
task-03 Bob wired the new `suggest_send_later` outcome into the Streamlit UI and refreshed docs.
Show one consumption screenshot (about 3.1 Bobcoins used across all three).

## Minute 3:00 — Links

- Team page: https://lablab.ai/ai-hackathons/ibm-bob-2-hackathon/bobnairaassist
- Builder: Joshua Jubelo · Quantumwoof · Independent
- Checklist: `docs/submission-checklist.md`
