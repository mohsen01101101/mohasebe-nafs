from pydantic_settings import BaseSettings


sqlite_file_name = "database.db"


class Settings(BaseSettings):
    sqlite_url = f"sqlite:///{sqlite_file_name}"


settings = Settings()
