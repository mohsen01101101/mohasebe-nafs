from pydantic import BaseModel
from datetime import datetime


class ListCreate(BaseModel):
    title: str
    created_at: datetime | None = None


class ListRead(BaseModel):
    id: int
    user_id: int
    title: str


class ListUpdate(BaseModel):
    title: str
