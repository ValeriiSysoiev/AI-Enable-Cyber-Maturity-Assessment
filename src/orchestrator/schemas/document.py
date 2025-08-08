from pydantic import BaseModel


class DocumentIngestRequest(BaseModel):
    project_id: str
    content: str


class DocumentIngestResponse(BaseModel):
    document_id: str
