# Wire the new suggest_send_later outcome into the product and refresh the docs. (1) app.py: add ActionKind.SUGGEST_SEND_LATER to ACTION_STYLE with a distinct emoji/style, and make sure the Playground tab lets a user reproduce it (naira strengthening >=3% with a planned remittance) and shows urgent bills (due within 3 days) when there is a shortfall. (2) Add a run_send_later_scenario helper in bob_naira_assist/demo.py (or agent.py, wherever the other scenarios live) plus a pytest test for it. (3) README.md: update the 'What works today vs pending' table and the judge demo section to mention the five outcomes and the bill-horizon / urgent-bills behaviour; do not claim anything that is not implemented. (4) bob_sessions/README.md: replace the 'Placeholder only' status section with a short index of the real exported sessions in that folder (task-01-architecture-review.md + task-01-consumption.webp, task-02-fix-decision-gaps.md + task-02-consumption.webp, and this task as task-03-ui-and-docs.md + task-03-consumption.webp) with one line each on what Bob did. Then run `.venv/bin/python -m pytest -q` and `.venv/bin/python -c "import ast,sys; ast.parse(open('app.py').read())"` and show results. Do not touch git, do not commit, do not modify .env files, do not install packages.

---

**Status:** active  **Date:** 2026-09-26

---

### 👤 User

Wire the new suggest_send_later outcome into the product and refresh the docs. (1) app.py: add ActionKind.SUGGEST_SEND_LATER to ACTION_STYLE with a distinct emoji/style, and make sure the Playground tab lets a user reproduce it (naira strengthening >=3% with a planned remittance) and shows urgent bills (due within 3 days) when there is a shortfall. (2) Add a run_send_later_scenario helper in bob_naira_assist/demo.py (or agent.py, wherever the other scenarios live) plus a pytest test for it. (3) README.md: update the 'What works today vs pending' table and the judge demo section to mention the five outcomes and the bill-horizon / urgent-bills behaviour; do not claim anything that is not implemented. (4) bob_sessions/README.md: replace the 'Placeholder only' status section with a short index of the real exported sessions in that folder (task-01-architecture-review.md + task-01-consumption.webp, task-02-fix-decision-gaps.md + task-02-consumption.webp, and this task as task-03-ui-and-docs.md + task-03-consumption.webp) with one line each on what Bob did. Then run `.venv/bin/python -m pytest -q` and `.venv/bin/python -c "import ast,sys; ast.parse(open('app.py').read())"` and show results. Do not touch git, do not commit, do not modify .env files, do not install packages.

---

### 🤖 Assistant

> 🔧 called: update_todo_list



> 🔧 **update_todo_list** — 
[-] Read existing files to understand current state (app.py, decisions.py, demo/agent.py, README.md, bob_sessions/README.md)
[ ] Update app.py: add SUGGEST_SEND_LATER to ACTION_STYLE, update Playground tab for send-later scenario and urgent bills
[ ] Add run_send_later_scenario helper in demo.py/agent.py
[ ] Add pytest test for run_send_later_scenario
[ ] Update README.md: outcomes table and judge demo section
[ ] Update bob_sessions/README.md: replace placeholder with real session index
[ ] Run pytest and AST check, show results


### 🤖 Assistant

> 🔧 called: list_files, list_files, list_files



> 🔧 **list_files** — bob_sessions

> 🔧 **list_files** — bob_naira_assist

> 🔧 **list_files** — .

### 🤖 Assistant

> 🔧 called: read_file, read_file, read_file



> 🔧 **read_file** — app.py

> 🔧 **read_file** — bob_naira_assist/decisions.py

> 🔧 **read_file** — bob_naira_assist/models.py

### 🤖 Assistant

> 🔧 called: read_file, read_file, read_file



> 🔧 **read_file** — bob_naira_assist/agent.py

> 🔧 **read_file** — bob_naira_assist/demo.py

> 🔧 **read_file** — README.md

### 🤖 Assistant

> 🔧 called: read_file, read_file, read_file



> 🔧 **read_file** — bob_naira_assist/fx.py

> 🔧 **read_file** — bob_naira_assist/bills.py

> 🔧 **read_file** — bob_sessions/README.md

### 🤖 Assistant

> 🔧 called: read_file



> 🔧 **read_file** — tests/test_fixes.py

### 🤖 Assistant

> 🔧 called: update_todo_list

Now I have a complete picture of the codebase. Let me plan the changes:

