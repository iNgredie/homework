from datetime import datetime

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    body: str
    created_at: datetime
    likes: int
    views: int


class Post(PostBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass
