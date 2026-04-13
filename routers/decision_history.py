from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.session import get_db
from services.decision_history_service import get_history_by_decision, delete_history
from schemas.decision_history import DecisionHistoryResponse
from core.dependencies import get_current_user, admin_required

router = APIRouter(prefix="/history", tags=["history"])

@router.get("/{decision_id}", response_model=list[DecisionHistoryResponse])
def get_history(
    decision_id: str,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return get_history_by_decision(db, decision_id)

@router.delete("/{history_id}")
def delete_history_endpoint(
    history_id: str,
    db: Session = Depends(get_db),
    user = Depends(admin_required)
):
    return delete_history(db, history_id)