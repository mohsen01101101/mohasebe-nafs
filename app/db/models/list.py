from sqlmodel import Field, SQLModel, UniqueConstraint
from datetime import datetime
from zoneinfo import ZoneInfo


IRAN_TZ = ZoneInfo("Asia/Tehran")


class List(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    title: str = Field(nullable=False)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(IRAN_TZ))

    __table_args__ = (
        UniqueConstraint("user_id", "title"),
    )
