from fasthtml.common import *
from datetime import datetime, date
from app.core.constants import IRAN_TZ
from app.web.client.lists import get_my_lists
from app.web.components.lists import lists_with_actions, lists_overview
from app.web.client.lists import create_list as client_create_list
from app.web.client.lists import update_list as client_update_list
from app.web.client.lists import delete_list as client_delete_list


def register_list_routes(rt):
    @rt("/web-api/lists/with-actions")
    def get_lists_with_actions(
        session,
        selected_date_iso: str | None = None
    ):
        token = session["access_token"]

        selected_date = None

        if selected_date_iso:
            selected_date = datetime.fromisoformat(
                selected_date_iso.replace("Z", "+00:00")
            ).astimezone(IRAN_TZ).date()

        lists_data = get_my_lists(
            token=token,
            selected_date=selected_date
        )
        lists_with_actions_html = lists_with_actions(lists_data)

        return lists_with_actions_html

    @rt("/web-api/lists/overview")
    def get_lists_overview(
        session
    ):
        token = session["access_token"]

        lists_data = get_my_lists(
            token=token
        )
        lists_overview_html = lists_overview(lists_data)

        return lists_overview_html

    @rt(
        "/web-api/lists",
        methods=["POST"]
    )
    def create_list(
        session,
        title: str,
        selected_date_iso: str | None = None
    ):
        token = session["access_token"]

        created_at = None

        if selected_date_iso:
            created_at = datetime.fromisoformat(
                selected_date_iso.replace("Z", "+00:00")
            ).astimezone(IRAN_TZ)

        client_create_list(
            token=token,
            title=title,
            created_at=created_at
        )

        return Response(
            headers={
                "HX-Trigger": "lists:changed"
            }
        )

    @rt(
        "/web-api/lists/{list_id}",
        methods=["PATCH"]
    )
    def update_list(
        session,
        list_id: int,
        title: str
    ):
        token = session["access_token"]

        client_update_list(
            token=token,
            list_id=list_id,
            title=title
        )

        return Response(
            headers={
                "HX-Trigger": "lists:changed"
            }
        )

    @rt(
        "/web-api/lists/{list_id}",
        methods=["DELETE"]
    )
    def delete_list(
        session,
        list_id: int
    ):
        token = session["access_token"]

        client_delete_list(
            token=token,
            list_id=list_id
        )

        response = Response(
            headers={
                "HX-Trigger": "lists:changed"
            }
        )

        return response
