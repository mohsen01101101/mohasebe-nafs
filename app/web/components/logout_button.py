from fasthtml.common import *


def logout_button():
    logout_btn = A(
        "خروج",
        hx_post="/web-api/logout",
        hx_swap="none",
        role="button",
        cls="btn btn-link btn-error no-underline absolute bottom-1 left-0"
    )

    return logout_btn
