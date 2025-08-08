import hashlib
import json
import time
from typing import Any, Dict
from ..clients.repos.audit_repo import AuditRepo


def _hash(data: Dict[str, Any]) -> str:
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()


class AuditService:
    def __init__(self, repo: AuditRepo):
        self.repo = repo

    async def log(
        self,
        actor: str,
        project_id: str,
        agent: str,
        inputs: Dict[str, Any],
        outputs: Dict[str, Any],
        model_deployment: str = "",
        agent_version: str = "",
        latency_ms: int = 0,
        status: str = "ok",
    ) -> Dict[str, Any]:
        record = {
            "id": str(time.time_ns()),
            "timestamp": time.time(),
            "actor": actor,
            "projectId": project_id,
            "agent": agent,
            "inputs_hash": _hash(inputs),
            "outputs_hash": _hash(outputs),
            "model_deployment": model_deployment,
            "agent_version": agent_version,
            "latency_ms": latency_ms,
            "status": status,
        }
        await self.repo.upsert(record)
        return record
