from functools import wraps
from threading import Thread
from typing import Any


def threaded(function_name: Any) -> Any:
    """A function to be used as decorator to execute a function in different thread.

    Args:
        function_name: decorated function.

    Returns:
        threaded function.

    """

    @wraps(function_name)
    def wrapper(*args: str, **kwargs: Any) -> Thread:
        thread = Thread(target=function_name, args=args, kwargs=kwargs)
        thread.start()
        return thread

    return wrapper