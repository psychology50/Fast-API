from sqlalchemy import Column, TEXT, INT, BIGINT, DATETIME, BOOLEAN, VARCHAR, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    username = Column(VARCHAR, nullable=False)
    password = Column(VARCHAR, nullable=True)
    password_updated_at = Column(DATETIME, nullable=True)
    profile_image_url = Column(VARCHAR, nullable=True)
    phone = Column(VARCHAR, nullable=False)
    role = Column(CHAR, nullable=False)
    profile_visibility = Column(CHAR, nullable=False)
    locked = Column(BOOLEAN, nullable=False)

    account_book_notify = Column(BOOLEAN, nullable=False)
    feed_notify = Column(BOOLEAN, nullable=False)
    chat_notify = Column(BOOLEAN, nullable=False)

    created_at = Column(DATETIME, nullable=False)
    updated_at = Column(DATETIME, nullable=False)
    deleted_at = Column(DATETIME, nullable=True)

    
