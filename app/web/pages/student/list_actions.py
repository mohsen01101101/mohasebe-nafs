from fasthtml.common import *
from datetime import datetime
from app.core.constants import IRAN_TZ
from app.web.layouts.base import app_layout
from app.web.client.lists import get_my_list
from app.web.client.actions import get_my_actions
from app.web.components.datepicker import datepicker
from app.web.components.actions import actions_overview
from app.web.components.back_button import back_button


def list_actions(
    req: Request,
    list_id: int
):
    token = req.session["access_token"]

    list_item = get_my_list(
        token=token,
        list_id=list_id
    )

    actions_data = get_my_actions(
        token=token,
        list_id=list_id,
        selected_date=datetime.now(IRAN_TZ).date()
    )
    actions_overview_html = actions_overview(
        list_id=list_id,
        actions_data=actions_data
    )

    page_content = (
        Form(
            Label(
                Input(
                    name="title",
                    type="text",
                    required=True,
                    placeholder="نام عمل *",
                    cls="input validator w-full",
                ),

                Span(
                    "وارد کردن نام عمل، ضروری است",
                    cls="validator-hint hidden"
                ),

                Input(
                    name="description",
                    type="text",
                    placeholder="توضیحات",
                    cls="input input-sm validator w-full",
                ),

                Div(
                    Input(
                        name="tracking_type",
                        type="radio",
                        required=True,
                        value="CHECKBOX",
                        aria_label="انجام شده / انجام نشده",
                        cls="btn btn-sm btn-soft flex-1/2 tracking-type-btn"
                    ),

                    Input(
                        name="tracking_type",
                        type="radio",
                        required=True,
                        value="RATING",
                        aria_label="امتیازی",
                        cls="btn btn-sm btn-soft flex-1/2 tracking-type-btn"
                    ),

                    cls="flex gap-2"
                ),

                cls="fieldset"
            ),

            datepicker(),

            Button(
                "افزودن عمل",
                type="submit",
                cls="btn btn-primary mt-4"
            ),

            hx_post=f"/web-api/lists/{list_item.id}/actions",
            hx_swap="none",
            cls="fieldset bg-base-200 border-base-300 rounded-box border p-4"
        ),

        H2(
            f"اعمال {list_item.title}",
            cls="text-center text-xl font-bold mt-8 mb-2"
        ),
        actions_overview_html,

        back_button(
            href="/lists"
        )
    )

    return app_layout(
        req=req,
        page_content=page_content,
        title="صفحه اعمال لیست"
    )
