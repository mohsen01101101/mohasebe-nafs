import bcrypt
import jwt
from datetime import datetime, timedelta
from app.core.constants import IRAN_TZ
from app.core.config import settings


def hash_password(password: str) -> str:
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")


def verify_password(password: str, password_hash: str) -> bool:
    return bcrypt.checkpw(
        password.encode("utf-8"),
        password_hash.encode("utf-8")
    )


def create_access_token(user_id: int):
    expire = datetime.now(IRAN_TZ) + timedelta(
        minutes=settings.access_token_expire_minutes
    )

    payload = {
        "sub": str(user_id),
        "exp": expire
    }

    token = jwt.encode(
        payload=payload,
        key=settings.secret_key,
        algorithm=settings.algorithm
    )

    return token


def decode_access_token(token: str):
    try:
        payload = jwt.decode(
            jwt=token,
            key=settings.secret_key,
            algorithms=[settings.algorithm]
        )

        return payload

    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired.")

    except jwt.InvalidTokenError:
        raise ValueError("Invalid token.")
