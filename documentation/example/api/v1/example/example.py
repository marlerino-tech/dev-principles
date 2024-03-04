module_example_variable1 = 1000

from fastapi import APIRouter, Query
from pydantic import BaseModel

router = APIRouter()
"""APIRouter: API router for example

Документ-строка может занимать несколько строк. Тип может быть указан необязательно на первой строке, разделенный двоеточием.
"""


@router.get(path="/work", status_code=200)
async def get_work(id: Query(...) = 1) -> dict:
    """
    Возвращает сообщение о работе

    Args:
        id (int): ID для работы эндпоинта

    Returns:
        dict: Словарь включающий сообщение и ID
    """
    return {"message": "Work", "id": id}


# FIXME: rewrite algorithm
@router.get(path="/dont_work")
async def dont_work() -> dict:
    """
    Показывает пример использования смысловых комментариев

    Returns:
        dict: Когда ошибка будет исправлена :)
    """
    return 10 / 0


class Todo(BaseModel):
    """
    Модель для создания таска
    """
    title: str
    description: str

# TODO: create connection to db and add todo dict in database
@router.post(path="/todo")
async def create_todo(todo: Todo) -> dict:
    """
    Создание todo таска
    Args:
        todo (Todo): Модель для создания таска
    """
    pass
