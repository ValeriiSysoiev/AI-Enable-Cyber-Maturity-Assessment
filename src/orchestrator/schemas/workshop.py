from pydantic import BaseModel


class WorkshopAnalysisRequest(BaseModel):
    project_id: str
    transcript: str


class WorkshopAnalysisResponse(BaseModel):
    summary: str
