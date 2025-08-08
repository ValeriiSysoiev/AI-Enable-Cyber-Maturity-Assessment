# Cyber AI–Enabled Maturity Assessment

An Azure-based solution that coordinates specialized AI agents to analyze cybersecurity evidence and build maturity roadmaps. A FastAPI orchestrator communicates with agent microservices backed by Azure OpenAI, Cosmos DB, and Key Vault.

## Quick Start
1. `python -m venv .venv && source .venv/bin/activate`
2. `pip install -r requirements/backend.txt`
3. `uvicorn src.orchestrator.main:app --reload`
4. `uvicorn src.agents.cyber.workshop_analyzer_service:app --reload`
5. `pytest -q`

## Repository Map
- `src/` – orchestrator, agents, utilities
- `config/` – YAML configuration files
- `docs/` – architecture, user and developer guides
- `docker/` – container build definitions
- `tests/` – unit and end-to-end tests
- `infra/` – infrastructure templates
- `requirements/` – Python dependencies
- `.github/` – CI workflows

## Documentation
- [Architecture](docs/architecture/ARCHITECTURE.md)
- [User Guide](docs/user_guide.md)
- [Developer Guide](docs/dev_guide.md)
