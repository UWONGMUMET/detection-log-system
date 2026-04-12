from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.session import get_db
from core.dependencies import admin_required
from services.user_dashboard_service import get_dashboard_stats, users_per_day

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/stats")
def dashboard_stats(db: Session = Depends(get_db), user = Depends(admin_required)):
    return get_dashboard_stats(db)

@router.get("/users-per-day")
def dashboard_users_per_day(db: Session = Depends(get_db), user = Depends(admin_required)):
    return users_per_day(db)