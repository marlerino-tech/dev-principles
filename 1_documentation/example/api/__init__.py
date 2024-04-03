"""
    Главный файл модуля ``api``
"""

from fastapi import APIRouter

from .v1 import v1_router

router = APIRouter()
"""
APIRouter: Docstring для главного роутера
"""

router.include_router(router=v1_router, prefix="/v1")

__all__ = ["router"]
