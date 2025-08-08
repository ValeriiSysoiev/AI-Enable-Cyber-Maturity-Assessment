from fastapi import APIRouter
from ..schemas.roadmap import RoadmapRequest, RoadmapResponse
from ..services.roadmap_service import RoadmapService

router = APIRouter(prefix="/roadmap", tags=["roadmap"])
service = RoadmapService()


@router.post("/build", response_model=RoadmapResponse)
async def build(request: RoadmapRequest) -> RoadmapResponse:
    return await service.run(request)
