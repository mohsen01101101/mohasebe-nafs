from fasthtml.common import *


def back_button(href: str):
    back_btn = A(
        "برگشت",
        role="button",
        href=href,
        cls="btn btn-link btn-error no-underline absolute bottom-1 left-0"
    )

    return back_btn
