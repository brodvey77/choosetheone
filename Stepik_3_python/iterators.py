# sentence = 'In the face of ambiguity refuse the temptation to guess'
#
# filter_iterator = filter(lambda word: len(word) > 4, sentence.split())   # фильтруем
# map_iterator = map(lambda word: word.upper(), filter_iterator)           # преобразовываем
# enumerate_iterator = enumerate(map_iterator, 1)                          # нумеруем
#
# for index, value in enumerate_iterator:                                  # выводим
# #     print(f'{index}. {value}')
# for i in enumerate('beegeek'):
#     print(i)
#
# for i in [1, 2, 3, 4, 5]:
#     print(i)
#
# for i in 'beegeek':
#     print(i)
#
# for i in range(10):
#     print(i)
#
# for i in map(str.upper, 'beegeek'):
#     print(i)
#
#
#
# for i in (1, 2, 3, 4, 5):
#     print(i)
#
# for i in filter(None, '11010111'):
#     print(i)
#
#
# for i in {'bee': 1, 'geek': 2}:
#     print(i)
#
#
# for i in {1, 2, 3, 4, 5}:
#     print(i)
#
#
# for i in zip('bee', 'geek'):
#     print(i)


# print(next(enumerate('beegeek')))
#
# # print(next([1, 2, 3, 4, 5]))
# # print(next('beegeek'))
# print(next(range(10)))
# print(next(map(str.upper, 'beegeek')))
# # print(next((1, 2, 3, 4, 5)))
# print(next(filter(None, '11010111')))
# # print(next({'bee': 1, 'geek': 2})
# # print(next({1, 2, 3, 4, 5}))
# print(next(zip('bee', 'geek')))

# from sys import getsizeof
#
# numbers1 = range(10)
# numbers2 = range(10000000)
#
# size1 = getsizeof(numbers1)
# size2 = getsizeof(numbers2)
#
# print(size1 == size2)


# numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64, -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88, -11, 16, -22]
#
# a = iter(numbers)
#
# for i in range(3):
#     next(a)
#
#
# print(next(a))

# numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64, -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88, -11, 16, -22]
#
# a = iter(numbers[::-1])
# print(next(a))
# print(next(a))
# print(next(iter(reversed(numbers))))
#
#
# numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64, -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88, -11, 16, -22]
# numbers = iter(numbers)
# while True:
#     try:
#         n = next(numbers)
#     except StopIteration:
#         print(n)
#         break


numbers = [-3, 6, 1, -90, 34, -25, 23, -21]

# positive_numbers = map(abs, numbers)     # создаем объект итератора
#
# for num in positive_numbers:             # обходим итератор циклом for
#     print(num)
#
# for num in positive_numbers:             # обходим пустой итератор, тело цикла выполнено не будет
#     print(num)

# for i in numbers:
#     print(i)
#
#
# for i in numbers:
#     print(i)


# non_zero = filter(None, [-2, -1, 0, 1, 2])
# positive = map(abs, non_zero)
#
# print(list(non_zero))
# print(list(positive))
#
# non_zero = filter(None, [-2, -1, 0, 1, 2])
# positive = map(abs, non_zero)
#
# print(list(positive))
# print(list(non_zero))

# numbers = [1, 3, 2, 5, 4]
# pairs = {'bee': 1, 'geek': 2}
# letters = 'beegeek'
#
# print(type(sorted(numbers)))
# print(sorted(pairs.items()))
# print(sorted(letters))

# numbers = iter([1, 2, 3, 4, 5])
#
# print(max(numbers) + min(numbers))
# positive = (1, 2, 3)
# negative = map(lambda x: -x, iter(positive))
#
#
#
# for a, b in zip(positive, negative):
#     print(a + b)

# import itertools
#
# def filterfalse(predicate, iterable):
#     return itertools.filterfalse(predicate, iterable)

# def filterfalse(func, iterable):
#     if func is None:
#         func = bool
#     return filter(lambda elem: not func(elem), iterable)

