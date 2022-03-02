from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from ..schemas import User


class BlogBase(BaseModel):
    title: str
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    authors: List[User] = []


class Blog(BlogBase):
    id: int
    owner: int

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
