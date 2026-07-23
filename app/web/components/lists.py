from fasthtml.common import *


def lists(lists_data: list[dict[str, str | int]]):
    lists_html = Section(
        *[
            Fieldset(
                Legend(
                    item["title"],
                    cls="fieldset-legend pr-6"
                ),

                Div(
                    data_actions_url=f"/web-api/lists/{item['id']}/actions"
                ),

                cls="fieldset bg-base-200 border-base-300 rounded-box border p-4"
            )
            for item in lists_data
        ],

        id="lists-container"
    )

    return lists_html
