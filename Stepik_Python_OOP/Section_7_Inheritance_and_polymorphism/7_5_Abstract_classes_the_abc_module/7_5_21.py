from collections.abc import Sequence


class CustomRange(Sequence):
    def __init__(self, *args):
        lst = []
        for value in args:
            if isinstance(value, str):
                l = value.split('-')
                lst.extend(range(int(l[0]), int(l[-1]) + 1))
            else:
                lst.append(value)
        self.elements = lst


    def __getitem__(self, item):
        return self.elements[item]


    def __len__(self):
        return len(self.elements)




customrange = CustomRange(1, '2-5', 5, '6-8')

print(customrange[0])
print(customrange[1])
print(customrange[2])
print(customrange[-1])
print(customrange[-2])
print(customrange[-3])



from collections.abc import Sequence


class CustomRange(Sequence):
    def __init__(self, *args):
        self._data = []
        for arg in args:
            start, stop = (arg, arg) if isinstance(arg, int) else map(int, arg.split('-'))
            self._data.extend(range(start, stop + 1))

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self._data[item]
        return NotImplemented

    def __len__(self):
        return len(self._data)



class CustomRange(list):
    def __init__(self, *args):
        # super().__init__()
        for i in args:
            if isinstance(i, int):
                self.append(i)
            elif isinstance(i, str):
                a, b = i.split("-")
                self.extend(range(int(a), int(b) + 1))
