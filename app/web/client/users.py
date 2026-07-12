from app.core.config import settings
from app.web.client.http import client


BASE_URL = f"{settings.api_base_url}/users"


def get_users(token: str):
    response = client.get(
        url=BASE_URL,
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    response.raise_for_status()

    return response.json()


def get_user_by_id(token: str, user_id: int):
    response = client.get(
        url=f"{BASE_URL}/{user_id}",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    response.raise_for_status()

    return response.json()


def get_me(token: str):
    response = client.get(
        url=f"{BASE_URL}/me",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    response.raise_for_status()

    return response.json()


def update_me(
        token: str,
        current_password: str,
        name: str | None = None,
        new_password: str | None = None
):
    data = {
        "current_password": current_password
    }

    if name is not None:
        data["name"] = name

    if new_password is not None:
        data["new_password"] = new_password

    response = client.patch(
        url=f"{BASE_URL}/me",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json=data
    )

    response.raise_for_status()

    return response.json()


def delete_me(token: str, password: str):
    response = client.request(
        method="DELETE",
        url=f"{BASE_URL}/me",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "password": password
        }
    )

    response.raise_for_status()
