from typing import Optional

try:
    from azure.identity.aio import DefaultAzureCredential
    from azure.keyvault.secrets.aio import SecretClient
except Exception:  # pragma: no cover - optional
    DefaultAzureCredential = None  # type: ignore
    SecretClient = None  # type: ignore


async def get_secret(vault_url: str, name: str) -> Optional[str]:
    if DefaultAzureCredential is None:
        return None
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=vault_url, credential=credential)
    secret = await client.get_secret(name)
    await client.close()
    await credential.close()
    return secret.value
