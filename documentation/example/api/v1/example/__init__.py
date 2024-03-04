from fastapi import APIRouter

from .example import router

example_router = APIRouter()
example_router.include_router(router, tags=["Example"])

__all__ = ["example_router"]