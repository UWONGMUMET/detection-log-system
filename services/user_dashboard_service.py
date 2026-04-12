from sqlalchemy.orm import Session
from models.user import User
from sqlalchemy import func
from datetime import date, timedelta, datetime

def get_dashboard_stats(db: Session):
    total_users = db.query(func.count(User.id)).scalar()
    active_users = db.query(func.count(User.id)).filter(User.is_active == True).scalar()
    inactive_users = db.query(func.count(User.id)).filter(User.is_active == False).scalar()
    
    today = date.today()
    new_users_today = db.query(func.count(User.id)).filter(func.date(User.created_at) == today).scalar()

    return {
        "total_users": total_users,
        "active_users": active_users,
        "inactive_users": inactive_users,
        "new_users_today": new_users_today
    }

def users_per_day(db: Session):
    last_7_days = datetime.utcnow() - timedelta(days=7)
    data = db.query(func.date(User.created_at), func.count(User.id)).filter(User.created_at >= last_7_days).group_by(func.date(User.created_at)).all()
    return [{"date": str(record[0]), "count": record[1]} for record in data]