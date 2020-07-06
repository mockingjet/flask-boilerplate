import datetime as dt

from marshmallow import fields, post_dump
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from jetblog.database import CamelCase
from .models import Category, Tag, Article


class CategorySchema(CamelCase, SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        exclude = ['created_at']

    tags = fields.Nested(lambda: TagSchema(exclude=['category']), many=True)


class TagSchema(CamelCase, SQLAlchemyAutoSchema):
    class Meta:
        model = Tag
        include_fk = True
        exclude = ['created_at', 'category_id']

    category = fields.Nested(CategorySchema(exclude=['tags']))


class ArticleSchema(CamelCase, SQLAlchemyAutoSchema):
    class Meta:
        model = Article
        exclude = ['tags.category']

    tags = fields.Nested(TagSchema, many=True)
