from fastapi import APIRouter, Query, Depends, HTTPException
from datetime import datetime, date
from app.core.constants import IRAN_TZ
from app.schemas.list import ListRead, ListCreate, ListUpdate
from app.schemas.user import UserRead
from app.api.permissions import require_teacher
from app.api.dependencies import get_list_service, get_current_user
from app.services.list import ListService


router = APIRouter(prefix="/users", tags=["Lists"])


@router.get("/me/lists", response_model=list[ListRead])
def get_my_lists(
    current_user: UserRead = Depends(get_current_user),
    selected_date: date = Query(
        default_factory=lambda: datetime.now(IRAN_TZ).date()
    ),
    service: ListService = Depends(get_list_service)
):
    assert current_user.id is not None
    lists = service.get_all(
        user_id=current_user.id,
        selected_date=selected_date
    )

    return lists


@router.post("/me/lists", response_model=ListRead)
def create_list(
    data: ListCreate,
    current_user: UserRead = Depends(get_current_user),
    service: ListService = Depends(get_list_service)
):
    assert current_user.id is not None

    try:
        new_list = service.create(
            user_id=current_user.id,
            title=data.title,
            created_at=data.created_at
        )

        return new_list

    except ValueError as e:
        raise HTTPException(
            status_code=409,
            detail=str(e)
        )


@router.get("/me/lists/{list_id}", response_model=ListRead)
def get_my_list(
    list_id: int,
    current_user: UserRead = Depends(get_current_user),
    service: ListService = Depends(get_list_service)
):
    assert current_user.id is not None

    list_item = service.get_by_user_id_and_list_id(
        user_id=current_user.id,
        list_id=list_id
    )

    if list_item is None:
        raise HTTPException(
            status_code=404,
            detail="List not found."
        )

    return list_item


@router.patch("/me/lists/{list_id}", response_model=ListRead)
def update_list(
    list_id: int,
    data: ListUpdate,
    current_user: UserRead = Depends(get_current_user),
    service: ListService = Depends(get_list_service)
):
    assert current_user.id is not None

    try:
        updated_list = service.update(
            user_id=current_user.id,
            list_id=list_id,
            new_title=data.title
        )

        return updated_list

    except ValueError as e:
        raise HTTPException(
            status_code=409,
            detail=str(e)
        )


@router.delete("/me/lists/{list_id}", status_code=204)
def delete_list(
    list_id: int,
    current_user: UserRead = Depends(get_current_user),
    service: ListService = Depends(get_list_service)
):
    assert current_user.id is not None

    try:
        service.delete(
            user_id=current_user.id,
            list_id=list_id
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.get("/{user_id}/lists", response_model=list[ListRead])
def get_lists(
    user_id: int,
    _: UserRead = Depends(require_teacher),
    selected_date: date = Query(
        default_factory=lambda: datetime.now(IRAN_TZ).date()
    ),
    service: ListService = Depends(get_list_service)
):
    lists = service.get_all(
        user_id=user_id,
        selected_date=selected_date
    )

    return lists
