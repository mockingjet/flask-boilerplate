from flask import Blueprint, request
from marshmallow import ValidationError

from jetblog.utils import wrap_response
from jetblog.exceptions import APIError
from .models import Article, Tag, Category
from .schemas import ArticleSchema, TagSchema, CategorySchema


bp = Blueprint('article', __name__)


@bp.route('/articles')
def get_articles():
    articles = Article.query.all()
    articles_schema = ArticleSchema(many=True)
    return {
        "apiVerison": "0.0",
        "data": {
            "articles": articles_schema.dump(articles)
        }
    }


@bp.route('/articles', methods=['POST'])
def post_articles():
    json_data = request.get_json()
    article_schema = ArticleSchema()
    try:
        data = article_schema.load(json_data)
    except ValidationError as verr:
        raise APIError(422, "invalid input", input_error=verr.messages)

    article = Article.create(**data)
    return {
        "apiVerison": "0.0",
        "data": {
            "article": article_schema.dump(article)
        }
    }


@bp.route('/articles/<int:_id>')
def get_article(_id):
    article = Article.query.get(_id)
    if not article:
        raise APIError(400, ["article not found"])

    article_schema = ArticleSchema()
    return {
        "apiVerison": "0.0",
        "data": {
            "article": article_schema.dump(article)
        }
    }


@bp.route('/articles/<_title>')
def get_article_by_title(_title):
    article = Article.query.filter(Article.title == _title).first()
    if not article:
        raise APIError(400, "article not found")

    article_schema = ArticleSchema(exclude=['tags.category'])
    return {
        "apiVerison": "0.0",
        "data": {
            "articles": article_schema.dump(article)
        }
    }


@bp.route('/tags')
def get_tags():
    tags = Tag.query.all()

    tags_schema = TagSchema(many=True)
    return {
        "apiVersion": "0.0",
        "data": {
            "tags": tags_schema.dump(tags)
        }
    }


@bp.route('/categories')
def get_categories():
    categories = Category.query.all()

    categories_schema = CategorySchema(many=True)
    return {
        "apiVersion": "0.0",
        "data": {
            "categogries": categories_schema.dump(categories)
        }
    }
