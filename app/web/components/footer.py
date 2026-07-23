from fasthtml.common import *


def footer():
    return (
        Div(
            H2(
                "محاسبه نفس",
                cls="mb-0.5 text-3xl font-bold"
            ),

            Span(
                "طراحی و توسعه با ❤️",
                cls="text-sm"
            ),

            cls="flex flex-col items-center mt-4"
        )
    )
