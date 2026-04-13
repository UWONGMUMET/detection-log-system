from sqlalchemy.orm import Session
from models.decision_history import DecisionHistory
from fastapi import HTTPException

def log_history(db: Session, data):
    history = DecisionHistory(
        decision_id = data.decision_id,
        user_id = data.user_id,
        action = data.action,
        field = data.field,
        old_value = str(data.old) if data.old else None,
        new_value = str(data.new) if data.new else None
    )
    db.add(history)

def get_history_by_decision(db: Session, decision_id: str):
    return db.query(DecisionHistory).filter(
        DecisionHistory.decision_id == decision_id
    ).order_by(
        DecisionHistory.created_at.desc()
    ).all()

def delete_history(db: Session, history_id: str):
    history = db.query(DecisionHistory).filter(DecisionHistory.id == history_id).first()
    if not history:
        raise HTTPException(status_code=404, detail="History not found")
    
    db.delete(history)
    db.commit()
    return {"detail": "History deleted successfully"}