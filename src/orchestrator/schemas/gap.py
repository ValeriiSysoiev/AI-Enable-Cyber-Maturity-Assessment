from pydantic import BaseModel
from typing import List


class GapAnalysisRequest(BaseModel):
    project_id: str
    data: str


class GapAnalysisResponse(BaseModel):
    gaps: List[str]
