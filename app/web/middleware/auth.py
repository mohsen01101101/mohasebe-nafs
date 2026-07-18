from fasthtml.common import Redirect, Beforeware, Request
from app.web.middleware.current_user import load_current_user


PUBLIC_PATHS = [
    "/fonts",
    "/tailwind-css"
]


def auth_before(req: Request, session):
    path = req.url.path
    is_authenticated = bool(session.get("access_token"))

    if path.startswith("/login"):
        if is_authenticated:
            return Redirect("/")

        return

    if any(path.startswith(public_path) for public_path in PUBLIC_PATHS):
        return

    if is_authenticated:
        response = load_current_user(
            req=req,
            session=session
        )

        if response:
            return response

        return

    return Redirect("/login")


before = Beforeware(auth_before)
