from ..schemas.project import Project


class OrchestratorService:
    async def run(self, project: Project) -> Project:
        return project
