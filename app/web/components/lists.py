from fasthtml.common import *


def lists_overview(lists_data: list[dict[str, str | int]]):
    lists_overview_html = Section(
        Div(
            Table(
                Tbody(
                    *[
                        Tr(
                            Td(
                                item["title"],
                                cls="w-full"
                            ),

                            Td(
                                Div(
                                    Button(
                                        "ویرایش",
                                        cls="btn btn-sm btn-soft"
                                    ),

                                    Button(
                                        "حذف",
                                        hx_delete=f"/web-api/lists/{item['id']}",
                                        hx_swap="none",
                                        hx_confirm=f"آیا از حذف لیست «{item['title']}» مطمئن هستید؟",
                                        cls="btn btn-sm btn-soft btn-error"
                                    ),

                                    cls="flex gap-2"
                                )
                            )
                        )
                        for item in lists_data
                    ]
                ),

                cls="table"
            ),

            cls="overflow-x-auto"
        ),

        id="lists_overview-container",
        hx_get="/web-api/lists/overview",
        hx_trigger="lists:changed from:body",
        hx_swap="outerHTML"
    )

    return lists_overview_html


def lists_with_actions(lists_data: list[dict[str, str | int]]):
    lists_with_actions_html = Section(
        *[
            Fieldset(
                Legend(
                    item["title"],
                    cls="fieldset-legend mr-6 p-0"
                ),

                Div(
                    hx_get=f"/web-api/lists/{item['id']}/actions",
                    hx_trigger="load",
                    hx_include="[name='selected_date_iso']",
                    hx_swap="innerHTML"
                ),

                cls="fieldset bg-base-200 border-base-300 rounded-box border mt-2 p-4"
            )
            for item in lists_data
        ],

        id="lists_with_actions-container",
        hx_get="/web-api/lists/with-actions",
        hx_trigger="app:dateChanged from:body",
        hx_include="[name='selected_date_iso']",
        hx_swap="outerHTML"
    )

    return lists_with_actions_html
