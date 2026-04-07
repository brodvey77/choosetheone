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
# class ElectricCar:
#     def __init__(self, color):
#         self.color = color
#
#     def __eq__(self, other):
#         print('Вызов метода __eq__()')
#         if isinstance(other, ElectricCar):
#             return self.color == other.color
#         return NotImplemented
#
#
# class ElectricBike:
#     def __init__(self, color):
#         self.color = color
#
#     def __eq__(self, other):
#         print('Вызов метода __eq__()')
#         if isinstance(other, ElectricBike):
#             return self.color == other.color
#         return NotImplemented
#
#
# car = ElectricCar('white')
# bike = ElectricBike('white')
#
# print(car == bike)

# num = 'str'
# id1 = id(num)
# print(id1)
#
# num += 'str'
# print(id1)
# print(num)
# id2 = id(num)
# # print(id2)
# print(id1 == id2)

# class PiggyBank:
#     def __init__(self, coins):
#         self.coins = coins
#
#     def __repr__(self):
#         return f'PiggyBank({self.coins})'
#
#     def __mul__(self, other):
#         return PiggyBank(self.coins * other)
#
#     def __imul__(self, other):
#         self.coins *= other
#
#
# bank = PiggyBank(10)
#
# bank *= 5
#
# print(bank)