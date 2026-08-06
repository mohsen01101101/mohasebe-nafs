from sqlmodel import Session
from app.db.database import engine
from app.services.user import UserService


if __name__ == "__main__":
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    password = input("Enter password: ")

    with Session(engine) as session:
        user = UserService(session).register_student(
            name=name,
            phone_number=phone_number,
            password=password,
        )

    print("\nStudent created:")
    print(f"ID: {user.id}")
    print(f"Name: {user.name}")
    print(f"Phone: {user.phone_number}")
