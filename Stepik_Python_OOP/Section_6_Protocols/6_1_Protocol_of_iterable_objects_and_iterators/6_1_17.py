
class AttrsIterator:
    def __init__(self, obj):
        self.obj = obj
        self.lst = [(k,v) for k,v in self.obj.__dict__.items()]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        # print(self.lst)
        if self.index > len(self.lst):
            raise StopIteration
        return self.lst[self.index - 1]


class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class Kish:
    def __init__(self, song, year):
        self.song = song
        self.year = year


forester = Kish('лесник', 1997)
attrs_iterator = AttrsIterator(forester)

next(attrs_iterator)
next(attrs_iterator)

try:
    next(attrs_iterator)
except StopIteration:
    print('Атрибуты закончились')


class AttrsIterator:
    def __init__(self, obj):
        self._obj = list(obj.__dict__.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self._obj):
            raise StopIteration
        return self._obj[self.index]



class AttrsIterator:
    def __new__(cls, obj):
        return iter(obj.__dict__.items())




class AttrsIterator:
    def __init__(self, obj):
        self.attrs = ((k, v) for k, v in obj.__dict__.items())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.attrs)

