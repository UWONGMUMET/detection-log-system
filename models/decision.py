from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from db.base import Base

class Decision(Base):
    __tablename__ = "decisions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)

    status = Column(String, nullable=False, default="PENDING")  # PENDING, APPROVED, REJECTED

    user_id = Column(String, ForeignKey("users.id"))

    histories = relationship(
        "DecisionHistory", cascade="all, delete", passive_deletes=True
    )
    created_at = Column(DateTime, default=datetime.utcnow)