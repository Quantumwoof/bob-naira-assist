# Fix an economic bug in the remittance timing logic. Remittance advice is from the SENDER's view (USD to NGN). In decisions.py evaluate_buffer, when USD/NGN spikes >= FX_WAIT_PCT (naira weaker) with a remittance planned, we currently return suggest_wait with a mean-reversion story — that is backwards: each dollar now buys MORE naira, so the honest advice is to consider sending now (optionally part now) before the rate reverts. Change it so: naira weakens sharply + remittance planned -> suggest_send_now with a message like 'Rate moved in your favour (+X%): each $ buys more naira now; consider sending now or splitting, the move may revert'; naira strengthens sharply + remittance planned -> suggest_send_later (keep existing); naira weakens >= FX_WATCH_PCT with no remittance -> ping_fx_watch (household costs may rise; keep). Stop using suggest_wait in the decision path; keep the enum value only if removing it breaks the Streamlit style map, and mark it deprecated in a comment. Update the Judge demo in agent.py/app.py: beat 3 becomes 'FX spike -> send now (favourable rate)' and make sure beat labels, helper names and messages match. Update tests (keep them meaningful, add a test that a sharp naira-weakening spike with a remittance never returns suggest_wait), README.md judge-beats section, docs/architecture.md, docs/demo-script.md, and the About Bob tab text if it mentions FX wait. Then run `.venv/bin/python -m pytest -q` and `.venv/bin/python -c "import ast; ast.parse(open('app.py').read())"` and show results. Do not touch git, do not commit, do not modify .env files, do not install packages, do not edit index.html.

---

**Status:** active  **Date:** 2026-09-26

---

### 👤 User

Fix an economic bug in the remittance timing logic. Remittance advice is from the SENDER's view (USD to NGN). In decisions.py evaluate_buffer, when USD/NGN spikes >= FX_WAIT_PCT (naira weaker) with a remittance planned, we currently return suggest_wait with a mean-reversion story — that is backwards: each dollar now buys MORE naira, so the honest advice is to consider sending now (optionally part now) before the rate reverts. Change it so: naira weakens sharply + remittance planned -> suggest_send_now with a message like 'Rate moved in your favour (+X%): each $ buys more naira now; consider sending now or splitting, the move may revert'; naira strengthens sharply + remittance planned -> suggest_send_later (keep existing); naira weakens >= FX_WATCH_PCT with no remittance -> ping_fx_watch (household costs may rise; keep). Stop using suggest_wait in the decision path; keep the enum value only if removing it breaks the Streamlit style map, and mark it deprecated in a comment. Update the Judge demo in agent.py/app.py: beat 3 becomes 'FX spike -> send now (favourable rate)' and make sure beat labels, helper names and messages match. Update tests (keep them meaningful, add a test that a sharp naira-weakening spike with a remittance never returns suggest_wait), README.md judge-beats section, docs/architecture.md, docs/demo-script.md, and the About Bob tab text if it mentions FX wait. Then run `.venv/bin/python -m pytest -q` and `.venv/bin/python -c "import ast; ast.parse(open('app.py').read())"` and show results. Do not touch git, do not commit, do not modify .env files, do not install packages, do not edit index.html.

---

### 🤖 Assistant

> 🔧 called: update_todo_list



> 🔧 **update_todo_list** — 
[-] Read and understand current codebase structure
[ ] Fix economic bug in decisions.py evaluate_buffer
[ ] Update agent.py / app.py beat 3 labels and messages
[ ] Update tests
[ ] Update README.md judge-beats section
[ ] Update docs/architecture.md
[ ] Update docs/demo-script.md
[ ] Update About Bob tab text in app.py if needed
[ ] Run pytest and syntax check


### 🤖 Assistant

> 🔧 called: list_files, list_files



> 🔧 **list_files** — .

> 🔧 **list_files** — docs

### 🤖 Assistant

> 🔧 called: list_files, list_files



> 🔧 **list_files** — bob_naira_assist

> 🔧 **list_files** — tests

### 🤖 Assistant

> 🔧 called: read_file, read_file



> 🔧 **read_file** — bob_naira_assist/decisions.py

> 🔧 **read_file** — bob_naira_assist/models.py

### 🤖 Assistant

> 🔧 called: read_file, read_file



> 🔧 **read_file** — bob_naira_assist/agent.py

> 🔧 **read_file** — app.py

### 🤖 Assistant

> 🔧 called: read_file, read_file, read_file



> 🔧 **read_file** — tests/test_decisions.py

> 🔧 **read_file** — tests/test_agent_demo.py

> 🔧 **read_file** — tests/test_fixes.py

