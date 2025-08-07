from __future__ import annotations
"""Benchmarking & Targeting Agent.

Provides industry benchmarks and helps set target maturity levels based on
similar organizations.
"""

from typing import Optional, List
from semantic_kernel.functions import KernelFunction

from kernel_agents.agent_base import BaseAgent


class BenchmarkingAgent(BaseAgent):
    """Agent delivering comparative industry insights."""

    @classmethod
    async def create(
        cls,
        session_id: str,
        user_id: str,
        memory_store,
        tools: Optional[List[KernelFunction]] = None,
        **kwargs,
    ) -> "BenchmarkingAgent":
        system_message = (
            "Leverage industry data to benchmark the client's cybersecurity "
            "maturity and propose realistic target states."
        )
        return cls(
            agent_name="BenchmarkingAgent",
            session_id=session_id,
            user_id=user_id,
            memory_store=memory_store,
            tools=tools,
            system_message=system_message,
            **kwargs,
        )
