from pydantic import BaseModel


class Initiative(BaseModel):
    id: str
    description: str
