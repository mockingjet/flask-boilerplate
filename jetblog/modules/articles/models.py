from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, TEXT, Table, ForeignKey

from jetblog.database import dt, Model

articles_assoc_tags = Table(
    "articles_assoc_tags", Model.metadata,
    Column("tag_id", Integer, ForeignKey('tags.tag_id')),
    Column("article_id", Integer, ForeignKey('articles.article_id')))


class Article(Model):
    __tablename__ = "articles"

    article_id = Column(Integer, primary_key=True)
    title = Column(String(30), unique=True, index=True)
    description = Column(String(120))
    body = Column(TEXT)
    tags = relationship("Tag",
                        secondary=articles_assoc_tags,
                        back_populates="articles")
    created_at = Column(DateTime, default=dt.utcnow)

    def __init__(self, title: str, description: str, body: str, **kwargs):
        Model.__init__(self, title=title,
                       description=description, body=body, **kwargs)


class Tag(Model):
    __tablename__ = "tags"

    tag_id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, index=True)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    articles = relationship("Article",
                            secondary=articles_assoc_tags,
                            back_populates="tags")
    created_at = Column(DateTime, default=dt.utcnow)

    def __init__(self, name, category_id):
        Model.__init__(self, name=name, category_id=category_id)


class Category(Model):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, index=True)
    tags = relationship('Tag')
    created_at = Column(DateTime, default=dt.utcnow)

    def __init__(self, name):
        Model.__init__(self, name=name)
