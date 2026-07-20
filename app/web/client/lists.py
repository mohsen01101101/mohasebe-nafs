from app.core.config import settings
from app.web.client.http import client
from datetime import datetime


BASE_URL = f"{settings.api_base_url}/users"


def get_my_lists(token: str):
    response = client.get(
        url=f"{BASE_URL}/me/lists",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    response.raise_for_status()

    return response.json()


def create_list(
    token: str,
    title: str,
    created_at: datetime | None = None
):
    data = {
        "title": title
    }

    if created_at is not None:
        data["created_at"] = created_at.isoformat()

    response = client.post(
        url=f"{BASE_URL}/me/lists",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json=data
    )

    response.raise_for_status()

    return response.json()


def update_list(
        token: str,
        list_id: int,
        title: str
):
    response = client.patch(
        url=f"{BASE_URL}/me/lists/{list_id}",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "title": title
        }
    )

    response.raise_for_status()

    return response.json()


def delete_list(token: str, list_id: int):
    response = client.delete(
        url=f"{BASE_URL}/me/lists/{list_id}",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    response.raise_for_status()


def get_lists(token: str, user_id: int):
    response = client.get(
        url=f"{BASE_URL}/{user_id}/lists",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    response.raise_for_status()

    return response.json()
