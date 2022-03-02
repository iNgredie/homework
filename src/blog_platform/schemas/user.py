from pydantic import BaseModel


class BaseUser(BaseModel):
    username: str
    is_admin: bool


class UserCreate(BaseUser):
    password: str


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True



