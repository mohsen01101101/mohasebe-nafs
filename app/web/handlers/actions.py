from fasthtml.common import *
from app.web.client.actions import get_my_actions
from app.core.utils.date_converter import jalali_to_gregorian
from app.web.components.actions import actions


def register_action_routes(rt):
    @rt("/web-api/lists/{list_id}/actions")
    def get_actions(
        session,
        list_id: int,
        jalali_date: str | None = None
    ):
        token = session["access_token"]

        selected_date = None

        if jalali_date:
            selected_date = jalali_to_gregorian(jalali_date)

        actions_data = get_my_actions(
            token=token,
            list_id=list_id,
            selected_date=selected_date
        )
        actions_html = actions(actions_data)

        return actions_html
