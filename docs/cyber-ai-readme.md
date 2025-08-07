# Cyber AI-Enabled Maturity Assessment Add-on

This document describes the Deloitte specific extension of the Multi-Agent
Custom Automation Engine. The extension introduces a set of specialized AI
agents and a coordinating orchestrator for performing cybersecurity maturity
assessments.

## Components

- **Web Interface** – Azure App Service frontend secured with Azure AD.
- **Cyber Orchestrator** – central API hosted on Azure Container Apps that
  coordinates specialized agents using Semantic Kernel.
- **Specialized Agents** – microservices each focusing on a discrete part of
  the assessment lifecycle (workshop guidance, document review, gap analysis,
  benchmarking, initiative generation, prioritization, roadmap planning,
  report creation and operational monitoring).
- **Azure OpenAI Service** – provides language capabilities with responsible
  AI filters.
- **Azure Cosmos DB** – stores project metadata, evidence and agent outputs.
- **Azure Monitor/Sentinel** – centralized logging, metrics and security
  alerting.

## Deployment

1. Provision base infrastructure using the provided `infra/` Bicep templates.
2. Deploy the orchestrator and agents as Azure Container Apps. Each agent
   container uses the corresponding module inside `src/backend/cyber_agents`.
3. Publish the frontend to Azure App Service enabling Azure AD authentication.
4. Configure Cosmos DB connection strings and OpenAI credentials in Azure
   Key Vault and reference them via managed identity.

## Notes

This readme captures only the high level additions. Individual modules are
heavily commented to explain behaviour and security considerations.
