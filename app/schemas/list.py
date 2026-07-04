from pydantic import BaseModel, ConfigDict
from datetime import datetime


class ListCreate(BaseModel):
    title: str
    created_at: datetime | None = None


class ListRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    title: str


class ListUpdate(BaseModel):
    title: str
