from __future__ import annotations
"""Monitoring & Security Agent.

Continuously observes operations and triggers alerts for anomalies or
security threats using Azure Monitor and Sentinel.
"""

from typing import Optional, List
from semantic_kernel.functions import KernelFunction

from kernel_agents.agent_base import BaseAgent


class MonitoringSecurityAgent(BaseAgent):
    """Agent responsible for operational monitoring and security alerts."""

    @classmethod
    async def create(
        cls,
        session_id: str,
        user_id: str,
        memory_store,
        tools: Optional[List[KernelFunction]] = None,
        **kwargs,
    ) -> "MonitoringSecurityAgent":
        system_message = (
            "Monitor system activities for anomalies, enforce security "
            "controls and raise alerts via Azure Monitor and Sentinel."
        )
        return cls(
            agent_name="MonitoringSecurityAgent",
            session_id=session_id,
            user_id=user_id,
            memory_store=memory_store,
            tools=tools,
            system_message=system_message,
            **kwargs,
        )
