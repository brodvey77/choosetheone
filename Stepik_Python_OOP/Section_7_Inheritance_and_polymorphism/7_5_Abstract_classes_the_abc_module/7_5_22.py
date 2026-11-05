from collections.abc import Sequence


class BitArray(Sequence):
    def __init__(self, iterable=()):
        self.elements = list(iterable)

    def __getitem__(self, item):
        return self.elements[item]

    def __len__(self):
        return len(self.elements)

    def __repr__(self) -> str:
        return f'{self.elements}'

    def __invert__(self):
        return BitArray([1 - i for i in self.elements])

    def __and__(self, other):
        if not isinstance(other, BitArray):
            return NotImplemented

        if len(self) != len(other):
            return NotImplemented

        return BitArray(a & b for a, b in zip(self, other))

    def __or__(self, other):
        if not isinstance(other, BitArray):
            return NotImplemented

        if len(self) != len(other):
            return NotImplemented

        return BitArray(a | b for a, b in zip(self, other))







bitarray = BitArray([1, 0, 1, 1])
print(bitarray.__or__(1))
print(bitarray.__and__(1.1))