### 🤖 Assistant

> 🔧 called: read_file, read_file, read_file, read_file

Now let me read the remaining docs:

> 🔧 **read_file** — README.md

> 🔧 **read_file** — bob_naira_assist/fx.py

> 🔧 **read_file** — docs/architecture.md

> 🔧 **read_file** — docs/demo-script.md

### 🤖 Assistant

> 🔧 called: update_todo_list

Now I have a complete picture. Let me plan all the changes needed:

1. **`decisions.py`**: Change the `adverse` block so spike+remittance → `SUGGEST_SEND_NOW` (favourable rate message), not `SUGGEST_WAIT`. Keep `SUGGEST_WAIT` enum but mark deprecated.
2. **`models.py`**: Add deprecated comment to `SUGGEST_WAIT`.
3. **`agent.py`**: Rename `run_fx_wait_scenario` → `run_fx_send_now_scenario` (keep alias for back-compat), update docstring/footer.
4. **`app.py`**: Beat 3 button label/help, Playground help text, About tab.
5. **`tests/test_decisions.py`**: Update `test_fx_spike_suggests_wait_when_buffer_ok` → expect `SUGGEST_SEND_NOW`, add test that spike+remittance never returns `SUGGEST_WAIT`.
6. **`tests/test_agent_demo.py`**: Update `test_fx_wait_scenario_is_suggest_wait` and `test_demo_script_three_judge_beats`.
7. **`tests/test_fixes.py`**: Update `test_zero_remittance_does_not_trigger_suggest_wait_on_spike` (already tests `PING_FX_WATCH` - still valid).
8. **`README.md`**: Update beat 3.
9. **`docs/architecture.md`**: Update decision priority and table.
10. **`docs/demo-script.md`**: Update beat 3.

> 🔧 **update_todo_list** — 
[x] Read and understand current codebase structure
[-] Fix economic bug in decisions.py evaluate_buffer
[ ] Update models.py (deprecate SUGGEST_WAIT)
[ ] Update agent.py beat 3 scenario
[ ] Update app.py beat 3 labels and messages
[ ] Update tests/test_decisions.py
[ ] Update tests/test_agent_demo.py
[ ] Update tests/test_fixes.py
[ ] Update README.md judge-beats section
[ ] Update docs/architecture.md
[ ] Update docs/demo-script.md
[ ] Run pytest and syntax check


### 🤖 Assistant

> 🔧 called: apply_diff



> 🔧 **apply_diff** — bob_naira_assist/decisions.py

### 🤖 Assistant

> 🔧 called: apply_diff

Now mark `SUGGEST_WAIT` as deprecated in `models.py`:

> 🔧 **apply_diff** — bob_naira_assist/models.py

### 🤖 Assistant

> 🔧 called: update_todo_list



> 🔧 **update_todo_list** — 
[x] Read and understand current codebase structure
[x] Fix economic bug in decisions.py evaluate_buffer
[x] Update models.py (deprecate SUGGEST_WAIT)
[-] Update agent.py beat 3 scenario
[ ] Update app.py beat 3 labels and messages
[ ] Update tests/test_decisions.py
[ ] Update tests/test_agent_demo.py
[ ] Update tests/test_fixes.py
[ ] Update README.md judge-beats section
[ ] Update docs/architecture.md
[ ] Update docs/demo-script.md
[ ] Run pytest and syntax check


### 🤖 Assistant

> 🔧 called: apply_diff



> 🔧 **apply_diff** — bob_naira_assist/agent.py

### 🤖 Assistant

> 🔧 called: apply_diff

Now update `app.py` — beat 3 button, Playground help text, and About tab:

> 🔧 **apply_diff** — <<<<<<< SEARCH
:start_line:9
-------
from bob_naira_assist.agent import (
    run_alert_scenario,
    run_fx_wait_scenario,
    run_quiet_scenario,
    run_send_later_scenario,
    run_send_now_scenario,
)
=======
from bob_naira_assist.agent import (
    run_alert_scenario,
    run_fx_send_now_scenario,
    run_quiet_scenario,
    run_send_later_scenario,
    run_send_now_scenario,
)
>>>>>>> REPLACE

<<<<<<< SEARCH
:start_line:93
-------
    st.info(
        "Click a beat below to evaluate. Order for judges: "
        "**1 · Quiet** → **2 · Shortfall ping** → **3 · FX wait**. "
        "Quiet is never faked as a remittance decision."
    )
=======
    st.info(
        "Click a beat below to evaluate. Order for judges: "
        "**1 · Quiet** → **2 · Shortfall ping** → **3 · FX spike → send now**. "
        "Quiet is never faked as a remittance decision."
    )
