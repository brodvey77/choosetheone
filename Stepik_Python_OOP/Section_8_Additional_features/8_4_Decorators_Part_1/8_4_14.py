import functools

class ignore_exception:
    def __init__(self, *args):
        self.args = args

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*aargs, **kwargs):
            try:
                return func(*aargs, **kwargs)
            except (self.args) as e:
                print(f'Исключение {type(e).__name__} обработано')
        return wrapper


@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def func(x):
    return 1 / x


func(0)



import functools


class ignore_exception:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                value = func(*args, **kwargs)
                return value
            except self.exceptions as e:
                print(f'Исключение {e.__class__.__name__} обработано')

        return wrapper