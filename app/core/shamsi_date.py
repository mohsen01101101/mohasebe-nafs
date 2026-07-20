import jdatetime
from datetime import datetime
from app.core.constants import IRAN_TZ, MONTHS, WEEKDAYS


def jalali_today_text():
    today = _jalali_today()

    return (
        f"{WEEKDAYS[today.weekday()]} "
        f"{today.day} "
        f"{MONTHS[today.month]} "
        f"{today.year}"
    )


def jalali_today_numeric():
    today = _jalali_today()

    return f"{today.year:04d}/{today.month:02d}/{today.day:02d}"


def _jalali_today():
    now = datetime.now(IRAN_TZ)

    today = jdatetime.date.fromgregorian(
        year=now.year,
        month=now.month,
        day=now.day
    )

    return today
