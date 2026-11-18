from collections import OrderedDict

class Queue:
    def __init__(self, pairs=None):
        if pairs is None:
            self._items = OrderedDict()
        else:
            self._items = OrderedDict(pairs)

    def add(self, pair):
        key, value = pair
        if key in self._items:
            del self._items[key]
        self._items[key] = value

    def pop(self):
        if not self._items:
            raise KeyError('Очередь пуста')
        key, value = self._items.popitem(last=False)
        return (key, value)

    def __len__(self):
        return len(self._items)

    def __repr__(self) -> str:
        return f'Queue({list(self._items.items())})'



queue = Queue()

try:
    queue.pop()
except KeyError as error:
    print(error)





from collections import OrderedDict


class Queue:
    def __init__(self, initial_data=None):
        self.data = OrderedDict()
        if initial_data is not None:
            self.data.update(initial_data)

    def add(self, item):
        key, value = item
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value

    def pop(self):
        try:
            return self.data.popitem(last=False)
        except KeyError as e:
            e.args = ('Очередь пуста',)
            raise

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return f'Queue({list(self.data.items())})'