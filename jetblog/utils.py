from functools import wraps


def list_jsonify(excludes=[], use_date=[]):
    """Decorator for transform sqlalchemy query results as json

    :param excludes: see in the database.Model.to_dict, defaults to []
    :type excludes: list, optional
    :param use_date: see in the database.Model.to_dict, defaults to []
    :type use_date: list, optional
    """

    def decorator(fn):
        @wraps(fn)
        def wrap(*args, **kwargs):
            as_list = [data.to_dict(excludes, use_date)
                       for data in fn(*args, **kwargs)]
            return {"list": as_list}
        return wrap
    return decorator


def print_exception(exception: Exception):
    def decorator(fn):
        @wraps(fn)
        def wrap(*args, **kwargs):
            try:
                fn(*args, **kwargs)
            except Exception as error:
                if isinstance(error, exception):
                    print(str(error))
        return wrap
    return decorator
