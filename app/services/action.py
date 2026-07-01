from sqlmodel import Session, select
from app.db.models.action import Action
from app.domain.enum.tracking_type import TrackingType
from datetime import datetime


class ActionService:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self, list_id: int):
        statement = select(Action).where(Action.list_id == list_id)
        result = self.session.exec(statement)

        return result.all()

    def create(
        self,
        list_id: int,
        title: str,
        description: str | None,
        tracking_type: TrackingType,
        is_done: bool | None,
        rating: int | None,
        started_at: datetime | None
    ):
        duplicate = self._get_by_list_id_and_title(list_id, title)

        if duplicate:
            raise ValueError("The action already exists.")

        data = {
            "list_id": list_id,
            "title": title,
            "tracking_type": tracking_type
        }

        if tracking_type == TrackingType.CHECKBOX:
            if is_done is None:
                raise ValueError("Checkbox is required.")
            data["is_done"] = is_done
        elif tracking_type == TrackingType.RATING:
            if rating is None:
                raise ValueError("Rating is required.")
            data["rating"] = rating

        if description is not None:
            data["description"] = description

        if started_at is not None:
            data["started_at"] = started_at

        new_action = Action(**data)

        self.session.add(new_action)
        self.session.commit()
        self.session.refresh(new_action)

        return new_action

    def update(
        self,
        list_id: int,
        action_id: int,
        new_title: str,
        new_description: str | None,
        is_done: bool | None,
        rating: int | None
    ):
        existing = self.session.get(Action, action_id)

        if not existing or existing.list_id != list_id:
            raise ValueError("Action not found.")

        duplicate = self._get_by_list_id_and_title(list_id, new_title)

        if duplicate and duplicate.id != action_id:
            raise ValueError("The action already exists.")

        existing.title = new_title
        existing.description = new_description

        if existing.tracking_type == TrackingType.CHECKBOX:
            if is_done is None:
                raise ValueError("Checkbox is required.")

            existing.is_done = is_done
        elif existing.tracking_type == TrackingType.RATING:
            if rating is None:
                raise ValueError("Rating is required.")
            elif not 0 <= rating <= 5:
                raise ValueError("Rating must be between 0 and 5.")

            existing.rating = rating

        self.session.commit()
        self.session.refresh(existing)

        return existing

    def delete(
        self,
        list_id: int,
        action_id: int
    ):
        existing = self.session.get(Action, action_id)

        if not existing or existing.list_id != list_id:
            raise ValueError("Action not found.")

        self.session.delete(existing)
        self.session.commit()

        return None

    def _get_by_list_id_and_title(
        self,
        list_id: int,
        title: str
    ):
        statement = select(Action).where(
            Action.list_id == list_id,
            Action.title == title
        )
        result = self.session.exec(statement)

        return result.first()
