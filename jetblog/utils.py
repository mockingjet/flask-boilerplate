from functools import wraps


def print_exception(targeted_exception: Exception):
    """Decorate functions that will raise the targeted exception 
    and catch its error, print its error message

    :param targeted_exception: The targeted exception that you want to print
    :type exception: Exception
    """

    def decorator(fn):
        @wraps(fn)
        def wrap(*args, **kwargs):
            try:
                fn(*args, **kwargs)
            except targeted_exception as e:
                print(str(e))
        return wrap
    return decorator