1. **`fx.py`**: Need a "strengthen" scenario for the Playground dropdown
2. **`app.py`**: Add `SUGGEST_SEND_LATER` to `ACTION_STYLE`, update Playground (add "strengthen" to FX dropdown, import `run_send_later_scenario`, add button in judge demo, show urgent bills on shortfall)
3. **`agent.py`**: Add `run_send_later_scenario` helper
4. **`tests/test_fixes.py`** (or new file): Add test for `run_send_later_scenario`
5. **`README.md`**: Update outcomes table and judge demo section
6. **`bob_sessions/README.md`**: Replace placeholder status

> 🔧 **update_todo_list** — 
[x] Read existing files to understand current state (app.py, decisions.py, demo/agent.py, README.md, bob_sessions/README.md)
[-] Update app.py: add SUGGEST_SEND_LATER to ACTION_STYLE, update Playground tab for send-later scenario and urgent bills
[ ] Add run_send_later_scenario helper in agent.py
[ ] Add pytest test for run_send_later_scenario
[ ] Update README.md: outcomes table and judge demo section
[ ] Update bob_sessions/README.md: replace placeholder with real session index
[ ] Run pytest and AST check, show results


### 🤖 Assistant

> 🔧 called: apply_diff

I need to add a "strengthen" FX scenario to [`fx.py`](bob_naira_assist/fx.py) first, then update [`app.py`](app.py).

> 🔧 **apply_diff** — bob_naira_assist/fx.py

### 🤖 Assistant

> 🔧 called: apply_diff

Now update [`app.py`](app.py) — add `SUGGEST_SEND_LATER` to `ACTION_STYLE`, import `run_send_later_scenario`, update Playground to include "strengthen" in FX dropdown and show urgent bills, add 5th judge demo button:

> 🔧 **apply_diff** — app.py

### 🤖 Assistant

> 🔧 called: read_file

Some parts of the diff weren't applied (the judge demo button section). Let me check the current state:

> 🔧 **read_file** — app.py

### 🤖 Assistant

> 🔧 called: read_file



> 🔧 **read_file** — app.py

### 🤖 Assistant

> 🔧 called: apply_diff



> 🔧 **apply_diff** — app.py

### 🤖 Assistant

> 🔧 called: update_todo_list

Now add `run_send_later_scenario` to [`agent.py`](bob_naira_assist/agent.py) and update the footer message:

> 🔧 **update_todo_list** — 
[x] Read existing files to understand current state (app.py, decisions.py, demo/agent.py, README.md, bob_sessions/README.md)
[x] Update app.py: add SUGGEST_SEND_LATER to ACTION_STYLE, update Playground tab for send-later scenario and urgent bills
[-] Add run_send_later_scenario helper in agent.py
[ ] Add pytest test for run_send_later_scenario
[ ] Update README.md: outcomes table and judge demo section
[ ] Update bob_sessions/README.md: replace placeholder with real session index
[ ] Run pytest and AST check, show results


### 🤖 Assistant

> 🔧 called: apply_diff



> 🔧 **apply_diff** — <<<<<<< SEARCH
:start_line:56
-------
# Back-compat alias used by older docs/imports.
run_fx_watch_scenario = run_fx_wait_scenario


def run_send_now_scenario() -> Tuple[List[str], AgentDecision]:
    """Optional 4th beat: buffer OK + stable FX + remittance planned → suggest_send_now."""
    bills = sample_bills()
    buffer = CashBuffer(balance_ngn=400_000.0)
    fx = mock_quote("stable")
    decision = evaluate_buffer(bills, buffer, fx, remittance_planned_usd=200.0)
    return _scenario_lines("send now (optional)", buffer, decision, bills), decision


def run_demo_script() -> str:
    """Judge CLI story: quiet → shortfall → FX wait (send-now is optional/playground)."""
    chunks: List[str] = []
    for runner in (run_quiet_scenario, run_alert_scenario, run_fx_wait_scenario):
        lines, _ = runner()
        chunks.append("\n".join(lines))
    footer = (
        "\n---\n"
        "Judge beats: quiet → shortfall ping → FX wait.\n"
        "Optional send-now: playground / run_send_now_scenario (not part of the three-beat story).\n"
        "DEMO_MODE=1: no IBM/watsonx credentials required.\n"
        "IBM Bob IDE is the planned core build partner (see AGENTS.md, bob_sessions/)."
    )
    return "\n\n".join(chunks) + footer
=======
# Back-compat alias used by older docs/imports.
run_fx_watch_scenario = run_fx_wait_scenario


