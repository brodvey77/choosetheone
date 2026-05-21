class CyclicList:
    """
    Класс, реализующий циклический список.
    Поддерживает append, pop (с циклическими индексами), len,
    бесконечную итерацию и доступ по индексу с зацикливанием.
    """

    def __init__(self, iterable=None):
        # Создаём независимую копию переданного итерируемого объекта
        if iterable is None:
            self._data = []
        else:
            self._data = list(iterable)

    def append(self, item):
        """Добавляет элемент в конец списка."""
        self._data.append(item)

    def pop(self, index=-1):
        """
        Удаляет и возвращает элемент по индексу (циклически).
        Если index не указан — удаляет последний элемент.
        """
        if not self._data:
            # В тестах пустой список не проверяется, но на всякий случай
            raise IndexError("pop from empty CyclicList")

        # Приводим индекс к реальному в пределах длины (циклически)
        real_index = index % len(self._data) if len(self._data) > 0 else 0
        return self._data.pop(real_index)

    def __len__(self):
        """Возвращает количество элементов в списке."""
        return len(self._data)

    def __getitem__(self, index):
        """
        Возвращает элемент по индексу (работает циклически).
        Поддерживаются только неотрицательные индексы (по условию).
        """
        if not self._data:
            raise IndexError("index out of range")
        real_index = index % len(self._data)
        return self._data[real_index]

    def __iter__(self):
        """
        Возвращает итератор, который бесконечно циклически обходит элементы.
        """
        while True:
            for item in self._data:
                yield item

cyclic_list = CyclicList([1, 2, 3])

for index, elem in enumerate(cyclic_list):
    if index > 6:
        break
    print(elem, end=' ')



from itertools import cycle


class CyclicList:
    def __init__(self, iterable=()):
        self._data = list(iterable) or []

    def append(self, item):
        self._data.append(item)

    def pop(self, index=None):
        if index is None:
            return self._data.pop()
        return self._data.pop(index)

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        yield from cycle(self._data)

    def __getitem__(self, index):
        return self._data[index % len(self._data)]


from itertools import cycle


class CyclicList:
    """Циклический список с поддержкой itertools.cycle."""

    def __init__(self, iterable=()):
        # Гарантированно создаём копию
        self._data = list(iterable)

    def append(self, item):
        """Добавляет элемент в конец списка."""
        self._data.append(item)

    def pop(self, index=-1):
        """
        Удаляет и возвращает элемент по индексу.
        Индекс работает циклически.
        Если индекс не передан — удаляет последний элемент.
        """
        if not self._data:
            raise IndexError("pop from empty CyclicList")

        # Циклическое приведение индекса
        real_index = index % len(self._data)
        return self._data.pop(real_index)

    def __len__(self):
        """Возвращает количество элементов в списке."""
        return len(self._data)

    def __getitem__(self, index):
        """Доступ по индексу с циклическим поведением."""
        if not self._data:
            raise IndexError("index out of range")
        return self._data[index % len(self._data)]

    def __iter__(self):
        """Бесконечная итерация по списку (используем cycle)."""
        # yield from cycle(self._data) — отличный и чистый способ
        yield from cycle(self._data)


class CyclicList:
    def __init__(self, iterable):
        self.iterable = list(iterable)

    def __getitem__(self, index):
        return self.iterable[index % len(self.iterable)]

    def __len__(self):
        return len(self.iterable)

    def append(self, value):
        self.iterable.append(value)

    def pop(self, value=-1):
        return self.iterable.pop(value)
