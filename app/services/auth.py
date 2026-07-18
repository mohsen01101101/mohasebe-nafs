from sqlmodel import Session, select
from app.domain.enum.role import Role
from app.db.models.user import UserModel
from app.core.security import hash_password, verify_password
from app.domain.enum.role import Role


class AuthService:
    def __init__(self, session: Session):
        self.session = session

    def register(
        self,
        phone_number: str,
        name: str,
        password: str,
        role: Role = Role.STUDENT
    ):
        if self._get_by_phone_number(phone_number):
            raise ValueError("Phone number already exists.")

        hashed_password = hash_password(password)

        user = UserModel(
            phone_number=phone_number,
            name=name,
            password_hash=hashed_password,
            role=role
        )

        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

        return user

    def login(
        self,
        phone_number: str,
        password: str
    ):
        user = self._get_by_phone_number(phone_number)

        if not user:
            raise ValueError("Invalid credentials.")

        if not verify_password(password, user.password_hash):
            raise ValueError("Invalid credentials.")

        return user

    def _get_by_phone_number(self, phone_number: str):
        statement = select(UserModel).where(
            UserModel.phone_number == phone_number)
        result = self.session.exec(statement)

        return result.first()
