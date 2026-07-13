from sqlmodel import Field, SQLModel
from app.domain.enum.role import Role


class UserModel(SQLModel, table=True):
    __tablename__ = "user"  # pyright: ignore[reportAssignmentType]

    id: int | None = Field(default=None, primary_key=True)
    phone_number: str = Field(nullable=False, unique=True)
    name: str = Field(nullable=False)
    password_hash: str = Field(nullable=False)
    role: Role = Field(default=Role.STUDENT)
