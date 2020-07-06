import datetime as dt

from marshmallow import Schema, fields, post_dump

from .models import Article


class CategorySchema(Schema):
    category_id = fields.Int()
    name = fields.Str()

    # tags = fields.Nested(lambda: TagSchema(exclude=['category']), many=True)
    tags = fields.Nested('TagSchema', exclude=['category'], many=True)


class TagSchema(Schema):
    tag_id = fields.Str()
    name = fields.Str()
    category_id = fields.Int()

    category = fields.Nested(CategorySchema(exclude=['tags']))


class ArticleSchema(Schema):
    article_id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    body = fields.Str()
    created_at = fields.DateTime()

    tags = fields.Nested(TagSchema(exclude=['category_id']), many=True)

    @post_dump(pass_many=True)
    def envelope(self, data, many, **kwargs):
        key = "articles" if many else "article"
        return {key: data}
