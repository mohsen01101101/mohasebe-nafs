from fasthtml.common import *
from app.schemas.user import UserRead
from app.core.utils.digits_converter import to_persian_digits


def students_overview(students_data: list[UserRead]):
    students_overview_html = Section(
        Div(
            Table(
                Tbody(
                    *[
                        Tr(
                            Td(
                                to_persian_digits(f"{index:02}"),
                                cls="font-thin opacity-80 tabular-nums"
                            ),

                            Td(
                                student.name,
                                cls="w-full"
                            ),

                            Td(
                                A(
                                    "مشاهده",
                                    role="button",
                                    href=f"/reports/{student.id}",
                                    cls="btn btn-sm btn-wide btn-soft btn-info"
                                )
                            )
                        )
                        for index, student in enumerate(students_data, start=1)
                    ]
                ),

                cls="table"
            ),

            cls="overflow-x-auto"
        ),
    )

    return students_overview_html
