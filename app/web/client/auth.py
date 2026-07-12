from app.core.config import settings
from app.web.client.http import client


BASE_URL = f"{settings.api_base_url}/auth"


def register(
    phone_number: str,
    name: str,
    password: str
):
    response = client.post(
        url=f"{BASE_URL}/register",
        json={
            "phone_number": phone_number,
            "name": name,
            "password": password
        }
    )

    response.raise_for_status()

    return response.json()


def login(
    phone_number: str,
    password: str
):
    response = client.post(
        url=f"{BASE_URL}/login",
        json={
            "phone_number": phone_number,
            "password": password
        }
    )

    response.raise_for_status()

    return response.json()
