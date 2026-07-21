from sqlmodel import Session, select
from app.db.models.list import ListModel
from datetime import datetime, date
from app.core.constants import IRAN_TZ


class ListService:
    def __init__(self, session: Session):
        self.session = session

    def get_all(
        self,
        user_id: int,
        selected_date: date | None = None
    ):
        if selected_date is None:
            selected_date = datetime.now(IRAN_TZ).date()

        statement = select(ListModel).where(
            ListModel.user_id == user_id,
            ListModel.created_date <= selected_date
        )
        result = self.session.exec(statement)

        return result.all()

    def create(
        self,
        user_id: int,
        title: str,
        created_at: datetime | None
    ):
        duplicate = self._get_by_user_id_and_title(user_id, title)

        if duplicate:
            raise ValueError("The list already exists.")

        data = {
            "user_id": user_id,
            "title": title
        }

        if created_at is not None:
            data["created_at"] = created_at

        new_list = ListModel(**data)

        self.session.add(new_list)
        self.session.commit()
        self.session.refresh(new_list)

        return new_list

    def update(
        self,
        user_id: int,
        list_id: int,
        new_title: str
    ):
        existing = self.session.get(ListModel, list_id)

        if not existing or existing.user_id != user_id:
            raise ValueError("List not found.")

        duplicate = self._get_by_user_id_and_title(user_id, new_title)

        if duplicate and duplicate.id != list_id:
            raise ValueError("The list already exists.")

        existing.title = new_title

        self.session.commit()
        self.session.refresh(existing)

        return existing

    def delete(
        self,
        user_id: int,
        list_id: int,
    ):
        existing = self.session.get(ListModel, list_id)

        if not existing or existing.user_id != user_id:
            raise ValueError("List not found.")

        self.session.delete(existing)
        self.session.commit()

        return None

    def _get_by_user_id_and_title(
        self,
        user_id: int,
        title: str
    ):
        statement = select(ListModel).where(
            ListModel.user_id == user_id,
            ListModel.title == title
        )
        result = self.session.exec(statement)

        return result.first()
