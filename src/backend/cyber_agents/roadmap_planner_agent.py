from __future__ import annotations
"""Roadmap Planner Agent.

Creates actionable roadmaps with timelines, resource needs and dependencies
based on prioritized initiatives.
"""

from typing import Optional, List
from semantic_kernel.functions import KernelFunction

from kernel_agents.agent_base import BaseAgent


class RoadmapPlannerAgent(BaseAgent):
    """Agent that assembles a program roadmap."""

    @classmethod
    async def create(
        cls,
        session_id: str,
        user_id: str,
        memory_store,
        tools: Optional[List[KernelFunction]] = None,
        **kwargs,
    ) -> "RoadmapPlannerAgent":
        system_message = (
            "Transform the prioritized backlog into a deliverable roadmap "
            "with timelines, resource estimates and key dependencies."
        )
        return cls(
            agent_name="RoadmapPlannerAgent",
            session_id=session_id,
            user_id=user_id,
            memory_store=memory_store,
            tools=tools,
            system_message=system_message,
            **kwargs,
        )
