from sqlmodel import Session, select
from app.domain.enum.role import Role
from app.db.models.user import User
from app.core.security import hash_password, verify_password
from app.domain.enum.role import Role


class UserService:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self, role: Role = Role.STUDENT):
        statement = select(User).where(User.role == role)
        result = self.session.exec(statement)

        return result.all()

    def get_by_id(self, user_id: int):
        user = self.session.get(User, user_id)

        if not user:
            raise ValueError("User not found.")

        return user

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

        user = User(
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

    def update(
        self,
        user_id: int,
        name: str | None,
        current_password: str,
        new_password: str | None,
    ):
        user = self.session.get(User, user_id)

        if not user:
            raise ValueError("User not found.")

        if not verify_password(current_password, user.password_hash):
            raise ValueError("Invalid password.")

        if name is not None:
            user.name = name

        if new_password is not None:
            hashed_password = hash_password(new_password)
            user.password_hash = hashed_password

        self.session.commit()
        self.session.refresh(user)

        return user

    def delete(
        self,
        user_id: int,
        password: str
    ):
        user = self.session.get(User, user_id)

        if not user:
            raise ValueError("User not found.")

        if not verify_password(password, user.password_hash):
            raise ValueError("Incorrect password.")

        self.session.delete(user)
        self.session.commit()

        return None

    def _get_by_phone_number(self, phone_number: str):
        statement = select(User).where(User.phone_number == phone_number)
        result = self.session.exec(statement)

        return result.first()
