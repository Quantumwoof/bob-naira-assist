# Architecture

BobNairaAssist keeps the agent story small and testable: pure Python decisions + Streamlit UI,
with IBM Bob IDE as the planned build partner (session exports in `bob_sessions/`).

## Mermaid overview

```mermaid
flowchart LR
  subgraph inputs [Inputs DEMO_MODE]
    Bills[Sample bills]
    Buffer[NGN cash buffer]
    FX[Mock USD/NGN FX]
  end

  subgraph core [bob_naira_assist]
    Eval[evaluate_buffer]
    Agent[agent demo script]
  end

  subgraph outs [Outputs]
    Quiet[Quiet]
    Ping[Ping shortfall / FX]
    Timing[Wait vs send now]
    UI[Streamlit app.py]
    CLI[python -m bob_naira_assist]
  end

  Bills --> Eval
  Buffer --> Eval
  FX --> Eval
  Eval --> Quiet
  Eval --> Ping
  Eval --> Timing
  Agent --> CLI
  Eval --> UI
  Agent --> UI

  Bob[IBM Bob IDE] -.->|scaffold tests docs review| core
  Bob -.->|exports| Sessions[bob_sessions/]
```

## Modules

| Module | Role |
|--------|------|
| `models.py` | Bills, buffer, FX quote, `AgentDecision` |
| `bills.py` | Deterministic sample Nigerian bills |
| `fx.py` | Mock stable / spike USD/NGN quotes |
| `decisions.py` | Pure quiet-vs-ping + remittance timing |
| `agent.py` | DEMO_MODE scripted scenarios |
| `app.py` | Streamlit judge path |

## Non-goals (MVP)

- Live bank APIs, live FX feeds, or paid SMS.
- Required watsonx / cloud LLM for the offline demo.
- Claiming Bob session reports before they are exported.
