from pydantic import BaseModel


class ReportRequest(BaseModel):
    project_id: str


class ReportResponse(BaseModel):
    url: str
