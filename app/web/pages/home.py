from fasthtml.common import *
from app.web.layouts.base import app_layout


def home():
    page_content = P("محتوای صفحه")

    return app_layout(
        page_content=page_content,
        title="صفحه اصلی"
    )
