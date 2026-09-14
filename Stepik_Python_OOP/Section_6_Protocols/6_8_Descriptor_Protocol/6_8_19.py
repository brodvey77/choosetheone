from random import randint

class RandomNumber:
    def __init__(self, start, end, cache=False):
        self.start = start
        self.end = end
        self.cache = cache
        self.a = randint(start, end)

    def __set_name__(self, cls, attr):
        self._attr = attr


    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self.cache == True:
            return self.a
        else:
            return randint(self.start, self.end)

    def __set__(self, obj, value):
        raise AttributeError("Изменение невозможно")






class CachedRandInt():
    n = RandomNumber(1, 10 ** 6, True)


x = CachedRandInt()
y = CachedRandInt()
z = CachedRandInt()

print(x.n == y.n)
print(x.n == z.n)
print(y.n == z.n)


import random


class RandomNumber:
    def __init__(self, start, end, cache=False):
        self.start = start
        self.end = end
        self.cache = cache

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self.cache and self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        number = random.randint(self.start, self.end)
        if self.cache:
            obj.__dict__[self._attr] = number
        return number

    def __set__(self, obj, value):
        raise AttributeError('Изменение невозможно')




