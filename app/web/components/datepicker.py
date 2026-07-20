from fasthtml.common import *
from app.core.shamsi_date import jalali_today


def datepicker(
    locale: str = "fa",
    show_holidays: bool = True,
    placeholder: str = jalali_today()
):
    datepicker_element = ft(
        "doran-datepicker",
        locale=locale,
        show_holidays=show_holidays,
        placeholder=placeholder
    )

    return datepicker_element
