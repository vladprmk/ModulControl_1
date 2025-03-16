from pydantic import BaseModel, Field


class UserRegisterModel(BaseModel):
    username: str = Field(
        ..., min_length=4, max_length=20, pattern=r"^[a-zA-Z0-9_]*$"
    )

    password: str = Field(...)


class UserRegisterResponseModel(BaseModel):
    id: int

    username: str


class UserLoginModel(BaseModel):
    username: str = Field(
        ..., min_length=4, max_length=20, pattern=r"^[a-zA-Z0-9_]*$"
    )

    password: str = Field(...)
