from fasthtml.common import *
from datetime import datetime
from app.core.constants import IRAN_TZ
from app.web.client import actions as client_actions
from app.web.components.actions import actions_with_state, action_item_with_state


def register_action_routes(rt):
    @rt(
        "/web-api/lists/{list_id}/actions",
        methods=["GET"]
    )
    def get_actions_with_state(
        session,
        list_id: int,
        selected_date_iso: str | None = None
    ):
        token = session["access_token"]

        selected_date = None

        if selected_date_iso:
            selected_date = datetime.fromisoformat(
                selected_date_iso.replace("Z", "+00:00")
            ).astimezone(IRAN_TZ).date()

        actions_with_state_data = client_actions.get_my_actions_with_state(
            token=token,
            list_id=list_id,
            selected_date=selected_date
        )
        actions_with_state_html = actions_with_state(
            list_id=list_id,
            actions_data=actions_with_state_data
        )

        return actions_with_state_html

    @rt(
        "/web-api/lists/{list_id}/actions/{action_id}/state",
        methods=["PATCH"]
    )
    def update_action_state(
        session,
        list_id: int,
        action_id: int,
        index: int,
        is_done: bool | None = None,
        rating: float | None = None,
        selected_date_iso: str | None = None

    ):
        token = session["access_token"]

        selected_day = None

        if selected_date_iso:
            selected_day = datetime.fromisoformat(
                selected_date_iso.replace("Z", "+00:00")
            ).astimezone(IRAN_TZ).date()

        client_actions.update_my_action_state(
            token=token,
            list_id=list_id,
            action_id=action_id,
            is_done=is_done,
            rating=rating,
            day=selected_day
        )

        actions_with_state_data = client_actions.get_my_actions_with_state(
            token=token,
            list_id=list_id,
            selected_date=selected_day
        )

        updated_action = next(
            item
            for item in actions_with_state_data
            if item.id == action_id
        )

        action_item_with_state_html = action_item_with_state(
            list_id=list_id,
            item=updated_action,
            index=index
        )

        return action_item_with_state_html
