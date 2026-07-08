from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserRegister, UserLogin, UserRead, TokenResponse
from app.services.user import UserService
from app.core.security import create_access_token
from app.api.dependencies import get_user_service


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register", response_model=UserRead)
def register(
    user_data: UserRegister,
    service: UserService = Depends(get_user_service)
):
    try:
        user = service.register(
            phone_number=user_data.phone_number,
            name=user_data.name,
            password=user_data.password,
        )

        return user

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post("/login", response_model=TokenResponse)
def login(
    user_data: UserLogin,
    service: UserService = Depends(get_user_service)
):
    try:
        user = service.login(
            phone_number=user_data.phone_number,
            password=user_data.password
        )

        assert user.id is not None
        token = create_access_token(user.id)

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )
