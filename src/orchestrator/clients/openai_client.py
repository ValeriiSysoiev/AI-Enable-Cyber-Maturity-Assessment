from typing import Any, Dict, List, Optional

try:
    from openai import AsyncAzureOpenAI
except Exception:  # pragma: no cover
    AsyncAzureOpenAI = None  # type: ignore


class OpenAIClient:
    def __init__(self, endpoint: Optional[str] = None, deployment: Optional[str] = None, api_version: str | None = None, credential: Any = None):
        self.endpoint = endpoint
        self.deployment = deployment
        self.api_version = api_version
        self.credential = credential
        if AsyncAzureOpenAI and endpoint and credential:
            self.client = AsyncAzureOpenAI(
                azure_endpoint=endpoint,
                azure_ad_token=credential,
                api_version=api_version,
            )
        else:  # pragma: no cover - simplified
            self.client = None

    async def complete(self, messages: List[Dict[str, str]], **kwargs) -> Dict[str, Any]:
        if self.client:
            resp = await self.client.chat.completions.create(
                model=self.deployment,
                messages=messages,
                **kwargs,
            )
            return resp  # type: ignore
        return {"choices": [{"message": {"content": "stub"}}]}
