from fasthtml.common import *
from datetime import datetime
from app.core.constants import IRAN_TZ
from app.domain.enum.tracking_type import TrackingType
from app.web.client import actions as client_actions
from app.web.components.actions import actions_overview, actions_with_state, action_row, action_item_with_state, action_edit_row, student_actions_overview


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
            actions_data=actions_with_state_data,
            is_teacher=False
        )

        return actions_with_state_html

    @rt(
        "/web-api/lists/{list_id}/actions/overview",
        methods=["GET"]
    )
    def get_list_actions_overview(
        session,
        list_id: int
    ):
        token = session["access_token"]

        actions_data = client_actions.get_my_actions(
            token=token,
            list_id=list_id
        )
        actions_overview_html = actions_overview(
            list_id=list_id,
            actions_data=actions_data
        )

        return actions_overview_html

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
            index=index,
            is_teacher=False
        )

        return action_item_with_state_html

    @rt(
        "/web-api/lists/{list_id}/actions",
        methods=["POST"]
    )
    def create_action(
        session,
        list_id: int,
        title: str,
        tracking_type: TrackingType,
        description: str | None = None,
        is_done: bool | None = None,
        rating: float | None = None,
        selected_date_iso: str | None = None
    ):
        token = session["access_token"]

        started_at = None

        if selected_date_iso:
            started_at = datetime.fromisoformat(
                selected_date_iso.replace("Z", "+00:00")
            ).astimezone(IRAN_TZ)

        client_actions.create_action(
            token=token,
            list_id=list_id,
            title=title,
            tracking_type=tracking_type,
            description=description,
            is_done=is_done,
            rating=rating,
            started_at=started_at
        )

        response = Response(
            headers={
                "HX-Trigger": "actions:changed"
            }
        )

        return response

    @rt(
        "/web-api/lists/{list_id}/actions/{action_id}/edit",
        methods=["GET"]
    )
    def get_action_edit_row(
        session,
        list_id: int,
        action_id: int
    ):
        token = session["access_token"]

        action_item = client_actions.get_my_action(
            token=token,
            list_id=list_id,
            action_id=action_id
        )

        action_edit_row_html = action_edit_row(
            list_id=list_id,
            action_item=action_item
        )

        return action_edit_row_html

    @rt(
        "/web-api/lists/{list_id}/actions/{action_id}/row",
        methods=["GET"]
    )
    def get_list_row(
        session,
        list_id: int,
        action_id: int
    ):
        token = session["access_token"]

        action_item = client_actions.get_my_action(
            token=token,
            list_id=list_id,
            action_id=action_id
        )

        action_row_html = action_row(
            list_id=list_id,
            action_item=action_item
        )

        return action_row_html

    @rt(
        "/web-api/lists/{list_id}/actions/{action_id}",
        methods=["PATCH"]
    )
    def update_action(
        session,
        list_id: int,
        action_id: int,
        title: str | None = None,
        description: str | None = None
    ):
        token = session["access_token"]

        client_actions.update_my_action(
            token=token,
            list_id=list_id,
            action_id=action_id,
            title=title,
            description=description
        )

        response = Response(
            headers={
                "HX-Trigger": "actions:changed"
            }
        )

        return response

    @rt(
        "/web-api/lists/{list_id}/actions/{action_id}",
        methods=["DELETE"]
    )
    def delete_list(
        session,
        list_id: int,
        action_id: int
    ):
        token = session["access_token"]

        client_actions.delete_action(
            token=token,
            list_id=list_id,
            action_id=action_id
        )

        response = Response(
            headers={
                "HX-Trigger": "actions:changed"
            }
        )

        return response

    @rt(
        "/web-api/users/{user_id}/lists/{list_id}/actions",
        methods=["GET"]
    )
    def get_student_actions_with_state(
        session,
        user_id: int,
        list_id: int,
        selected_date_iso: str | None = None
    ):
        token = session["access_token"]

        selected_date = None

        if selected_date_iso:
            selected_date = datetime.fromisoformat(
                selected_date_iso.replace("Z", "+00:00")
            ).astimezone(IRAN_TZ).date()

        student_actions_with_state_data = client_actions.get_student_actions_with_state(
            token=token,
            user_id=user_id,
            list_id=list_id,
            selected_date=selected_date
        )
        student_actions_with_state_html = actions_with_state(
            list_id=list_id,
            actions_data=student_actions_with_state_data,
            is_teacher=True
        )

        return student_actions_with_state_html

    @rt(
        "/web-api/users/{user_id}/lists/{list_id}/actions/overview",
        methods=["GET"]
    )
    def get_student_actions(
        session,
        user_id: int,
        list_id: int,
    ):
        token = session["access_token"]

        student_actions_data = client_actions.get_actions(
            token=token,
            user_id=user_id,
            list_id=list_id
        )
        student_actions_html = student_actions_overview(
            user_id=user_id,
            list_id=list_id,
            actions_data=student_actions_data,
        )

        return student_actions_html
