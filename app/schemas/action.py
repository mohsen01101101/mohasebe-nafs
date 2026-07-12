from pydantic import BaseModel, Field, ConfigDict
from app.domain.enum.tracking_type import TrackingType
from datetime import datetime


class ActionCreate(BaseModel):
    title: str
    description: str | None = None
    tracking_type: TrackingType
    is_done: bool | None = None
    rating: int | None = Field(default=None, ge=0, le=5)
    started_at: datetime | None = None


class ActionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    list_id: int
    title: str
    description: str | None
    tracking_type: TrackingType
    is_done: bool | None
    rating: int | None


class ActionUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    is_done: bool | None = None
    rating: int | None = Field(default=None, ge=0, le=5)
