from fastapi import APIRouter, Query, Depends, HTTPException
from datetime import datetime, date
from app.core.constants import IRAN_TZ
from app.schemas.action import ActionRead, ActionCreate, ActionUpdate, ActionStateRead, ActionStateUpdate
from app.api.permissions import require_teacher
from app.api.dependencies import get_action_service, get_action_state_service, get_current_user
from app.db.models.user import UserModel
from app.services.action import ActionService, ActionStateService


router = APIRouter(prefix="/users", tags=["Actions"])


@router.get("/me/lists/{list_id}/actions", response_model=list[ActionRead])
def get_my_actions(
    list_id: int,
    current_user: UserModel = Depends(get_current_user),
    selected_date: date = Query(
        default_factory=lambda: datetime.now(IRAN_TZ).date()
    ),
    service: ActionService = Depends(get_action_service)
):
    assert current_user.id is not None
    actions = service.get_all(
        user_id=current_user.id,
        list_id=list_id,
        selected_date=selected_date
    )

    return actions


@router.get("/me/lists/{list_id}/actions/{action_id}/state", response_model=ActionStateRead)
def get_my_action_state_by_day(
    list_id: int,
    action_id: int,
    day: date | None = None,
    current_user: UserModel = Depends(get_current_user),
    service: ActionStateService = Depends(get_action_state_service)
):
    assert current_user.id is not None
    action_state = service.get_by_day(
        user_id=current_user.id,
        list_id=list_id,
        action_id=action_id,
        day=day
    )

    return action_state


@router.post("/me/lists/{list_id}/actions", response_model=ActionRead)
def create_action(
    data: ActionCreate,
    list_id: int,
    current_user: UserModel = Depends(get_current_user),
    service: ActionService = Depends(get_action_service)
):
    assert current_user.id is not None

    try:
        action = service.create(
            user_id=current_user.id,
            list_id=list_id,
            title=data.title,
            description=data.description,
            tracking_type=data.tracking_type,
            started_at=data.started_at
        )

        return action

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.patch("/me/lists/{list_id}/actions/{action_id}", response_model=ActionRead)
def update_action(
    data: ActionUpdate,
    list_id: int,
    action_id: int,
    current_user: UserModel = Depends(get_current_user),
    service: ActionService = Depends(get_action_service)
):
    assert current_user.id is not None

    try:
        action = service.update(
            user_id=current_user.id,
            list_id=list_id,
            action_id=action_id,
            new_title=data.title,
            new_description=data.description
        )

        return action

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.patch("/me/lists/{list_id}/actions/{action_id}/state", response_model=ActionStateRead)
def update_action_state_by_day(
    data: ActionStateUpdate,
    list_id: int,
    action_id: int,
    current_user: UserModel = Depends(get_current_user),
    service: ActionStateService = Depends(get_action_state_service)
):
    assert current_user.id is not None

    try:
        action_state = service.update(
            user_id=current_user.id,
            list_id=list_id,
            action_id=action_id,
            is_done=data.is_done,
            rating=data.rating,
            day=data.day
        )

        return action_state

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/me/lists/{list_id}/actions/{action_id}", status_code=204)
def delete_action(
    list_id: int,
    action_id: int,
    current_user: UserModel = Depends(get_current_user),
    service: ActionService = Depends(get_action_service)
):
    assert current_user.id is not None

    try:
        service.delete(
            user_id=current_user.id,
            list_id=list_id,
            action_id=action_id
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.get("/{user_id}/lists/{list_id}/actions", response_model=list[ActionRead])
def get_actions(
    user_id: int,
    list_id: int,
    _: UserModel = Depends(require_teacher),
    service: ActionService = Depends(get_action_service)
):
    actions = service.get_all(
        user_id=user_id,
        list_id=list_id
    )

    return actions


@router.get("/{user_id}/lists/{list_id}/actions/{action_id}/state", response_model=ActionStateRead)
def get_action_state_by_day(
    user_id: int,
    list_id: int,
    action_id: int,
    day: date | None = None,
    _: UserModel = Depends(require_teacher),
    service: ActionStateService = Depends(get_action_state_service)
):
    action_state = service.get_by_day(
        user_id=user_id,
        list_id=list_id,
        action_id=action_id,
        day=day
    )

    return action_state
