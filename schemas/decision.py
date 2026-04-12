from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DecisionCreate(BaseModel):
    title: str
    description: Optional[str] = None

class DecisionUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None  # PENDING, APPROVED, REJECTED

class DecisionResponse(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    status: str
    user_id: str
    created_at: datetime

    class Config:
        from_attributes = True