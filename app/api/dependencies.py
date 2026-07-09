from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session
from app.db.database import get_session
from app.services.user import UserService
from app.services.list import ListService
from app.core.security import decode_access_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")


def get_user_service(
    session: Session = Depends(get_session)
):
    return UserService(session)


def get_list_service(
    session: Session = Depends(get_session)
):
    return ListService(session)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    service: UserService = Depends(get_user_service)
):
    try:
        payload = decode_access_token(token)

        user_id = int(payload["sub"])

        user = service.get_by_id(user_id)

        return user

    except (ValueError, KeyError, TypeError) as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )
