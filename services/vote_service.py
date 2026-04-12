from sqlalchemy.orm import Session
from models.vote import Vote
from fastapi import HTTPException

def vote_decision(db: Session, user, data):
    existing = db.query(Vote).filter(Vote.decision_id == data.decision_id, Vote.user_id == user.get("sub")).first()
    if existing:
        raise HTTPException(status_code=400, detail="You have already voted on this decision")
    
    vote = Vote(
        decision_id=data.decision_id,
        user_id=user.get("sub"),
        vote_type=data.vote_type
    )

    db.add(vote)
    db.commit()
    db.refresh(vote)
    return vote

def get_votes_by_decision(db: Session, decision_id: str):
    return db.query(Vote).filter(Vote.decision_id == decision_id).all()