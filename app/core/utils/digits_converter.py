TO_PERSIAN_DIGITS = str.maketrans(
    "0123456789",
    "۰۱۲۳۴۵۶۷۸۹"
)


def to_persian_digits(value: object):
    result = str(value).translate(TO_PERSIAN_DIGITS)

    return result
