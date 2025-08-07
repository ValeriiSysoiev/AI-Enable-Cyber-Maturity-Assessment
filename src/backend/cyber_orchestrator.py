"""Cybersecurity Maturity Orchestrator.

Coordinates specialized AI agents for Deloitte's Cyber AI-enabled Maturity
Assessment solution. The orchestrator exposes a single entry point for the
frontend and manages agent invocations, result aggregation and secure
interaction with Azure OpenAI.
"""

from __future__ import annotations
from typing import Dict, Any

from context.cosmos_memory_kernel import CosmosMemoryContext
from kernel_agents.agent_base import BaseAgent

from cyber_agents.workshop_analyzer_agent import WorkshopAnalyzerAgent
from cyber_agents.documentation_analyzer_agent import DocumentationAnalyzerAgent
from cyber_agents.gap_analysis_agent import GapAnalysisAgent
from cyber_agents.benchmarking_agent import BenchmarkingAgent
from cyber_agents.initiative_generation_agent import InitiativeGenerationAgent
from cyber_agents.prioritization_agent import PrioritizationAgent
from cyber_agents.roadmap_planner_agent import RoadmapPlannerAgent
from cyber_agents.report_generator_agent import ReportGeneratorAgent
from cyber_agents.monitoring_security_agent import MonitoringSecurityAgent


class CyberOrchestrator:
    """High level orchestrator managing all specialized agents."""

    def __init__(self, memory_store: CosmosMemoryContext, user_id: str):
        self._memory_store = memory_store
        self._user_id = user_id
        self._agents: Dict[str, BaseAgent] = {}

    async def initialize_agents(self, session_id: str) -> None:
        """Initialize all specialized agents for a session."""
        self._agents = {
            "workshop": await WorkshopAnalyzerAgent.create(session_id, self._user_id, self._memory_store),
            "docs": await DocumentationAnalyzerAgent.create(session_id, self._user_id, self._memory_store),
            "gaps": await GapAnalysisAgent.create(session_id, self._user_id, self._memory_store),
            "benchmark": await BenchmarkingAgent.create(session_id, self._user_id, self._memory_store),
            "initiatives": await InitiativeGenerationAgent.create(session_id, self._user_id, self._memory_store),
            "prioritization": await PrioritizationAgent.create(session_id, self._user_id, self._memory_store),
            "roadmap": await RoadmapPlannerAgent.create(session_id, self._user_id, self._memory_store),
            "report": await ReportGeneratorAgent.create(session_id, self._user_id, self._memory_store),
            "monitor": await MonitoringSecurityAgent.create(session_id, self._user_id, self._memory_store),
        }

    async def run_assessment(self, session_id: str, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Execute full assessment workflow returning aggregated results.

        This is a simplified orchestration flow used for demonstration.
        """
        if not self._agents:
            await self.initialize_agents(session_id)

        # Example flow - only wiring; actual business logic would be more complex
        workshop_notes = await self._agents["workshop"].chat(inputs.get("workshop"))
        doc_findings = await self._agents["docs"].chat(inputs.get("documents"))
        gap_results = await self._agents["gaps"].chat(doc_findings)
        benchmark = await self._agents["benchmark"].chat(gap_results)
        initiatives = await self._agents["initiatives"].chat(gap_results)
        priorities = await self._agents["prioritization"].chat(initiatives)
        roadmap = await self._agents["roadmap"].chat(priorities)
        report = await self._agents["report"].chat({"roadmap": roadmap, "benchmark": benchmark})
        await self._agents["monitor"].chat("Assessment run complete")

        return {
            "workshop": workshop_notes,
            "documents": doc_findings,
            "gaps": gap_results,
            "benchmark": benchmark,
            "initiatives": initiatives,
            "priorities": priorities,
            "roadmap": roadmap,
            "report": report,
        }
