from fastapi import APIRouter, Depends, HTTPException
from app.schemas.auth import AuthRegister, AuthLogin, TokenResponse
from app.schemas.user import UserRead
from app.services.auth import AuthService
from app.core.security import create_access_token
from app.api.dependencies import get_auth_service


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserRead)
def register(
    data: AuthRegister,
    service: AuthService = Depends(get_auth_service)
):
    try:
        user = service.register(
            phone_number=data.phone_number,
            name=data.name,
            password=data.password,
        )

        return user

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post("/login", response_model=TokenResponse)
def login(
    data: AuthLogin,
    service: AuthService = Depends(get_auth_service)
):
    try:
        user = service.login(
            phone_number=data.phone_number,
            password=data.password
        )

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )

    assert user.id is not None
    token = create_access_token(user.id)

    return {
        "access_token": token,
        "token_type": "bearer"
    }
