# Cyber AI-Enabled Maturity Assessment Solution

## Business Purpose
The Cyber AI-Enabled Maturity Assessment Solution helps Deloitte cyber consultants accelerate security reviews.  It automates workshops, document analysis, gap detection, benchmarking, and final reporting so teams can focus on high-value advisory work.

## Architecture
- **Frontend UI** – React-based web experience for consultants and clients.
- **Orchestrator** – Python service built with Semantic Kernel to coordinate every agent and process.
- **Specialized AI Agents** – modular agents handle workshops, document review, gap analysis, benchmarking, recommendations, and report generation.
- **Azure OpenAI Service** – large language models power conversation, reasoning, and content generation.
- **Azure Cosmos DB** – stores assessment state, uploaded content, and generated insights.
- **Azure Key Vault** – keeps secrets, keys, and certificates secure.
- **Azure Active Directory** – authenticates consultants and clients and provides RBAC.
- **Monitoring & Logging** – Azure Monitor/Application Insights collect telemetry and audit trails.
- **Infrastructure as Code** – Bicep templates in `/infra` provision all resources consistently.

```
+------------+      +---------------+      +---------------------+
| Consultant |<---->| Frontend (UI) |<---->| Orchestrator/Agents |
+------------+      +---------------+      +---------------------+
       |                     |                     |
       |             Azure Active Directory        |
       |                     |                     |
       +-------> Azure OpenAI & Cosmos DB <--------+
                         |
                Key Vault / Monitoring
```

## Consultant Workflow
1. **Sign in** with Azure AD.
2. **Start new assessment** and choose scope or template.
3. **Run workshop** through guided questions with the Workshop Agent.
4. **Upload documents** such as policies or architectures.
5. **AI agents analyze** content, identify gaps, and compare with benchmarks.
6. **Review recommendations** and adjust results if needed.
7. **Generate and export report** for the client.

## Quick Start
### Prerequisites
- Azure subscription with access to Azure OpenAI, Cosmos DB, and Key Vault.
- Python 3.10+ and Node.js 18+.
- Azure CLI and logged in (`az login`).

### Run Locally
1. Clone the repository.
2. Install backend dependencies: `pip install -r src/backend/requirements.txt`.
3. Install frontend dependencies: `cd src/frontend && npm install`.
4. Set environment variables (see Configuration).
5. Start the backend: `cd src/backend && python app_kernel.py`.
6. Start the frontend: `cd src/frontend && npm run dev`.

### Deploy to Azure
1. Review the infrastructure templates under `/infra`.
2. Update parameters in `infra/main.parameters.json`.
3. Deploy with Bicep: `az deployment sub create -f infra/main.bicep -l <region>`.
4. Configure DNS/SSL and share the URL with users.

## Configuration
Set the following environment variables for the backend:

```
AZURE_TENANT_ID, AZURE_CLIENT_ID, AZURE_CLIENT_SECRET
COSMOSDB_ENDPOINT, COSMOSDB_DATABASE, COSMOSDB_CONTAINER
AZURE_OPENAI_DEPLOYMENT_NAME, AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_VERSION
AZURE_AI_SUBSCRIPTION_ID, AZURE_AI_RESOURCE_GROUP, AZURE_AI_PROJECT_NAME, AZURE_AI_AGENT_ENDPOINT
FRONTEND_SITE_NAME (optional), USER_LOCAL_BROWSER_LANGUAGE (optional)
```

Grant the application identity access to Key Vault, Cosmos DB, and Azure OpenAI using role-based access control (RBAC).

## AI Agents
- **Workshop Facilitator** – guides live assessment sessions.
- **Document Analyzer** – extracts insights from uploaded files.
- **Gap Identifier** – compares current state to frameworks.
- **Benchmarking Agent** – measures maturity against industry data.
- **Recommendation Agent** – drafts prioritized improvement actions.
- **Reporting Agent** – compiles findings into client-ready output.
- **Human Oversight Agent** – lets consultants review and override AI output.

## Security and Compliance
- Authentication through Azure AD with least-privilege RBAC.
- Secrets and keys stored only in Azure Key Vault.
- All data encrypted at rest and in transit; sensitive data is minimized.
- Logs and telemetry captured in Application Insights for auditing.
- Supports alignment with common standards (ISO 27001, SOC 2, NIST CSF).

## Further Documentation & Support
- Deployment guide and additional docs are in the `/docs` folder.
- For questions or issues, see [SUPPORT.md](./SUPPORT.md).
- Contact your Deloitte engagement team for customized guidance.

## What's Different from the Microsoft Accelerator?
- Retooled for Deloitte cyber maturity assessments rather than generic automation.
- Default agents and prompts focus on security workshops and documentation review.
- Added guidance on compliance, RBAC, and client privacy expectations.
- Deloitte-focused UI wording and workflow.

## Changelog
| Date | Change |
|------|--------|
| 2025-03-05 | Initial Deloitte cyber maturity adaptation and README rewrite. |
