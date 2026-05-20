from pandas._libs import index


class SparseArray:
    def __init__(self, default):
        self.default = default
        self.d = {}

    def __getitem__(self, index):
        return self.d.get(index, self.default)

    def __setitem__(self, key, value):
        self.d[key] = value


array = SparseArray('Тут ничего нет')

array[1000] = 1000
print(array[999])
print(array[1000])


class SparseArray:
    def __init__(self, default):
        self._sequence = []
        self._default = default

    def __len__(self):
        return len(self._sequence)

    def __setitem__(self, key, value):
        if len(self) <= key:
            self._sequence += [self._default] * (key + 10)
        self._sequence[key] = value

    def __getitem__(self, key):
        if len(self) <= key:
            return self._default
        return self._sequence[key]


