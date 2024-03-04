import os
from enum import Enum
from typing import Any, List

from dotenv import load_dotenv
from pydantic import BaseSettings, PostgresDsn, RedisDsn

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path=dotenv_path)


class EnvironmentType(str, Enum):
    """
    Типы возможного окружения
    """

    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"


class BaseConfig(BaseSettings):
    class Config:
        case_sensitive = True


class Config(BaseConfig):
    """
    Конфиг для работы программы.

    Notes:
        Переменные могут браться как и из окружения, так и задаваться в ``config`` напрямую
    """

    DEBUG: int = 0
    DEFAULT_LOCALE: str = "en_US"
    ENVIRONMENT: str = EnvironmentType(os.environ.get("ENVIRONMENT"))
    PORT: int = os.environ.get("PORT")
    BOT_TOKEN: str = os.environ.get("BOT_TOKEN")
    CHAT_IDS: Any
    PATH_LOG: str = os.path.join(os.path.dirname(os.path.dirname(__file__)), "log")


chat_ids = list(map(int, os.getenv("CHAT_IDS").split(",")))
config: Config = Config(CHAT_IDS=chat_ids)
