from fastapi import FastAPI, Request
from .routes import projects, workshops, documents, gaps, roadmap, reports
import uuid
from ..utils.telemetry import correlation_id_var

app = FastAPI(title="Cyber AI Maturity Orchestrator", version="1.0.0")

@app.middleware("http")
async def add_correlation_id(request: Request, call_next):
    cid = request.headers.get("x-correlation-id") or str(uuid.uuid4())
    correlation_id_var.set(cid)
    response = await call_next(request)
    response.headers["x-correlation-id"] = cid
    return response

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

app.include_router(projects.router)
app.include_router(workshops.router)
app.include_router(documents.router)
app.include_router(gaps.router)
app.include_router(roadmap.router)
app.include_router(reports.router)
