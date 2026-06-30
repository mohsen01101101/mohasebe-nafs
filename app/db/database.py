from sqlmodel import create_engine, Session
from app.core.config import settings
from sqlalchemy import event


engine = create_engine(settings.sqlite_url)


@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, _):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


def get_session():
    with Session(engine) as session:
        yield session
