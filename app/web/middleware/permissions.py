from fastapi import HTTPException
from app.domain.enum.role import Role
from app.schemas.user import UserRead


def require_teacher(
    current_user: UserRead,
):
    if current_user.role != Role.TEACHER:
        raise HTTPException(
            status_code=403,
            detail="You don't have permission to access this resource."
        )

    return current_user


def require_student(
    current_user: UserRead,
):
    if current_user.role != Role.STUDENT:
        raise HTTPException(
            status_code=403,
            detail="You don't have permission to access this resource."
        )

    return current_user