# def filterfalse(predicate, iterable):
#     if predicate is None:
#         predicate = bool
#     return filter(lambda x: not predicate(x), iterable)
#
# # INPUT DATA:
#
# # TEST_1:
# objects = [0, 1, True, False, 17, []]
#
# print(*filterfalse(None, objects))
#
# # TEST_2:
# numbers = (1, 2, 3, 4, 5)
#
# print(*filterfalse(lambda x: x % 2 == 0, numbers))
#
# # TEST_3:
# numbers = [1, 2, 3, 4, 5]
#
# print(*filterfalse(lambda x: x >= 3, numbers))
#
# # TEST_4:
# numbers = range(1, 150, 8)
# result = filterfalse(lambda num: num % 8 == 3, numbers)
# print(*result)
#
# # TEST_5:
# import string
# letters = string.ascii_letters
# result = filterfalse(lambda char: ord(char) > 75, letters)
# print(*result, sep=',')
#
# # TEST_6:
# objects = [0, 0, 0, True, False, 1788, [], {}, set(), (), '', 0.0, None, 'stepik', dict()]
#
# print(*filterfalse(None, objects))


# def transpose(matrix):
#     return [list(item) for item in zip(*matrix)]
#
# transpose = lambda matrix: list(map(list, zip(*matrix)))
#
# # INPUT DATA:
#
# # TEST_1:
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# for row in transpose(matrix):
#     print(row)
#
# # TEST_2:
# matrix = [[1, 2, 3, 4, 5],
#           [6, 7, 8, 9, 10]]
#
# for row in transpose(matrix):
#     print(row)
#
# # TEST_3:
# matrix = [[1, 2, 3, 4, 5]]
#
# for row in transpose(matrix):
#     print(row)
#
# # TEST_4:
# matrix = [[69]]
#
# for row in transpose(matrix):
#     print(row)
#
# # TEST_5:
# matrix = [['1', '2', '3'],
#           ['4', '5', '6'],
#           ['7', '8', '9']]
#
# print(*transpose(matrix))
#
# # TEST_6:
# matrix = [['1', '2'],
#           ['4', '5'],
#           ['7', '8'],
#           ['3', 4],
#           [True, None],
#           [9, 80],
# #           [1, -1]]
# #
# # print(transpose(matrix))
#
# def get_min_max(data: list) -> tuple[int, int] | None:
#     if len(data) > 0:
#         return (data.index(min(data)), data.index(max(data)))
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# data = [2, 3, 8, 1, 7]
#
# print(get_min_max(data))
#
# # TEST_2:
# data = [1, 1, 2, 3, 8, 8]
#
# print(get_min_max(data))
#
# # TEST_3:
# data = [9]
#
# print(get_min_max(data))
#
# # TEST_4:
# data = []
#
# print(get_min_max(data))
#
# # TEST_5:
# data = [9, 9, 9, 9, 9]
#
# print(get_min_max(data))
#
# # TEST_6:
# data = list(range(1, 101))
#
# print(get_min_max(data))
#
# # TEST_7:
# data = list(range(1, 101))[::-1]
#
# print(get_min_max(data))
#
# # TEST_8:
# data = [-86, -51, 33, -23, 40, 96, 19, -65, 26, 12, -93, 68, 82, 47, -58, -37, -100, 5, 75, 54, -79, -72, -2, 61, -16, -9, 89, -44, -30]
#
# print(get_min_max(data))
#
# # TEST_9:
# data = [-86, -51, 33, -23, 40, 96, 19, -65, 26, 12, -93, 68, 82, 47, -58, -37, -100, 5, 75, 54, -79, -72, -2, 61, -16, -9, 89, -44, -30, -100, 96, -100, 1, 2, -99, 96]
#
# print(get_min_max(data))


# def starmap(func, iterable):
#     return map(func, *zip(*iterable))


