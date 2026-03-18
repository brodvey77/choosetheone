# class MyClass:
#     def __new__(cls, *args, **kwargs):
#         instance = object.__new__(cls)
#         return instance
#
#
# obj = MyClass()
#
# print(obj)
# print(type(obj))

# class Cat:
#     def __new__(cls, *args, **kwargs):
#         print('1. Создание экземпляра класса Cat')
#         instance = object.__new__(cls)
#         return instance
#
#     def __init__(self, name):
#         print('2. Инициализация созданного экземпляра класса Cat')
#         self.name = name
#
#
# cat = Cat('Кемаль')
#
# print(type(cat))
# print(cat.name)


# class ElectricCar:
#     def __new__(cls, *args, **kwargs):
#         return object.__new__(cls)
#
#     def __init__(self, color):
#         self.color = color
#         return self
#
#
# car = ElectricCar('yellow')
#
# print(car.color)

# class ElectricCar:
#     def __init__(self, color):
#         self.color = color
#
#     def __str__(self):
#         return f'ElectricCar >> color: {self.color}'
#
#
# car = ElectricCar('black')
#
# print(car)
# print(str(car))


# class ElectricCar:
#     def __init__(self, color):
#         self.color = color
#
#     def __str__(self):
#         return None
#
#
# car = ElectricCar('black')
#
# print(str(car))

# class ElectricCar:
#     def __init__(self, color):
#         self.color = color
#
#     def __str__(self):
#         return f'ElectricCar >> color: {self.color}'
#
#     def __repr__(self):
#         return f'{self.color}'
#
#
# car = ElectricCar('black')
#
# print(str(car))
# print(repr(car))

# class ElectricCar:
#     def __init__(self, color):
#         self.color = color
#
#     def __str__(self):
#         return f'ElectricCar >> color: {self.color}'
#
#
# car = ElectricCar('black')
#
# print(repr(car) == str(car))