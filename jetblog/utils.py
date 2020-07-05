from functools import wraps


def print_exception(exception: Exception):
    """Decorate functions that will raise the targeted exception 
    and catch its error, print its error message

    :param exception: The targeted exception that you want to track
    :type exception: Exception
    """

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
