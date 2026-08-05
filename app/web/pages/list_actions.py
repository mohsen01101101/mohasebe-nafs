from fasthtml.common import *
from app.schemas.user import UserRead
from app.domain.enum.role import Role
from app.web.pages.student import list_actions as student


def list_actions(
        req: Request,
        list_id: int,
        current_user: UserRead
):
    if current_user.role == Role.STUDENT:
        return student.list_actions(
            req=req,
            list_id=list_id
        )
