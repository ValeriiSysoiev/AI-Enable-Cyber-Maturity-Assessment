from ..schemas.gap import GapAnalysisRequest, GapAnalysisResponse
from ..clients.agent_client import AgentClient
from ..app_config import get_agent_url
from ..utils.telemetry import get_logger

logger = get_logger("gap_service")


class GapAnalysisService:
    async def run(self, request: GapAnalysisRequest) -> GapAnalysisResponse:
        logger.info("gap analysis start")
        url = get_agent_url("gap_analysis")
        if url:
            try:
                client = AgentClient(url)
                result = await client.run("run", request.project_id, request.model_dump())
                gaps = result.get("result", {}).get("gaps", [])
                logger.info("gap analysis end")
                return GapAnalysisResponse(gaps=gaps)
            except Exception:
                logger.error("gap agent call failed")
        logger.info("gap analysis end")
        return GapAnalysisResponse(gaps=[])
