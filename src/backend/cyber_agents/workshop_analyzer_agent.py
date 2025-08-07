from __future__ import annotations
"""Workshop Analyzer Agent.

This agent provides real-time support during client workshops, suggesting
questions and capturing key cybersecurity evidence. It is designed to run
as a containerized microservice within Azure Container Apps.
"""

from typing import Optional, List
from semantic_kernel.functions import KernelFunction

from kernel_agents.agent_base import BaseAgent


class WorkshopAnalyzerAgent(BaseAgent):
    """Specialized agent for live workshop guidance."""

    @classmethod
    async def create(
        cls,
        session_id: str,
        user_id: str,
        memory_store,
        tools: Optional[List[KernelFunction]] = None,
        **kwargs,
    ) -> "WorkshopAnalyzerAgent":
        """Factory method to initialize the agent with default instructions."""
        system_message = (
            "You assist consultants during client calls by suggesting probing "
            "questions and capturing evidence relevant to cybersecurity maturity "
            "assessments. Focus on clarity and keep responses short."
        )
        return cls(
            agent_name="WorkshopAnalyzerAgent",
            session_id=session_id,
            user_id=user_id,
            memory_store=memory_store,
            tools=tools,
            system_message=system_message,
            **kwargs,
        )
