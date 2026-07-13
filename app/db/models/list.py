from sqlmodel import Field, SQLModel, UniqueConstraint
from datetime import datetime
from app.core.constants import IRAN_TZ


class ListModel(SQLModel, table=True):
    __tablename__ = "list"  # pyright: ignore[reportAssignmentType]

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", ondelete="CASCADE")
    title: str = Field(nullable=False)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(IRAN_TZ))

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "title",
            name="unique_list_title_per_user"
        ),
    )
