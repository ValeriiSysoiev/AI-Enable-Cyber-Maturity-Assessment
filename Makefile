run-orchestrator:
	uvicorn src.orchestrator.main:app --reload

run-agent-workshop:
	uvicorn src.agents.cyber.workshop_analyzer_service:app --reload

build-orchestrator:
	docker build -t orchestrator -f docker/orchestrator/Dockerfile .

build-agents:
	echo building agents

test:
	pytest -q
