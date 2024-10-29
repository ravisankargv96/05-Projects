# app/db/models/script.py
from sqlalchemy import Column, Integer, Text, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Script(Base):
    __tablename__ = "scripts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    code = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    # Relationship with User model
    user = relationship("User", back_populates="scripts")
    execution_steps = relationship("ExecutionStep", back_populates="script", cascade="all, delete-orphan")