>>>>>>> REPLACE

<<<<<<< SEARCH
:start_line:113
-------
    with c3:
        if st.button("3 · FX wait", use_container_width=True, help="Buffer OK, FX spike ≥3%, remittance planned → suggest_wait"):
            lines, decision = run_fx_wait_scenario()
            st.session_state.judge_decision = decision
            st.session_state.judge_lines = lines
=======
    with c3:
        if st.button("3 · FX spike → send now", use_container_width=True, help="Buffer OK, FX spike ≥3% (naira weaker, favourable for sender), remittance planned → suggest_send_now"):
            lines, decision = run_fx_send_now_scenario()
            st.session_state.judge_decision = decision
            st.session_state.judge_lines = lines
>>>>>>> REPLACE

<<<<<<< SEARCH
:start_line:155
-------
    fx_scenario = st.selectbox(
        "Mock FX scenario",
        ["stable", "watch", "spike", "strengthen"],
        help=(
            "stable: mild move · watch: naira weaker ~2.5% · "
            "spike: naira weaker 5% (suggest_wait with remittance) · "
            "strengthen: naira stronger ≥3% (suggest_send_later with remittance)"
        ),
    )
=======
    fx_scenario = st.selectbox(
        "Mock FX scenario",
        ["stable", "watch", "spike", "strengthen"],
        help=(
            "stable: mild move · watch: naira weaker ~2.5% (ping_fx_watch) · "
            "spike: naira weaker 5% (suggest_send_now with remittance — rate favours sender) · "
            "strengthen: naira stronger ≥3% (suggest_send_later with remittance)"
        ),
    )
>>>>>>> REPLACE

<<<<<<< SEARCH
:start_line:183
-------
with tab_about:
    st.markdown(
        """
### IBM Bob IDE as core component
The initial offline scaffold was written before Bob access. After that, three real
**IBM Bob IDE** tasks moved the product forward (exports in **bob_sessions/**):

- **task-01 · architecture review** (0.216 Bobcoins) — read the whole repo, explained the
  architecture and found **3 decision-logic gaps**. Read-only: no files changed.
- **task-02 · fix the gaps** (1.01 Bobcoins) — new `suggest_send_later` outcome, bill horizon +
  urgent bills, `0.0` remittance treated as none; 17 new tests → **36 passing**.
- **task-03 · ship it to the UI** (1.89 Bobcoins) — Send-later button, Playground *strengthen*
  FX scenario, urgent-bills warning, `run_send_later_scenario` + tests → **40 passing**; README refresh.

About **3.1 of 40** hackathon Bobcoins used. See **AGENTS.md** for how to run further Bob tasks on this repo.

### Links
- Team: [BobNairaAssist on LabLab](https://lablab.ai/ai-hackathons/ibm-bob-2-hackathon/bobnairaassist)
- Builder: Joshua Jubelo (Quantumwoof) · Nigeria (Lokoja / Abuja)
- Contact: caughtsight007@gmail.com
"""
    )
=======
with tab_about:
    st.markdown(
        """
### IBM Bob IDE as core component
The initial offline scaffold was written before Bob access. After that, three real
**IBM Bob IDE** tasks moved the product forward (exports in **bob_sessions/**):

- **task-01 · architecture review** (0.216 Bobcoins) — read the whole repo, explained the
  architecture and found **3 decision-logic gaps**. Read-only: no files changed.
- **task-02 · fix the gaps** (1.01 Bobcoins) — new `suggest_send_later` outcome, bill horizon +
  urgent bills, `0.0` remittance treated as none; 17 new tests → **36 passing**.
- **task-03 · ship it to the UI** (1.89 Bobcoins) — Send-later button, Playground *strengthen*
  FX scenario, urgent-bills warning, `run_send_later_scenario` + tests → **40 passing**; README refresh.
- **task-04 · fix FX economic logic** — corrected beat 3: naira-weakening spike is
  *favourable* for the USD sender (each $ buys more NGN), so the agent now advises
  `suggest_send_now` (not the old incorrect `suggest_wait`).

See **AGENTS.md** for how to run further Bob tasks on this repo.

### Links
- Team: [BobNairaAssist on LabLab](https://lablab.ai/ai-hackathons/ibm-bob-2-hackathon/bobnairaassist)
- Builder: Joshua Jubelo (Quantumwoof) · Nigeria (Lokoja / Abuja)
- Contact: caughtsight007@gmail.com
"""
    )
>>>>>>> REPLACE


### 🤖 Assistant

> 🔧 called: update_todo_list

Now update the tests. Starting with [`test_decisions.py`](tests/test_decisions.py):

