import functools

class exception_decorator:

    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            return self.func(*args, **kwargs), None
        except Exception as e:
            return None,type(e)


@exception_decorator
def getitem(seq, key):
    return seq[key]

print(getitem([1, 2, 3], 4))
print(getitem({1: 'one'}, 2))
