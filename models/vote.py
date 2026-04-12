from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
import uuid
from db.base import Base

class Vote(Base):
    __tablename__ = "votes"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    decision_id = Column(String, ForeignKey("decisions.id"), nullable=False)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)

    vote_type = Column(String) # UP / DOWN 

    __table_args__ = (UniqueConstraint('decision_id', 'user_id', name='unique_user_vote'),)