# def starmap(func, iterable):
#     return map(lambda x: func(*x), iterable)
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# pairs = [(1, 3), (2, 5), (6, 4)]
#
# print(*starmap(lambda a, b: a + b, pairs))
#
# # TEST_2:
# points = [(1, 1, 1), (1, 1, 2), (2, 2, 3)]
#
# print(*starmap(lambda x, y, z: x * y * z, points))
#
# # TEST_3:
# points = [(1, 1, 1, 0), (1, 1, 2, 0), (2, 2, 3, 10)]
#
# print(*starmap(lambda x, y, z, t: x + y + z + t, points))
#
# # TEST_4:
# points = [[10], [-9], [2]]
#
# print(*starmap(lambda x: x ** 2, points))
#
# # TEST_5:
# points = [(1, 1, 1, 0, 90),
#           (1, 1, 2, 0, 67),
#           (2, 2, 3, 10, -56),
#           (5, 21, 3, 10, -56),
#           (6, 24, 35, 100, 36),
#           (8, 34, 3, 10, 56)]
#
# print(*starmap(lambda x, y, z, t, w: x + y * z + t + w ** 6, points))

# def get_min_max(iterable):
#     a = sorted(iterable)
#     if a:
#         return (a[0], a[-1])

import copy

# def get_min_max(iterable):
#     iterable_2 = iterable.deepcopy()
#

# def get_min_max(iterable):
#     try:
#         iterator = iter(iterable)
#         first = next(iterator)
#         min_val = max_val = first
#
#         for item in iterator:
#             if item < min_val:
#                 min_val = item
#             if item > max_val:
#                 max_val = item
#
#         return (min_val, max_val)
#     except StopIteration:
#         return None
#
#     import copy
#
#     def get_min_max(iterable):
#         try:
#             C = copy.deepcopy(iterable)
#             return (min(C), max(iterable))
#         except:
#             return None
#
#
# # def get_min_max(iterable):
# #     if iterable:
# #         min_pair = min(enumerate(iterable), key=lambda pair: pair[1])
# #         max_pair = max(enumerate(iterable), key=lambda pair: pair[1])
# #         return min_pair[0], max_pair[0]
#
#
# # INPUT DATA:
#
# # TEST_1:
# iterable = iter(range(10))
#
# print(get_min_max(iterable))
#
# # TEST_2:
# iterable = [6, 4, 2, 33, 19, 1]
#
# print(get_min_max(iterable))
#
# # TEST_3:
# iterable = iter([])
#
# print(get_min_max(iterable))
#
# # TEST_4:
# data = iter((9, 9, 9, 9, 9))
#
# print(get_min_max(data))
#
# # TEST_5:
# data = iter(range(1, 101))
#
# print(get_min_max(data))
#
# # TEST_6:
# data = list(range(1, 101))[::-1]
#
# print(get_min_max(data))
#
# # TEST_7:
# data = iter([-86, -51, 33, -23, 40, 96, 19, -65, 26, 12, -93, 68, 82, 47, -58, -37, -100, 5, 75, 54, -79, -72, -2, 61, -16, -9, 89, -44, -30])
#
# print(get_min_max(data))
#
# # TEST_8:
# data = iter([-86, -51, 33, -23, 40, 96, 19, -65, 26, 12, -93, 68, 82, 47, -58, -37, -100, 5, 75, 54, -79, -72, -2, 61, -16, -9, 89, -44, -30, -100, 96, -100, 1, 2, -99, 96])
#
# print(get_min_max(data))
#
# # TEST_9:
# iterable = []
#
# print(get_min_max(iterable))
#
# # TEST_10:
# iterable = [69]
#
# print(get_min_max(iterable))
#
# # TEST_11:
# data = iter(range(100_000_000))
#
# print(get_min_max(data))
#
# # TEST_12:
# data = iter(['a', 'b', 'c', 'aaa', 'abc', 'cbc', 'bbb'])
#
# print(get_min_max(data))
#
# # TEST_13:
# data = iter(['bbb'])
#
# print(get_min_max(data))



