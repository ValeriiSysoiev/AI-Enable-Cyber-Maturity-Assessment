# Architecture

![Architecture](diagrams/architecture.png)

## Components
- Web frontend
- FastAPI orchestrator
- Specialized agents (workshop, documents, gap, roadmap, report)
- Azure Cosmos DB
- Azure OpenAI
- Azure Key Vault
- Azure Active Directory
- Azure Monitor

## Consultant Flow
1. Consultant uploads workshop transcript.
2. Orchestrator calls Workshop Analyzer agent.
3. Evidence stored in Cosmos DB.
4. Gap Analysis agent evaluates controls.
5. Initiatives are generated and prioritized.
6. Roadmap planner sequences initiatives.
7. Report generator produces deliverable stored for review.
