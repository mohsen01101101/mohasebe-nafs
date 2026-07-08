from fastapi import Depends
from sqlmodel import Session
from app.db.database import get_session
from app.services.user import UserService


def get_user_service(
    session: Session = Depends(get_session)
):
    return UserService(session)
