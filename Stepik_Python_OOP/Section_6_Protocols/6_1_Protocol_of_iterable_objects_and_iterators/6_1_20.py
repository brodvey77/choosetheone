class Peekable:
    def __init__(self, iterable):
        self._iterator = iter(iterable)
        self._has_peeked = False
        self._peeked_value = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._has_peeked:
            self._has_peeked = False
            return self._peeked_value

        return next(self._iterator)

    def peek(self, default=...):
        if not self._has_peeked:
            try:
                self._peeked_value = next(self._iterator)
                self._has_peeked = True
            except StopIteration:
                if default is ...:
                    raise
                return default

        return self._peeked_value




iterator = Peekable(iter([]))

try:
    iterator.peek()
except StopIteration:
    print('Пустой итератор')

try:
    next(iterator)
except StopIteration:
    print('Пустой итератор')

SENTINEL = object()


class Peekable:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.cache = []

    def __iter__(self):
        return self

    def __next__(self):
        self.peek()
        return self.cache.pop()

    def peek(self, default=SENTINEL):
        if not self.cache:
            try:
                self.cache.append(next(self.iterator))
            except StopIteration:
                if default is not SENTINEL:
                    return default
                raise
        return self.cache[0]