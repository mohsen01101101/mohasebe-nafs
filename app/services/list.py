from sqlmodel import Session, select
from app.db.models.list import List
from datetime import datetime


class ListService:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self, user_id: int):
        statement = select(List).where(List.user_id == user_id)
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

        new_list = List(**data)

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
        existing = self.session.get(List, list_id)

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
        existing = self.session.get(List, list_id)

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
        statement = select(List).where(
            List.user_id == user_id,
            List.title == title
        )
        result = self.session.exec(statement)

        return result.first()
