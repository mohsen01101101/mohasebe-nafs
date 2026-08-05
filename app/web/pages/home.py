from fasthtml.common import *
from app.db.models.user import UserModel
from app.domain.enum.role import Role
from app.web.pages.student import home as student


def home(
        req: Request,
        current_user: UserModel
):
    if current_user.role == Role.STUDENT:
        return student.home(req)
