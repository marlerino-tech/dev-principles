"""
Модуль для примера документирования роутера

Attributes:
    example_router (APIRouter): осмысленное описание роутера и его назначение
"""

from fastapi import APIRouter

from .example import router

example_router = APIRouter()
example_router.include_router(router, tags=["Example"])

__all__ = ["example_router"]