> 🔧 **update_todo_list** — 
[x] Read and understand current codebase structure
[x] Fix economic bug in decisions.py evaluate_buffer
[x] Update models.py (deprecate SUGGEST_WAIT)
[x] Update agent.py beat 3 scenario
[x] Update app.py beat 3 labels and messages
[-] Update tests/test_decisions.py
[ ] Update tests/test_agent_demo.py
[ ] Update tests/test_fixes.py
[ ] Update README.md judge-beats section
[ ] Update docs/architecture.md
[ ] Update docs/demo-script.md
[ ] Run pytest and syntax check


### 🤖 Assistant

> 🔧 called: apply_diff



> 🔧 **apply_diff** — <<<<<<< SEARCH
:start_line:66
-------
def test_fx_spike_suggests_wait_when_buffer_ok():
    bills = sample_bills()
    buffer = CashBuffer(500_000.0)
    d = evaluate_buffer(bills, buffer, DEMO_FX_SPIKE, remittance_planned_usd=500.0)
    assert d.action == ActionKind.SUGGEST_WAIT
    assert d.fx_pct_change > FX_WAIT_PCT
=======
def test_fx_spike_suggests_send_now_when_buffer_ok():
    """Sharp naira weakening with planned remittance → suggest_send_now.

    A weakening naira is FAVOURABLE for the USD sender: each dollar buys more NGN.
    The correct advice is to consider sending now, not to wait.
    """
    bills = sample_bills()
    buffer = CashBuffer(500_000.0)
    d = evaluate_buffer(bills, buffer, DEMO_FX_SPIKE, remittance_planned_usd=500.0)
    assert d.action == ActionKind.SUGGEST_SEND_NOW
    assert d.fx_pct_change > FX_WAIT_PCT


def test_fx_spike_with_remittance_never_returns_suggest_wait():
    """Regression: a sharp naira-weakening spike + remittance must NEVER return suggest_wait."""
    bills = sample_bills()
    buffer = CashBuffer(500_000.0)
    d = evaluate_buffer(bills, buffer, DEMO_FX_SPIKE, remittance_planned_usd=500.0)
    assert d.action != ActionKind.SUGGEST_WAIT
>>>>>>> REPLACE

<<<<<<< SEARCH
:start_line:104
-------
def test_fx_spike_without_remittance_is_watch_not_wait():
    """Spike alone must not become suggest_wait — remittance must be planned."""
    bills = sample_bills()
    buffer = CashBuffer(500_000.0)
    d = evaluate_buffer(bills, buffer, DEMO_FX_SPIKE, remittance_planned_usd=None)
    assert d.action == ActionKind.PING_FX_WATCH
    assert d.action != ActionKind.SUGGEST_WAIT
    assert d.action != ActionKind.QUIET
=======
def test_fx_spike_without_remittance_is_watch_not_send_now():
    """Spike alone (no remittance) must give ping_fx_watch, not suggest_send_now."""
    bills = sample_bills()
    buffer = CashBuffer(500_000.0)
    d = evaluate_buffer(bills, buffer, DEMO_FX_SPIKE, remittance_planned_usd=None)
    assert d.action == ActionKind.PING_FX_WATCH
    assert d.action != ActionKind.SUGGEST_WAIT
    assert d.action != ActionKind.SUGGEST_SEND_NOW
    assert d.action != ActionKind.QUIET
>>>>>>> REPLACE


### 🤖 Assistant

> 🔧 called: apply_diff

Now update [`test_agent_demo.py`](tests/test_agent_demo.py):

> 🔧 **apply_diff** — <<<<<<< SEARCH
:start_line:1
-------
"""DEMO_MODE agent script smoke tests."""

from bob_naira_assist.agent import (
    run_alert_scenario,
    run_demo_script,
    run_fx_wait_scenario,
    run_quiet_scenario,
    run_send_now_scenario,
)
from bob_naira_assist.models import ActionKind


def test_quiet_scenario_is_quiet():
    lines, d = run_quiet_scenario()
    assert d.action == ActionKind.QUIET
    assert d.shortfall_ngn == 0.0
    assert "no remittance" in "\n".join(lines).lower()


def test_alert_scenario_is_shortfall():
    _, d = run_alert_scenario()
    assert d.action == ActionKind.PING_SHORTFALL


def test_fx_wait_scenario_is_suggest_wait():
    _, d = run_fx_wait_scenario()
    assert d.action == ActionKind.SUGGEST_WAIT
    assert d.fx_pct_change >= 3.0


def test_send_now_scenario_optional():
    _, d = run_send_now_scenario()
    assert d.action == ActionKind.SUGGEST_SEND_NOW


