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



