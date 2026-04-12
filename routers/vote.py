from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.vote import VoteCreate, VoteResponse
from services.vote_service import vote_decision, get_votes_by_decision
from core.dependencies import get_current_user

router = APIRouter(prefix="/votes", tags=["votes"])

@router.post("/", response_model=VoteResponse)
def vote(data: VoteCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return vote_decision(db, user, data)

@router.get("/{decision_id}", response_model=list[VoteResponse])
def get_votes(decision_id: str, db: Session = Depends(get_db)):
    return get_votes_by_decision(db, decision_id)