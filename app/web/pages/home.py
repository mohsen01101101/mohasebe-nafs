from fasthtml.common import *
from app.web.layouts.base import base_layout


def home():
    page_content = P("محتوای صفحه"),

    return base_layout(
        page_content=page_content,
        title="صفحه اصلی"
    )
