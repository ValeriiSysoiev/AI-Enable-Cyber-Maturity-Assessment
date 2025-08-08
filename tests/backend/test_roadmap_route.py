from fastapi.testclient import TestClient
from src.orchestrator.main import app
from src.orchestrator import app_config

client = TestClient(app)
app_config.get_agent_url = lambda name: None


def test_roadmap_build():
    resp = client.post(
        "/roadmap/build",
        json={"project_id": "p1", "gaps": ["g1"]},
    )
    assert resp.status_code == 200
    assert "initiatives" in resp.json()
