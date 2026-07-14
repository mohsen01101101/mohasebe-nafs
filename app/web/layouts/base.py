from fasthtml.common import *
from app.web.components.header import header
from app.web.components.footer import footer


def base_layout(page_content, title="Mohasebe Nafs"):
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
            Header(
                header()
            ),
            Main(
                page_content
            ),
            Footer(
                footer()
            )
        ),

        lang="fa"
    )
