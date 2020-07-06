import datetime as dt

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, TEXT, Table, ForeignKey

from jetblog.database import Model

articles_assoc_tags = Table(
    "articles_assoc_tags", Model.metadata,
    Column("tagId", Integer, ForeignKey('tags.tagId')),
    Column("articleId", Integer, ForeignKey('articles.articleId')))


class Category(Model):
    __tablename__ = 'categories'

    categoryId = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, index=True)
    createdAt = Column(DateTime, default=dt.datetime.utcnow)

    tags = relationship("Tag")

    def __init__(self, name):
        Model.__init__(self, name=name)


class Tag(Model):
    __tablename__ = "tags"

    tagId = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, index=True)
    categoryId = Column(Integer, ForeignKey('categories.categoryId'))
    createdAt = Column(DateTime, default=dt.datetime.utcnow)

    category = relationship("Category")
    articles = relationship("Article", secondary=articles_assoc_tags,
                            back_populates="tags")

    def __init__(self, name, category):
        Model.__init__(self, name=name, category=category)


class Article(Model):
    __tablename__ = "articles"

    articleId = Column(Integer, primary_key=True)
    title = Column(String(30), unique=True, index=True)
    description = Column(String(120))
    body = Column(TEXT)
    createdAt = Column(DateTime, default=dt.datetime.utcnow)

    tags = relationship("Tag", secondary=articles_assoc_tags,
                        back_populates="articles")

    def __init__(self, title, description, body, extended_tags=[], **kwargs):
        Model.__init__(self, title=title,
                       description=description, body=body, **kwargs)
        self.tags.extend(extended_tags)
