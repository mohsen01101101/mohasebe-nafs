from fasthtml.common import *
from datetime import date
from app.web.client.lists import get_my_lists
from app.web.components.lists import lists_with_actions


def register_list_routes(rt):
    @rt("/web-api/lists")
    def get_lists(
        session,
        selected_date_iso: str | None = None
    ):

        token = session["access_token"]

        selected_date = None

        if selected_date_iso:
            selected_date = date.fromisoformat(selected_date_iso)

        lists_data = get_my_lists(
            token=token,
            selected_date=selected_date
        )
        lists_with_actions_html = lists_with_actions(lists_data)

        return lists_with_actions_html
