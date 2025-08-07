#!/bin/bash
set -e

mkdir -p src/orchestrator/{context,handlers,middleware} \
         src/agents/{cyber,kernel} \
         src/{tools,models,auth,utils,frontend} \
         docker/{backend,frontend} \
         requirements tests/{backend,unit,e2e} \
         docs/images config pipelines

# Orchestrator
mv src/backend/app_config.py src/orchestrator/
mv src/backend/app_kernel.py src/orchestrator/
mv src/backend/cyber_orchestrator.py src/orchestrator/
mv src/backend/context/* src/orchestrator/context/
mv src/backend/handlers/* src/orchestrator/handlers/
mv src/backend/middleware/* src/orchestrator/middleware/

# Agents & tools
mv src/backend/cyber_agents/* src/agents/cyber/
mv src/backend/kernel_agents/* src/agents/kernel/
mv src/backend/kernel_tools/* src/tools/

# Models, auth, utils
mv src/backend/models/* src/models/
mv src/backend/auth/* src/auth/
mv src/backend/helpers/azure_credential_utils.py src/utils/
mv src/backend/event_utils.py src/utils/
mv src/backend/otlp_tracing.py src/utils/
mv src/backend/utils_date.py src/utils/
mv src/backend/utils_kernel.py src/utils/

# Tests
mv src/backend/test_utils_date_fixed.py tests/unit/
mv src/backend/tests/* tests/backend/
rm -r src/backend/tests
mv tests/e2e-test tests/e2e

# Configuration & dependencies
mv src/backend/requirements.txt requirements/backend.txt
mv src/frontend/requirements.txt requirements/frontend.txt
mv tests/e2e/sample_dotenv_file.txt config/.env.example
mv azure.yaml config/
mv src/backend/pyproject.toml pyproject.toml

# Docs & diagrams
mv src/backend/README.md docs/backend.md
mv src/frontend/README.md docs/frontend.md
mv next-steps.md docs/
mv TRANSPARENCY_FAQS.md docs/
mv diagram-export-8-7-2025-11_02_19-AM.png docs/images/

# Dockerfiles & pipelines
mv src/backend/Dockerfile docker/backend/
mv src/frontend/Dockerfile docker/frontend/
mv .azdo/pipelines/azure-dev.yml pipelines/

# Cleanup
rm __azurite_db_queue__.json __azurite_db_queue_extent__.json
rm -r src/backend

