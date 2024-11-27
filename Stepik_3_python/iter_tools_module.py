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

