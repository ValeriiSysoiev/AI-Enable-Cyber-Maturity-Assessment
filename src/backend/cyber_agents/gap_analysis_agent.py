from __future__ import annotations
"""Gap Analysis Agent.

Compares current maturity evidence with standard frameworks such as NIST
and ISO to identify control gaps.
"""

from typing import Optional, List
from semantic_kernel.functions import KernelFunction

from kernel_agents.agent_base import BaseAgent


class GapAnalysisAgent(BaseAgent):
    """Agent that performs cybersecurity gap analysis."""

    @classmethod
    async def create(
        cls,
        session_id: str,
        user_id: str,
        memory_store,
        tools: Optional[List[KernelFunction]] = None,
        **kwargs,
    ) -> "GapAnalysisAgent":
        system_message = (
            "Evaluate extracted evidence against NIST and ISO frameworks to "
            "identify maturity gaps and recommend controls to address them."
        )
        return cls(
            agent_name="GapAnalysisAgent",
            session_id=session_id,
            user_id=user_id,
            memory_store=memory_store,
            tools=tools,
            system_message=system_message,
            **kwargs,
        )
