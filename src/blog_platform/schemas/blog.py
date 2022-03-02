from datetime import datetime
from typing import List

from pydantic import BaseModel

from ..schemas import User


class BlogBase(BaseModel):
    id: int
    title: str
    description: str
    created_at: datetime
    updated_at: datetime
    authors: List[User]
    owner: User


class Blog(BlogBase):
    id: int

    class Config:
        orm_mode = True


class BlogCreate(BlogBase):
    pass


class BlogUpdate(BlogBase):
    pass


class UserBlog(BaseModel):
    id: int
    user_id: User
    blog_id: Blog