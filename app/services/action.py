from sqlmodel import Session, select
from app.db.models.action import ActionModel, ActionStateModel
from app.db.models.list import ListModel
from app.schemas.action import ActionStateRead
from app.domain.enum.tracking_type import TrackingType
from datetime import datetime, date
from app.core.constants import IRAN_TZ


class ActionService:
    def __init__(self, session: Session):
        self.session = session

    def get_all(
        self,
        user_id: int,
        list_id: int
    ):
        user_list = self._get_user_list_by_id(
            user_id=user_id,
            list_id=list_id
        )

        if not user_list:
            raise ValueError("List not found.")

        statement = select(ActionModel).where(
            ActionModel.list_id == list_id
        )
        result = self.session.exec(statement)

        return result.all()

    def create(
        self,
        user_id: int,
        list_id: int,
        title: str,
        description: str | None,
        tracking_type: TrackingType,
        started_at: datetime | None
    ):
        user_list = self._get_user_list_by_id(
            user_id=user_id,
            list_id=list_id
        )

        if not user_list:
            raise ValueError("List not found.")

        duplicate = self._get_by_list_id_and_title(list_id, title)

        if duplicate:
            raise ValueError("The action already exists.")

        data = {
            "list_id": list_id,
            "title": title,
            "tracking_type": tracking_type
        }

        if description is not None:
            data["description"] = description

        if started_at is not None:
            data["started_at"] = started_at

        action = ActionModel(**data)

        self.session.add(action)
        self.session.commit()
        self.session.refresh(action)

        return action

    def update(
        self,
        user_id: int,
        list_id: int,
        action_id: int,
        new_title: str | None,
        new_description: str | None,
    ):
        user_list = self._get_user_list_by_id(
            user_id=user_id,
            list_id=list_id
        )

        if not user_list:
            raise ValueError("List not found.")

        existing = self.session.get(ActionModel, action_id)

        if not existing or existing.list_id != list_id:
            raise ValueError("Action not found.")

        if new_title is not None:
            duplicate = self._get_by_list_id_and_title(list_id, new_title)

            if duplicate and duplicate.id != action_id:
                raise ValueError("The action already exists.")

            existing.title = new_title

        if new_description is not None:
            existing.description = new_description

        self.session.commit()
        self.session.refresh(existing)

        return existing

    def delete(
        self,
        user_id: int,
        list_id: int,
        action_id: int
    ):
        user_list = self._get_user_list_by_id(
            user_id=user_id,
            list_id=list_id
        )

        if not user_list:
            raise ValueError("List not found.")

        existing = self.session.get(ActionModel, action_id)

        if not existing or existing.list_id != list_id:
            raise ValueError("Action not found.")

        self.session.delete(existing)
        self.session.commit()

        return None

    def _get_user_list_by_id(
        self,
        user_id: int,
        list_id: int
    ):
        statement = select(ListModel).where(
            ListModel.id == list_id,
            ListModel.user_id == user_id
        )
        result = self.session.exec(statement)

        return result.first()

    def _get_by_list_id_and_title(
        self,
        list_id: int,
        title: str
    ):
        statement = select(ActionModel).where(
            ActionModel.list_id == list_id,
            ActionModel.title == title
        )
        result = self.session.exec(statement)

        return result.first()


class ActionStateService:
    def __init__(self, session: Session):
        self.session = session

    def get_by_day(
        self,
        user_id: int,
        list_id: int,
        action_id: int,
        day: date | None = None
    ):
        action = self._get_user_action(
            user_id=user_id,
            list_id=list_id,
            action_id=action_id
        )

        if not action:
            raise ValueError("Action not found.")

        if day is None:
            day = datetime.now(IRAN_TZ).date()

        state = self._get_by_action_and_day(
            action_id=action_id,
            day=day
        )

        if state is not None:
            return state

        return ActionStateRead(
            id=None,
            action_id=action_id,
            is_done=False,
            rating=None,
            day=day
        )

    def update(
        self,
        user_id: int,
        list_id: int,
        action_id: int,
        is_done: bool | None = None,
        rating: int | None = None,
        day: date | None = None
    ):
        if is_done is None and rating is None:
            raise ValueError("No state change provided.")

        action = self._get_user_action(
            user_id=user_id,
            list_id=list_id,
            action_id=action_id
        )

        if not action:
            raise ValueError("Action not found.")

        if action.tracking_type == TrackingType.CHECKBOX:
            if rating is not None:
                raise ValueError("Checkbox actions do not support rating.")

        elif action.tracking_type == TrackingType.RATING:
            if is_done is not None:
                raise ValueError(
                    "Rating actions do not support checkbox state."
                )

            if rating is not None and not 0 <= rating <= 5:
                raise ValueError(
                    "Rating must be between 0 and 5."
                )

        if day is None:
            day = datetime.now(IRAN_TZ).date()

        state = self._get_by_action_and_day(
            action_id=action_id,
            day=day
        )

        if state is None:
            state = self._create(
                action_id=action_id,
                day=day
            )

        if is_done is not None:
            state.is_done = is_done

        if rating is not None:
            state.rating = rating

        self.session.commit()
        self.session.refresh(state)

        return state

    def _get_user_action(
            self,
            user_id: int,
            list_id: int,
            action_id: int
    ):
        statement = select(ActionModel).join(ListModel).where(
            ListModel.user_id == user_id,
            ListModel.id == list_id,
            ActionModel.id == action_id
        )

        action = self.session.exec(statement)

        return action.first()

    def _get_by_action_and_day(
            self,
            action_id: int,
            day: date
    ):
        statement = select(ActionStateModel).where(
            ActionStateModel.action_id == action_id,
            ActionStateModel.day == day
        )
        state = self.session.exec(statement)

        return state.first()

    def _create(
        self,
        action_id: int,
        day: date
    ):
        state = ActionStateModel(
            action_id=action_id,
            day=day
        )

        self.session.add(state)

        return state
