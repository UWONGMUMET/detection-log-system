from sqlalchemy.orm import Session
from models.decision import Decision
from fastapi import HTTPException 
from services.decision_history_service import log_history

def create_decision(db: Session, user, data):
    decision = Decision(
        title=data.title,
        description=data.description,
        user_id=user.get("sub")
    )
    db.add(decision)
    db.commit()
    db.refresh(decision)

    log_history(db, decision.id, user.get("sub"), "CREATE")
    db.commit()
    return decision

def get_all_decisions(db: Session, user):
    return db.query(Decision).all()

def get_decision_by_id(db: Session, decision_id: str, user):
    decision = db.query(Decision).filter(Decision.id == decision_id).first()
    if not decision:
        raise HTTPException(status_code=404, detail="Decision not found")
    return decision

def update_decision(db: Session, decision_id: str, data, user):
    decision = db.query(Decision).filter(Decision.id == decision_id).first()
    if not decision:
        raise HTTPException(status_code=404, detail="Decision not found")
    
    if user.get("role") != "ADMIN" and decision.user_id != user.get("sub"):
        raise HTTPException(status_code=403, detail="Not authorized to update this decision")
    
    for key, value in data.dict(exclude_unset=True).items():
        old_value = getattr(decision, key)

        if old_value != value:
            log_history(
                db,
                decision.id,
                user.get("sub"),
                "UPDATE",
                field=key,
                old=old_value,
                new=value
            )
        setattr(decision, key, value)

    db.commit()
    db.refresh(decision)
    return decision

def delete_decision(db: Session, decision_id: str, user):
    decision = db.query(Decision).filter(Decision.id == decision_id).first()
    if not decision:
        raise HTTPException(status_code=404, detail="Decision not found")
    
    if user.get("role") != "ADMIN" and decision.user_id != user.get("sub"):
        raise HTTPException(status_code=403, detail="Not authorized to delete this decision")
    
    log_history(db, decision.id, user.get("sub"), "DELETE")
    db.commit()
    
    db.delete(decision)
    db.commit()
    return {"detail": "Decision deleted successfully"}