from fasthtml.common import *


def lists(lists_data: list[dict[str, str | int]]):
    lists_html = Section(
        *[
            Fieldset(
                Legend(
                    item["title"],
                    cls="fieldset-legend mr-6 p-0"
                ),

                Div(
                    hx_get=f"/web-api/lists/{item['id']}/actions",
                    hx_trigger="load",
                    hx_vals="js:{selected_date_iso: getSelectedDate()}",
                    hx_swap="innerHTML"
                ),

                cls="fieldset bg-base-200 border-base-300 rounded-box border mt-2 p-4"
            )
            for item in lists_data
        ],

        id="lists-container",
        hx_get="/web-api/lists",
        hx_trigger="app:dateChanged from:body",
        hx_vals="js:{selected_date_iso: getSelectedDate()}",
        hx_swap="outerHTML"
    )

    return lists_html
