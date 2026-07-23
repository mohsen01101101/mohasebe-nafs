from fasthtml.common import *
from app.core.utils.digits_converter import to_persian_digits


def actions(actions_data: list[dict[str, str | int]]):
    actions_html = Section(
        Ul(
            *[
                Li(
                    Div(
                        to_persian_digits(f"{index:02}"),
                        cls="text-4xl font-thin opacity-30 tabular-nums"
                    ),

                    Div(
                        Div(
                            item["title"]
                        ),

                        P(
                            item["description"],
                            cls="text-xs opacity-60"
                        ),

                        cls="list-col-grow"
                    ),

                    cls="list-row"
                )

                for index, item in enumerate(actions_data, start=1)
            ],

            cls="list bg-base-100 rounded-box shadow-md flex flex-col gap-2"
        )
    )

    return actions_html
