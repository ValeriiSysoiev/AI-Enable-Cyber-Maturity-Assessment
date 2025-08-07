"""Pydantic models for cyber maturity assessment data stored in Cosmos DB."""

from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class Evidence(BaseModel):
    """Represents a single piece of maturity evidence."""

    id: str = Field(..., description="Unique evidence identifier")
    description: str
    source: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class AssessmentRecord(BaseModel):
    """Top level document persisted per assessment."""

    id: str = Field(..., description="Assessment identifier")
    client_name: str
    created_by: str
    created_on: datetime = Field(default_factory=datetime.utcnow)
    evidence: List[Evidence] = Field(default_factory=list)
    gap_summary: Optional[str] = None
    recommendations: Optional[List[str]] = None

    class Config:
        json_schema_extra = {
            "description": "Schema for storing cyber maturity assessment data in Cosmos DB",
            "examples": [
                {
                    "id": "A1",
                    "client_name": "Contoso",
                    "created_by": "user@example.com",
                    "evidence": [
                        {
                            "id": "E1",
                            "description": "Documented incident response plan",
                            "source": "documentation",
                        }
                    ],
                }
            ],
        }
