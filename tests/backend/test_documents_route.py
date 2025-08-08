from fastapi.testclient import TestClient
from src.orchestrator.main import app
from src.orchestrator import app_config

client = TestClient(app)
app_config.get_agent_url = lambda name: None


def test_documents_ingest():
    resp = client.post(
        "/documents/ingest",
        json={"project_id": "p1", "content": "doc"},
        headers={"Authorization": "Bearer Consultant"},
    )
    assert resp.status_code == 200
    assert resp.json()["document_id"]
