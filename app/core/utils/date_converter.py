import jdatetime
from datetime import datetime
from app.core.constants import IRAN_TZ, MONTHS, WEEKDAYS
from app.core.utils.digits_converter import to_persian_digits, to_english_digits


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


def jalali_to_gregorian(jalali_date: str):
    jalali_date = to_english_digits(jalali_date)

    year, month, day = map(
        int,
        jalali_date.split("/")
    )

    result = jdatetime.date(
        year,
        month,
        day
    ).togregorian()

    return result


def _jalali_today():
    now = datetime.now(IRAN_TZ).date()

    today = jdatetime.date.fromgregorian(
        year=now.year,
        month=now.month,
        day=now.day
    )

    return today