def run_send_now_scenario() -> Tuple[List[str], AgentDecision]:
    """Optional 4th beat: buffer OK + stable FX + remittance planned → suggest_send_now."""
    bills = sample_bills()
    buffer = CashBuffer(balance_ngn=400_000.0)
    fx = mock_quote("stable")
    decision = evaluate_buffer(bills, buffer, fx, remittance_planned_usd=200.0)
    return _scenario_lines("send now (optional)", buffer, decision, bills), decision


def run_send_later_scenario() -> Tuple[List[str], AgentDecision]:
    """Optional 5th beat: naira strengthening ≥3% + remittance planned → suggest_send_later.

    Buffer covers bills. USD/NGN has fallen ~3.1% (naira stronger), so sending now
    yields fewer naira per dollar than waiting might. The outcome is advisory only.
    """
    bills = sample_bills()
    buffer = CashBuffer(balance_ngn=500_000.0)
    fx = mock_quote("strengthen")  # ~3.1% naira strengthening
    decision = evaluate_buffer(bills, buffer, fx, remittance_planned_usd=300.0)
    return _scenario_lines("send later (optional)", buffer, decision, bills), decision


def run_demo_script() -> str:
    """Judge CLI story: quiet → shortfall → FX wait (send-now/send-later are optional/playground)."""
    chunks: List[str] = []
    for runner in (run_quiet_scenario, run_alert_scenario, run_fx_wait_scenario):
        lines, _ = runner()
        chunks.append("\n".join(lines))
    footer = (
        "\n---\n"
        "Judge beats: quiet → shortfall ping → FX wait.\n"
        "Optional: send-now (run_send_now_scenario) and send-later (run_send_later_scenario).\n"
        "DEMO_MODE=1: no IBM/watsonx credentials required.\n"
        "IBM Bob IDE is the planned core build partner (see AGENTS.md, bob_sessions/)."
    )
    return "\n\n".join(chunks) + footer
>>>>>>> REPLACE


### 🤖 Assistant

> 🔧 called: update_todo_list

Now add the test. I'll add it to [`tests/test_fixes.py`](tests/test_fixes.py) since that's the natural home:

> 🔧 **update_todo_list** — 
[x] Read existing files to understand current state (app.py, decisions.py, demo/agent.py, README.md, bob_sessions/README.md)
[x] Update app.py: add SUGGEST_SEND_LATER to ACTION_STYLE, update Playground tab for send-later scenario and urgent bills
[x] Add run_send_later_scenario helper in agent.py
[-] Add pytest test for run_send_later_scenario
[ ] Update README.md: outcomes table and judge demo section
[ ] Update bob_sessions/README.md: replace placeholder with real session index
[ ] Run pytest and AST check, show results


### 🤖 Assistant

> 🔧 called: insert_content



> 🔧 **insert_content** — tests/test_fixes.py

### 🤖 Assistant

> 🔧 called: update_todo_list

Now update the README and bob_sessions/README.md simultaneously:

> 🔧 **update_todo_list** — 
[x] Read existing files to understand current state (app.py, decisions.py, demo/agent.py, README.md, bob_sessions/README.md)
[x] Update app.py: add SUGGEST_SEND_LATER to ACTION_STYLE, update Playground tab for send-later scenario and urgent bills
[x] Add run_send_later_scenario helper in agent.py
[x] Add pytest test for run_send_later_scenario
[-] Update README.md: outcomes table and judge demo section
[ ] Update bob_sessions/README.md: replace placeholder with real session index
[ ] Run pytest and AST check, show results


### 🤖 Assistant

> 🔧 called: apply_diff



> 🔧 **apply_diff** — <<<<<<< SEARCH
:start_line:9
-------
## What works today vs pending

| Status | Item |
|--------|------|
| **Works offline now** | `DEMO_MODE` CLI (`python -m bob_naira_assist` / `bob-naira-assist`), Streamlit UI, pytest, mock bills + FX decisions |
| **CI workflow** | `.github/workflows/ci.yml` ready locally (pytest on 3.11/3.12); push blocked until `gh` token has `workflow` scope |
| **Pending Bob access** | Exported Bob IDE session reports + screenshots in `bob_sessions/` (placeholders only until trial/Enterprise invite) |
| **Not required for demo** | watsonx / cloud LLM / live bank or FX APIs |
=======
## What works today vs pending

