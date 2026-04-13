
class CachedFunction:
    cache = {}
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        val = self.func(*args)
        self.cache[args] = val
        return val


@CachedFunction
def slow_fibonacci(n):
    if n == 1:
        return 0
    elif n in (2, 3):
        return 1
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)


print(slow_fibonacci(100))


class CachedFunction:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        result = self.cache.get(args) or self.func(*args)
        self.cache.setdefault(args, result)
        return result

from functools import lru_cache

class CachedFunction:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    @lru_cache()
    def __call__(self, *args):
        return self.cache.setdefault(args, self.func(*args))


