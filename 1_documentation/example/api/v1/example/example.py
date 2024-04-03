module_example_variable1 = 1000

from fastapi import APIRouter, Query
from pydantic import BaseModel

router = APIRouter()
"""APIRouter: API router for example

Документ-строка может занимать несколько строк. Тип может быть указан необязательно на первой строке, разделенный двоеточием.
"""


class MessageModel(BaseModel):
    """
    Модель для сообщения
    """

    message: str
    id: int


@router.get(
    path="/work",
    response_model=MessageModel,
    description="empty"
)
async def get_work(id: int = 1):
    """
    Возвращает сообщение о работе

    Args:
        id (int): ID для работы эндпоинта

    Returns:
        dict: Словарь включающий сообщение и ID
    """
    return MessageModel(message="Work", id=id)


# FIXME: rewrite algorithm
@router.get(
    path="/dont_work",
    response_model=dict,
    description="empty"
)
async def dont_work():
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
@router.post(
    path="/todo",
    response_model=Todo,
    description="empty"
)
async def create_todo(todo: Todo) -> dict:
    """
    Создание todo таска
    Args:
        todo (Todo): Модель для создания таска
    """
    pass
