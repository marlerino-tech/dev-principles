from datetime import datetime, timezone
from typing import Optional, Tuple

from fastapi.responses import JSONResponse
from jose import JWTError, jwt
from starlette.authentication import AuthenticationBackend
from starlette.middleware.authentication import (
    AuthenticationMiddleware as BaseAuthenticationMiddleware,
)
from starlette.requests import HTTPConnection

from app.schemas.extras.current_user import CurrentUser
from core.config import config
from core.exceptions import CustomException
from core.security.jwt import JWTExpiredError


class AuthBackend(AuthenticationBackend):
    async def authenticate(
        self, conn: HTTPConnection
    ) -> Tuple[bool, Optional[CurrentUser]]:
        current_user = CurrentUser()
        authorization: str = conn.headers.get("Authorization")
        if not authorization:
            return False, current_user

        try:
            scheme, token = authorization.split(" ")
            if scheme.lower() != "bearer":
                return False, current_user
        except ValueError:
            return False, current_user

        if not token:
            return False, current_user

        try:
            payload = jwt.decode(
                token=token,
                key=config.SECRET_KEY,
                algorithms=[config.JWT_ALGORITHM],
                # options={"verify_exp": False},
            )
            user_id = payload.get("user_id")
        except JWTError:
            raise JWTExpiredError()
            # return False, current_user

        expire = payload.get("exp")
        if expire is None or datetime.now(timezone.utc) > datetime.fromtimestamp(
            expire, tz=timezone.utc
        ):
            print("DONT WORK")
            # raise JWTExpiredError()

        current_user.id = user_id
        return True, current_user


class AuthenticationMiddleware(BaseAuthenticationMiddleware):
    pass
