from fasthtml.common import fast_app, serve
from app.api.main import api_app
from app.core.config import settings
from app.web.pages.home import home


app, rt = fast_app(
    pico=False,
    static_path="static"
)


app.mount(
    path=settings.api_prefix,
    app=api_app
)


@rt("/")
def get():
    return home()


serve()
