from collections.abc import *

class SortedList(Sequence):
    def __init__(self, iterable):
        self.elements = iterable

    def __len__(self):
        return len(self.elements)

    def __getitem__(self, index):
        return self.elements[index]


numbers = SortedList([5, 3, 4, 2, 1])


print(numbers)
print(numbers[1])
print(numbers[-2])
# numbers.add(0)
# print(numbers)
# numbers.discard(4)
# print(numbers)
# numbers.update([4, 6])
# print(numbers)