# LabLab submission checklist (BobNairaAssist)

Use before the **Sep 27 2026 15:00 UTC** deadline.

## Demo path (must work offline)

- [ ] `DEMO_MODE=1` (default) — no secrets, no watsonx required
- [ ] `pytest -q` passes
- [ ] `python -m bob_naira_assist` shows: `quiet` → `ping_shortfall` → `suggest_wait`
- [ ] `streamlit run app.py` — Judge demo buttons match those actions
- [ ] Team link visible in README / About tab: https://lablab.ai/ai-hackathons/ibm-bob-2-hackathon/bobnairaassist

## Bob as core component

- [ ] Planned sessions documented in `docs/bob-workflow.md` + `AGENTS.md`
- [ ] Export Bob task reports + screenshots into `bob_sessions/` (see that folder’s README)
- [ ] No secrets / API keys in exports or `.env`
- [ ] README status updated from “pending” to linked artifacts once exports exist
- [ ] Do **not** invent or fake Bob session reports

## Repo hygiene

- [ ] `.env` with secrets never committed (`.env.example` only)
- [ ] `.pytest_cache/` / `*.egg-info/` gitignored and untracked
- [ ] CI green on `main` (add `.github/workflows/ci.yml` — needs GitHub `workflow` OAuth scope to push; file is ready in working tree)

## Builder facts (do not invent beyond)

Joshua Jubelo · Quantumwoof · caughtsight007@gmail.com · Independent · Lokoja / Abuja, Nigeria
