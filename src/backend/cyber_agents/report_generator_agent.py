from __future__ import annotations
"""Report Generator Agent.

Compiles comprehensive maturity assessment reports and executive summaries
based on outputs from other agents.
"""

from typing import Optional, List
from semantic_kernel.functions import KernelFunction

from kernel_agents.agent_base import BaseAgent


class ReportGeneratorAgent(BaseAgent):
    """Agent that formats results into consultant-ready reports."""

    @classmethod
    async def create(
        cls,
        session_id: str,
        user_id: str,
        memory_store,
        tools: Optional[List[KernelFunction]] = None,
        **kwargs,
    ) -> "ReportGeneratorAgent":
        system_message = (
            "Aggregate outputs from all agents and craft a professional "
            "report with an executive summary and detailed appendices."
        )
        return cls(
            agent_name="ReportGeneratorAgent",
            session_id=session_id,
            user_id=user_id,
            memory_store=memory_store,
            tools=tools,
            system_message=system_message,
            **kwargs,
        )
