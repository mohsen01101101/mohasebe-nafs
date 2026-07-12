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
        name: str,
        current_password: str,
        new_password: str
):
    response = client.patch(
        url=f"{BASE_URL}/me",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "name": name,
            "current_password": current_password,
            "new_password": new_password
        }
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
