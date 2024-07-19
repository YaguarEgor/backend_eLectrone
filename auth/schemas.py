import uuid
from typing import Optional

from fastapi_users import schemas
from fastapi_users.schemas import PYDANTIC_V2


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    name: str
    second_name: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    id: int
    email: str
    name: str
    second_name: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    pass
