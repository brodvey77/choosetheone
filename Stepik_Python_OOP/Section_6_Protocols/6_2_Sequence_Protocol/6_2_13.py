
class OrderedSet:
    def __init__(self, iterable=()):
        self._data = list(iterable)


    def add(self, obj):
        self._data.append(obj)

    def discard(self, obj):
        while obj in self._data:
            self._data.remove(obj)

    def __len__(self):
        return len(list(dict.fromkeys(self._data)))

    def __iter__(self):
        yield from list(dict.fromkeys(self._data))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return self._data == other._data
        if isinstance(other, set):
            return set(self._data) == other
        return NotImplemented


print(OrderedSet([1, 2, 3]) == {3, 2, 1})
print(OrderedSet([1, 2]) == {1, 2, 3})
print(OrderedSet([1, 2, 3]) == {1, 2, 2})


class OrderedSet:
    def __init__(self, iterable=[]):
        self.ord_set = []
        for item in iterable:
            if item not in self.ord_set:
                self.ord_set.append(item)

    def add(self, obj):
        if obj not in self.ord_set:
            self.ord_set.append(obj)

    def discard(self, obj):
        if obj in self.ord_set:
            del self.ord_set[self.ord_set.index(obj)]

    def __iter__(self):
        return iter(self.ord_set)

    def __len__(self):
        return len(self.ord_set)

    def __contains__(self, obj):
        return obj in self.ord_set

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.ord_set == other.ord_set
        elif isinstance(other, set):
            return set(self.ord_set) == other
        return NotImplemented