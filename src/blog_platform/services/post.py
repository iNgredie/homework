from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models
from .. import schemas
from ..db.session import get_session


class PostService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int, post_id: int) -> models.Post:
        post = (
            self.session.query(models.Post).filter_by(id=post_id, owner=user_id).first()
        )
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return post

    def get(self, user_id: int, post_id: int) -> models.Post:
        return self._get(user_id, post_id)

    def get_list(self) -> List[models.Post]:
        return self.session.query(models.Post).all()

    def create(self, user_id: int, post_data: schemas.PostCreate) -> models.Post:
        post = models.Post(**post_data.dict(), author=user_id)
        self.session.add(post)
        self.session.commit()
        self.session.refresh(post)
        return post

    def update(
        self,
        user_id: int,
        post_id: int,
        post_data: schemas.PostUpdate,
    ) -> models.Post:
        post = self._get(user_id, post_id)
        for field, value in post_data:
            setattr(post, field, value)
        self.session.commit()
        return post

    def delete(self, user_id: int, post_id: int) -> None:
        post = self._get(user_id, post_id)
        self.session.delete(post)
        self.session.commit()
