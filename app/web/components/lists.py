from fasthtml.common import *


def lists(lists_data: list[dict[str, str | int]]):
    lists_html = Section(
        *[
            Fieldset(
                Legend(
                    item["title"],
                    cls="fieldset-legend"
                ),
                cls="fieldset bg-base-200 border-base-300 rounded-box border p-4 pr-6"
            )
            for item in lists_data
        ],

        id="lists-container"
    )

    return lists_html
