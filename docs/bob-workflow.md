# IBM Bob IDE workflow (as it actually ran)

Bob is the **core development partner** for this hackathon entry (judging requirement).
Access: hackathon Enterprise instance (40 Bobcoin budget). Build window **Sep 25–27 2026**.

The initial offline scaffold (package layout, first decision rules, Streamlit shell, first
tests) was written **before** Bob access and is not presented as Bob output.

## Sessions run (exports in `bob_sessions/`)

| # | Task given to Bob | Outcome | Bobcoins | Context |
|---|-------------------|---------|----------|---------|
| task-01 | Explain the architecture; walk through `evaluate_buffer`; list the top 3 decision-logic risks. **Read-only.** | Found 3 gaps: send-now during sharp naira strengthening; `total_due` ignoring `due_in_days`; `remittance_planned_usd=0.0` untested/ambiguous | 0.216 | 25.5k |
| task-02 | Fix all three gaps, add tests, update `docs/architecture.md`, run pytest | New `suggest_send_later` outcome, `horizon_days` + `urgent_bills()`, `_is_remittance_planned()`; 17 new tests (19 → **36 passing**) | 1.01 | 36.0k |
| task-03 | Wire `suggest_send_later` into Streamlit, add a scenario helper + tests, refresh README / `bob_sessions/README.md` | Send-later button, Playground `strengthen` FX, urgent-bills warning; `run_send_later_scenario` + 4 new tests → **40 passing** | 1.89 | 50.1k |
| task-04 | Fix the backwards FX logic: a sharp naira weakening is *favourable* for a USD→NGN sender, so beat 3 should not say "wait"; update code, tests and docs, run pytest | Beat 3 now `suggest_send_now` ("Rate moved in your favour… the move may revert"); naira strengthening → `suggest_send_later`; weakening with no remittance → `ping_fx_watch`; `suggest_wait` deprecated (enum kept); 2 new tests → **42 passing** | 2.20 | 59.4k |

Total ≈ **5.3 Bobcoins** of 40 (0.216 + 1.01 + 1.89 + 2.20) (figures from the consumption screenshots in `bob_sessions/`).

## Pattern that worked

1. **Review first, read-only** — let Bob read the whole repo and name concrete risks with file/function citations.
2. **Fix with guardrails** — one task that fixes, tests, documents, and runs `pytest`, with explicit "do not touch git / .env" limits.
3. **Ship to the UI** — a follow-up task that carries the new behaviour through to the user-facing app and docs, again ending with a test run.
4. **Correct from the user's point of view** — when a review of the demo showed the FX advice was backwards for a sender, one scoped Bob task fixed the logic, tests, UI labels and docs together.

## Next candidate Bob tasks

- Live FX adapter behind a feature flag (keep `DEMO_MODE` default), with Bob-generated contract tests.
- Optional watsonx.ai (Granite) layer to phrase decisions in plain English / Pidgin — decisions stay deterministic.
- CI workflow (`.github/workflows/ci.yml`) once the GitHub token has `workflow` scope.

## After each session

1. Export the Bob task report → `bob_sessions/task-NN-*.md`
2. Add the consumption screenshot → `bob_sessions/task-NN-consumption.webp`
3. Remove any secrets before commit
