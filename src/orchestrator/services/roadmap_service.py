from ..schemas.roadmap import RoadmapRequest, RoadmapResponse
from ..schemas.initiative import Initiative
from ..clients.agent_client import AgentClient
from ..app_config import get_agent_url
from ..utils.telemetry import get_logger

logger = get_logger("roadmap_service")


class RoadmapService:
    async def run(self, request: RoadmapRequest) -> RoadmapResponse:
        logger.info("roadmap build start")
        url = get_agent_url("roadmap_planner")
        if url:
            try:
                client = AgentClient(url)
                result = await client.run("run", request.project_id, request.model_dump())
                initiatives = [
                    Initiative(**i) for i in result.get("result", {}).get("initiatives", [])
                ]
                logger.info("roadmap build end")
                return RoadmapResponse(initiatives=initiatives)
            except Exception:
                logger.error("roadmap agent call failed")
        logger.info("roadmap build end")
        return RoadmapResponse(initiatives=[Initiative(id="1", description="stub")])
