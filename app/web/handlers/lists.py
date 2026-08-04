from fasthtml.common import *
from datetime import datetime
from app.core.constants import IRAN_TZ
from app.web.client import lists as client_list
from app.web.components.lists import lists_with_actions, lists_overview, list_edit_row, list_row


def register_list_routes(rt):
    @rt(
        "/web-api/lists/with-actions",
        methods=["GET"]
    )
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

        lists_data = client_list.get_my_lists(
            token=token,
            selected_date=selected_date
        )
        lists_with_actions_html = lists_with_actions(lists_data)

        return lists_with_actions_html

    @rt(
        "/web-api/lists/overview",
        methods=["GET"]
    )
    def get_lists_overview(
        session
    ):
        token = session["access_token"]

        lists_data = client_list.get_my_lists(
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

        client_list.create_list(
            token=token,
            title=title,
            created_at=created_at
        )

        response = Response(
            headers={
                "HX-Trigger": "lists:changed"
            }
        )

        return response

    @rt(
        "/web-api/lists/{list_id}/edit",
        methods=["GET"]
    )
    def get_list_edit_row(
        session,
        list_id: int
    ):
        token = session["access_token"]

        list_item = client_list.get_my_list(
            token=token,
            list_id=list_id
        )

        list_edit_row_html = list_edit_row(list_item)

        return list_edit_row_html

    @rt(
        "/web-api/lists/{list_id}/row",
        methods=["GET"]
    )
    def get_list_row(
        session,
        list_id: int
    ):
        token = session["access_token"]

        list_item = client_list.get_my_list(
            token=token,
            list_id=list_id
        )

        list_row_html = list_row(list_item)

        return list_row_html

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

        client_list.update_list(
            token=token,
            list_id=list_id,
            title=title
        )

        response = Response(
            headers={
                "HX-Trigger": "lists:changed"
            }
        )

        return response

    @rt(
        "/web-api/lists/{list_id}",
        methods=["DELETE"]
    )
    def delete_list(
        session,
        list_id: int
    ):
        token = session["access_token"]

        client_list.delete_list(
            token=token,
            list_id=list_id
        )

        response = Response(
            headers={
                "HX-Trigger": "lists:changed"
            }
        )

        return response
