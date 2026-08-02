from fasthtml.common import *
from datetime import date
from app.web.client.actions import get_my_actions_with_state, update_my_action_state
from app.web.components.actions import actions, action_item


def register_action_routes(rt):
    @rt("/web-api/lists/{list_id}/actions")
    def get_actions_with_state(
        session,
        list_id: int,
        selected_date_iso: str | None = None
    ):
        token = session["access_token"]

        selected_date = None

        if selected_date_iso:
            selected_date = date.fromisoformat(selected_date_iso)

        actions_with_state_data = get_my_actions_with_state(
            token=token,
            list_id=list_id,
            selected_date=selected_date
        )
        actions_with_state_html = actions(
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
        day: str | None = None

    ):
        token = session["access_token"]

        selected_day = None

        if day:
            selected_day = date.fromisoformat(day)

        update_my_action_state(
            token=token,
            list_id=list_id,
            action_id=action_id,
            is_done=is_done,
            rating=rating,
            day=selected_day
        )

        actions_with_state_data = get_my_actions_with_state(
            token=token,
            list_id=list_id,
            selected_date=selected_day
        )

        updated_action = next(
            item
            for item in actions_with_state_data
            if item.id == action_id
        )

        action_with_state_html = action_item(
            list_id=list_id,
            item=updated_action,
            index=index
        )

        return action_with_state_html
