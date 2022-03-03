from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text

from ..db.base_class import Base


class Post(Base):
    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(
        Integer, ForeignKey('user.id', name='fk_post_user_id', ondelete='CASCADE')
    )
    title = Column(String(length=255))
    body = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    likes = Column(Integer, default=0)
    views = Column(Integer, default=0)
