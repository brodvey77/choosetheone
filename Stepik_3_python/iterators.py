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





