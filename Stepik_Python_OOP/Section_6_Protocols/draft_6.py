# class ForgivingIndexer:
#     def __init__(self, sequence):
#         self.sequence = sequence
#
#     def __getitem__(self, index):
#         return self.sequence[int(index)]
#
#     def __len__(self):
#         return len(self.sequence)
#
#
# words = ForgivingIndexer(['beegeek', 'pygen', 'stepik', 'python'])
#
# print(len(words[1.9]))


# class PositiveNumber:
#     def __set_name__(self, cls, attr):
#         self._attr = attr
#
#     def __get__(self, obj, cls):
#         print('Вызов метода __get__()')
#         return obj.__dict__[self._attr]
#
# class Cat:
#     age = PositiveNumber()
#
#     def __init__(self, age):
#         self.age = age
#
#
# cat = Cat(1)
#
# print(cat.age)

# class PositiveNumber:
#     def __set_name__(self, cls, attr):
#         self._attr = attr
#
#     def __get__(self, obj, cls):
#         print('Вызов метода __get__()')
#         return obj.__dict__[self._attr]
#
# class Cat:
#     age = PositiveNumber()
#
#     def __init__(self, age):
#         self.age = age
#
#
# cat = Cat(1)
#
# print(cat.age)

class PositiveNumber:
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        return getattr(obj, self._attr)

    def __set__(self, obj, value):
        if type(value) in (int, float) and value > 0:
            setattr(obj, self._attr, value)
        else:
            raise ValueError('Некорректное значение')

class Cat:
    age = PositiveNumber()

    def __init__(self, age):
        self.age = age


cat = Cat(1)

print(cat.age)