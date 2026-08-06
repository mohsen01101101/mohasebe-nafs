from app.core.security import hash_password


if __name__ == "__main__":
    password = input("Enter password: ")

    password_hash = hash_password(password)

    print("\nGenerated password hash:")
    print(password_hash)
