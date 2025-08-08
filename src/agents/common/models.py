from pydantic import BaseModel
from typing import Dict, Any, Optional


class AgentRequest(BaseModel):
    task_id: str
    payload: Dict[str, Any]


class AgentResponse(BaseModel):
    task_id: str
    result: Dict[str, Any]
    notes: Optional[str] = None
