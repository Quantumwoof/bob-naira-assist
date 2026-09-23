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

Run `python -m bob_naira_assist`. Point to:

1. **Quiet / healthy** — buffer covers bills, stable FX.
2. **Alert / shortfall** — buffer too low → `ping_shortfall`.
3. **FX wait** — buffer OK but spiked FX → suggest wait before sending USD.

## Minute 2:00 — Streamlit

Open **Judge demo** tab → click the three buttons. Optionally use **Playground** to move
the NGN buffer slider and toggle mock FX.

## Minute 2:30 — Bob as core component

Open `AGENTS.md` + `docs/bob-workflow.md`. Explain planned Bob sessions and that
`bob_sessions/` will hold exported task reports + screenshots before final submit.
**Honest:** reports are pending until Bob IDE access (trial / Enterprise invite).

## Minute 3:00 — Links

- Team page: https://lablab.ai/ai-hackathons/ibm-bob-2-hackathon/bobnairaassist
- Builder: Joshua Jubelo · Quantumwoof · Independent
