# app/db/models/user.py
from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from app.db.session import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    # Relationship with script model
    scripts = relationship("Script", back_populates="user", cascade="all, delete-orphan")
