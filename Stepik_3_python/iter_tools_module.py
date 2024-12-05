# import itertools as it
# import time
#
# symbols = ['.', '-', "'", '"', "'", '-', '.', '_']
#
# for c in it.cycle(symbols):
#     print(c, end='')
#     time.sleep(0.05)
#
# import itertools as it
# import time
#
# dicso = ['🟥', '🟥', '🟧', '🟧', '🟨', '🟨', '🟧', '🟧',
#          '🟥', '🟥', '🟧', '🟧', '🟨', '🟨', '🟧', '🟧',
#          '🟩', '🟩', '🟦', '🟦', '🟪', '🟪', '🟦', '🟦',
#          '🟩', '🟩', '🟦', '🟦', '🟪', '🟪', '🟦', '🟦',]
#
# dance = ['__(ツ)__', '\_(ツ)__', '¯\(ツ)__', '¯¯(ツ)__', '/¯(ツ)\_',
#          '_/(ツ)¯\\', '__(ツ)¯¯', '__(ツ)/¯', '__(ツ)_/', '__(ツ)__',
#          '__(ツ)__', '__(ツ)_/', '__(ツ)/¯', '__(ツ)¯¯', '_/(ツ)¯\\',
#          '/¯(ツ)\_', '¯¯(ツ)__', '¯\(ツ)__', '\_(ツ)__', '__(ツ)__',]
#
# for light, move in zip(it.cycle(dicso), it.cycle(dance)):
#     print(f'{light} {move} {light}', end='\r')
#     time.sleep(0.075)
#
# #
# from itertools import cycle
#
# cycler = cycle('17')
#
# print(next(cycler))
# print(next(cycler))
# print(next(cycler))
# from itertools import repeat
#
# repeater = repeat(['bee', 'ff'])
#
# for _ in range(100):
#     next(repeater)
#
# print(next(repeater))
# print(next(repeater))

# from itertools import repeat
#
# repeater = repeat('geek', 4)
#
# print(list(repeater))

#
# from itertools import repeat
#
# beegeek = ['bee', 'geek']
# repeater = repeat(beegeek)
#
# print(next(repeater))
#
# beegeek = beegeek + ['imposter']
#
# print(next(repeater))


# import itertools as it
# def tabulate(func):
#     return (func(i) for i in it.count(1))
#
#
# from itertools import count
#
# def tabulate(func):
#     return map(func, count(1))
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# func = lambda x: x
# values = tabulate(func)
#
# print(next(values))
# print(next(values))
#
# # TEST_2:
# func = lambda x: x + 10
# values = tabulate(func)
#
# print(next(values))
# print(next(values))
# print(next(values))
#
# # TEST_3:
# func = lambda x: x ** 2
# values = tabulate(func)
#
# for _ in range(100):
#     print(next(values))
#
# # TEST_4:
# def func(n):
#     return 'beegeek' * n
#
# values = tabulate(func)
#
# for _ in range(10):
#     print(next(values))


# from itertools import accumulate, count
# from operator import mul
#
# def fuck(x):
#     if x == 1 or x == 0:
#         return 1
#     else:
#         return x * factorials(x - 1)
#
#
# def factorials(n):
#     return accumulate(range(1, n + 1), mul)
#
# from itertools import accumulate
#
# def factorials(n):
#     yield from accumulate(range(1, n + 1), lambda x, y: x * y)
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# numbers = factorials(6)
#
# print(*numbers)
#
# # TEST_2:
# numbers = factorials(2)
#
# print(next(numbers))
# print(next(numbers))
#
# # TEST_3:
# numbers = factorials(100)
#
# print(*numbers)
#
# # TEST_4:
# numbers = factorials(1001)
#
# for _ in range(1000):
#     next(numbers)
#
# print(next(numbers))
# from itertools import cycle
# import string
#
# def alnum_sequence():
#     digits = (num for num in range(1, 27))
#     letters = map(lambda x: x, string.ascii_uppercase)
#     return cycle(j for i in zip(digits, letters) for j in i)
#
# from itertools import cycle
# from string import ascii_uppercase
#
#
# def alnum_sequence():
#     for item in zip(cycle(range(1, 27)), cycle(ascii_uppercase)):
#         yield from item
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# alnum = alnum_sequence()
#
# print(*(next(alnum) for _ in range(55)))
#
# # TEST_2:
# alnum = alnum_sequence()
#
# print(*(next(alnum) for _ in range(100)))
#
# # TEST_3:
# alnum = alnum_sequence()
#
# print(next(alnum))
# print(next(alnum))
# print(next(alnum))
# print(next(alnum))
#
# # TEST_4:
# alnum = alnum_sequence()
#
# for _ in range(10_000):
#     next(alnum)
#
# print(next(alnum))
# print(next(alnum))
# print(next(alnum))
# print(next(alnum))
#
# # TEST_5:
# alnum = alnum_sequence()
#
# for _ in range(100_000):
#     next(alnum)
#
# print(next(alnum))
# print(next(alnum))
# print(next(alnum))
# print(next(alnum))

# import itertools
#
# def roundrobin(*args):
#     a = itertools.zip_longest(*args, fillvalue='')
#     return (j for i in a for j in i if j != '')
#
# def roundrobin(*args):
#     iters = tuple(iter(a) for a in args)
#     while True:
#         err_counter = 0
#         for i in iters:
#             try: res = next(i)
#             except: err_counter += 1
#             else: yield res
#         if err_counter == len(iters):
#             break


