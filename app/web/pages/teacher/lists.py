from fasthtml.common import *
from app.web.middleware.permissions import require_teacher
from app.schemas.user import UserRead
from app.web.layouts.base import app_layout
from app.web.client.users import get_user_by_id
from app.web.client.lists import get_lists
from app.web.components.lists import student_lists_overview
from app.web.components.back_button import back_button


def lists(
    req: Request,
    current_user: UserRead,
    user_id: int
):
    require_teacher(current_user)

    token = req.session["access_token"]

    student = get_user_by_id(
        token=token,
        user_id=user_id
    )

    student_lists_data = get_lists(
        token=token,
        user_id=user_id
    )
    lists_overview_html = student_lists_overview(
        user_id=user_id,
        lists_data=student_lists_data,
    )

    page_content = (
        H2(
            f"لیست‌های {student.name}",
            cls="text-center text-xl font-bold mb-2"
        ),
        lists_overview_html,

        back_button(
            href=f"/reports/{user_id}/"
        )
    )

    return app_layout(
        req=req,
        page_content=page_content,
        title="صفحه لیست‌ها"
    )
