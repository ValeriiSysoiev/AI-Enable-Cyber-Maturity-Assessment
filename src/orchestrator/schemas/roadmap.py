from pydantic import BaseModel
from typing import List
from .gap import GapAnalysisRequest
from .initiative import Initiative


class RoadmapRequest(BaseModel):
    project_id: str
    gaps: List[str]


class RoadmapResponse(BaseModel):
    initiatives: List[Initiative]
