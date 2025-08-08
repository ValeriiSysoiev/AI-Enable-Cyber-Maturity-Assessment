from fastapi import APIRouter, Depends
from ..schemas.gap import GapAnalysisRequest, GapAnalysisResponse
from ..services.gap_analysis_service import GapAnalysisService
from ..security.auth import require_roles

router = APIRouter(prefix="/gaps", tags=["gaps"])
service = GapAnalysisService()


@router.post("/analyze", response_model=GapAnalysisResponse, dependencies=[Depends(require_roles("Consultant", "Reviewer", "Admin"))])
async def analyze(request: GapAnalysisRequest) -> GapAnalysisResponse:
    return await service.run(request)
