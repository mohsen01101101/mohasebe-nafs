from app.core.config import settings
from app.web.client.http import client
from app.domain.enum.tracking_type import TrackingType
from datetime import datetime


BASE_URL = f"{settings.api_base_url}/users"


def get_actions(
    token: str,
    user_id: int,
    list_id: int
):
    response = client.get(
        url=f"{BASE_URL}/{user_id}/lists/{list_id}/actions",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    response.raise_for_status()

    return response.json()


def get_my_actions(token: str, list_id: int):
    response = client.get(
        url=f"{BASE_URL}/me/lists/{list_id}/actions",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    response.raise_for_status()

    return response.json()


def create_action(
    token: str,
    list_id: int,
    title: str,
    tracking_type: TrackingType,
    description: str | None = None,
    is_done: bool | None = None,
    rating: int | None = None,
    started_at: datetime | None = None
):
    data = {
        "title": title,
        "tracking_type": tracking_type.value
    }

    if description is not None:
        data["description"] = description

    if is_done is not None:
        data["is_done"] = is_done  # pyright: ignore[reportArgumentType]

    if rating is not None:
        if not 0 <= rating <= 5:
            raise ValueError("Rating must be between 0 and 5.")

        data["rating"] = rating  # pyright: ignore[reportArgumentType]

    if started_at is not None:
        data["started_at"] = started_at.isoformat()

    response = client.post(
        url=f"{BASE_URL}/me/lists/{list_id}/actions",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json=data
    )

    response.raise_for_status()

    return response.json()


def update_action(
        token: str,
        list_id: int,
        action_id: int,
        title: str | None = None,
        description: str | None = None,
        is_done: bool | None = None,
        rating: int | None = None,
):
    data = {}

    if title is not None:
        data["title"] = title

    if description is not None:
        data["description"] = description

    if is_done is not None:
        data["is_done"] = is_done

    if rating is not None:
        if not 0 <= rating <= 5:
            raise ValueError("Rating must be between 0 and 5.")

        data["rating"] = rating

    if not data:
        raise ValueError("No fields to update.")

    response = client.patch(
        url=f"{BASE_URL}/me/lists/{list_id}/actions/{action_id}",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json=data
    )

    response.raise_for_status()

    return response.json()


def delete_action(
        token: str,
        list_id: int,
        action_id: int,
):
    response = client.delete(
        url=f"{BASE_URL}/me/lists/{list_id}/actions/{action_id}",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    response.raise_for_status()
