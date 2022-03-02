from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from ..db.base_class import Base


class Blog(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=255))
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(
        DateTime(timezone=True), onupdate=datetime.utcnow, default=datetime.utcnow
    )
    authors = relationship('UserBlog', backref='blog')
    owner = Column(
        Integer, ForeignKey('user.id', name='fk_blog_user_id', ondelete='CASCADE')
    )


class UserBlog(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(
        Integer,
        ForeignKey('user.id', name='fk_user_blog_user_id', ondelete='CASCADE'),
        nullable=True,
    )
    blog_id = Column(
        Integer,
        ForeignKey('blog.id', name='fk_user_blog_blog_id', ondelete='CASCADE'),
        nullable=True,
    )
