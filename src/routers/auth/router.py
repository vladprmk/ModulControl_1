from __future__ import annotations

import typing

import bcrypt
import jwt
from fastapi import APIRouter, Depends, HTTPException
from loguru import logger

from .config import auth_settings
from .dependencies import get_user_repository
from .schemas import (
    UserLoginModel,
    UserRegisterModel,
    UserRegisterResponseModel,
)

if typing.TYPE_CHECKING:
    from src.db import UserRepository


router = APIRouter(prefix="/auth", tags=["auth"])


def do_hash_password(password: str) -> str:
    return bcrypt.hashpw(
        password=password.encode("utf-8"), salt=bcrypt.gensalt()
    ).decode("utf-8")


def do_check_password(password: str, pwhash: str) -> bool:
    return bcrypt.checkpw(
        password=password.encode("utf-8"),
        hashed_password=pwhash.encode("utf-8"),
    )


@router.post("/register")
async def register(
    user_register_model: UserRegisterModel,
    user_repository: UserRepository = Depends(get_user_repository),
):
    pwhash = do_hash_password(user_register_model.password)
    user_in_db = user_repository.insert(
        username=user_register_model.username,
        pwhash=pwhash,
    )
    if not user_in_db:
        raise HTTPException(status_code=400, detail="User already exists")

    return UserRegisterResponseModel(
        id=user_in_db.id,
        username=user_in_db.username,
    )


@router.post("/login")
async def login(
    user_login_model: UserLoginModel,
    user_repository: UserRepository = Depends(get_user_repository),
):
    user_in_db = user_repository.select_by_username(user_login_model.username)
    if not user_in_db:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password (user not found)",
        )

    ok = do_check_password(user_login_model.password, user_in_db.pwhash)
    if not ok:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password (hash is not ok)",
        )

    return {
        "token": jwt.encode(
            payload={"sub": str(user_in_db.id)},
            key=auth_settings.JWT_SECRET_KEY,
            algorithm=auth_settings.JWT_ALGORITHM,
        ),
        "token_type": "bearer",
    }


@router.get("/me")
async def me(token: str):
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


def get_router() -> APIRouter:
    return router
