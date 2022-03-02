from sqlalchemy import Boolean, Column, Integer, String, Text
from sqlalchemy.sql import expression

from ..db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(length=255), unique=True)
    password_hash = Column(Text)

    is_admin = Column(
        Boolean, server_default=expression.false(), default=False,
        nullable=False
    )
