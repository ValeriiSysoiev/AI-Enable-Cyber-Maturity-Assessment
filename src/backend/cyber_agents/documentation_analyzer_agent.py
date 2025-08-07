from __future__ import annotations
"""Documentation Analyzer Agent.

This agent reviews uploaded client cybersecurity documentation and extracts
maturity evidence. It highlights inconsistencies or missing controls.
"""

from typing import Optional, List
from semantic_kernel.functions import KernelFunction

from kernel_agents.agent_base import BaseAgent


class DocumentationAnalyzerAgent(BaseAgent):
    """Agent that processes and analyzes client documents."""

    @classmethod
    async def create(
        cls,
        session_id: str,
        user_id: str,
        memory_store,
        tools: Optional[List[KernelFunction]] = None,
        **kwargs,
    ) -> "DocumentationAnalyzerAgent":
        system_message = (
            "Analyze uploaded cybersecurity documents, extract maturity "
            "evidence and flag gaps or inconsistencies. Provide traceable "
            "citations for all findings."
        )
        return cls(
            agent_name="DocumentationAnalyzerAgent",
            session_id=session_id,
            user_id=user_id,
            memory_store=memory_store,
            tools=tools,
            system_message=system_message,
            **kwargs,
        )
