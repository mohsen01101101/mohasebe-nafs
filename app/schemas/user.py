from pydantic import BaseModel, ConfigDict, Field


class UserRegister(BaseModel):
    phone_number: str
    name: str
    password: str = Field(min_length=8)


class UserLogin(BaseModel):
    phone_number: str
    password: str = Field(min_length=8)


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


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
