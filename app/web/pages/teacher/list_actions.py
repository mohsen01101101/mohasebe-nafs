from fasthtml.common import *
from app.web.middleware.permissions import require_teacher
from app.schemas.user import UserRead
from app.web.layouts.base import app_layout
from app.web.client.users import get_user_by_id
from app.web.client.lists import get_list
from app.web.client.actions import get_actions
from app.web.components.actions import student_actions_overview
from app.web.components.back_button import back_button


def list_actions(
    req: Request,
    current_user: UserRead,
    user_id: int,
    list_id: int
):
    require_teacher(current_user)

    token = req.session["access_token"]

    student = get_user_by_id(
        token=token,
        user_id=user_id
    )

    student_list_item = get_list(
        token=token,
        user_id=user_id,
        list_id=list_id
    )

    actions_data = get_actions(
        token=token,
        user_id=user_id,
        list_id=list_id,
    )
    actions_overview_html = student_actions_overview(
        user_id=user_id,
        list_id=list_id,
        actions_data=actions_data
    )

    page_content = (
        H2(
            f"اعمال {student_list_item.title} ({student.name})",
            cls="text-center text-xl font-bold mb-2"
        ),
        actions_overview_html,

        back_button(
            href=f"/reports/{user_id}/lists"
        )
    )

    return app_layout(
        req=req,
        page_content=page_content,
        title="صفحه اعمال لیست"
    )
