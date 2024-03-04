from fastapi import APIRouter, Depends

router = APIRouter()


@router.get(path="/work", status_code=200)
async def get_work(id: int = 1) -> dict:
    """
    Returns a message about work.

    :param id: ID for work endpoint

    :return: A dictionary containing the message.
    :rtype: dict
    """
    return {"message": "Work", "id": id}


# FIXME: rewrite algorithm
@router.get(path="/dont_work")
async def dont_work() -> dict:
    return 10 / 0


# TODO: create connection to db and add todo dict in database
@router.post(path="/todo")
async def create_todo(todo: dict) -> dict:
    pass
