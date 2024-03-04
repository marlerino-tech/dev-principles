"""
Версия API 1.0 для примера шаблона документирования
"""

from fastapi import APIRouter

from .example import example_router

v1_router = APIRouter()
v1_router.include_router(router=example_router, prefix="/example")
