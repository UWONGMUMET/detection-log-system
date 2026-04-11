from sqlalchemy.orm import Session
from models.user import User
from core.security import hash_password
from fastapi import HTTPException

def get_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: str):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def update_user(db: Session, user_id: str, data):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if data.email:
        user.email = data.email
    if data.password:
        user.password = hash_password(data.password)
    
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: str):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"detail": "User deleted successfully"}