from fasthtml.common import *
from app.core.shamsi_date import jalali_today_text


def header(req: Request):
    return (
        Div(
            Div(
                P(
                    Span(
                        req.state.user["name"],
                        cls="font-bold"
                    ),
                    " عزیز، خوش آمدی"
                ),

                Span(
                    req.state.user["phone_number"],
                    cls="text-sm opacity-50"
                ),
            ),

            Div(
                jalali_today_text(),
                cls="text-sm"
            ),

            cls="flex justify-between w-full"
        ),

        Div(
            cls="divider -mt-1"
        )
    )
