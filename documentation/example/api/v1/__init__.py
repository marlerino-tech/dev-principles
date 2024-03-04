from fastapi import APIRouter

from .example import example_router

v1_router = APIRouter()
v1_router.include_router(router=example_router, prefix="/example")