# # INPUT DATA:
#
# # TEST_1:
# print(*roundrobin('abc', 'd', 'ef'))
#
# # TEST_2:
# numbers = [1, 2, 3]
# letters = iter('beegeek')
#
# print(*roundrobin(numbers, letters))
#
# # TEST_3:
# print(list(roundrobin()))
#
# # TEST_4:
# numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers2 = range(5)
# letters = iter('beegeek')
#
# print(*roundrobin(numbers1, numbers2, letters))
#
# # TEST_5:
# letters = iter('stepik')
#
# print(*roundrobin(letters))
#
# # TEST_6:
# numbers = roundrobin(map(abs, range(-10, 10)))
#
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
#
# # TEST_7:
# numbers1 = map(abs, range(-10, 10))
# numbers2 = filter(None, range(-10, 10))
# numbers3 = map(abs, range(-5, 5))
# numbers4 = filter(None, range(-5, 5))
# numbers5 = map(abs, range(-1, 1))
# numbers6 = filter(None, range(-1, 1))
#
# print(*roundrobin(numbers1, numbers2, numbers3, numbers4, numbers5, numbers6))
#
# # TEST_8:
# print(list(roundrobin([], [], [], [])))
#
# # TEST_9:
# numbers = iter([1, 2, 3])
# nones = iter([None, None, None, None])
#
# print(*roundrobin(numbers, nones))


# from itertools import islice
#
# print(*islice('hello world!', None))


# from itertools import count
# def factorial(x):
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return x * factorial(x - 1)
#
#
# for i in count():
#     print(factorial(i))


# from itertools import dropwhile
#
#
# def drop_while_negative(iterable):
#     return dropwhile(lambda x: x >= 0, iterable)


# from itertools import takewhile, dropwhile
#
# def drop_this(iterable, obj):
#     return dropwhile(lambda x: x == obj, iterable)
#
#
# iterator = iter('bbbbeebee')
#
# print(*drop_this(iterator, 'b'))
#
#
# iterator = iter('ssssssssssssssssssssssss')
#
# print(list(drop_this(iterator, 's')))


from itertools import filterfalse, takewhile, dropwhile

# def first_true(iterable, predicate=None):
#     for item in iterable:
#         if predicate is None:
#             if item:  # Если predicate не задан, используем bool()
#                 return item
#         elif predicate(item):
#             return item
#     return None



# def first_true(iterable, predicate):
#     for i in filter(predicate, iterable):
#         return i

# from itertools import islice
# def first_true(it, pred):
#     return next(islice(filter(pred, it), 1), None)
#
#
# numbers = [1, 1, 1, 1, 2, 4, 5, 6]
# print(first_true(numbers, lambda num: num % 2 == 0))
#
#
# numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])
# print(first_true(numbers, lambda num: num > 10))
#
#
# numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200)
# print(first_true(numbers, None))

#
# import itertools
#
# def take(iterable, n):
#     return itertools.islice(iterable, n)
#
#
# print(*take(range(10), 5))
#
#
# iterator = iter('beegeek')
# print(*take(iterator, 22))
#
#
#
# iterator = iter('beegeek')
# print(*take(iterator, 1))


# import itertools
#
# def take_nth(iterable, n):
#     for i in itertools.islice(iterable, n-1, n):
#         return i
#
#
# # INPUT DATA:
#
# # TEST_1:
# numbers = [11, 22, 33, 44, 55]
#
# print(take_nth(numbers, 3))
#
# # TEST_2:
# iterator = iter('beegeek')
#
# print(take_nth(iterator, 4))
#
# # TEST_3:
# iterator = iter('beegeek')
#
# print(take_nth(iterator, 10))
#
# # TEST_4:
# iterator = iter('beegeek')
#
# print(take_nth(iterator, 1))
#
# # TEST_5:
# iterator = tuple('stepik')
#
# print(take_nth(iterator, 6))
#
# # TEST_6:
# iterator = iter('p')
#
# print(take_nth(iterator, 1))
#
# # TEST_7:
# iterator = iter('p')
#
# print(take_nth(iterator, 2))
#
# # TEST_8:
# iterator = iter('beegeek')
#
# print(take_nth(iterator, 7))
#
# # TEST_9:
# iterator = iter('beegeek')
#
# print(take_nth(iterator, 8))
#
# # TEST_10:
# print(take_nth([], 4))



# import itertools
#
# def first_largest(iterable, number):
#     for k,v in enumerate(iterable):
#         if v > number:
#             return k
#     return -1
#
#
# from itertools import compress, count
#
# first_largest = lambda it, n: next(compress(count(), (i > n for i in it)), -1)
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
# numbers = [10, 2, 14, 7, 7, 18, 20]
#
# print(first_largest(numbers, 11))
#
# # TEST_2:
# iterator = iter([-1, -2, -3, -4, -5])
#
# print(first_largest(iterator, 10))
#
# # TEST_3:
# iterator = iter([18, 21, 14, 72, 73, 18, 20])
#
# print(first_largest(iterator, 10))
#
# # TEST_4:
# iterator = iter([18, 21, 14, 72, 73, 18, 20, 101, 102, 110])
#
# print(first_largest(iterator, 105))
#
# # TEST_5:
# iterator = iter([123, 423, 224, 722, 713, 158, 230, 1101, 1022, 1210, 222, 333, 334])
#
# print(first_largest(iterator, 105))
#
# # TEST_6:
# iterator = iter([2, 3, 4, 5, 6, 7, 8, 999])
#
# print(first_largest(iterator, 105))
#
# # TEST_7:
# iterator = iter([999])
#
# print(first_largest(iterator, 105))
#
# # TEST_8:
# iterator = iter([998])
#
# print(first_largest(iterator, 999))
#
# # TEST_9:
# iterator = iter([4, 100, 102, 334, 5])
#
# print(first_largest(iterator, 101))
#
# # TEST_10:
# print(first_largest([], 7))
#
# # TEST_11:
# iterator = iter([-400, -100, -102, -334, -5])
#
# print(first_largest(iterator, -6))