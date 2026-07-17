from fastapi import APIRouter, Depends, HTTPException
from app.schemas.list import ListRead, ListCreate, ListUpdate
from app.db.models.user import UserModel
from app.api.permissions import require_teacher
from app.api.dependencies import get_list_service, get_current_user
from app.services.list import ListService


router = APIRouter(prefix="/users", tags=["Lists"])


@router.get("/me/lists", response_model=list[ListRead])
def get_my_lists(
    current_user: UserModel = Depends(get_current_user),
    service: ListService = Depends(get_list_service)
):
    assert current_user.id is not None
    lists = service.get_all(current_user.id)

    return lists


@router.post("/me/lists", response_model=ListRead)
def create_list(
    data: ListCreate,
    current_user: UserModel = Depends(get_current_user),
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


@router.patch("/me/{list_id}", response_model=ListRead)
def update_list(
    list_id: int,
    data: ListUpdate,
    current_user: UserModel = Depends(get_current_user),
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


@router.delete("/me/{list_id}", status_code=204)
def delete_list(
    list_id: int,
    current_user: UserModel = Depends(get_current_user),
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
    _: UserModel = Depends(require_teacher),
    service: ListService = Depends(get_list_service)
):
    lists = service.get_all(user_id)

    return lists
