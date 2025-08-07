from __future__ import annotations
"""Initiative Generation Agent.

Suggests practical cybersecurity initiatives to close identified maturity gaps.
"""

from typing import Optional, List
from semantic_kernel.functions import KernelFunction

from kernel_agents.agent_base import BaseAgent


class InitiativeGenerationAgent(BaseAgent):
    """Agent proposing initiatives to address maturity gaps."""

    @classmethod
    async def create(
        cls,
        session_id: str,
        user_id: str,
        memory_store,
        tools: Optional[List[KernelFunction]] = None,
        **kwargs,
    ) -> "InitiativeGenerationAgent":
        system_message = (
            "Given identified gaps, generate actionable cybersecurity "
            "initiatives that can be executed by the client organization."
        )
        return cls(
            agent_name="InitiativeGenerationAgent",
            session_id=session_id,
            user_id=user_id,
            memory_store=memory_store,
            tools=tools,
            system_message=system_message,
            **kwargs,
        )
