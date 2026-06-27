from sqlmodel import SQLModel
from app.db.database import engine
from app.db.models import user, list, action


SQLModel.metadata.create_all(engine)
