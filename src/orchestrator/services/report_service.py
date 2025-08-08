from ..schemas.report import ReportRequest, ReportResponse
from ..clients.agent_client import AgentClient
from ..app_config import get_agent_url
from ..utils.telemetry import get_logger

logger = get_logger("report_service")


class ReportService:
    async def run(self, request: ReportRequest) -> ReportResponse:
        logger.info("report generation start")
        url = get_agent_url("report_generator")
        if url:
            try:
                client = AgentClient(url)
                result = await client.run("run", request.project_id, request.model_dump())
                url_out = result.get("result", {}).get("url", "https://example.com/report.pdf")
                logger.info("report generation end")
                return ReportResponse(url=url_out)
            except Exception:
                logger.error("report agent call failed")
        logger.info("report generation end")
        return ReportResponse(url="https://example.com/report.pdf")