| Status | Item |
|--------|------|
| **Works offline now** | `DEMO_MODE` CLI, Streamlit UI, pytest — 5 decision outcomes, bill-horizon filter, urgent-bill naming |
| **5 decision outcomes** | `quiet` · `ping_shortfall` (names urgent bills ≤3 days) · `ping_fx_watch` · `suggest_wait` · `suggest_send_now` · `suggest_send_later` (naira strengthening ≥3%) |
| **Bill-horizon / urgent bills** | `total_due` accepts `horizon_days`; shortfall message names bills due ≤3 days; Streamlit shows them in a warning box |
| **CI workflow** | `.github/workflows/ci.yml` ready locally (pytest on 3.11/3.12); push blocked until `gh` token has `workflow` scope |
| **Bob IDE sessions** | `bob_sessions/` holds real exported session reports (task-01 architecture review, task-02 decision fixes, task-03 UI & docs) |
| **Not required for demo** | watsonx / cloud LLM / live bank or FX APIs |
>>>>>>> REPLACE

<<<<<<< SEARCH
:start_line:27
-------
## Judge demo beats (honest)

CLI / Streamlit **Judge demo** run three deterministic beats:

1. **Quiet** — buffer covers bills, stable FX, **no** remittance planned → `quiet`
2. **Shortfall ping** — buffer below bills → `ping_shortfall`
3. **FX wait** — buffer OK, FX spike ≥3%, remittance planned → `suggest_wait`

**Optional 4th** (Playground / `run_send_now_scenario`): buffer OK + stable FX + remittance → `suggest_send_now`.
=======
## Judge demo beats (honest)

CLI / Streamlit **Judge demo** run three deterministic beats, plus two optional extras:

1. **Quiet** — buffer covers bills, stable FX, **no** remittance planned → `quiet`
2. **Shortfall ping** — buffer below bills → `ping_shortfall`; urgent bills due ≤3 days are named in the message and surfaced in the Streamlit warning box
3. **FX wait** — buffer OK, FX spike ≥3% (naira weaker), remittance planned → `suggest_wait`
4. **Optional · Send now** (Playground / `run_send_now_scenario`): buffer OK + stable FX + remittance → `suggest_send_now`
5. **Optional · Send later** (Playground / `run_send_later_scenario`): naira strengthening ≥3% (USD/NGN falling), remittance planned → `suggest_send_later` (advisory: fewer NGN per USD right now; consider waiting for a possible reversal)

All five outcomes are implemented in [`decisions.py`](bob_naira_assist/decisions.py), tested in [`tests/test_fixes.py`](tests/test_fixes.py), and wired into Streamlit [`app.py`](app.py).
>>>>>>> REPLACE


### 🤖 Assistant

> 🔧 called: apply_diff

Also fix the "honest status" paragraph in README.md further down:

> 🔧 **apply_diff** — <<<<<<< SEARCH
:start_line:103
-------
### Honest status

**Bob session reports are pending** until Bob IDE access is available. `bob_sessions/` currently holds placeholders only — we do not claim completed session exports yet.

watsonx is optional later and is **not** required for the offline demo.
=======
### Honest status

Three real Bob IDE session exports are in `bob_sessions/`: task-01 (architecture review), task-02 (decision-logic fixes), task-03 (UI wiring + docs). Each includes a markdown report and a screenshot.

watsonx is optional later and is **not** required for the offline demo.
>>>>>>> REPLACE


### 🤖 Assistant

> 🔧 called: update_todo_list

Now update bob_sessions/README.md:

> 🔧 **update_todo_list** — 
[x] Read existing files to understand current state (app.py, decisions.py, demo/agent.py, README.md, bob_sessions/README.md)
[x] Update app.py: add SUGGEST_SEND_LATER to ACTION_STYLE, update Playground tab for send-later scenario and urgent bills
[x] Add run_send_later_scenario helper in agent.py
[x] Add pytest test for run_send_later_scenario
[x] Update README.md: outcomes table and judge demo section
[-] Update bob_sessions/README.md: replace placeholder with real session index
[ ] Run pytest and AST check, show results


### 🤖 Assistant

> 🔧 called: apply_diff



> 🔧 **apply_diff** — <<<<<<< SEARCH
:start_line:21
-------
## Status

**Placeholder only** (`.gitkeep`). Session reports are **pending** until Bob IDE access
(personal trial and/or hackathon Enterprise invite ~40 Bobcoins at kickoff).

Do **not** claim completed Bob session exports until real files are here.
=======
## Exported sessions

