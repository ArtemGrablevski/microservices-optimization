from dotenv import find_dotenv

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=find_dotenv(),
        env_file_encoding="utf-8"
    )

    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: int
    postgres_db: str

    @property
    def postgres_dsn(self) -> PostgresDsn:
        return (
            f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@"
            f"{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )
