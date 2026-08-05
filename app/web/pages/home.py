from fasthtml.common import *
from app.schemas.user import UserRead
from app.domain.enum.role import Role
from app.web.pages.student import home as student
from app.web.pages.teacher import home as teacher


def home(
        req: Request,
        current_user: UserRead
):
    if current_user.role == Role.STUDENT:
        return student.home(req)

    return teacher.home(req)
