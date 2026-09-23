# Planned IBM Bob IDE workflow

Bob is the **core development partner** for this hackathon entry (judging requirement).
Until access is live, this doc is the contract for sessions we will run and export.

## Access paths

| Path | When | Notes |
|------|------|-------|
| Personal trial | Available now | May be used to start Bob tasks early |
| Hackathon Enterprise invite | ~kickoff Sep 25 2026 | ~40 Bobcoins expected — use for denser multi-step sessions |

Build window: **Sep 25–27 2026**. Submit by **Sep 27 15:00 UTC**.

## Planned Bob sessions (export each to `bob_sessions/`)

### Session 01 — Scaffold polish
- Goal: Review package layout, `app.py`, CLI `__main__`, ignore secrets.
- Deliverable: report + screenshot of Bob plan/diff.

### Session 02 — Tests
- Goal: Extend pytest coverage for `decisions.py` edge cases (exact shortfall boundary, FX thresholds).
- Deliverable: report showing Bob-authored or Bob-reviewed tests.

### Session 03 — Docs
- Goal: Tighten README quick start + architecture mermaid for judges.
- Deliverable: markdown export + screenshot.

### Session 04 — Remittance logic review
- Goal: Have Bob critique quiet-vs-ping priority and remittance wait/send heuristics; apply safe fixes.
- Deliverable: review notes in `bob_sessions/04-logic-review.md`.

## After each session

1. Export Bob task report → `bob_sessions/NN-*.md`
2. Add screenshots → `bob_sessions/NN-*.png`
3. Remove any secrets before commit
4. Update main README status from “pending” to linked artifacts

## What we will not claim

We will **not** claim Bob session reports already exist until files are present under
`bob_sessions/` (beyond this placeholder README).