| Session | Artifacts | What Bob did |
|---------|-----------|--------------|
| **task-01** | [`task-01-architecture-review.md`](task-01-architecture-review.md) · [`task-01-consumption.webp`](task-01-consumption.webp) | Reviewed end-to-end architecture; identified three decision-logic gaps (SUGGEST_SEND_LATER missing, horizon_days unimplemented, zero-remittance treated as planned); produced a detailed findings report |
| **task-02** | [`task-02-fix-decision-gaps.md`](task-02-fix-decision-gaps.md) · [`task-02-consumption.webp`](task-02-consumption.webp) | Implemented all three fixes across `decisions.py`, `bills.py`, and `models.py`; wrote 20+ pytest cases in `tests/test_fixes.py`; all tests passing |
| **task-03** | [`task-03-ui-and-docs.md`](task-03-ui-and-docs.md) · [`task-03-consumption.webp`](task-03-consumption.webp) | Wired `SUGGEST_SEND_LATER` into `app.py` (ACTION_STYLE, Judge demo button, Playground "strengthen" FX scenario, urgent-bills warning box); added `run_send_later_scenario` helper and 4 new tests; refreshed README and this file |
>>>>>>> REPLACE


### 🤖 Assistant

> 🔧 called: update_todo_list

Now run pytest and the AST check:

> 🔧 **update_todo_list** — 
[x] Read existing files to understand current state (app.py, decisions.py, demo/agent.py, README.md, bob_sessions/README.md)
[x] Update app.py: add SUGGEST_SEND_LATER to ACTION_STYLE, update Playground tab for send-later scenario and urgent bills
[x] Add run_send_later_scenario helper in agent.py
[x] Add pytest test for run_send_later_scenario
[x] Update README.md: outcomes table and judge demo section
[x] Update bob_sessions/README.md: replace placeholder with real session index
[-] Run pytest and AST check, show results


### 🤖 Assistant

> 🔧 called: execute_command



> 🔧 **execute_command** — .venv/bin/python -m pytest -q 2>&1

### 🤖 Assistant

> 🔧 called: execute_command



> 🔧 **execute_command** — .venv/bin/python -c "import ast,sys; ast.parse(open('app.py').read()); print('app.py: AST OK')"

### 🤖 Assistant

Both checks pass. Here's a summary of every change made:

---

## Changes summary

### [`bob_naira_assist/fx.py`](bob_naira_assist/fx.py)
- Added `DEMO_FX_STRENGTHEN` fixture (`usd_ngn=1550`, `previous=1600` → ~3.1% naira stronger)
- Added `"strengthen"` / `"strengthening"` branch in [`mock_quote()`](bob_naira_assist/fx.py:15)

### [`bob_naira_assist/agent.py`](bob_naira_assist/agent.py)
- Added [`run_send_later_scenario()`](bob_naira_assist/agent.py:69): buffer ₦500k (covers bills), `mock_quote("strengthen")`, ₦300 USD remittance → `SUGGEST_SEND_LATER`
- Updated `run_demo_script()` footer to mention both optional scenarios

### [`app.py`](app.py)
- Import: added `run_send_later_scenario`, `urgent_bills`
- [`ACTION_STYLE`](app.py:28): added `ActionKind.SUGGEST_SEND_LATER → ("warning", "🟣")`
- Judge demo tab: updated copy, updated button help text, split optional row into two side-by-side buttons (`Send now` + `Send later`)
- Judge demo output: shows a `st.warning` box listing urgent bills (≤3 days) when action is `PING_SHORTFALL`
- Playground tab: `st.selectbox` now includes `"strengthen"` with descriptive help text; same urgent-bills warning box on `PING_SHORTFALL` result

### [`tests/test_fixes.py`](tests/test_fixes.py)
- Added 4 tests for `run_send_later_scenario`:
  - `test_run_send_later_scenario_returns_suggest_send_later`
  - `test_run_send_later_scenario_lines_non_empty`
  - `test_run_send_later_scenario_decision_fields`
  - `test_run_send_later_scenario_fx_is_strengthening`

### [`README.md`](README.md)
- "What works today" table: replaced single row with 3 specific rows covering 5 outcomes, bill-horizon/urgent-bills behaviour, and real Bob session exports
- "Judge demo beats" section: expanded from 3 beats to 5 (with accurate descriptions), added cross-links to code files
- "Honest status" paragraph: replaced placeholder claim with accurate statement about the three exported sessions

### [`bob_sessions/README.md`](bob_sessions/README.md)
- Replaced `## Status / Placeholder only` section with `## Exported sessions` table listing task-01, task-02, and task-03 with one-line summaries of what Bob did in each session

**Validation:** `40 passed in 0.04s` · `app.py: AST OK`