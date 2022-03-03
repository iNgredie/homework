from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models
from .. import schemas
from ..db.session import get_session


class BlogService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int, blog_id: int) -> models.Blog:
        blog = (
            self.session.query(models.Blog).filter_by(id=blog_id, owner=user_id).first()
        )
        if not blog:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return blog

    def get(self, user_id: int, blog_id: int) -> models.Blog:
        return self._get(user_id, blog_id)

    def get_list(self) -> List[models.Blog]:
        return self.session.query(models.Blog).all()

    def create(self, user_id: int, blog_data: schemas.BlogCreate) -> models.Blog:
        blog = models.Blog(**blog_data.dict(), owner=user_id)
        self.session.add(blog)
        self.session.commit()
        self.session.refresh(blog)
        return blog

    def update(
        self,
        user_id: int,
        blog_id: int,
        blog_data: schemas.BlogUpdate,
    ) -> models.Blog:
        blog = self._get(user_id, blog_id)
        for field, value in blog_data:
            setattr(blog, field, value)
        self.session.commit()
        return blog

    def delete(self, user_id: int, blog_id: int) -> None:
        blog = self._get(user_id, blog_id)
        self.session.delete(blog)
        self.session.commit()
