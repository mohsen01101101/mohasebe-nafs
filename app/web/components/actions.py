from fasthtml.common import *
from app.core.utils.digits_converter import to_persian_digits
from app.schemas.action import ActionRead, ActionWithStateRead
from app.domain.enum.tracking_type import TrackingType


def actions_overview(
    list_id: int,
    actions_data: list[ActionRead]
):
    actions_overview_html = Section(
        Div(
            Table(
                Tbody(
                    *[
                        action_row(
                            list_id=list_id,
                            action_item=item
                        )
                        for item in actions_data
                    ]
                ),

                cls="table"
            ),

            cls="overflow-x-auto"
        ),

        id="actions_overview-container",
        hx_get=f"/web-api/lists/{list_id}/actions/overview",
        hx_trigger="actions:changed from:body",
        hx_swap="outerHTML"
    )

    return actions_overview_html


def actions_with_state(
    list_id: int,
    actions_data: list[ActionWithStateRead]
):
    actions_with_state_html = Section(
        Ul(
            *[
                action_item_with_state(
                    list_id=list_id,
                    item=item,
                    index=index
                )
                for index, item in enumerate(actions_data, start=1)
            ],

            cls="list bg-base-100 rounded-2xl shadow-md"
        )
    )

    return actions_with_state_html


def action_row(
        list_id: int,
        action_item: ActionRead
):
    action_row_html = Tr(
        Td(
            Div(
                action_item.title,
                cls="font-bold"
            ),

            Div(
                action_item.description,
                cls="text-sm opacity-50"
            )
            if action_item.description
            else None,

            cls="w-full"
        ),

        Td(
            Div(
                Button(
                    "ویرایش",
                    hx_get=f"/web-api/lists/{list_id}/actions/{action_item.id}/edit",
                    hx_target=f"#action-{action_item.id}",
                    hx_swap="outerHTML",
                    cls="btn btn-sm"
                ),

                Button(
                    "حذف",
                    hx_delete=f"/web-api/lists/{list_id}/actions/{action_item.id}",
                    hx_swap="none",
                    hx_confirm=f"آیا از حذف عمل «{action_item.title}» مطمئن هستید؟",
                    cls="btn btn-sm btn-soft btn-error"
                ),

                cls="flex gap-2 justify-end"
            )
        ),

        id=f"action-{action_item.id}"
    )

    return action_row_html


