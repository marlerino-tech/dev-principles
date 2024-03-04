"""
Инициализация сервера fastapi со всеми настройками
"""

from typing import List

from fastapi import Depends, FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api import router
from core.config import config
from core.exceptions import CustomException
from core.fastapi.dependencies import Logging
from core.fastapi.middlewares import (
    AuthBackend,
    AuthenticationMiddleware,
    ResponseLoggerMiddleware,
    SQLAlchemyMiddleware,
)


def on_auth_error(request: Request, exc: Exception):
    """
    Функция, которая будет испольняться при возникновении ошибок в ходе работы Middleware
    Args:
        request: Встроенная информация о запросе
        exc: Само исключение

    Returns:
        Ответ в формате ``JSON``
    """
    status_code, error_code, message = 401, None, str(exc)
    if isinstance(exc, CustomException):
        status_code = int(exc.code)
        error_code = exc.error_code
        message = exc.message

    return JSONResponse(
        status_code=status_code,
        content={"error_code": error_code, "message": message},
    )


def init_routers(app_: FastAPI) -> None:
    """
    Инициализация роутера
    """
    app_.include_router(router=router)


def init_listeners(app_: FastAPI) -> None:
    """
    Прослушка исключения порождённых от ``CustomException`` и возврат кастомного ответа в виде ``JSON``
    """
    @app_.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )


def make_middleware() -> List[Middleware]:
    """
    Создание необходимых Middlewares

    Returns:
        Список созданных Middlewares
    """
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        Middleware(
            AuthenticationMiddleware,
            backend=AuthBackend(),
            on_error=on_auth_error,
        ),
        Middleware(SQLAlchemyMiddleware),
        Middleware(ResponseLoggerMiddleware),
    ]
    return middleware


def create_app() -> FastAPI:
    """
    Главная фунция, которая инициализирует главный объект ``FastAPI``

    Returns:
        FastAPI: Объект ``FastAPI``, который будет использоваться для запуска сервера
    """

    app_ = FastAPI(
        title="example",
        description="FastAPI backend for example documentation",
        version="1.0.0",
        docs_url=None if config.ENVIRONMENT == "production" else "/docs",
        redoc_url=None if config.ENVIRONMENT == "production" else "/redoc",
        dependencies=[Depends(Logging)],
        middleware=make_middleware(),
    )
    init_routers(app_=app_)
    init_listeners(app_=app_)
    return app_


app = create_app()
