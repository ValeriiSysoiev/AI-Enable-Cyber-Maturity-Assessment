from ..schemas.document import DocumentIngestRequest, DocumentIngestResponse
from ..clients.agent_client import AgentClient
from ..app_config import get_agent_url
from ..utils.telemetry import get_logger

logger = get_logger("document_service")


class DocumentIngestService:
    async def run(self, request: DocumentIngestRequest) -> DocumentIngestResponse:
        logger.info("document ingest start")
        url = get_agent_url("documentation_analyzer")
        if url:
            try:
                client = AgentClient(url)
                result = await client.run("run", request.project_id, request.model_dump())
                doc_id = result.get("result", {}).get("document_id", "doc-1")
                logger.info("document ingest end")
                return DocumentIngestResponse(document_id=doc_id)
            except Exception:
                logger.error("document agent call failed")
        logger.info("document ingest end")
        return DocumentIngestResponse(document_id="doc-1")
