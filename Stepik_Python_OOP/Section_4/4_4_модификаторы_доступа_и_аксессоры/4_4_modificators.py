# class ElectricCar:
#     def __init__(self, color):
#         self.__color = color
#
#     def get_color(self):
#         return self.__color
#
#
# car = ElectricCar('black')
#
# car._ElectricCar__color = 'yellow'
#
# print(car.__dict__)
# print(car.get_color())

#
# class Cat:
#     def __init__(self, name):
#         self._name = name
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, name):
#         if isinstance(name, str) and name.isalpha():
#             self._name = name
#         else:
#             raise ValueError('Не корректное имя')
#
#
#
# cat = Cat('Кемаль')
# print(cat.get_name())
#
# cat.set_name('dод3жер')
# print(cat.get_name())


# class Cat:
#     def __init__(self, name):
#         self._name = name
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, name):
#         if isinstance(name, str) and name.isalpha():
#             self._name = name
#         else:
#             raise ValueError('Некорректное имя')
#
#     def del_name(self):
#         del self._name
#
#
# cat = Cat('Кемаль')
#
# print(cat.get_name())
# print(Cat.__dict__)
#
# cat.del_name()
# print(cat.__dict__)
# print(cat.get_name())

