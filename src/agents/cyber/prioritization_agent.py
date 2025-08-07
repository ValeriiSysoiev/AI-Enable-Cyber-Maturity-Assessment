from __future__ import annotations
"""Prioritization & Sequencing Agent.

Ranks initiatives by impact, complexity and alignment to strategy using
multi-criteria analysis.
"""

from typing import Optional, List
from semantic_kernel.functions import KernelFunction

from kernel_agents.agent_base import BaseAgent


class PrioritizationAgent(BaseAgent):
    """Agent that ranks and sequences cybersecurity initiatives."""

    @classmethod
    async def create(
        cls,
        session_id: str,
        user_id: str,
        memory_store,
        tools: Optional[List[KernelFunction]] = None,
        **kwargs,
    ) -> "PrioritizationAgent":
        system_message = (
            "Prioritize proposed initiatives considering impact, effort, "
            "and strategic alignment. Output an ordered backlog with "
            "rationale for each ranking."
        )
        return cls(
            agent_name="PrioritizationAgent",
            session_id=session_id,
            user_id=user_id,
            memory_store=memory_store,
            tools=tools,
            system_message=system_message,
            **kwargs,
        )
