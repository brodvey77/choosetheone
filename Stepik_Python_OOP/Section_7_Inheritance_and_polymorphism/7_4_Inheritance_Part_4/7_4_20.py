
from collections import UserList


class NumberList(UserList):
    def __init__(self, iterable=()):
        self._check(iterable)
        super().__init__(iterable)

    @staticmethod
    def _check(iterable):
        if not all(isinstance(item, (int, float)) for item in iterable):
            raise TypeError(
                'Элементами экземпляра класса NumberList должны быть числа'
            )

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            self._check(value)
        else:
            self._check([value])
        super().__setitem__(index, value)

    def __add__(self, other):
        self._check(other)
        return super().__add__(other)

    def __iadd__(self, other):
        self._check(other)
        return super().__iadd__(other)

    def append(self, item):
        self._check([item])
        super().append(item)

    def extend(self, other):
        self._check(other)
        super().extend(other)

    def insert(self, index, item):
        self._check([item])
        super().insert(index, item)






# numberlist = NumberList([1, 2])
# numberlist.append(3)
# numberlist.extend([4, 5])
# numberlist.insert(0, 0)
# print(numberlist)




# numberlist = NumberList([0, 1.0])
# numberlist[1] = 1
# numberlist = numberlist + NumberList([2, 3])
# numberlist += NumberList([4, 5])
# print(numberlist)


#
try:
    numberlist = NumberList(['a', 'b', 'c'])
except TypeError as error:
    print(error)

#
#
numberlist = NumberList([1, 2, 3])
try:
    numberlist.append('4')
except TypeError as error:
    print(error)

#
