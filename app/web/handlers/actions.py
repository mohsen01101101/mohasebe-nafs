from fasthtml.common import *
from app.web.client.actions import get_my_actions_with_state
from app.core.utils.date_converter import jalali_to_gregorian
from app.web.components.actions import actions


def register_action_routes(rt):
    @rt("/web-api/lists/{list_id}/actions")
    def get_actions_with_state(
        session,
        list_id: int,
        jalali_date: str | None = None
    ):
        token = session["access_token"]

        selected_date = None

        if jalali_date:
            selected_date = jalali_to_gregorian(jalali_date)

        actions_with_state_data = get_my_actions_with_state(
            token=token,
            list_id=list_id,
            selected_date=selected_date
        )
        actions_with_state_html = actions(actions_with_state_data)

        return actions_with_state_html