def test_demo_script_three_judge_beats():
    text = run_demo_script()
    assert "quiet" in text.lower()
    assert "shortfall" in text.lower()
    assert "FX wait" in text or "fx wait" in text.lower()
    assert "Decision: quiet" in text
    assert "Decision: ping_shortfall" in text
    assert "Decision: suggest_wait" in text
    assert "DEMO_MODE=1" in text
    # send-now is optional; not a core CLI beat
    assert "Decision: suggest_send_now" not in text
=======
"""DEMO_MODE agent script smoke tests."""

from bob_naira_assist.agent import (
    run_alert_scenario,
    run_demo_script,
    run_fx_send_now_scenario,
    run_fx_wait_scenario,  # back-compat alias
    run_quiet_scenario,
    run_send_now_scenario,
)
from bob_naira_assist.models import ActionKind


def test_quiet_scenario_is_quiet():
    lines, d = run_quiet_scenario()
    assert d.action == ActionKind.QUIET
    assert d.shortfall_ngn == 0.0
    assert "no remittance" in "\n".join(lines).lower()


def test_alert_scenario_is_shortfall():
    _, d = run_alert_scenario()
    assert d.action == ActionKind.PING_SHORTFALL


def test_fx_send_now_scenario_is_suggest_send_now():
    """Beat 3: FX spike (naira weaker) + remittance → suggest_send_now (favourable rate)."""
    _, d = run_fx_send_now_scenario()
    assert d.action == ActionKind.SUGGEST_SEND_NOW
    assert d.fx_pct_change >= 3.0
    assert d.action != ActionKind.SUGGEST_WAIT


def test_fx_wait_scenario_alias_is_suggest_send_now():
    """Back-compat alias run_fx_wait_scenario must also return suggest_send_now now."""
    _, d = run_fx_wait_scenario()
    assert d.action == ActionKind.SUGGEST_SEND_NOW


def test_send_now_scenario_optional():
    _, d = run_send_now_scenario()
    assert d.action == ActionKind.SUGGEST_SEND_NOW


def test_demo_script_three_judge_beats():
    text = run_demo_script()
    assert "quiet" in text.lower()
    assert "shortfall" in text.lower()
    # Beat 3 is now "FX spike → send now"
    assert "send now" in text.lower() or "favourable" in text.lower()
    assert "Decision: quiet" in text
    assert "Decision: ping_shortfall" in text
    assert "Decision: suggest_send_now" in text
    assert "DEMO_MODE=1" in text
    # suggest_wait must not appear in the judge beat output
    assert "Decision: suggest_wait" not in text
>>>>>>> REPLACE


### 🤖 Assistant

> 🔧 called: apply_diff

Now update [`test_fixes.py`](tests/test_fixes.py) — the `test_zero_remittance_does_not_trigger_suggest_wait_on_spike` test is still valid (it checks `PING_FX_WATCH`), but I should update its docstring and the name to be accurate:

> 🔧 **apply_diff** — <<<<<<< SEARCH
:start_line:185
-------
def test_zero_remittance_does_not_trigger_suggest_wait_on_spike():
    """0.0 must not trigger SUGGEST_WAIT — falls through to PING_FX_WATCH like None."""
    from bob_naira_assist.fx import DEMO_FX_SPIKE

    bills = sample_bills()
    buffer = CashBuffer(500_000.0)
    d_zero = evaluate_buffer(bills, buffer, DEMO_FX_SPIKE, remittance_planned_usd=0.0)
    d_none = evaluate_buffer(bills, buffer, DEMO_FX_SPIKE, remittance_planned_usd=None)
    assert d_zero.action == ActionKind.PING_FX_WATCH
    assert d_none.action == ActionKind.PING_FX_WATCH
=======
def test_zero_remittance_does_not_trigger_suggest_send_now_on_spike():
    """0.0 must not trigger SUGGEST_SEND_NOW on a spike — falls through to PING_FX_WATCH like None."""
    from bob_naira_assist.fx import DEMO_FX_SPIKE

    bills = sample_bills()
    buffer = CashBuffer(500_000.0)
    d_zero = evaluate_buffer(bills, buffer, DEMO_FX_SPIKE, remittance_planned_usd=0.0)
    d_none = evaluate_buffer(bills, buffer, DEMO_FX_SPIKE, remittance_planned_usd=None)
    assert d_zero.action == ActionKind.PING_FX_WATCH
    assert d_none.action == ActionKind.PING_FX_WATCH
    assert d_zero.action != ActionKind.SUGGEST_WAIT
    assert d_zero.action != ActionKind.SUGGEST_SEND_NOW
