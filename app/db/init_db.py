from sqlmodel import SQLModel
from app.db.database import engine
from app.db.models import user, list, action


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
