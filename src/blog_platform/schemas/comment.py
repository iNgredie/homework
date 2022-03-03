from datetime import datetime

from pydantic import BaseModel


class CommentBase(BaseModel):
    body: str
    created_at: datetime


class Comment(CommentBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True


class CommentCreate(CommentBase):
    pass


class CommentUpdate(CommentBase):
    pass
