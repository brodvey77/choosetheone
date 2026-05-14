from itertools import islice

class SkipIterator:
    def __init__(self, iterable, n: int):
        self.iterable = islice(iterable, None, None, n + 1)


    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterable)





data = ['к', 'б', 'ш', 'к', 'к', 'о', 'т', 'г', 'о', 'д', 'р', 'в', 'с', 'с', 'и', 'о', 'в', 'п', 'у', 'с', 'л', 'т',
        'г', 'т', 'з', 'ь', 'о', 'п', 'н', 'в', 'и', 'н', 'с', 'п', 'р', 'ш', 'е', 'к', 'н', 'с', 'у', 'в', 'п', 'т',
        'х', 'т', 'с', 'с', 'л', 'с']
skipiterator = SkipIterator(iter(data), 4)

print(*skipiterator)

class SkipIterator:
    def __init__(self, iterable, n):
        self.iterable = iter(iterable)
        self.n = n
        self.first = True

    def __iter__(self):
        return self

    def __next__(self):
        if self.first:
            self.first = False
            return next(self.iterable)
        for _ in range(self.n):
            next(self.iterable)
        return next(self.iterable)




class SkipIterator:
    def __new__(self, iterable, n):
        return (v for k, v in enumerate(iterable) if k % (n + 1) == 0)

from itertools import islice

class SkipIterator:
    def __new__(self, iterable, n):
        return islice(iterable, None, None, n+1)


class SkipIterator:
    def __init__(self, iterable, n):
        self.__it_iterable = iter(iterable)
        self.__n = n
        self.__skip = 0

    def __iter__(self):
        return self

    def __next__(self):
        for _ in range(self.__skip):
            next(self.__it_iterable)
        self.__skip = self.__n
        return next(self.__it_iterable)