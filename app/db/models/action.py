from sqlmodel import Field, SQLModel, UniqueConstraint, CheckConstraint
from app.domain.enum.tracking_type import TrackingType
from datetime import datetime
from app.core.constants import IRAN_TZ


class Action(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    list_id: int = Field(foreign_key="list.id", ondelete="CASCADE")
    title: str = Field(nullable=False)
    description: str | None = Field(default=None)
    tracking_type: TrackingType = Field(nullable=False)
    is_done: bool | None = Field(default=None)
    rating: int | None = Field(default=None)
    started_at: datetime = Field(
        default_factory=lambda: datetime.now(IRAN_TZ))

    __table_args__ = (
        UniqueConstraint("list_id", "title"),
        CheckConstraint(
            """
            (
                tracking_type = 'CHECKBOX'
                AND rating IS NULL
                AND is_done IS NOT NULL
            )
            OR
            (
                tracking_type = 'RATING'
                AND is_done IS NULL
                AND rating BETWEEN 0 AND 5
            )
            """,
            name="validate_tracking_fields"
        ),
    )
