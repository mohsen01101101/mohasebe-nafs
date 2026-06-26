from sqlmodel import Field, SQLModel
from app.domain.enum.role import Role


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    role: Role = Field(default=Role.STUDENT)
