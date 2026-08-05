from fasthtml.common import *
from app.web.layouts.base import app_layout


def home(req: Request):
    page_content = (
        H1(
            "لیست شاگردان",
            cls="text-center text-2xl font-bold mb-4"
        )
    )

    return app_layout(
        req=req,
        page_content=page_content,
        title="صفحه اصلی"
    )
