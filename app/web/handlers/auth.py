from fasthtml.common import *
from httpx2 import HTTPStatusError
from app.web.client.auth import login as client_login
from app.web.pages.login import login as login_page


def register_auth_routes(rt):
    @rt(
        "/web-api/login",
        methods=["POST"]
    )
    def login_submit(
        session,
        phone_number: str,
        password: str
    ):
        try:
            data = client_login(
                phone_number=phone_number,
                password=password
            )

        except HTTPStatusError:
            return Redirect("/login?error=1")

        session["access_token"] = data["access_token"]

        return Redirect("/")

    @rt(
        "/web-api/logout",
        methods=["POST"]
    )
    def logout(
        session
    ):
        session.pop("access_token", None)

        response = Response(
            headers={
                "HX-Redirect": "/login"
            }
        )

        return response
