from sqlalchemy import Column, String, DateTime, ForeignKey
from datetime import datetime
import uuid
from db.base import Base

class DecisionHistory(Base):
    __tablename__ = 'decision_histories'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    decision_id = Column(String, ForeignKey('decisions.id', ondelete="CASCADE"))
    user_id = Column(String, ForeignKey('users.id'))

    action = Column(String)  # CREATE / UPDATE / DELETE
    field = Column(String)  

    old_value = Column(String, nullable=True)
    new_value = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)