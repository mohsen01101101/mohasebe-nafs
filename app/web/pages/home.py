from fasthtml.common import *
from datetime import date
from app.web.layouts.base import app_layout
from app.web.client.lists import get_my_lists
from app.web.components.datepicker import datepicker
from app.web.components.lists import lists


def home(req: Request):
    token = req.session["access_token"]

    lists_data = get_my_lists(
        token=token,
        selected_date=date.today()
    )
    lists_html = lists(lists_data)

    page_content = (
        H1(
            "اعمال امروز",
            cls="text-center text-2xl font-bold mb-4"
        ),

        datepicker(),

        lists_html
    )

    return app_layout(
        req=req,
        page_content=page_content,
        title="صفحه اصلی"
    )
