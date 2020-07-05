from flask import Blueprint, request

from jetblog.exceptions import APIError
from .models import Article, Tag, Category
from .schemas import ArticleSchema, TagSchema, CategorySchema


bp = Blueprint('articles', __name__)


@bp.route('/articles')
def get_articles():
    articles_schema = ArticleSchema(many=True, exclude=['tags.category'])
    articles = Article.query.all()
    return {
        "apiVerison": "1.0",
        "data": articles_schema.dump(articles)
    }


@bp.route('/articles/<int:_id>')
def get_article(_id):
    article_schema = ArticleSchema(exclude=['tags.category'])
    article = Article.query.get(_id)
    if not article:
        raise APIError(400, "article not found")

    return {
        "apiVerison": "0.0",
        "data": article_schema.dump(article)
    }


@bp.route('/tags')
def get_tags():
    tags_schema = TagSchema(many=True)
    tags = Tag.query.all()
    return {
        "apiVersion": "0.0",
        "data": tags_schema.dump(tags)
    }


@bp.route('/categories')
def get_categories():
    categories_schema = CategorySchema(many=True)
    categories = Category.query.all()
    return {
        "apiVersion": "0.0",
        "data": categories_schema.dump(categories)
    }
