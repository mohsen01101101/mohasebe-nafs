from pydantic import BaseModel, Field, ConfigDict
from app.domain.enum.tracking_type import TrackingType
from datetime import datetime, date


class ActionCreate(BaseModel):
    title: str
    description: str | None = None
    tracking_type: TrackingType
    started_at: datetime | None = None


class ActionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    list_id: int
    title: str
    description: str | None = None
    tracking_type: TrackingType


class ActionStateRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    action_id: int
    is_done: bool | None = None
    rating: int | None = None
    day: date


class ActionUpdate(BaseModel):
    title: str | None = None
    description: str | None = None


class ActionStateUpdate(BaseModel):
    is_done: bool | None = None
    rating: int | None = Field(default=None, ge=0, le=5)
    day: date | None = None
