from collections.abc import MutableSequence
import bisect


class SortedList(MutableSequence):
    def __init__(self, iterable=None):
        # Примечание 3: создаем независимую копию данных
        if iterable is None:
            self._data = []
        else:
            self._data = sorted(list(iterable))

    # --- Реализация абстрактных методов MutableSequence ---

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        # Изменение по индексу запрещено, так как это нарушит сортировку
        raise NotImplementedError

    def __delitem__(self, index):
        del self._data[index]

    def __len__(self):
        return len(self._data)

    def insert(self, *args, **kwargs):
        # Метод insert отключен согласно условию
        raise NotImplementedError

    # --- Собственные методы класса ---

    def add(self, item):
        # bisect.insort находит место и вставляет элемент, сохраняя сортировку
        bisect.insort(self._data, item)

    def discard(self, item):
        # Находим диапазон всех вхождений элемента с помощью бинарного поиска
        left = bisect.bisect_left(self._data, item)
        right = bisect.bisect_right(self._data, item)
        # Удаляем срезом (если элемента нет, left == right и ничего не удалится)
        del self._data[left:right]

    def update(self, iterable):
        # Добавляем элементы и пересортировываем список
        # Алгоритм Timsort в Python отлично работает с частично отсортированными данными
        self._data.extend(iterable)
        self._data.sort()

    # --- Отключение стандартных методов списка ---

    def append(self, *args, **kwargs):
        raise NotImplementedError

    def extend(self, *args, **kwargs):
        raise NotImplementedError

    def reverse(self, *args, **kwargs):
        raise NotImplementedError

    def __reversed__(self):
        raise NotImplementedError

    # --- Магические методы для отображения и итерации ---

    def __repr__(self):
        return f"SortedList({self._data!r})"

    def __contains__(self, item):
        # Оптимизированный поиск за O(log N) вместо O(N)
        i = bisect.bisect_left(self._data, item)
        return i != len(self._data) and self._data[i] == item

    # --- Арифметические операции ---

    def __add__(self, other):
        if not isinstance(other, SortedList):
            return NotImplemented
        return SortedList(self._data + other._data)

    def __iadd__(self, other):
        if not isinstance(other, SortedList):
            return NotImplemented
        self._data.extend(other._data)
        self._data.sort()
        return self

    def __mul__(self, n):
        if not isinstance(n, int):
            return NotImplemented
        return SortedList(self._data * n)

    def __imul__(self, n):
        if not isinstance(n, int):
            return NotImplemented
        self._data *= n
        self._data.sort()
        return self





from bisect import bisect_left, bisect_right, insort
from collections.abc import MutableSequence


class SortedList(MutableSequence):
    def __init__(self, iterable=()):
        self._data = sorted(iterable)

    def add(self, obj):
        insort(self._data, obj)

    def discard(self, obj):
        left = bisect_left(self._data, obj)
        right = bisect_right(self._data, obj)
        self._data[left:right] = []

    def update(self, iterable):
        for it in iterable:
            self.add(it)

    def __getitem__(self, index):
        return self._data[index]

    def __delitem__(self, index):
        del self._data[index]

    def __len__(self):
        return len(self._data)

    def __contains__(self, item):
        return item in self._data

    def __iter__(self):
        yield from self._data

    def __add__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self._data + other._data)
        return NotImplemented

    def __iadd__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        self.update(other._data)
        return self

    def __mul__(self, other):
        if isinstance(other, int):
            return type(self)(self._data * other)
        return NotImplemented

    def __imul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        self._data.clear() if other <= 0 else self.update(self._data * (other - 1))
        return self

    def __repr__(self):
        return f'SortedList({self._data})'

    def append(self, value):
        raise NotImplementedError

    def insert(self, index, value):
        raise NotImplementedError

    def extend(self, values):
        raise NotImplementedError

    def reverse(self):
        raise NotImplementedError

    def __reversed__(self):
        raise NotImplementedError

    def __setitem__(self, key, value):
        raise NotImplementedError