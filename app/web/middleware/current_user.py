from fasthtml.common import Redirect, Request
from app.web.client.users import get_me
from httpx2 import HTTPStatusError


def load_current_user(req: Request, session):
    token = session.get("access_token")

    if not token:
        return Redirect("/login")

    try:
        user = get_me(token)

    except HTTPStatusError as e:
        if e.response.status_code == 401:
            session.clear()
            return Redirect("/login")

        raise

    req.state.token = token
    req.state.user = user
