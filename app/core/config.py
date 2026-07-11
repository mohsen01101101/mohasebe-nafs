from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    # Database
    sqlite_url: str

    # Auth
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    # API
    api_url: str
    api_prefix: str = "/api"

    @property
    def api_base_url(self):
        return f"{self.api_url}{self.api_prefix}"


settings = Settings()  # type: ignore[call-arg]
