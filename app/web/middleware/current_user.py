from app.web.client.users import get_me
from starlette.requests import Request


def load_current_user(req: Request, session):
    token = session.get("access_token")

    if not token:
        return

    user = get_me(token)

    req.state.token = token
    req.state.user = user
