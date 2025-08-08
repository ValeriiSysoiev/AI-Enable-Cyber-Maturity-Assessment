from typing import Any, Dict, List


class CosmosClient:
    """Simplified Cosmos DB repository wrapper."""

    def __init__(self):
        self._store: Dict[str, Dict[str, Any]] = {}

    async def upsert(self, item: Dict[str, Any], partition_key: str) -> Dict[str, Any]:
        pk_store = self._store.setdefault(partition_key, {})
        pk_store[item["id"]] = item
        return item

    async def get(self, item_id: str, partition_key: str) -> Dict[str, Any] | None:
        return self._store.get(partition_key, {}).get(item_id)

    async def query(self, partition_key: str) -> List[Dict[str, Any]]:
        return list(self._store.get(partition_key, {}).values())
