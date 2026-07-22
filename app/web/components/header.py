from fasthtml.common import *
from app.core.utils.shamsi_date import jalali_today_text
from app.core.utils.digits_converter import to_persian_digits


def header(req: Request):
    user = req.state.user

    name = to_persian_digits(user["name"])
    phone_number = to_persian_digits(user["phone_number"])

    return (
        Div(
            Div(
                P(
                    Span(
                        name,
                        cls="font-bold"
                    ),
                    " عزیز، خوش آمدی"
                ),

                Span(
                    phone_number,
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
