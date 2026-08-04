from fasthtml.common import *
from datetime import datetime
from app.core.constants import IRAN_TZ
from app.web.layouts.base import app_layout
from app.web.client.lists import get_my_lists
from app.web.components.datepicker import datepicker
from app.web.components.lists import lists_with_actions


def home(req: Request):
    token = req.session["access_token"]

    lists_data = get_my_lists(
        token=token,
        selected_date=datetime.now(IRAN_TZ).date()
    )
    lists_with_actions_html = lists_with_actions(lists_data)

    page_content = (
        H1(
            "اعمال امروز",
            id="homepage-title",
            cls="text-center text-2xl font-bold mb-4"
        ),

        datepicker(),

        lists_with_actions_html,

        A(
            "مشاهده و ویرایش لیست‌ها",
            role="button",
            href="/lists",
            cls="btn mt-4"
        )
    )

    return app_layout(
        req=req,
        page_content=page_content,
        title="صفحه اصلی"
    )
