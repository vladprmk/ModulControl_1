import jwt
from fastapi import Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from loguru import logger
from sqlalchemy import Engine

from src.db import UserRepository, user_table

from .config import auth_settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_engine(request: Request) -> Engine:
    return request.app.state.engine


def get_user_repository(
    engine: Engine = Depends(get_engine),
) -> UserRepository:
    return UserRepository(
        engine=engine,
        table=user_table,
    )


def get_active_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            jwt=token,
            key=auth_settings.JWT_SECRET_KEY,
            algorithms=[auth_settings.JWT_ALGORITHM],
        )
    except jwt.PyJWTError as err:
        logger.exception(err)
        raise HTTPException(status_code=401, detail=str(err)) from err

    return {"id": payload["sub"]}
