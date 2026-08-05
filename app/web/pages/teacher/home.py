from fasthtml.common import *
from app.web.layouts.base import app_layout
from app.web.client.users import get_users
from app.web.components.students_list import students_list


def home(req: Request):
    token = req.session["access_token"]

    students_data = get_users(token)

    students_list_html = students_list(students_data)

    page_content = (
        H1(
            "لیست شاگردان",
            cls="text-center text-2xl font-bold mb-4"
        ),

        students_list_html
    )

    return app_layout(
        req=req,
        page_content=page_content,
        title="صفحه اصلی"
    )
