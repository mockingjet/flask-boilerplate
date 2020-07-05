import os

from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

from .settings import Config


engine = create_engine(
    Config.DATABASE_URI,
    pool_size=2,
    pool_timeout=2,
    poolclass=QueuePool,
    max_overflow=1,
    connect_args={"check_same_thread": False})

session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)

db_session = scoped_session(session)

Base = declarative_base()
Base.query = db_session.query_property()


class Model(Base):
    __abstract__ = True

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return self.save()

    def save(self):
        db_session.add(self)
        db_session.commit()
        return self

    def delete(self):
        db_session.delete(self)
        db_session.commit()
