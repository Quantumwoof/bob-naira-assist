# bob_sessions/

**Required for final LabLab submit:** IBM Bob IDE task reports + screenshots live here.

## Export steps (crisp)

1. Run an intentional multi-step Bob task (`docs/bob-workflow.md`, `AGENTS.md`).
2. Export / copy the Bob task report or summary from the IDE → save as `NN-topic-report.md`.
3. Screenshot Bob plan, tool use, or diff review → save as `NN-topic.png`.
4. Scrub secrets (no API keys, tokens, `.env` contents).
5. Commit under this folder; link artifacts from the main README before **Sep 27 15:00 UTC**.

## Naming

| Artifact | Example |
|----------|---------|
| Session 01 report | `01-scaffold-report.md` |
| Session 01 screenshot | `01-scaffold.png` |
| Later sessions | `02-tests-report.md`, `03-docs-report.md`, … |

## Exported sessions

| Session | Artifacts | What Bob did |
|---------|-----------|--------------|
| **task-01** | [`task-01-architecture-review.md`](task-01-architecture-review.md) · [`task-01-consumption.webp`](task-01-consumption.webp) | Reviewed end-to-end architecture; identified three decision-logic gaps (send-now suggested during sharp naira strengthening, `total_due` ignoring `Bill.due_in_days`, `remittance_planned_usd=0.0` untested); produced a detailed findings report |
| **task-02** | [`task-02-fix-decision-gaps.md`](task-02-fix-decision-gaps.md) · [`task-02-consumption.webp`](task-02-consumption.webp) | Implemented all three fixes across `decisions.py`, `bills.py`, and `models.py`; wrote 20+ pytest cases in `tests/test_fixes.py`; all tests passing |
| **task-03** | [`task-03-ui-and-docs.md`](task-03-ui-and-docs.md) · [`task-03-consumption.webp`](task-03-consumption.webp) | Wired `SUGGEST_SEND_LATER` into `app.py` (ACTION_STYLE, Judge demo button, Playground "strengthen" FX scenario, urgent-bills warning box); added `run_send_later_scenario` helper and 4 new tests; refreshed README and this file |
