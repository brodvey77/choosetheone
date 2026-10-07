from collections import UserList

class DefaultList(UserList):
    def __init__(self, iterable=[], default=None):
        super().__init__(iterable)
        self.default = default

    def __getitem__(self, i):
        if isinstance(i, slice):
            return self.__class__(self.data[i])
        else:
            try:
                return self.data[i]
            except IndexError:
                return self.default


defaultlist = DefaultList()

print(defaultlist)



from collections import UserList


class DefaultList(UserList):
    def __init__(self, iterable=(), default=None):
        super().__init__(item for item in iterable)
        self._default = default

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except IndexError:
            return self._default
