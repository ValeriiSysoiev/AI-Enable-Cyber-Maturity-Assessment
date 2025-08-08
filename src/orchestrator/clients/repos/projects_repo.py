from ..cosmos_client import CosmosClient
from typing import Any, Dict, List


class ProjectsRepo:
    def __init__(self, client: CosmosClient):
        self.client = client
        self.pk = "project"

    async def upsert(self, item: Dict[str, Any]) -> Dict[str, Any]:
        return await self.client.upsert(item, self.pk)

    async def get(self, item_id: str) -> Dict[str, Any] | None:
        return await self.client.get(item_id, self.pk)

    async def query(self) -> List[Dict[str, Any]]:
        return await self.client.query(self.pk)
