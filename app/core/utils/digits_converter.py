TO_PERSIAN_DIGITS = str.maketrans(
    "0123456789",
    "۰۱۲۳۴۵۶۷۸۹"
)

TO_ENGLISH_DIGITS = str.maketrans(
    "۰۱۲۳۴۵۶۷۸۹",
    "0123456789"
)


def to_persian_digits(value: object):
    result = str(value).translate(TO_PERSIAN_DIGITS)

    return result


def to_english_digits(value: object):
    result = str(value).translate(TO_ENGLISH_DIGITS)

    return result
