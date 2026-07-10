from fastapi import Depends, HTTPException
from app.api.dependencies import get_current_user
from app.db.models.user import UserModel
from app.domain.enum.role import Role


def require_teacher(
    current_user: UserModel = Depends(get_current_user),
):
    if current_user.role != Role.TEACHER:
        raise HTTPException(
            status_code=403,
            detail="You don't have permission to access this resource."
        )

    return current_user