# zero_iterator = iter(int, -1)
#
# for i in range(10):
#     print(next(zero_iterator))
#
# print(type(zero_iterator))


# from random import choice
#
# def test_iter():
#     values = list(range(1, 11))
#     return choice(values)
#
# random_iterator = iter(test_iter, 2)
#
# for num in random_iterator:
#     print(num)

# print(int())


# numbers = [1, 2, 3, 4, 5]
#
# if 'pop' in dir(numbers):
#     numbers.pop()
#
# print(numbers)

# beegeek = 'beegeek'
# iterator = iter(beegeek)
#
# print(beegeek == iterator)
# print(iterator == iter(iterator))


# iterator = iter(int, 1)

# infinite_love = iter(lambda: 'i love beegeek!', 1)
#
#
# # print(next(infinite_love))
#
#
# print(next(infinite_love))
# print(next(infinite_love))
# print(next(infinite_love))
#
# def is_iterable(obj) -> bool:
#     try:
#         iter(obj)
#         return True
#     except:
#         return False
#
#
# def is_iterable(obj):
#     return '__iter__' in dir(obj)
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# print(is_iterable(18731))
#
# # TEST_2:
# print(is_iterable('18731'))
#
# # TEST_3:
# objects = [(1, 13), 7.0004, [1, 2, 3]]
#
# for obj in objects:
#     print(is_iterable(obj))
#
# # TEST_4:
# for element in [34, [4, 5], (4, 5), {"a":4}, "dfsdf", 4.5]:
#     print(element, 'iterable: ', is_iterable(element))


# def is_iterator(obj):
#     try:
#         if iter(obj) == obj:
#             return True
#         else:
#             return False
#     except:
#         return False

# def is_iterator(obj):
#     return hasattr(obj, '__next__')
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# print(is_iterator([1, 2, 3, 4, 5]))
#
# # TEST_2:
# beegeek = map(str.upper, 'beegeek')
#
# print(is_iterator(beegeek))
#
# # TEST_3:
# beegeek = filter(None, [0, 0, 1, 1, 0, 1])
#
# print(is_iterator(beegeek))
#
# # TEST_4:
# beegeek = zip([1, 2, 3], [3, 4, 5])
#
# print(is_iterator(beegeek))
#
# # TEST_5:
# beegeek = enumerate('beegeek', start=1)
#
# print(is_iterator(beegeek))
#
# # TEST_6:
# beegeek = 'beegeek'
#
# print(is_iterator(beegeek))
#
# # TEST_7:
# beegeek = 199999111199991919191
#
# print(is_iterator(beegeek))
#
# # TEST_8:
# beegeek = iter('199999111199991919191')
#
# print(is_iterator(beegeek))

# from random import choice
#
# def test_iter():
#     values = list(range(1, 11))
#     return choice(values)
#
# random_iterator = iter(test_iter, 2)
#
# for num in random_iterator:
#     print(num)


# from random import choice
# def random_numbers(left: int, right: int):
#     values = list(range(left, right + 1))
#     return iter(lambda: choice(values), -1)
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# iterator = random_numbers(1, 1)
#
# print(next(iterator))
# print(next(iterator))
#
# # TEST_2:
# iterator = random_numbers(1, 10)
#
# print(next(iterator) in range(1, 11))
# print(next(iterator) in range(1, 11))
# print(next(iterator) in range(1, 11))
#
# # TEST_3:
# iterator = random_numbers(-100, -92)
#
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
#
# # TEST_4:
# iterator = random_numbers(5, 5)
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
# # TEST_5:
# iterator = random_numbers(1000, 1001)
#
# print(next(iterator) in range(1000, 1002))
# print(next(iterator) in range(1000, 1002))
# print(next(iterator) in range(1000, 1002))
# print(next(iterator) in range(1000, 1002))
# print(next(iterator) in range(1000, 1002))
# print(next(iterator) in range(1000, 1002))
# print(next(iterator) in range(1000, 1002))
# print(next(iterator) in range(1000, 1002))
# print(next(iterator) in range(1000, 1002))
# print(next(iterator) in range(1000, 1002))
#
# # TEST_6:
# iterator = random_numbers(-100, 99)
#
# print(next(iterator) in range(-100, 100))
# print(next(iterator) in range(-100, 100))
# print(next(iterator) in range(-100, 100))
# print(next(iterator) in range(-100, 100))
# print(next(iterator) in range(-100, 100))
# print(next(iterator) in range(-100, 100))
# print(next(iterator) in range(-100, 100))



