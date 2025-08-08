from .benchmarking_agent import BenchmarkingAgent  # noqa: F401
from ..common.agent_base import create_agent_service


async def run_fn(payload: dict) -> dict:
    return {"echo": payload}


app = create_agent_service(run_fn)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
