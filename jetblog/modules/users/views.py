from flask import Blueprint, request

from jetblog.utils import list_jsonify
from .models import User

bp = Blueprint('users', __name__)


@bp.route('/users', methods=['GET'])
@list_jsonify(use_date=["created_at"])
def get_users():
    users = User.query.all()
    return users
