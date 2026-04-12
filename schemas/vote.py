from pydantic import BaseModel

class VoteCreate(BaseModel):
    decision_id: str
    vote_type: str  # UP / DOWN

class VoteResponse(BaseModel):
    id: str
    decision_id: str
    user_id: str
    vote_type: str

    class Config:
        from_attributes = True