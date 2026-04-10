from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.auth import UserCreate, UserLogin, UserResponse, TokenResponse
from services.auth_service import register_user, login_user
from db.session import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, email=user.email, password=user.password)

@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(db, email=user.email, password=user.password)