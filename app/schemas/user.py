from pydantic import BaseModel, ConfigDict, Field
from app.domain.enum.role import Role


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    phone_number: str
    id: int
    name: str
    role: Role


class UserUpdate(BaseModel):
    name: str | None = None
    current_password: str
    new_password: str | None = Field(default=None, min_length=8)


class UserDelete(BaseModel):
    password: str = Field(min_length=8)
