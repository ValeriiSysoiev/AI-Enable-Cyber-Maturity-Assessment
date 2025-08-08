from ..schemas.workshop import WorkshopAnalysisRequest, WorkshopAnalysisResponse
from ..clients.agent_client import AgentClient
from ..app_config import get_agent_url
from ..utils.telemetry import get_logger

logger = get_logger("workshop_service")


class WorkshopService:
    async def run(self, request: WorkshopAnalysisRequest) -> WorkshopAnalysisResponse:
        logger.info("workshop analysis start")
        url = get_agent_url("workshop_analyzer")
        if url:
            try:
                client = AgentClient(url)
                result = await client.run("run", request.project_id, request.model_dump())
                summary = result.get("result", {}).get("summary", "")
                logger.info("workshop analysis end")
                return WorkshopAnalysisResponse(summary=summary)
            except Exception:
                logger.error("workshop agent call failed")
        logger.info("workshop analysis end")
        return WorkshopAnalysisResponse(summary="")
