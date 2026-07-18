from fasthtml.common import *
from app.web.layouts.base import app_layout


def home(req: Request):
    page_content = P("محتوای صفحه")

    return app_layout(
        req=req,
        page_content=page_content,
        title="صفحه اصلی"
    )
