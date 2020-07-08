import datetime as dt

from marshmallow import fields, post_dump

from jetblog.database import SaAutoCamelSchema
from .models import Category, Tag, Article


class CategorySchema(SaAutoCamelSchema):
    class Meta:
        model = Category
        exclude = ['created_at']

    tags = fields.Nested(lambda: TagSchema(exclude=['category']), many=True)


class TagSchema(SaAutoCamelSchema):
    class Meta:
        model = Tag
        include_fk = True
        exclude = ['created_at', 'category_id']

    category = fields.Nested(CategorySchema(exclude=['tags']))


class ArticleSchema(SaAutoCamelSchema):
    class Meta:
        model = Article
        exclude = ['tags.category']

    tags = fields.Nested(TagSchema, many=True)
