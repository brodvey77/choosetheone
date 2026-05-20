
class CyclicList:
    def __init__(self, iterable):
        self._iterable = list(iterable)

    def append(self, obj):
        self._iterable.append(obj)


    def pop(self, ind):
        if ind >= 0:
            self._iterable.pop(ind)
        else:
            self._iterable.pop(-1)

    def __len__(self):
        return len(self._iterable)

    def __getitem__(self, index):
        return self._iterable[index]



cyclic_list = CyclicList([1, 2, 3])

cyclic_list.append(4)
print(cyclic_list.pop())
print(len(cyclic_list))
print(cyclic_list.pop(0))
print(len(cyclic_list))
