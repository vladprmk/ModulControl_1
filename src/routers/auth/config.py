from pydantic_settings import BaseSettings, SettingsConfigDict


class AuthConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    JWT_ALGORITHM: str
    JWT_SECRET_KEY: str
    JWT_EXPIRE_MINUTES: int = 30


auth_settings = AuthConfig()  # type: ignore[call-arg]
