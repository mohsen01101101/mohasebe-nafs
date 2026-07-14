from fasthtml.common import fast_app, serve
from app.web.pages.home import home


app, rt = fast_app(
    pico=False,
    static_path="static"
)


@rt("/")
def get():
    return home()


serve()
