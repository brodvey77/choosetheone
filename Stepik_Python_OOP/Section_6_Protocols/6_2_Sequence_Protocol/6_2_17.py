import copy


class SequenceZip:
    def __init__(self, *sequences):
        self.sequences = copy.deepcopy(sequences)

    def __len__(self):
        return min((len(s) for s in self.sequences), default=0)

    def __getitem__(self, index):
        count = -1
        for item in self:
            count += 1
            if count == index:
                return item

    def __iter__(self):
        yield from zip(*self.sequences)


class SequenceZip:
    """
    Экономичная по памяти реализация SequenceZip.
    Не материализует все данные сразу.
    """

    def __init__(self, *sequences):
        """
        Сохраняем копии последовательностей только когда это действительно нужно.
        """
        self._sequences = []

        for seq in sequences:
            # Если последовательность уже tuple или range — можно не копировать (они immutable)
            if isinstance(seq, (tuple, range)) or not hasattr(seq, '__getitem__'):
                self._sequences.append(seq)
            else:
                # Для изменяемых последовательностей (list и т.п.) делаем tuple
                # tuple занимает меньше памяти, чем list
                self._sequences.append(tuple(seq))

        # Вычисляем минимальную длину
        if not self._sequences:
            self._length = 0
        else:
            self._length = min(len(seq) for seq in self._sequences)

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("index out of range")

        # Получаем элемент из каждой последовательности по индексу
        return tuple(seq[index] for seq in self._sequences)

    def __iter__(self):
        # Ленивая итерация
        return zip(*self._sequences)


from copy import copy
from itertools import islice


class SequenceZip:
    def __init__(self, *args):
        self.iterables = tuple(map(copy, args))
        self.quantity = min(map(len, args), default=0)

    def __len__(self):
        return self.quantity

    def __iter__(self):
        return zip(*self.iterables)

    def __getitem__(self, key):
        return next(islice(iter(self), key, key + 1))