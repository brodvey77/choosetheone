
class AdvancedList(list):

    def join(self, l=' '):
        s = l.join(map(str, self))
        return s

    def map(self, func):
        l = map(func, self)
        self[:] = l
        return l


    def filter(self, func):
        self[:] = [item for item in self if func(item)]





advancedlist = AdvancedList([0, 1, 2, '', 3, (), 4, 5, False, {}])
id1 = id(advancedlist)

advancedlist.filter(bool)
id2 = id(advancedlist)

print(advancedlist)
print(id1 == id2)

class AdvancedList(list):
    def __init__(self, iterable=(), default=None):
        super().__init__(item for item in iterable)
        self._default = default

    def extend_self(self, data):
        self.clear()
        self.extend(data)

    def join(self, sep=' '):
        return sep.join(str(item) for item in self)

    def map(self, func):
        new_data = list(func(item) for item in self)
        self.extend_self(new_data)

    def filter(self, predicate):
        new_data = list(filter(predicate, self))
        self.extend_self(new_data)


class AdvancedList(list):

    def join(self, sep=" "):
        return sep.join(str(item) for item in self)

    def map(self, func):
        self[:] = map(func, self)

    def filter(self, func):
        self[:] = filter(func, self)


class AdvancedList(list):

    def join(self, sep=' '):
        return sep.join(map(str, self))

    def map(self, func):
        self[:] = [func(i) for i in self]

    def filter(self, func):
        self[:] = [i for i in self if func(i)]



