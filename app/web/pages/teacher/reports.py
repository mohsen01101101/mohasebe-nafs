from fasthtml.common import *
from app.web.middleware.permissions import require_teacher
from app.schemas.user import UserRead
from app.web.layouts.base import app_layout
from app.web.client.users import get_user_by_id
from app.web.client.lists import get_lists
from app.web.components.datepicker import datepicker
from app.web.components.lists import student_lists_with_actions


def reports(
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
    student_lists_with_actions_html = student_lists_with_actions(
        user_id=user_id,
        lists_data=student_lists_data
    )

    page_content = (
        H1(
            "اعمال امروز",
            id="homepage-title",
            cls="text-center text-2xl font-bold mb-4"
        ),

        datepicker(),

        student_lists_with_actions_html,

        A(
            f"مشاهده لیست‌های {student.name}",
            role="button",
            href=f"/reports/{user_id}/lists",
            cls="btn mt-4"
        )
    )

    return app_layout(
        req=req,
        page_content=page_content,
        title="صفحه گزارش"
    )
