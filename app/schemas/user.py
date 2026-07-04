from pydantic import BaseModel
from app.domain.enum.role import Role


class UserRegister(BaseModel):
    phone_number: str
    name: str
    password: str
    role: Role = Role.STUDENT


class UserLogin(BaseModel):
    phone_number: str
    password: str


class UserRead(BaseModel):
    phone_number: str
    id: int
    name: str


class UserUpdate(BaseModel):
    name: str | None = None
    password: str | None = None


class UserDelete(BaseModel):
    password: str
