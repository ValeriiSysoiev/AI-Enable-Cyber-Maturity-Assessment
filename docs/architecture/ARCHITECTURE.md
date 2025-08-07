# Architecture Overview

## Repository Layout
- **src/** – application source code including orchestrator, agents, and utilities.
- **infra/** – infrastructure-as-code templates (Bicep).
- **docs/** – documentation and diagrams.
- **tests/** – unit, integration, and end-to-end tests.
- **config/** – configuration examples and environment files.
- **requirements/** – Python dependency lists.
- **pipelines/** – CI/CD definitions.
- **docker/** – container build definitions.

## Solution Diagram
![High-level architecture](diagrams/architecture.png)

This diagram shows the core components of the platform:
- Web interface hosted on Azure App Service.
- AI orchestrator and agents running in Azure Container Apps.
- Data stored securely in Azure Cosmos DB and Key Vault.
- Supporting Azure services such as OpenAI, Monitor, and Active Directory.

## Data Flow
User requests enter through the web interface, pass to the orchestrator, and are dispatched to
specialized agents. Results and state are persisted to the data stores while telemetry flows to
monitoring services.

## Deployment
Infrastructure is defined in `infra/main.bicep` and automated pipelines are provided in
`pipelines/azure-dev.yml` for continuous deployment.