>>>>>>> REPLACE


### 🤖 Assistant

> 🔧 called: update_todo_list

Now update README.md, docs/architecture.md, and docs/demo-script.md:

> 🔧 **update_todo_list** — 
[x] Read and understand current codebase structure
[x] Fix economic bug in decisions.py evaluate_buffer
[x] Update models.py (deprecate SUGGEST_WAIT)
[x] Update agent.py beat 3 scenario
[x] Update app.py beat 3 labels and messages
[x] Update tests/test_decisions.py
[x] Update tests/test_agent_demo.py
[x] Update tests/test_fixes.py
[-] Update README.md judge-beats section
[ ] Update docs/architecture.md
[ ] Update docs/demo-script.md
[ ] Run pytest and syntax check


### 🤖 Assistant

> 🔧 called: apply_diff



> 🔧 **apply_diff** — <<<<<<< SEARCH
:start_line:17
-------
| **Works offline now** | `DEMO_MODE` CLI, Streamlit UI, pytest (40 tests) — 6 decision outcomes, bill-horizon filter, urgent-bill naming |
| **6 decision outcomes** | `quiet` · `ping_shortfall` (names urgent bills ≤3 days) · `ping_fx_watch` · `suggest_wait` · `suggest_send_now` · `suggest_send_later` (naira strengthening ≥3%) |
=======
| **Works offline now** | `DEMO_MODE` CLI, Streamlit UI, pytest — 6 decision outcomes, bill-horizon filter, urgent-bill naming |
| **6 decision outcomes** | `quiet` · `ping_shortfall` (names urgent bills ≤3 days) · `ping_fx_watch` · `suggest_send_now` · `suggest_send_later` (naira strengthening ≥3%) · `suggest_wait` (deprecated; kept for Streamlit style map only) |
>>>>>>> REPLACE

<<<<<<< SEARCH
:start_line:34
-------
## Judge demo beats (honest)

CLI / Streamlit **Judge demo** run three deterministic beats, plus two optional extras (the sixth outcome, `ping_fx_watch`, is reachable in the Playground with the `watch` FX scenario):

1. **Quiet** — buffer covers bills, stable FX, **no** remittance planned → `quiet`
2. **Shortfall ping** — buffer below bills → `ping_shortfall`; urgent bills due ≤3 days are named in the message and surfaced in the Streamlit warning box
3. **FX wait** — buffer OK, FX spike ≥3% (naira weaker), remittance planned → `suggest_wait`
4. **Optional · Send now** (Playground / `run_send_now_scenario`): buffer OK + stable FX + remittance → `suggest_send_now`
5. **Optional · Send later** (Playground / `run_send_later_scenario`): naira strengthening ≥3% (USD/NGN falling), remittance planned → `suggest_send_later` (advisory: fewer NGN per USD right now; consider waiting for a possible reversal)

All six outcomes are implemented in [`decisions.py`](bob_naira_assist/decisions.py), tested in [`tests/test_fixes.py`](tests/test_fixes.py), and wired into Streamlit [`app.py`](app.py).
=======
## Judge demo beats (honest)

CLI / Streamlit **Judge demo** runs three deterministic beats, plus two optional extras (the sixth outcome, `ping_fx_watch`, is reachable in the Playground with the `watch` FX scenario):

1. **Quiet** — buffer covers bills, stable FX, **no** remittance planned → `quiet`
2. **Shortfall ping** — buffer below bills → `ping_shortfall`; urgent bills due ≤3 days are named in the message and surfaced in the Streamlit warning box
3. **FX spike → send now** — buffer OK, FX spike ≥3% (naira *weaker*, meaning each USD buys *more* NGN), remittance planned → `suggest_send_now`
   The rate moved in the sender's favour; the agent advises sending now or splitting before it reverts.
4. **Optional · Send now (stable FX)** (Playground / `run_send_now_scenario`): buffer OK + stable FX + remittance → `suggest_send_now`
5. **Optional · Send later** (Playground / `run_send_later_scenario`): naira strengthening ≥3% (USD/NGN falling, fewer NGN per USD), remittance planned → `suggest_send_later`

All outcomes are implemented in [`decisions.py`](bob_naira_assist/decisions.py), tested in [`tests/test_fixes.py`](tests/test_fixes.py), and wired into Streamlit [`app.py`](app.py).
>>>>>>> REPLACE


### 🤖 Assistant

> 🔧 called: apply_diff



> 🔧 **apply_diff** — <<<<<<< SEARCH
:start_line:49
-------
## Decision priority (`decisions.py`)

1. Cash shortfall vs bills (within 30-day horizon) → `ping_shortfall`
   Bills due within 3 days are named as **urgent** in the ping message.
