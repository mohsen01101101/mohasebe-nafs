from fasthtml.common import *
from app.core.utils.shamsi_date import jalali_today_numeric


def datepicker(
    locale: str = "fa",
    show_holidays: bool = True,
    placeholder: str = jalali_today_numeric()
):
    datepicker_element = ft(
        "doran-datepicker",
        locale=locale,
        show_holidays=show_holidays,
        placeholder=placeholder
    )

    return datepicker_element
