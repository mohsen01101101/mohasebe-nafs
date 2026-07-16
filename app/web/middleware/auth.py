from fasthtml.common import Redirect, Beforeware
from starlette.requests import Request


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
        return

    return Redirect("/login")


before = Beforeware(auth_before)