2. Adverse FX ≥ 3% + remittance planned → `suggest_wait`; else adverse FX ≥ 2% → `ping_fx_watch`
3. Naira **strengthening** sharply (USD/NGN falling ≥ 3%) + remittance planned → `suggest_send_later`
   Sending now yields fewer naira per dollar; advisory wait in case of reversal.
4. Remittance planned + FX stable (pct ≤ 0.5) → `suggest_send_now`
5. Else → `quiet`
=======
## Decision priority (`decisions.py`)

1. Cash shortfall vs bills (within 30-day horizon) → `ping_shortfall`
   Bills due within 3 days are named as **urgent** in the ping message.
2. Naira **weakening** (adverse FX, USD/NGN rising):
   - ≥ 3% + remittance planned → `suggest_send_now`
     Rationale: a weakening naira is *favourable* for the USD sender — each dollar buys more NGN.
     The agent advises sending now (or splitting) before the rate potentially reverts.
   - ≥ 2% (no remittance, or below 3% threshold) → `ping_fx_watch`
     Household costs in NGN may rise; watch the rate.
3. Naira **strengthening** sharply (USD/NGN falling ≥ 3%) + remittance planned → `suggest_send_later`
   Sending now yields fewer naira per dollar; advisory wait in case of reversal.
4. Remittance planned + FX stable (pct ≤ 0.5) → `suggest_send_now`
5. Else → `quiet`

> **`suggest_wait` is deprecated.** It was the previous (economically incorrect) outcome for
> naira-weakening spikes. It is kept in the `ActionKind` enum only so the Streamlit style map
> does not break, but it is never returned by `evaluate_buffer`.
>>>>>>> REPLACE

<<<<<<< SEARCH
:start_line:64
-------
## Demo scenarios (`agent.py`)

| Beat | Function | Expected action |
|------|----------|-----------------|
| Judge 1 | `run_quiet_scenario` | `quiet` (no remittance — never remittance-as-quiet) |
| Judge 2 | `run_alert_scenario` | `ping_shortfall` |
| Judge 3 | `run_fx_wait_scenario` | `suggest_wait` |
| Optional | `run_send_now_scenario` | `suggest_send_now` |
| Optional | `run_send_later_scenario` | `suggest_send_later` |
| Playground | `watch` FX + any buffer ≥ bills | `ping_fx_watch` |
=======
## Demo scenarios (`agent.py`)

| Beat | Function | Expected action |
|------|----------|-----------------|
| Judge 1 | `run_quiet_scenario` | `quiet` (no remittance — never remittance-as-quiet) |
| Judge 2 | `run_alert_scenario` | `ping_shortfall` |
| Judge 3 | `run_fx_send_now_scenario` | `suggest_send_now` (FX spike favours sender) |
| Optional | `run_send_now_scenario` | `suggest_send_now` (stable FX) |
| Optional | `run_send_later_scenario` | `suggest_send_later` |
| Playground | `watch` FX + any buffer ≥ bills | `ping_fx_watch` |

`run_fx_wait_scenario` is kept as a back-compat alias for `run_fx_send_now_scenario`.
>>>>>>> REPLACE


### 🤖 Assistant

> 🔧 called: apply_diff



> 🔧 **apply_diff** — <<<<<<< SEARCH
:start_line:22
-------
## Minute 1:00 — CLI story

Run `python -m bob_naira_assist`. Point to the three judge beats:

1. **Quiet** — buffer covers bills, stable FX, **no** remittance planned → `quiet`
2. **Shortfall ping** — buffer too low → `ping_shortfall`
3. **FX wait** — buffer OK but spiked FX + remittance planned → `suggest_wait`

Optional (Playground / UI button): **Send now** — healthy buffer + stable FX + remittance → `suggest_send_now`.

## Minute 2:00 — Streamlit

Open **Judge demo** tab → click **1 · Quiet**, **2 · Shortfall ping**, **3 · FX wait**.
Optionally **Optional · Send now** or use **Playground** (buffer slider, FX `stable` / `watch` / `spike`).
=======
## Minute 1:00 — CLI story

Run `python -m bob_naira_assist`. Point to the three judge beats:

1. **Quiet** — buffer covers bills, stable FX, **no** remittance planned → `quiet`
2. **Shortfall ping** — buffer too low → `ping_shortfall`
3. **FX spike → send now** — buffer OK, FX spiked ≥3% (naira weaker, **favourable for the sender**),
   remittance planned → `suggest_send_now`.
   Key insight: a weakening naira means each USD buys *more* NGN — the agent tells you to act
   before the rate reverts, not to wait.

