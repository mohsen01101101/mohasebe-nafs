from fasthtml.common import *
from app.web.layouts.base import app_layout
from app.web.client.users import get_users
from app.web.components.students_overview import students_overview
from app.web.components.logout_button import logout_button


def home(req: Request):
    token = req.session["access_token"]

    students_data = get_users(token)

    students_overview_html = students_overview(students_data)

    page_content = (
        H1(
            "لیست شاگردان",
            cls="text-center text-2xl font-bold mb-4"
        ),

        students_overview_html,

        logout_button()
    )

    return app_layout(
        req=req,
        page_content=page_content,
        title="صفحه اصلی"
    )
