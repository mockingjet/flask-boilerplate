from flask import Blueprint, request

from jetblog.utils import list_jsonify
from .models import Article, Tag, Category

bp = Blueprint('articles', __name__)


@bp.route('/articles', methods=['GET'])
def get_articles():
    articles = Article.query.all()
    return articles


@bp.route('/categories', methods=['GET'])
@list_jsonify()
def get_categories():
    categories = Category.query.all()
    return categories


@bp.route('/tags', methods=['GET'])
@list_jsonify()
def get_tags():
    tags = Tag.query.all()
    return tags
