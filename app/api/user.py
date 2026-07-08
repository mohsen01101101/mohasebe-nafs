from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserRegister, UserLogin, UserRead, UserUpdate, UserDelete, TokenResponse
from app.services.user import UserService
from app.core.security import create_access_token
from app.api.dependencies import get_user_service, get_current_user
from app.db.models.user import User
from app.api.permissions import require_teacher


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[UserRead])
def get_users(
    _: User = Depends(require_teacher),
    service: UserService = Depends(get_user_service)
):
    users = service.get_all()

    return users


@router.get("/{user_id}", response_model=UserRead)
def get_user_by_id(
    user_id: int,
    _: User = Depends(require_teacher),
    service: UserService = Depends(get_user_service)
):
    try:
        user = service.get_by_id(user_id)

        return user
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.get("/me", response_model=UserRead)
def get_me(
    current_user: User = Depends(get_current_user),
):
    return current_user


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


@router.patch("/me", response_model=UserRead)
def update_me(
    data: UserUpdate,
    current_user: User = Depends(get_current_user),
    service: UserService = Depends(get_user_service)
):
    try:
        assert current_user.id is not None
        user = service.update(
            user_id=current_user.id,
            name=data.name,
            current_password=data.current_password,
            new_password=data.new_password
        )

        return user

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/me", status_code=204)
def delete_me(
    data: UserDelete,
    current_user: User = Depends(get_current_user),
    service: UserService = Depends(get_user_service)
):
    try:
        assert current_user.id is not None
        service.delete(
            user_id=current_user.id,
            password=data.password
        )
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
