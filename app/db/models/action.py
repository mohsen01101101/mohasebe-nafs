from sqlmodel import Field, SQLModel, UniqueConstraint
from app.domain.enum.tracking_type import TrackingType
from datetime import datetime, date
from app.core.constants import IRAN_TZ


class ActionModel(SQLModel, table=True):
    __tablename__ = "action"  # pyright: ignore[reportAssignmentType]

    id: int | None = Field(default=None, primary_key=True)
    list_id: int = Field(foreign_key="list.id", ondelete="CASCADE")
    title: str = Field(nullable=False)
    description: str | None = Field(default=None)
    tracking_type: TrackingType = Field(nullable=False)
    started_date: datetime = Field(
        default_factory=lambda: datetime.now(IRAN_TZ).date())

    __table_args__ = (
        UniqueConstraint(
            "list_id",
            "title",
            name="unique_action_title_per_list"
        ),
    )


class ActionStateModel(SQLModel, table=True):
    __tablename__ = "action_state"  # pyright: ignore[reportAssignmentType]

    id: int | None = Field(default=None, primary_key=True)
    action_id: int = Field(foreign_key="action.id", ondelete="CASCADE")
    is_done: bool | None = Field(default=None)
    rating: int | None = Field(default=None)
    day: date = Field(
        default_factory=lambda: datetime.now(IRAN_TZ).date()
    )

    __table_args__ = (
        UniqueConstraint(
            "action_id",
            "day",
            name="unique_action_state_per_day"
        ),
    )
