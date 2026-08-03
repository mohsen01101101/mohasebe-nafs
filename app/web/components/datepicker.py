from fasthtml.common import *
from app.core.utils.date_converter import jalali_today_numeric


def datepicker(
    name: str = "selected_date_iso",
    locale: str = "fa",
    show_holidays: bool = True,
    placeholder: str = jalali_today_numeric()
):
    datepicker_element = Div(
        ft(
            "doran-datepicker",
            locale=locale,
            show_holidays=show_holidays,
            placeholder=placeholder,
            input_width="100%",
            dropdown_width="trigger",
            style=""
            "--doran-focus-ring: var(--color-primary-content);"
            "--doran-primary: var(--color-primary);"
            ""
        ),

        Input(
            type="hidden",
            name=name,
            id=f"{name}-input"
        )
    )

    return datepicker_element
