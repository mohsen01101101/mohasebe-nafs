from sqlmodel import Session, select
from app.domain.enum.role import Role
from app.db.models.user import UserModel
from app.core.security import hash_password, verify_password
from app.domain.enum.role import Role


class UserService:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self, role: Role = Role.STUDENT):
        statement = select(UserModel).where(UserModel.role == role)
        result = self.session.exec(statement)

        return result.all()

    def get_by_id(self, user_id: int):
        user = self.session.get(UserModel, user_id)

        if not user:
            raise ValueError("User not found.")

        return user

    def update(
        self,
        user_id: int,
        name: str | None,
        current_password: str,
        new_password: str | None,
    ):
        user = self.session.get(UserModel, user_id)

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
        user = self.session.get(UserModel, user_id)

        if not user:
            raise ValueError("User not found.")

        if not verify_password(password, user.password_hash):
            raise ValueError("Incorrect password.")

        self.session.delete(user)
        self.session.commit()

        return None

    # Used only by the internal register_student.py script to create student accounts.
    def register_student(
        self,
        name: str,
        phone_number: str,
        password: str,
    ):
        statement = select(UserModel).where(
            UserModel.phone_number == phone_number)

        existing_user = self.session.exec(statement).first()

        if existing_user:
            raise ValueError("Phone number already exists.")

        user = UserModel(
            name=name,
            phone_number=phone_number,
            password_hash=hash_password(password),
            role=Role.STUDENT,
        )

        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

        return user
