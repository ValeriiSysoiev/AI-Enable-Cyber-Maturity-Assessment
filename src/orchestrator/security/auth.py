from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from typing import List, Callable

bearer_scheme = HTTPBearer(auto_error=False)


async def get_current_roles(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)) -> List[str]:
    if not credentials:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    token = credentials.credentials
    roles = token.split(",") if token else []
    return roles


def require_roles(*required: str) -> Callable:
    async def verifier(roles: List[str] = Depends(get_current_roles)):
        if not any(role in roles for role in required):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return verifier
