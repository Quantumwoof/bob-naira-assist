# BobNairaAssist

**Nigeria remittance + everyday money assistant** — built to showcase **IBM Bob IDE** as the core development partner (*turn idea into impact faster*).

IBM Bob 2.0 LabLab hackathon · team **BobNairaAssist** · builder **Joshua Jubelo** (Quantumwoof) · Independent · Nigeria (Lokoja / Abuja)

[Team page](https://lablab.ai/ai-hackathons/ibm-bob-2-hackathon/bobnairaassist) · Contact: caughtsight007@gmail.com · Org: [Quantumwoof](https://github.com/Quantumwoof)

## What works today vs pending

| Status | Item |
|--------|------|
| **Works offline now** | `DEMO_MODE` CLI, Streamlit UI, pytest — 5 decision outcomes, bill-horizon filter, urgent-bill naming |
| **5 decision outcomes** | `quiet` · `ping_shortfall` (names urgent bills ≤3 days) · `ping_fx_watch` · `suggest_wait` · `suggest_send_now` · `suggest_send_later` (naira strengthening ≥3%) |
| **Bill-horizon / urgent bills** | `total_due` accepts `horizon_days`; shortfall message names bills due ≤3 days; Streamlit shows them in a warning box |
| **CI workflow** | `.github/workflows/ci.yml` ready locally (pytest on 3.11/3.12); push blocked until `gh` token has `workflow` scope |
| **Bob IDE sessions** | `bob_sessions/` holds real exported session reports (task-01 architecture review, task-02 decision fixes, task-03 UI & docs) |
| **Not required for demo** | watsonx / cloud LLM / live bank or FX APIs |

## Problem / who for / why an agent

**Who:** Nigerian households and diaspora helpers who pay rent, DSTV, MTN data, and generator fuel while timing USD→NGN remittances.

**Pain:** Constant rate and bill noise. People either over-check FX or miss a shortfall until DSTV or fuel is due.

**Why an agent:** Stay **quiet** when the NGN buffer covers bills and FX is calm; **ping** on shortfall or adverse FX; suggest **wait vs send now** for a planned remittance. Small, explainable tools — not a black-box chatbot.

## Judge demo beats (honest)

CLI / Streamlit **Judge demo** run three deterministic beats, plus two optional extras:

1. **Quiet** — buffer covers bills, stable FX, **no** remittance planned → `quiet`
2. **Shortfall ping** — buffer below bills → `ping_shortfall`; urgent bills due ≤3 days are named in the message and surfaced in the Streamlit warning box
3. **FX wait** — buffer OK, FX spike ≥3% (naira weaker), remittance planned → `suggest_wait`
4. **Optional · Send now** (Playground / `run_send_now_scenario`): buffer OK + stable FX + remittance → `suggest_send_now`
5. **Optional · Send later** (Playground / `run_send_later_scenario`): naira strengthening ≥3% (USD/NGN falling), remittance planned → `suggest_send_later` (advisory: fewer NGN per USD right now; consider waiting for a possible reversal)

All five outcomes are implemented in [`decisions.py`](bob_naira_assist/decisions.py), tested in [`tests/test_fixes.py`](tests/test_fixes.py), and wired into Streamlit [`app.py`](app.py).

## Architecture

```mermaid
flowchart LR
  subgraph inputs [DEMO_MODE inputs]
    Bills[Sample bills]
    Buffer[NGN cash buffer]
    FX[Mock USD/NGN]
  end
  subgraph core [bob_naira_assist]
    Eval[evaluate_buffer]
  end
  subgraph outs [Outputs]
    Quiet[Quiet]
    Ping[Ping]
    Timing[Wait / send now]
    UI[Streamlit]
    CLI[CLI demo]
  end
  Bills --> Eval
  Buffer --> Eval
  FX --> Eval
  Eval --> Quiet
  Eval --> Ping
  Eval --> Timing
  Eval --> UI
  Eval --> CLI
  Bob[IBM Bob IDE] -.->|build partner| core
  Bob -.-> bob_sessions
```

More detail: [`docs/architecture.md`](docs/architecture.md) · checklist: [`docs/submission-checklist.md`](docs/submission-checklist.md).

## Quick start (`DEMO_MODE`)

No IBM / watsonx / cloud LLM credentials required.

```bash
git clone https://github.com/Quantumwoof/bob-naira-assist.git
cd bob-naira-assist
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# optional editable install for console script:
# pip install -e ".[dev]"
export DEMO_MODE=1   # default if unset

pytest -q
python -m bob_naira_assist
# or: bob-naira-assist   (after pip install -e .)
streamlit run app.py
```

Optional env template (empty keys only): [`.env.example`](.env.example).

## How IBM Bob was used

Hackathon judging expects **IBM Bob IDE as a core component**. This repo is structured for that:

| Artifact | Purpose |
|----------|---------|
| [`AGENTS.md`](AGENTS.md) | How to run intentional multi-step Bob tasks on this codebase |
| [`docs/bob-workflow.md`](docs/bob-workflow.md) | Planned sessions: scaffold, tests, docs, remittance-logic review |
| [`bob_sessions/`](bob_sessions/) | Exported Bob IDE task reports + consumption screenshots (3 sessions) |

**Access:** Hackathon Enterprise instance (40 Bobcoin budget). The three sessions used about 3.1 Bobcoins in total. Build window **Sep 25–27 2026**.

### Honest status

Three real Bob IDE session exports are in `bob_sessions/`: task-01 (architecture review), task-02 (decision-logic fixes), task-03 (UI wiring + docs). Each includes a markdown report and a screenshot.

watsonx is optional later and is **not** required for the offline demo.

## Related prior work (cite only)

Earlier Quantumwoof experiments in the remittance / Naira space (separate repos; not copied here): `naira-pulse`, `edge-remit`, `voice-remit-ng`, `naira-remit`.


## Known limitations

| Blocker | Impact | Notes |
|---------|--------|-------|
| GitHub `workflow` OAuth scope | Cannot push `.github/workflows/ci.yml` to `main` yet | File ready locally; CI note in checklist |
| No watsonx / live FX | Offline DEMO only | Intentional for judge path |

## License

MIT © 2026 Joshua Jubelo (Quantumwoof)
