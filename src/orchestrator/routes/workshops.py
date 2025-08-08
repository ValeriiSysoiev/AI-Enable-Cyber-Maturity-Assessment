from fastapi import APIRouter
from ..schemas.workshop import WorkshopAnalysisRequest, WorkshopAnalysisResponse
from ..services.workshop_service import WorkshopService

router = APIRouter(prefix="/workshops", tags=["workshops"])
service = WorkshopService()


@router.post("/analyze", response_model=WorkshopAnalysisResponse)
async def analyze(request: WorkshopAnalysisRequest) -> WorkshopAnalysisResponse:
    return await service.run(request)
