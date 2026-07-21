import jdatetime
from datetime import datetime
from app.core.constants import IRAN_TZ, MONTHS, WEEKDAYS
from app.core.utils.persian_digits import to_persian_digits


def jalali_today_text():
    today = _jalali_today()

    date = (
        f"{WEEKDAYS[today.weekday()]} "
        f"{today.day} "
        f"{MONTHS[today.month]} "
        f"{today.year}"
    )
    date = to_persian_digits(date)

    return date


def jalali_today_numeric():
    today = _jalali_today()

    date = f"{today.year:04d}/{today.month:02d}/{today.day:02d}"
    date = to_persian_digits(date)

    return date


def _jalali_today():
    now = datetime.now(IRAN_TZ).date()

    today = jdatetime.date.fromgregorian(
        year=now.year,
        month=now.month,
        day=now.day
    )

    return today
