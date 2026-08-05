from fasthtml.common import fast_app, serve, Request
from app.api.main import api_app
from app.core.config import settings
from app.web.middleware.auth import before
from app.web.handlers.auth import register_auth_routes
from app.web.handlers.lists import register_list_routes
from app.web.handlers.actions import register_action_routes
from app.web.pages.login import login
from app.web.pages.home import home
from app.web.pages.student.lists import lists
from app.web.pages.student.list_actions import list_actions


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


register_auth_routes(rt)
register_list_routes(rt)
register_action_routes(rt)


@rt("/login")
def get(req: Request):  # pyright: ignore[reportRedeclaration]
    return login(req)


@rt("/")
def get(req: Request):  # pyright: ignore[reportRedeclaration]
    return home(
        req=req,
        current_user=req.state.user
    )


@rt("/lists")
def get(req: Request):  # pyright: ignore[reportRedeclaration]
    return lists(
        req=req,
        current_user=req.state.user
    )


@rt("/lists/{list_id}")
def get(
    req: Request,
    list_id: int,
):
    return list_actions(
        req=req,
        list_id=list_id,
        current_user=req.state.user
    )


serve()
