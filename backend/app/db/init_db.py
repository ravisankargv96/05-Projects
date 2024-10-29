from app.db.models.user import User
from app.db.models.script import Script  # Import all models
from app.db.models.execution_step import ExecutionStep
from app.db.session import Base, engine

# Initializing db tables
# init_db() -> models/*.py, session.py

def init_db():
    """Create all tables in the database."""
    Base.metadata.create_all(bind=engine)
