from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.user import UserResponse, UserUpdate
from services.user_service import get_users, get_user_by_id, update_user, delete_user
from core.dependencies import admin_required

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db), user = Depends(admin_required)):
    return get_users(db)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: str, db: Session = Depends(get_db), user = Depends(admin_required)):
    return get_user_by_id(db, user_id)

@router.put("/{user_id}", response_model=UserResponse)
def update_user_info(user_id: str, data: UserUpdate, db: Session = Depends(get_db), user = Depends(admin_required)):
    return update_user(db, user_id, data)

@router.delete("/{user_id}")
def delete_user_info(user_id: str, db: Session = Depends(get_db), user = Depends(admin_required)):
    return delete_user(db, user_id)