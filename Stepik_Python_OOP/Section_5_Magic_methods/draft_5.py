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

# class Adder:
#     def __init__(self, value):
#         self.value = value
#
#
# add_ten = Adder(10)
#
# print(add_ten(11))



# class ElectricCar:
#     def __init__(self, power_reserve):
#         self.power_reserve = power_reserve
#
#     def __int__(self):
#         return int(self.power_reserve)
#
#     def __float__(self):
#         return float(self.power_reserve)
#
#
# car = ElectricCar(330.8)
#
# print(int(car))
# print(float(car))

# print(hash(-1) == hash(-2))                          # хеш-значение целого числа
# print(hash(2.5))                        # хеш-значение вещественного числа
# print(hash('bee'))                      # хеш-значение строки
# print(hash((1, 2, 3)))                  # хеш-значение кортежа
#
# print(hash('beegeek'))
# print(hash('beegeek'))
# print(hash('beegeek!'))
# print(hash('beek'))
# print(hash('geek'))
# import sys
#
# print(sys.hash_info)
#
# print(hash('beegeek'))
#
# from fractions import Fraction
#
# num1 = 0.5
# num2 = Fraction(1, 2)
#
# print(num1 == num2)
# print(hash(num1) == hash(num2))
#
# hashes = set()
#
# for _ in range(100):
#     hashes.add(hash('beegeek'))
#
# print(len(hashes))
#
#
# def hash_function(obj):
#     return hash(obj) % 1000
#
# data = [2077, 3.14, 'beaeeee', 'geek', (1, 2, 3)]
#
# for obj in data:
#     print(hash_function(obj))
#
#
#
# from time import perf_counter
#
# start = perf_counter()
#
# hash('b' * 100_000_000)
#
# end = perf_counter()
# print(end - start)                      # результат в секундах
#
#
#
# from collections import defaultdict
# from string import printable
#
# hashes = defaultdict(int)
#
# for char in printable:
#     hashes[hash(char) % 20] += 1
#
# for hash_value, hash_count in sorted(hashes.items()):
#     print(hash_value, '■' * hash_count)
#



# def hash_function(obj):
#     return sum(ord(character) for character in obj)

# def hash_function(obj):
#     return sum(ord(character) for character in str(obj))

# def hash_function(obj):
#     return sum(index * ord(character) for index, character in enumerate(str(obj), start=1))


# def hash_function(obj):
#     return sum(index * ord(character) for index, character in enumerate(str(obj), start=1)) % 123456761
#
#
# print(hash_function('Python'))
# print(hash_function(123))
# print(hash_function(12.34))
# print(hash_function(None))
# print(hash_function(True))
# print(hash_function('Python'))
# print(hash_function('Beegeek'*1000))
# print(hash_function('Stepik'*10000000))

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#
# cat1 = Cat('Кемаль')
# print(hash(cat1))
# cat2 = Cat('Кемаль')
# print(hash(cat2))
#
# print(cat1 == cat2)
# print(hash(cat1) == hash(cat2))


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __eq__(self, other):
#         if isinstance(other, Cat):
#             return self.name == other.name
#         return NotImplemented
#
#
# cat1 = Cat('Кемаль')
# cat2 = Cat('Кемаль')
#
# print(cat1 == cat2)
#
# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __eq__(self, other):
#         if isinstance(other, Cat):
#             return self.name == other.name
#         return NotImplemented
#
#     def __hash__(self):
#         return hash(self.name)
#
#
#
# cat1 = Cat('Кемаль')
# cat2 = Cat('Кемаль')
#
# print(cat1 == cat2)
# print(hash(cat1) == hash(cat2))

