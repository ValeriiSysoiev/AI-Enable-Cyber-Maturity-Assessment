from fastapi.testclient import TestClient
from src.orchestrator.main import app
from src.orchestrator import app_config

client = TestClient(app)

app_config.get_agent_url = lambda name: None


def test_gaps_analyze():
    resp = client.post(
        "/gaps/analyze",
        json={"project_id": "p1", "data": "info"},
        headers={"Authorization": "Bearer Consultant"},
    )
    assert resp.status_code == 200
    assert "gaps" in resp.json()