# numbers = [1, 2, 3, 4, 5]
#
# iterator = iter(numbers)
#
# next(iterator)
# next(iterator)
#
# del numbers[0]
# del numbers[1]
#
# print(next(iterator))


# numbers = [1, 2, 3, 4, 5]
#
# for i in numbers:
#     del numbers[0]
#     print(i)

# class Repeater:
#     def __init__(self, obj):  # конструктор принимает obj (помимо self)
#         self.obj = obj
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return self.obj


# class BoundedRepeater:
#     def __init__(self, obj, times):
#         self.obj = obj
#         self.times = times
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.index += 1
#         if self.times < self.index:
#             raise StopIteration
#         return self.obj
#
#
# class BoundedRepeater:
#     def __init__(self, obj, times):
#         self.obj = obj
#         self.times = times
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.times == 0:
#             raise StopIteration
#         self.times -= 1
#         return self.obj
#
#
# # INPUT DATA:
#
# # TEST_1:
# bee = BoundedRepeater('bee', 2)
#
# print(next(bee))
# print(next(bee))
#
# # TEST_2:
# geek = BoundedRepeater('geek', 3)
#
# print(next(geek))
# print(next(geek))
# print(next(geek))
#
# try:
#     print(next(geek))
# except StopIteration:
#     print('Error')
#
# # TEST_3:
# repeater = BoundedRepeater(['bee', 'geek'], 10)
#
# for _ in range(9):
#     next(repeater)
#
# print(next(repeater))
#
# try:
#     next(repeater)
# except StopIteration:
#     print('Error')
#
# # TEST_4:
# repeater = BoundedRepeater(9999, 1)
#
# try:
#     print(next(repeater))
#     print(next(repeater))
# except StopIteration:
#     print('Error')
#
# # TEST_5:
# repeater = BoundedRepeater((1, 2, 3, 4), 15)
#
# for _ in range(10):
#     next(repeater)
#
# next(repeater)
# next(repeater)
# next(repeater)
# next(repeater)
# next(repeater)
#
# try:
#     print(next(repeater))
# except StopIteration:
#     print('Error')
#
# # TEST_6:
# repeater = BoundedRepeater({'bee': 'geek'}, 55)
#
# for elem in repeater:
#     print(elem)
#
# # TEST_7:
# repeater = BoundedRepeater(1, 10)
#
# print(list(repeater))

# class Square:
#     def __init__(self, n):
#         self.n = n
#         self.index = 0
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.index += 1
#         if self.n < self.index:
#             raise StopIteration
#         return self.index**2
#
#
#
#
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# squares = Square(2)
#
# print(next(squares))
# print(next(squares))
#
# # TEST_2:
# squares = Square(10)
#
# print(list(squares))
#
# # TEST_3:
# squares = Square(1)
#
# print(list(squares))
#
# # TEST_4:
# squares = Square(5)
#
# next(squares)
# next(squares)
# next(squares)
# next(squares)
# next(squares)
#
# try:
#     next(squares)
# except StopIteration:
#     print('Error')
#
# # TEST_5:
# squares = Square(9)
#
# print(*squares)
#
# # TEST_6:
# squares = Square(2)
#
# try:
#     print(next(squares))
#     print(next(squares))
#     print(next(squares))
# except:
#     print('Error')




