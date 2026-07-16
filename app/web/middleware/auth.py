from fasthtml.common import Redirect, Beforeware
from starlette.requests import Request


PUBLIC_PATHS = [
    "/login",
    "/fonts",
    "/tailwind-css",
]


def auth_before(req: Request, session):
    path = req.url.path

    if any(path.startswith(public_path) for public_path in PUBLIC_PATHS):
        return

    if session.get("access_token"):
        return

    return Redirect("/login")


before = Beforeware(auth_before)
