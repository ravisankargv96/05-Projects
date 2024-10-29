# app/db/models/execution_step.py
from sqlalchemy import Column, Integer, JSON, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class ExecutionStep(Base):
    __tablename__ = "execution_steps"

    id = Column(Integer, primary_key=True, index=True)
    script_id = Column(Integer, ForeignKey("scripts.id", ondelete="CASCADE"))
    step_number = Column(Integer, nullable=False)
    state = Column(JSON, nullable=False)  # JSON format for the state of the array at each step
    created_at = Column(TIMESTAMP, server_default=func.now())

    # Relationship with Script model
    script = relationship("Script", back_populates="execution_steps")
