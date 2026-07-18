from fasthtml.common import *
from app.web.components.header import header
from app.web.components.footer import footer


def base_layout(page_content, title="Mohasebe Nafs", show_header_footer=True):
    return Html(
        Head(
            Meta(charset="UTF-8"),
            Meta(
                name="viewport",
                content="width=device-width, initial-scale=1.0"
            ),
            Link(
                rel="stylesheet",
                href="/tailwind-css/output.css"
            ),
            Title(title)
        ),

        Body(
            *(
                [Header(header())] if show_header_footer else []
            ),

            Main(
                page_content,
                cls="flex-1 min-h-0"
            ),

            Footer(
                footer(),
                cls="mb-4"
            ),

            cls="h-dvh flex flex-col items-center"
        ),

        lang="fa",
        dir="rtl",
        data_theme="emerald"
    )


def auth_layout(page_content, title="Login"):
    return base_layout(
        page_content=page_content,
        title=title,
        show_header_footer=False
    )


def app_layout(page_content, title="Mohasebe Nafs"):
    return base_layout(
        page_content=page_content,
        title=title,
        show_header_footer=True
    )
