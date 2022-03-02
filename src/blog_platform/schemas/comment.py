from datetime import datetime

from pydantic import BaseModel

from ..schemas import User


class CommentBase(BaseModel):
    id: int
    author: User
    body: str
    created_at: datetime


class Comment(CommentBase):
    id: int

    class Config:
        orm_mode = True


class CommentCreate(CommentBase):
    pass


class CommentUpdate(CommentBase):
    pass
