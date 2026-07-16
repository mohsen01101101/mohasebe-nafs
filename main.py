from fasthtml.common import fast_app, serve, Redirect
from app.api.main import api_app
from app.core.config import settings
from app.web.middleware.auth import before
from app.web.pages.home import home
from app.web.pages.login import login
from app.web.client.auth import login as client_login


app, rt = fast_app(
    pico=False,
    static_path="static",
    secret_key=settings.secret_key,
    before=before
)


app.mount(
    path=settings.api_prefix,
    app=api_app
)


@rt("/login")
def get():  # pyright: ignore[reportRedeclaration]
    return login()


@rt("/login")
def post(
    phone_number: str,
    password: str,
    session
):
    data = client_login(
        phone_number=phone_number,
        password=password
    )

    session["access_token"] = data["access_token"]

    return Redirect("/")


@rt("/")
def get():
    return home()


serve()
