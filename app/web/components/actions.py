from fasthtml.common import *
from app.core.utils.digits_converter import to_persian_digits
from app.schemas.action import ActionWithStateRead
from app.domain.enum.tracking_type import TrackingType


def actions(
    list_id: int,
    actions_data: list[ActionWithStateRead]
):
    actions_with_state_html = Section(
        Ul(
            *[
                action_item(
                    list_id=list_id,
                    item=item,
                    index=index
                )
                for index, item in enumerate(actions_data, start=1)
            ],

            cls="list bg-base-100 rounded-box shadow-md"
        )
    )

    return actions_with_state_html


def action_item(
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
                hx_vals=f'js:{{is_done: event.target.checked, index: {index}, day: document.querySelector("#new-date").value}}',                cls="checkbox"
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
                    hx_vals=f'js:{{rating: event.target.value, index: {index}, day: document.querySelector("#new-date").value}}'
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
                    hx_vals=f'js:{{rating: event.target.value, index: {index}, day: document.querySelector("#new-date").value}}'
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
                    hx_vals=f'js:{{rating: event.target.value, index: {index}, day: document.querySelector("#new-date").value}}'
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
                    hx_vals=f'js:{{rating: event.target.value, index: {index}, day: document.querySelector("#new-date").value}}'
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
                    hx_vals=f'js:{{rating: event.target.value, index: {index}, day: document.querySelector("#new-date").value}}'
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
                    hx_vals=f'js:{{rating: event.target.value, index: {index}, day: document.querySelector("#new-date").value}}'
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
                    hx_vals=f'js:{{rating: event.target.value, index: {index}, day: document.querySelector("#new-date").value}}'
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
                    hx_vals=f'js:{{rating: event.target.value, index: {index}, day: document.querySelector("#new-date").value}}'
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
                    hx_vals=f'js:{{rating: event.target.value, index: {index}, day: document.querySelector("#new-date").value}}'
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
                    hx_vals=f'js:{{rating: event.target.value, index: {index}, day: document.querySelector("#new-date").value}}'
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
                    hx_vals=f'js:{{rating: event.target.value, index: {index}, day: document.querySelector("#new-date").value}}'
                ),

                cls="rating rating-md rating-half"
            )
        ),

        id=f"action-{item.id}",
        cls="list-row items-center"
    )

    return action_with_state_html
