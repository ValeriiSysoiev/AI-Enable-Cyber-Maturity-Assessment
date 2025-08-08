from fastapi import APIRouter
from ..schemas.project import Project
from ..services.orchestrator_service import OrchestratorService

router = APIRouter(prefix="/projects", tags=["projects"])
service = OrchestratorService()


@router.post("/")
async def create_project(project: Project) -> Project:
    return await service.run(project)