# @lru_cache()
# def fibonacci(n):
#     if n <= 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

#
# from functools import lru_cache
# class Fibonacci:
#     def __init__(self):
#         self.n = 0
#
#     def __iter__(self):
#         return self
#
#     @lru_cache()
#     def fibonacci(self, n):
#         if n <= 2:
#             return 1
#         else:
#             return self.fibonacci(n - 1) + self.fibonacci(n - 2)
#
#
#     def __next__(self):
#         result = self.fibonacci(self.n)
#         self.n += 1
#         return result
#
#
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# fibonacci = Fibonacci()
#
# print(next(fibonacci))
#
# # TEST_2:
# fibonacci = Fibonacci()
#
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
#
# # TEST_3:
# fibonacci = Fibonacci()
#
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
#
# # TEST_4:
# fibonacci = Fibonacci()
#
# for _ in range(50):
#     print(next(fibonacci))
#
# # TEST_5:
# fibonacci = Fibonacci()
#
# for _ in range(100):
#     next(fibonacci)
#
# print(next(fibonacci))
#
# # TEST_6:
# fibonacci = Fibonacci()
#
# for _ in range(76):
#     next(fibonacci)
#
# next(fibonacci)
# next(fibonacci)
# next(fibonacci)
# next(fibonacci)
#
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))

# class PowerOf:
#     def __init__(self, number):
#         self.number = number
#         self.index = 0
#
#
#     def __iter__(self):
#         return self
#
#
#     def __next__(self):
#         result = self.number ** self.index
#         self.index += 1
#         return result
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# power_of_two = PowerOf(2)
#
# print(next(power_of_two))
# print(next(power_of_two))
# print(next(power_of_two))
# print(next(power_of_two))
#
# # TEST_2:
# power_of_two = PowerOf(1)
#
# for _ in range(55):
#     print(next(power_of_two))
#
# # TEST_3:
# power_of_two = PowerOf(3)
#
# for _ in range(10):
#     print(next(power_of_two))
#
# # TEST_4:
# power_of_two = PowerOf(11)
#
# for _ in range(11):
#     print(next(power_of_two))
#
# # TEST_5:
# power_of_two = PowerOf(100)
#
# for _ in range(20):
#     next(power_of_two)
#
# print(next(power_of_two))

# class DictItemsIterator:
#     def __init__(self, data):
#         self._data = data
#         self._keys = list(data)
#         self._index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self._index < len(self._keys):
#             key = self._keys[self._index]
#             value = self._data[key]
#             self._index += 1
#             return (key, value)
#         else:
#             raise StopIteration
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})
#
# print(*pairs)
#
# # TEST_2:
# data = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
#
# pairs = DictItemsIterator(data)
#
# print(*pairs)
#
# # TEST_3:
# data = {'Arthur': 100, 'Timur': 100, 'Dima': 100,
#         'Anri': 101, 'Roma': 99, 'German': 98}
#
# pairs = DictItemsIterator(data)
#
# print(list(pairs))
#
# # TEST_4:
# data = {'Arthur': [100, 5], 'Timur': [100, 6], 'Dima': [100, 7, 8],
#         'Anri': [100, 101], 'Roma': [99]}
#
# pairs = DictItemsIterator(data)
#
# print(next(pairs))
# print(next(pairs))
# print(next(pairs))
# print(next(pairs))
# print(next(pairs))
#
# try:
#     print(next(pairs))
# except StopIteration:
#     print('Error')
#
# # TEST_5:
# data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
#
# pairs = DictItemsIterator(data)
#
# print(tuple(pairs))
#
# try:
#     print(next(pairs))
# except StopIteration:
#     print('Error')


