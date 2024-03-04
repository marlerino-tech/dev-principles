import os
from enum import Enum
from typing import Any, List

from dotenv import load_dotenv
from pydantic import BaseSettings, PostgresDsn, RedisDsn

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path=dotenv_path)


class EnvironmentType(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"


class BaseConfig(BaseSettings):
    class Config:
        case_sensitive = True


class Config(BaseConfig):
    DEBUG: int = 0
    DEFAULT_LOCALE: str = "en_US"
    ENVIRONMENT: str = EnvironmentType(os.environ.get("ENVIRONMENT"))
    BACKEND_HOST: str = os.environ.get("BACKEND_HOST")
    POSTGRES_URL: PostgresDsn = (
        f"postgresql+asyncpg://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASS')}@"
        f"{os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')}/{os.environ.get('DB_NAME')}"
    )
    REDIS_URL: RedisDsn = f"redis://:{os.environ.get('REDIS_PASSWORD')}@{os.environ.get('REDIS_HOST')}:{os.environ.get('REDIS_PORT')}/0"
    PORT: int = os.environ.get("PORT")
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60 * 24 * 7
    API_FB_URL: str = "https://graph.facebook.com/v19.0/"
    EXCLUDE_COLUMNS: list[str] = [
        "id",
        "user_id",
        "fb_id",
        "datetime_start",
        "interval_from",
        "interval_to",
        "created_at",
        "updated_at",
    ]
    BOT_TOKEN: str = os.environ.get("BOT_TOKEN")
    CHAT_IDS: Any
    PATH_LOG: str = os.path.join(os.path.dirname(os.path.dirname(__file__)), "log")


chat_ids = list(map(int, os.getenv("CHAT_IDS").split(",")))
config: Config = Config(CHAT_IDS=chat_ids)
