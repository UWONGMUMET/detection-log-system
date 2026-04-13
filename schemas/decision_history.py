from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DecisionHistoryResponse(BaseModel):
    id: str
    decision_id: str
    user_id: str
    action: str
    field: Optional[str] = None
    old_value: Optional[str] = None
    new_value: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True