# bob_sessions/

**Required for final LabLab submit:** IBM Bob IDE task reports + screenshots live here.

## Export steps (crisp)

1. Run an intentional multi-step Bob task (`docs/bob-workflow.md`, `AGENTS.md`).
2. Export the Bob task report from the IDE → save as `task-NN-topic.md`.
3. Screenshot the Bob task panel (context length, Bobcoins) → save as `task-NN-consumption.webp`.
4. Scrub secrets (no API keys, tokens, `.env` contents).
5. Commit under this folder and link it from the main README.

## Exported sessions

| Session | Artifacts | What Bob did |
|---------|-----------|--------------|
| **task-01** | [`task-01-architecture-review.md`](task-01-architecture-review.md) · [`task-01-consumption.webp`](task-01-consumption.webp) | Reviewed end-to-end architecture; identified three decision-logic gaps (send-now suggested during sharp naira strengthening, `total_due` ignoring `Bill.due_in_days`, `remittance_planned_usd=0.0` untested); produced a detailed findings report |
| **task-02** | [`task-02-fix-decision-gaps.md`](task-02-fix-decision-gaps.md) · [`task-02-consumption.webp`](task-02-consumption.webp) | Implemented all three fixes across `decisions.py`, `bills.py`, and `models.py`; wrote 17 new pytest cases in `tests/test_fixes.py` (19 → 36 passing) |
| **task-03** | [`task-03-ui-and-docs.md`](task-03-ui-and-docs.md) · [`task-03-consumption.webp`](task-03-consumption.webp) | Wired `SUGGEST_SEND_LATER` into `app.py` (ACTION_STYLE, Judge demo button, Playground "strengthen" FX scenario, urgent-bills warning box); added `run_send_later_scenario` helper and 4 new tests; refreshed README and this file |
| **task-04** | [`task-04-fx-sender-logic.md`](task-04-fx-sender-logic.md) · [`task-04-consumption.webp`](task-04-consumption.webp) | Fixed the backwards FX logic in `decisions.py`: a sharp naira weakening with a planned remittance now returns `SUGGEST_SEND_NOW` (favourable rate, "the move may revert") instead of `SUGGEST_WAIT` (deprecated, enum kept); updated `models.py`, `agent.py`, `app.py` beat 3 label, 3 test files, README and docs; 2 new tests (40 → 42 passing). 2.20 Bobcoins, 59.4k context |
