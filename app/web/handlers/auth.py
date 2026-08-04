from fasthtml.common import *
from app.web.client.auth import login


def register_auth_routes(rt):
    @rt(
        "/web-api/login",
        methods=["POST"]
    )
    def login_submit(
        phone_number: str,
        password: str,
        session
    ):
        data = login(
            phone_number=phone_number,
            password=password
        )

        session["access_token"] = data["access_token"]

        return Redirect("/")
