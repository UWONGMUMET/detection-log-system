from db.session import SessionLocal
from models.user import User 
from core.security import hash_password

def seed_admin():
    db = SessionLocal()

    admin_email = "admin@example.com"

    existing = db.query(User).filter(User.email == admin_email).first()
    if existing:
        print("Admin user already exists")
        return
    
    admin = User(
        email=admin_email,
        password=hash_password("admin123"),
        role="admin"
    )

    db.add(admin)
    db.commit()
    db.close()

    print("Admin created!")

if __name__ == "__main__":
    seed_admin()