# class CardDeck:
#     def __init__(self):
#         self.suits = ['пик', 'треф', 'бубен', 'червей']
#         self.ranks = [
#             2, 3, 4, 5, 6,
#             7, 8, 9, 10, 'валет',
#             'дама', 'король', 'туз'
#         ]
#         self._index = 0  # Индекс для отслеживания текущей карты
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self._index < 52:
#             rank = self.ranks[self._index % 13]
#             suit = self.suits[self._index // 13]
#             self._index += 1
#             return f"{rank} {suit}"
#         else:
#             raise StopIteration
#
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# cards = CardDeck()
#
# print(next(cards))
# print(next(cards))

# TEST_2:
# cards = list(CardDeck())
#
# print(cards[9])
# print(cards[23])
# print(cards[37])
# print(cards[51])
#
# # TEST_3:
# cards = list(CardDeck())
#
# print(cards)
#
# # TEST_4:
# cards1 = list(CardDeck())
# cards2 = tuple(CardDeck())
# cards3 = list(CardDeck())
#
# print(cards1)
# print(cards2)
# print(cards3)
#
# # TEST_5:
# cards = list(CardDeck())
#
# try:
#     next(cards)
# except:
#     print('Error')

# class Cycle:
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self._iterator = iter(iterable)  # Создаем итератор из переданного итерируемого объекта
#         self._current = None  # Переменная для хранения текущего элемента
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         try:
#             self._current = next(self._iterator)  # Получаем следующий элемент
#         except StopIteration:
#             self._iterator = iter(self.iterable)  # Если достигнут конец, создаем новый итератор
#             self._current = next(self._iterator)  # Получаем первый элемент нового итератора
#         return self._current
#
#
# class Cycle:
#
#     def __init__(self, obj):
#         self.obj = obj
#         self.it = iter(self.obj)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         try:
#             return next(self.it)
#         except StopIteration:
#             self.it = iter(self.obj)
#             return next(self.it)
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# cycle = Cycle('be')
#
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
#
# # TEST_2:
# cycle = Cycle([1])
#
# print(next(cycle) + next(cycle) + next(cycle))
#
# # TEST_3:
# cycle = Cycle(range(100_000_000))
#
# print(next(cycle))
# print(next(cycle))
#
# # TEST_4:
# cycle = Cycle(range(10_000_000))
#
# for _ in range(1000):
#     next(cycle)
#
# print(next(cycle))
#
# # TEST_5:
# cycle = Cycle('beegeek')
#
# for _ in range(1000):
#     next(cycle)
#
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
#
# # TEST_6:
# cycle = Cycle((0, 9, 8, 7, 6, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 0, 9, 8, 87, 5666666))
#
# for _ in range(2000):
#     next(cycle)
#
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
#
# # TEST_7:
# cycle = Cycle((0,))
#
# for _ in range(2000):
#     next(cycle)
#
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
#
# # TEST_8:
# cycle = Cycle('B')
#
# for _ in range(500):
#     next(cycle)
#
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
#
# # TEST_9:
# cycle = Cycle('AJFHKJSDHFWIEFJIOFKDKSVNCVNJVDJSFNdfkdsjfiwej943257438j2j123')
#
# for _ in range(666):
#     next(cycle)
#
# print(next(cycle))
#
# # TEST_10:
# cycle = Cycle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#
# for _ in range(100):
#     print(next(cycle))

# class Cycle:
#
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.ind = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.ind += 1
#         if self.ind == len(self.iterable):
#             self.ind = 0
#         return self.iterable[self.ind]


