# Developer Guide

## Run Locally
1. `python -m venv .venv && source .venv/bin/activate`
2. `pip install -r requirements/backend.txt`
3. `uvicorn src.orchestrator.main:app --reload`
4. `uvicorn src.agents.cyber.workshop_analyzer_service:app --reload`
5. Visit http://localhost:8000/docs

## Add a New Agent
- Create `src/agents/cyber/<name>_agent.py` with logic.
- Add wrapper `src/agents/cyber/<name>_service.py` using `create_agent_service`.
- Register URL in `config/agents.yaml`.

## Add a Route/Schema/Service
- Create Pydantic models under `src/orchestrator/schemas`.
- Implement service in `src/orchestrator/services`.
- Expose endpoint via router in `src/orchestrator/routes`.
- Include router in `src/orchestrator/main.py`.

## Configure Cosmos, Key Vault, OpenAI
- Edit `config/azure.yaml` with resource URLs and deployment names.
- Store Cosmos key in Key Vault and reference `key_secret_name`.
- Environment authenticates via `DefaultAzureCredential`.
