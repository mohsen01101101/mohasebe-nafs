from fasthtml.common import *
from app.schemas.user import UserRead
from app.domain.enum.role import Role
from app.web.pages.student import lists as student


def lists(
        req: Request,
        current_user: UserRead
):
    if current_user.role == Role.STUDENT:
        return student.lists(req)
