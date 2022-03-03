from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models
from .. import schemas
from ..db.session import get_session


class CommentService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int, comment_id: int) -> models.Comment:
        comment = (
            self.session.query(models.Comment).filter_by(id=comment_id, owner=user_id).first()
        )
        if not comment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return comment

    def get(self, user_id: int, comment_id: int) -> models.Comment:
        return self._get(user_id, comment_id)

    def get_list(self) -> List[models.Comment]:
        return self.session.query(models.Comment).all()

    def create(self, user_id: int, comment_data: schemas.CommentCreate) -> models.Comment:
        comment = models.Comment(**comment_data.dict(), author=user_id)
        self.session.add(comment)
        self.session.commit()
        self.session.refresh(comment)
        return comment

    def update(
        self,
        user_id: int,
        comment_id: int,
        comment_data: schemas.CommentUpdate,
    ) -> models.Comment:
        comment = self._get(user_id, comment_id)
        for field, value in comment_data:
            setattr(comment, field, value)
        self.session.commit()
        return comment

    def delete(self, user_id: int, comment_id: int) -> None:
        comment = self._get(user_id, comment_id)
        self.session.delete(comment)
        self.session.commit()
