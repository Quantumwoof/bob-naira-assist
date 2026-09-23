# AGENTS.md — Working this repo in IBM Bob IDE

BobNairaAssist is built so **IBM Bob IDE** is a first-class collaborator, not an afterthought.
Theme: *turn idea into impact faster*.

## Product in one line

Nigeria remittance + everyday money assistant: bills (rent, DSTV, MTN data, generator fuel),
NGN cash buffer, mock USD/NGN FX, quiet-vs-ping decisions, remittance timing — **DEMO_MODE**
offline first; watsonx optional later.

## How to use Bob here

Prefer **intentional multi-step Bob tasks** over one-shot prompts. Example session goals:

1. **Scaffold polish** — tighten package layout, CLI, Streamlit entry, `.gitignore`.
2. **Generate / extend tests** — pure decision logic in `tests/` (no network).
3. **Write / refresh docs** — README quick start, architecture, demo script.
4. **Review remittance logic** — shortfall vs FX-watch priority, thresholds in `decisions.py`.

After each real Bob session: export the task report + screenshots into `bob_sessions/`
(see that folder’s README). Judges require Bob as a **core component**.

## Constraints Bob (and humans) must honor

- `DEMO_MODE=1` by default; do not require IBM/watsonx credentials for the offline demo.
- No secrets in git (no `.env` with keys, no passwords).
- Do not invent builder bio beyond Joshua Jubelo / Quantumwoof facts in the README.
- Session exports are empty until access lands — be honest in docs.

## Access notes

- **Personal trial** may be used for early Bob sessions before kickoff.
- **Hackathon Enterprise invite** (~40 Bobcoins) may arrive at kickoff (Sep 25–27 2026).
- Document whichever path was used when filling `bob_sessions/`.

## Local commands (no Bob required)

```bash
export DEMO_MODE=1
python -m bob_naira_assist          # deterministic quiet + alert + FX demo
pytest -q
streamlit run app.py
```
