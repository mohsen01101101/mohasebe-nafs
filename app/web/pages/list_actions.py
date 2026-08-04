from fasthtml.common import *
from datetime import datetime
from app.core.constants import IRAN_TZ
from app.web.layouts.base import app_layout
from app.web.client.actions import get_my_actions
from app.web.components.actions import actions_overview
from app.web.components.back_button import back_button


def list_actions(
    req: Request,
    list_id: int
):
    token = req.session["access_token"]

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
        H2(
            f"اعمال لیست {list_id}",
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
