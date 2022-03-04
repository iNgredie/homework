from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class UserBlog(BaseModel):
    id: int
    user_id: int
    blog_id: int


class BlogBase(BaseModel):
    title: str
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    authors: List[UserBlog] = []


class Blog(BlogBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class BlogCreate(BlogBase):
    pass


class BlogUpdate(BlogBase):
    pass
