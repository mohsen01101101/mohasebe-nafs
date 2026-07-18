import jdatetime
from datetime import datetime
from app.core.constants import IRAN_TZ, MONTHS, WEEKDAYS


def jalali_today():
    now = datetime.now(IRAN_TZ)

    today = jdatetime.date.fromgregorian(
        year=now.year,
        month=now.month,
        day=now.day
    )

    return (
        f"{WEEKDAYS[today.weekday()]} "
        f"{today.day} "
        f"{MONTHS[today.month]} "
        f"{today.year}"
    )
