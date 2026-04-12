from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.decision import DecisionCreate, DecisionUpdate, DecisionResponse
from services.decision_service import create_decision, get_all_decisions, get_decision_by_id, update_decision, delete_decision
from core.dependencies import get_current_user

router = APIRouter(prefix="/decisions", tags=["decisions"])

@router.post("/", response_model=DecisionResponse)
def create(data: DecisionCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return create_decision(db, user, data)

@router.get("/", response_model=list[DecisionResponse])
def read_decisions(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return get_all_decisions(db, user)

@router.get("/{decision_id}", response_model=DecisionResponse)
def read_decision(decision_id: str, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return get_decision_by_id(db, decision_id, user)

@router.put("/{decision_id}", response_model=DecisionResponse)
def update_decision_endpoint(decision_id: str, data: DecisionUpdate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return update_decision(db, decision_id, data, user)

@router.delete("/{decision_id}")
def delete_decision_endpoint(decision_id: str, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return delete_decision(db, decision_id, user)