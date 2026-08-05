from fasthtml.common import *
from datetime import datetime
from app.core.constants import IRAN_TZ
from app.web.middleware.permissions import require_student
from app.schemas.user import UserRead
from app.web.layouts.base import app_layout
from app.web.client.lists import get_my_lists
from app.web.components.datepicker import datepicker
from app.web.components.lists import lists_overview
from app.web.components.back_button import back_button


def lists(
    req: Request,
    current_user: UserRead
):
    require_student(current_user)

    token = req.session["access_token"]

    lists_data = get_my_lists(
        token=token,
        selected_date=datetime.now(IRAN_TZ).date()
    )
    lists_overview_html = lists_overview(
        lists_data=lists_data,
    )

    page_content = (
        Form(
            Label(
                Input(
                    name="title",
                    type="text",
                    required=True,
                    placeholder="نام لیست *",
                    cls="input validator w-full",
                ),

                Span(
                    "وارد کردن نام لیست، ضروری است",
                    cls="validator-hint hidden"
                ),

                cls="fieldset"
            ),

            datepicker(),

            Button(
                "ایجاد لیست",
                type="submit",
                cls="btn btn-primary mt-4"
            ),

            hx_post="/web-api/lists",
            hx_swap="none",
            cls="fieldset bg-base-200 border-base-300 rounded-box border p-4"
        ),

        H2(
            "لیست‌های من",
            cls="text-center text-xl font-bold mt-8 mb-2"
        ),
        lists_overview_html,

        back_button(
            href="/"
        )
    )

    return app_layout(
        req=req,
        page_content=page_content,
        title="صفحه لیست‌ها"
    )
