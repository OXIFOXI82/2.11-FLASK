from abc import ABC
from typing import Optional

import pydantic


class AbstractUser(pydantic.BaseModel, ABC):
    name: str
    password: str

    @pydantic.field_validator("password")
    @classmethod
    def secure_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError(f"Minimal length of password is 8")
        return v


class CreateUser(AbstractUser):
    name: str
    password: str




class UpdateUser(AbstractUser):
    name: Optional[str] = None
    password: Optional[str] = None


class CreateAdvert(pydantic.BaseModel, ABC):
    header: str
    description: str
    owner_id: int


class UpdateAdvert(pydantic.BaseModel, ABC):
    header: Optional[str] = None
    description: Optional[str] = None
    owner_id: Optional[int] = None