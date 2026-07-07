from pydantic import BaseModel, ConfigDict


class UserRegister(BaseModel):
    phone_number: str
    name: str
    password: str


class UserLogin(BaseModel):
    phone_number: str
    password: str


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    phone_number: str
    id: int
    name: str


class UserUpdate(BaseModel):
    name: str | None = None
    password: str | None = None


class UserDelete(BaseModel):
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
