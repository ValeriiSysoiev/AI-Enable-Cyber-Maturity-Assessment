from fastapi import APIRouter, Depends
from ..schemas.document import DocumentIngestRequest, DocumentIngestResponse
from ..services.document_ingest_service import DocumentIngestService
from ..security.auth import require_roles

router = APIRouter(prefix="/documents", tags=["documents"])
service = DocumentIngestService()


@router.post("/ingest", response_model=DocumentIngestResponse, dependencies=[Depends(require_roles("Consultant", "Admin"))])
async def ingest(request: DocumentIngestRequest) -> DocumentIngestResponse:
    return await service.run(request)