# import random
# class RandomNumbers:
#     def __init__(self, left, right, n):
#         self.left = left
#         self.right = right
#         self.n = n
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n >= 1:
#             self.n -= 1
#             return random.randrange(self.left, self.right + 1)
#
#         else:
#             raise StopIteration
#
#
# from random import randint
#
# class RandomNumbers():
#     def __init__(self, left, right, n):
#         self.n = n
#         self.left = left
#         self.right = right
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n == 0:
#             raise StopIteration
#         self.n -= 1
#         return randint(self.left, self.right)
#
#
# # INPUT DATA:
#
# # TEST_1:
# iterator = RandomNumbers(1, 1, 3)
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
# # TEST_2:
# iterator = RandomNumbers(1, 10, 2)
#
# print(next(iterator) in range(1, 11))
# print(next(iterator) in range(1, 11))
#
# # TEST_3:
# iterator = RandomNumbers(-100, -92, 99)
#
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
# print(next(iterator) in range(-100, -91))
#
# # TEST_4:
# iterator = RandomNumbers(5, 5, 98)
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
# # TEST_5:
# iterator = RandomNumbers(1000, 1001, 108)
#
# print(next(iterator) in range(1000, 1002))
# print(next(iterator) in range(1000, 1002))
# print(next(iterator) in range(1000, 1002))
# print(next(iterator) in range(1000, 1002))
# print(next(iterator) in range(1000, 1002))
# print(next(iterator) in range(1000, 1002))
# print(next(iterator) in range(1000, 1002))
# print(next(iterator) in range(1000, 1002))
# print(next(iterator) in range(1000, 1002))
# print(next(iterator) in range(1000, 1002))
#
# # TEST_6:
# iterator = RandomNumbers(-100, 99, 100)
#
# print(next(iterator) in range(-100, 100))
# print(next(iterator) in range(-100, 100))
# print(next(iterator) in range(-100, 100))
# print(next(iterator) in range(-100, 100))
# print(next(iterator) in range(-100, 100))
# print(next(iterator) in range(-100, 100))
# print(next(iterator) in range(-100, 100))
#
# # TEST_7:
# iterator = RandomNumbers(-1000, -900, 1)
#
# print(next(iterator) in range(-1000, -899))
#
# try:
#     next(iterator)
# except StopIteration:
#     print('Error')
#
# # TEST_8:
# iterator = RandomNumbers(-1000, -900, 4)
#
# print(next(iterator) in range(-1000, -899))
# print(next(iterator) in range(-1000, -899))
# print(next(iterator) in range(-1000, -899))
# print(next(iterator) in range(-1000, -899))
#
# try:
#     next(iterator)
# except StopIteration:
#     print('Error')


# class Alphabet:
#     def __init__(self, language):
#         self.language = language
#         self.data = {'en': 'abcdefghijklmnopqrstuvwxyz', 'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя'}.get(language)
#         self._iterator = iter(self.data)
#         self._current = None
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         try:
#             self._current = next(self._iterator)
#         except StopIteration:
#             self._iterator = iter(self.data)
#             self._current = next(self._iterator)
#         return self._current
#
#
#
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# ru_alpha = Alphabet('ru')
#
# print(next(ru_alpha))
# print(next(ru_alpha))
# print(next(ru_alpha))
#
# # TEST_2:
# en_alpha = Alphabet('en')
#
# letters = [next(en_alpha) for _ in range(28)]
#
# print(*letters)
#
# # TEST_3:
# en_alpha = Alphabet('en')
#
# for _ in range(100):
#     print(next(en_alpha))
#
# # TEST_4:
# en_alpha = Alphabet('en')
#
# for _ in range(1000):
#     next(en_alpha)
#
# print(next(en_alpha))
#
# # TEST_5:
# ru_alpha = Alphabet('ru')
#
# for _ in range(1000):
#     next(ru_alpha)
#
# print(next(ru_alpha))
#
# # TEST_6:
# ru_alpha = Alphabet('ru')
#
# for _ in range(50):
#     print(next(ru_alpha))
#
# # TEST_7:
# ru_alpha = Alphabet('ru')
#
# for _ in range(40):
#     next(ru_alpha)
#
# for _ in range(40):
#     next(ru_alpha)
#
# for _ in range(40):
#     next(ru_alpha)
#
# print(next(ru_alpha))
#
# # TEST_8:
# en_alpha = Alphabet('en')
#
# for _ in range(40):
#     next(en_alpha)
#
# for _ in range(40):
#     next(en_alpha)
#
# for _ in range(40):
#     next(en_alpha)
#
# print(next(en_alpha))




