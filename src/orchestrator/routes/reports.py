from fastapi import APIRouter, Depends
from ..schemas.report import ReportRequest, ReportResponse
from ..services.report_service import ReportService
from ..security.auth import require_roles

router = APIRouter(prefix="/reports", tags=["reports"])
service = ReportService()


@router.post("/generate", response_model=ReportResponse, dependencies=[Depends(require_roles("Consultant", "Reviewer", "Admin"))])
async def generate(request: ReportRequest) -> ReportResponse:
    return await service.run(request)
