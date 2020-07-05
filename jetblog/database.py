import os
import datetime.datetime as dt

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


d_format = "%Y-%m-%d"
dt_format = "%Y-%m-%dT%H:%M:%S.%fZ"


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

    def to_dict(self, excludes=[], use_date=[]):
        data = {}
        for column in self.__table__.columns:
            if column.name in excludes:
                continue

            value = getattr(self, column.name)
            if isinstance(value, dt):
                if column.name in use_date:
                    value = str(dt.strftime(value, d_format))
                else:
                    value = str(dt.strftime(value, dt_format))

            data.update({column.name: value})
        return data
