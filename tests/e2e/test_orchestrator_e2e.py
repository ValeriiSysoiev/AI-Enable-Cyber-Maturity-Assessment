from fastapi import FastAPI
from fastapi.testclient import TestClient
from src.orchestrator.main import app
from src.orchestrator.clients.agent_client import AgentClient
from src.orchestrator import app_config

fake_agent = FastAPI()


@fake_agent.post("/run")
async def run(payload: dict):
    return {
        "task_id": payload.get("task_id"),
        "result": {
            "summary": "s",
            "gaps": ["g1"],
            "initiatives": [{"id": "1", "description": "i"}],
            "document_id": "d1",
            "url": "u",
        },
    }


fake_client = TestClient(fake_agent)


async def fake_run(self, endpoint, task_id, payload, correlation_id=None):
    resp = fake_client.post(f"/{endpoint}", json={"task_id": task_id, "payload": payload})
    return resp.json()


AgentClient.run = fake_run  # type: ignore
app_config.get_agent_url = lambda name: "http://fake"

client = TestClient(app)


def test_full_flow():
    r1 = client.post(
        "/workshops/analyze",
        json={"project_id": "p1", "transcript": "t"},
    )
    assert r1.status_code == 200
    r2 = client.post(
        "/gaps/analyze",
        json={"project_id": "p1", "data": "d"},
        headers={"Authorization": "Bearer Consultant"},
    )
    assert r2.status_code == 200
    r3 = client.post("/roadmap/build", json={"project_id": "p1", "gaps": ["g1"]})
    assert r3.status_code == 200
    assert r3.json()["initiatives"]
