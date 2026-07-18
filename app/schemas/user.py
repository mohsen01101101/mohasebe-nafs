from pydantic import BaseModel, ConfigDict, Field


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    phone_number: str
    id: int
    name: str


class UserUpdate(BaseModel):
    name: str | None = None
    current_password: str
    new_password: str | None = Field(default=None, min_length=8)


class UserDelete(BaseModel):
    password: str = Field(min_length=8)
