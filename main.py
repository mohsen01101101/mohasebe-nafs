from fasthtml.common import fast_app, serve, Request
from app.api.main import api_app
from app.core.config import settings
from app.web.middleware.auth import before
from app.web.handlers.auth import register_auth_routes
from app.web.handlers.lists import register_list_routes
from app.web.handlers.actions import register_action_routes
from app.web.pages.login import login
from app.web.pages.home import home
from app.web.pages.student.lists import lists as student_list
from app.web.pages.teacher.lists import lists as teacher_list
from app.web.pages.student.list_actions import list_actions
from app.web.pages.teacher.reports import reports


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
    return student_list(
        req=req,
        current_user=req.state.user
    )


@rt("/lists/{list_id}")
def get(  # pyright: ignore[reportRedeclaration]
    req: Request,
    list_id: int,
):
    return list_actions(
        req=req,
        list_id=list_id,
        current_user=req.state.user
    )


@rt("/reports/{user_id}")
def get(  # pyright: ignore[reportRedeclaration]
    req: Request,
    user_id: int,
):
    return reports(
        req=req,
        current_user=req.state.user,
        user_id=user_id
    )


@rt("/reports/{user_id}/lists")
def get(
    req: Request,
    user_id: int,
):
    return teacher_list(
        req=req,
        current_user=req.state.user,
        user_id=user_id
    )


serve()
