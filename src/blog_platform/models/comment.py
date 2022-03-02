from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text

from ..db.base_class import Base


class Comment(Base):
    id = Column(Integer, primary_key=True, index=True)
    author = Column(
        Integer, ForeignKey('user.id', name='fk_comment_user_id', ondelete='CASCADE')
    )
    body = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)

