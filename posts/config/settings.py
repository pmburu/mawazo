from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = ""
    # MONGO_INITDB_DATABASE: str

    # CLIENT_ORIGIN: str

    class Config:
        env_prefix = ""
        env_file = ".env"
        env_encoding = "utf-8"


@lru_cache
def get_settings():
    return Settings()


settings = Settings()
