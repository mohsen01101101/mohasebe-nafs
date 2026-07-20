from fasthtml.common import *
from app.web.components.header import header
from app.web.components.footer import footer


def base_layout(req: Request, page_content, title="Mohasebe Nafs", show_header_footer=True):
    return Html(
        Head(
            Meta(charset="UTF-8"),
            Meta(
                name="viewport",
                content="width=device-width, initial-scale=1.0"
            ),

            Link(
                rel="stylesheet",
                href="/build/css/bundle.css"
            ),
            Script(
                src="/build/js/bundle.js",
                type="module"
            ),

            Title(title)
        ),

        Body(
            *(
                [
                    Header(
                        header(req)
                    )
                ]
                if show_header_footer
                else []
            ),

            Main(
                page_content,
                cls="flex-1 min-h-0"
            ),

            Footer(
                footer()
            ),

            cls="flex flex-col max-w-2xl h-dvh mx-auto p-4"
        ),

        lang="fa",
        dir="rtl",
        data_theme="emerald"
    )


def auth_layout(req: Request, page_content, title="Login"):
    return base_layout(
        req=req,
        page_content=page_content,
        title=title,
        show_header_footer=False
    )


def app_layout(req: Request, page_content, title="Mohasebe Nafs"):
    return base_layout(
        req=req,
        page_content=page_content,
        title=title,
        show_header_footer=True
    )
