from sqlmodel import Field, SQLModel, UniqueConstraint, CheckConstraint
from app.domain.enum.tracking_type import TrackingType
from datetime import datetime
from zoneinfo import ZoneInfo


IRAN_TZ = ZoneInfo("Asia/Tehran")


class Action(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    list_id: int = Field(foreign_key="list.id")
    title: str = Field(nullable=False)
    description: str | None = Field(default=None)
    tracking_type: TrackingType = Field(nullable=False)
    is_done: bool = Field(default=False)
    rating: int = Field(default=0)
    started_at: datetime = Field(
        default_factory=lambda: datetime.now(IRAN_TZ))

    __table_args__ = (
        UniqueConstraint("list_id", "title"),
        CheckConstraint(
            "(tracking_type != 'RATING') OR (rating BETWEEN 0 and 5)",
            name="validate_rating_range"
        ),
    )
