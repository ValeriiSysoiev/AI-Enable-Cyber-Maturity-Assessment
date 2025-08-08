from fastapi import FastAPI
from typing import Callable, Awaitable, Dict, Any
from .models import AgentRequest, AgentResponse


def create_agent_service(run_fn: Callable[[Dict[str, Any]], Awaitable[Dict[str, Any]]]) -> FastAPI:
    app = FastAPI()

    @app.get("/healthz")
    async def healthz():
        return {"status": "ok"}

    @app.post("/run", response_model=AgentResponse)
    async def run(request: AgentRequest) -> AgentResponse:
        result = await run_fn(request.payload)
        return AgentResponse(task_id=request.task_id, result=result)

    return app