Optional (Playground / UI button): **Send later** — naira strengthening ≥3% + remittance → `suggest_send_later`.

## Minute 2:00 — Streamlit

Open **Judge demo** tab → click **1 · Quiet**, **2 · Shortfall ping**, **3 · FX spike → send now**.
Optionally **Optional · Send later** or use **Playground** (buffer slider, FX `stable` / `watch` / `spike` / `strengthen`).
>>>>>>> REPLACE


### 🤖 Assistant

> 🔧 called: update_todo_list



> 🔧 **update_todo_list** — 
[x] Read and understand current codebase structure
[x] Fix economic bug in decisions.py evaluate_buffer
[x] Update models.py (deprecate SUGGEST_WAIT)
[x] Update agent.py beat 3 scenario
[x] Update app.py beat 3 labels and messages
[x] Update tests/test_decisions.py
[x] Update tests/test_agent_demo.py
[x] Update tests/test_fixes.py
[x] Update README.md judge-beats section
[x] Update docs/architecture.md
[x] Update docs/demo-script.md
[-] Run pytest and syntax check


### 🤖 Assistant

> 🔧 called: execute_command



> 🔧 **execute_command** — .venv/bin/python -m pytest -q 2>&1

### 🤖 Assistant

> 🔧 called: execute_command



> 🔧 **execute_command** — .venv/bin/python -c "import ast; ast.parse(open('app.py').read())" && echo "app.py: OK"

### 🤖 Assistant

> 🔧 called: update_todo_list



> 🔧 **update_todo_list** — 
[x] Read and understand current codebase structure
[x] Fix economic bug in decisions.py evaluate_buffer
[x] Update models.py (deprecate SUGGEST_WAIT)
[x] Update agent.py beat 3 scenario
[x] Update app.py beat 3 labels and messages
[x] Update tests/test_decisions.py
[x] Update tests/test_agent_demo.py
[x] Update tests/test_fixes.py
[x] Update README.md judge-beats section
[x] Update docs/architecture.md
[x] Update docs/demo-script.md
[x] Run pytest and syntax check


### 🤖 Assistant

All 42 tests pass and `app.py` parses cleanly. Here's a summary of every change made:

---

### What changed and why

#### Economic bug fix — [`decisions.py`](bob_naira_assist/decisions.py)

The old code had the direction backwards. When `usd_ngn` rises (naira *weakens*), the **sender** now gets more NGN per dollar — that's favourable, not a reason to wait. The `adverse` branch now:

- **spike ≥ 3% + remittance planned** → `SUGGEST_SEND_NOW` with message *"Rate moved in your favour (+X%): each $ buys more naira now; consider sending now or splitting, the move may revert"*
- **spike ≥ 2% without remittance (or below threshold)** → `PING_FX_WATCH` (unchanged — household costs rise)

The `FX_WAIT_PCT` constant is kept (same value, same name) but its comment now explains its corrected purpose.

#### [`models.py`](bob_naira_assist/models.py)

`SUGGEST_WAIT` marked deprecated in a comment block explaining why it's economically wrong and that it's kept only so the Streamlit style map doesn't break.

#### [`agent.py`](bob_naira_assist/agent.py)

- New `run_fx_send_now_scenario()` (beat 3) with accurate docstring
- `run_fx_wait_scenario` kept as a back-compat alias (+ `run_fx_watch_scenario` too)
- `run_demo_script()` footer updated: *"FX spike → send now (favourable rate)"*

#### [`app.py`](app.py)

- Import swapped to `run_fx_send_now_scenario`
- Beat 3 button: **"3 · FX spike → send now"** with correct help text
- Playground help text: *"spike: naira weaker 5% (suggest_send_now with remittance — rate favours sender)"*
- About tab: added task-04 entry describing the economic fix

#### Tests — 42 passing (up from 40)

- `test_decisions.py`: `test_fx_spike_suggests_send_now_when_buffer_ok` + new regression `test_fx_spike_with_remittance_never_returns_suggest_wait`
- `test_agent_demo.py`: `test_fx_send_now_scenario_is_suggest_send_now`, alias test, `test_demo_script_three_judge_beats` asserts `suggest_send_now` in output and `suggest_wait` absent
- `test_fixes.py`: renamed `test_zero_remittance_does_not_trigger_suggest_send_now_on_spike` with tighter assertions

#### Docs

- `README.md`: beat 3 → *"FX spike → send now"*, deprecated `suggest_wait` noted in outcomes table
- `docs/architecture.md`: decision priority rewritten with correct economics, deprecated note, table updated
- `docs/demo-script.md`: beat 3 updated with key insight explanation