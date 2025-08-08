import httpx
from typing import Any, Dict


class AgentClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    async def run(self, endpoint: str, task_id: str, payload: Dict[str, Any], correlation_id: str | None = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint.lstrip('/') }"
        headers = {}
        if correlation_id:
            headers["x-correlation-id"] = correlation_id
        timeout = httpx.Timeout(10.0)
        for _ in range(3):
            try:
                async with httpx.AsyncClient(timeout=timeout) as client:
                    resp = await client.post(url, json={"task_id": task_id, "payload": payload}, headers=headers)
                resp.raise_for_status()
                return resp.json()
            except Exception:
                continue
        raise RuntimeError("agent call failed")
