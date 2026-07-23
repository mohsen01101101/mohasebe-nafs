from fasthtml.common import *
from app.web.client.lists import get_my_lists
from app.core.utils.date_converter import jalali_to_gregorian
from app.web.components.lists import lists


def register_list_routes(rt):
    @rt("/web-api/lists")
    def get_lists(
        session,
        jalali_date: str | None = None
    ):

        token = session["access_token"]

        selected_date = None

        if jalali_date:
            selected_date = jalali_to_gregorian(jalali_date)

        lists_data = get_my_lists(
            token=token,
            selected_date=selected_date
        )
        lists_html = lists(lists_data)

        return lists_html