def action_item_with_state(
    list_id: int,
    item: ActionWithStateRead,
    index: int
):
    action_with_state_html = Li(
        Div(
            to_persian_digits(f"{index:02}"),
            cls="text-4xl font-thin opacity-30 tabular-nums"
        ),

        Div(
            Div(
                item.title
            ),

            P(
                item.description,
                cls="text-xs opacity-60"
            ),

            cls="list-col-grow"
        ),

        (
            Input(
                type="checkbox",
                name="is_done",
                checked=item.is_done,
                hx_patch=f"/web-api/lists/{list_id}/actions/{item.id}/state",
                hx_trigger="change",
                hx_target=f"#action-{item.id}",
                hx_swap="outerHTML",
                hx_include="[name='selected_date_iso']",
                hx_vals=f'js:{{is_done: event.target.checked, index: {index}}}',
                cls="checkbox"
            )
            if item.tracking_type == TrackingType.CHECKBOX
            else Div(
                Input(
                    type="radio",
                    name=f"rating-{item.id}",
                    value="0",
                    checked=item.rating == 0,
                    cls="rating-hidden",
                    hx_patch=f"/web-api/lists/{list_id}/actions/{item.id}/state",
                    hx_trigger="change",
                    hx_target=f"#action-{item.id}",
                    hx_swap="outerHTML",
                    hx_include="[name='selected_date_iso']",
                    hx_vals=f'js:{{rating: event.target.value, index: {index}}}'
                ),

                Input(
                    type="radio",
                    name=f"rating-{item.id}",
                    value="0.5",
                    checked=item.rating == 0.5,
                    cls="mask mask-star-2 mask-half-1",
                    aria_label="0.5 star",
                    hx_patch=f"/web-api/lists/{list_id}/actions/{item.id}/state",
                    hx_trigger="change",
                    hx_target=f"#action-{item.id}",
                    hx_swap="outerHTML",
                    hx_include="[name='selected_date_iso']",
                    hx_vals=f'js:{{rating: event.target.value, index: {index}}}'
                ),

                Input(
                    type="radio",
                    name=f"rating-{item.id}",
                    value="1",
                    checked=item.rating == 1,
                    cls="mask mask-star-2 mask-half-2",
                    aria_label="1 star",
                    hx_patch=f"/web-api/lists/{list_id}/actions/{item.id}/state",
                    hx_trigger="change",
                    hx_target=f"#action-{item.id}",
                    hx_swap="outerHTML",
                    hx_include="[name='selected_date_iso']",
                    hx_vals=f'js:{{rating: event.target.value, index: {index}}}'
                ),

                Input(
                    type="radio",
                    name=f"rating-{item.id}",
                    value="1.5",
                    checked=item.rating == 1.5,
                    cls="mask mask-star-2 mask-half-1",
                    aria_label="1.5 star",
                    hx_patch=f"/web-api/lists/{list_id}/actions/{item.id}/state",
                    hx_trigger="change",
                    hx_target=f"#action-{item.id}",
                    hx_swap="outerHTML",
                    hx_include="[name='selected_date_iso']",
                    hx_vals=f'js:{{rating: event.target.value, index: {index}}}'
                ),

                Input(
                    type="radio",
                    name=f"rating-{item.id}",
                    value="2",
                    checked=item.rating == 2,
                    cls="mask mask-star-2 mask-half-2",
                    aria_label="2 star",
                    hx_patch=f"/web-api/lists/{list_id}/actions/{item.id}/state",
                    hx_trigger="change",
                    hx_target=f"#action-{item.id}",
                    hx_swap="outerHTML",
                    hx_include="[name='selected_date_iso']",
                    hx_vals=f'js:{{rating: event.target.value, index: {index}}}'
                ),

                Input(
                    type="radio",
                    name=f"rating-{item.id}",
                    value="2.5",
                    checked=item.rating == 2.5,
                    cls="mask mask-star-2 mask-half-1",
                    aria_label="2.5 star",
                    hx_patch=f"/web-api/lists/{list_id}/actions/{item.id}/state",
                    hx_trigger="change",
                    hx_target=f"#action-{item.id}",
                    hx_swap="outerHTML",
                    hx_include="[name='selected_date_iso']",
                    hx_vals=f'js:{{rating: event.target.value, index: {index}}}'
                ),

                Input(
                    type="radio",
                    name=f"rating-{item.id}",
                    value="3",
                    checked=item.rating == 3,
                    cls="mask mask-star-2 mask-half-2",
                    aria_label="3 star",
                    hx_patch=f"/web-api/lists/{list_id}/actions/{item.id}/state",
                    hx_trigger="change",
                    hx_target=f"#action-{item.id}",
                    hx_swap="outerHTML",
                    hx_include="[name='selected_date_iso']",
                    hx_vals=f'js:{{rating: event.target.value, index: {index}}}'
                ),

                Input(
                    type="radio",
                    name=f"rating-{item.id}",
                    value="3.5",
                    checked=item.rating == 3.5,
                    cls="mask mask-star-2 mask-half-1",
                    aria_label="3.5 star",
                    hx_patch=f"/web-api/lists/{list_id}/actions/{item.id}/state",
                    hx_trigger="change",
                    hx_target=f"#action-{item.id}",
                    hx_swap="outerHTML",
                    hx_include="[name='selected_date_iso']",
                    hx_vals=f'js:{{rating: event.target.value, index: {index}}}'
                ),

                Input(
                    type="radio",
                    name=f"rating-{item.id}",
                    value="4",
                    checked=item.rating == 4,
                    cls="mask mask-star-2 mask-half-2",
                    aria_label="4 star",
                    hx_patch=f"/web-api/lists/{list_id}/actions/{item.id}/state",
                    hx_trigger="change",
                    hx_target=f"#action-{item.id}",
                    hx_swap="outerHTML",
                    hx_include="[name='selected_date_iso']",
                    hx_vals=f'js:{{rating: event.target.value, index: {index}}}'
                ),

                Input(
                    type="radio",
                    name=f"rating-{item.id}",
                    value="4.5",
                    checked=item.rating == 4.5,
                    cls="mask mask-star-2 mask-half-1",
                    aria_label="4.5 star",
                    hx_patch=f"/web-api/lists/{list_id}/actions/{item.id}/state",
                    hx_trigger="change",
                    hx_target=f"#action-{item.id}",
                    hx_swap="outerHTML",
                    hx_include="[name='selected_date_iso']",
                    hx_vals=f'js:{{rating: event.target.value, index: {index}}}'
                ),

                Input(
                    type="radio",
                    name=f"rating-{item.id}",
                    value="5",
                    checked=item.rating == 5,
                    cls="mask mask-star-2 mask-half-2",
                    aria_label="5 star",
                    hx_patch=f"/web-api/lists/{list_id}/actions/{item.id}/state",
                    hx_trigger="change",
                    hx_target=f"#action-{item.id}",
                    hx_swap="outerHTML",
                    hx_include="[name='selected_date_iso']",
                    hx_vals=f'js:{{rating: event.target.value, index: {index}}}'
                ),

                cls="rating rating-md rating-half"
            )
        ),

        id=f"action-{item.id}",
        cls="list-row items-center"
    )

    return action_with_state_html
