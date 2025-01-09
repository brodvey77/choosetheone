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

# from itertools import tee
#
# iters = tee('beegeek')
#
# print(type(iters), len(iters))
#
# for i in iters:
#     print(*i)


# from itertools import tee
#
# iters = tee([1, 2, 3], 3)
#
# totals = map(lambda a, b, c: a + b + c, *iters)
#
# print(list(totals))

# import itertools
#
# def sum_of_digits(iterable):
#     return sum(map(int, itertools.chain.from_iterable(map(str, iterable))))
#
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# print(sum_of_digits([13, 20, 41, 2, 2, 5]))
#
# # TEST_2:
# print(sum_of_digits((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
#
# # TEST_3:
# print(sum_of_digits([123456789]))
#
# # TEST_4:
# numbers = [10]*100
#
# iterator = iter(numbers)
# print(sum_of_digits(iterator))
#
# # TEST_5:
# numbers = [100, 20, 30, 400, 500, 5]*100000
#
# print(sum_of_digits(numbers))

# from itertools import pairwise
#
# def is_rising(iterable):
#     return all(a < b for a, b in pairwise(iterable))
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# print(is_rising([1, 2, 3, 4, 5]))
#
# # TEST_2:
# iterator = iter([1, 1, 1, 2, 3, 4])
#
# print(is_rising(iterator))
#
# # TEST_3:
# iterator = iter(list(range(100, 200)))
#
# print(is_rising(iterator))
#
# # TEST_4:
# iterator = iter(list(range(200, 100, -1)))
#
# print(is_rising(iterator))
#
# # TEST_5:
# iterator = iter(list(range(100, 201)) + [200])
#
# print(is_rising(iterator))
#
# # TEST_6:
# iterator = iter([10]*50)
#
# print(is_rising(iterator))

# from itertools import pairwise
#
# def max_pair(iterable):
#     return  max(sum(i) for i in pairwise(iterable))
#
#
# from itertools import pairwise
#
# def max_pair(iterable):
#     return max(map(sum, pairwise(iterable)))
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# print(max_pair([1, 8, 2, 4, 3]))
#
# # TEST_2:
# iterator = iter([1, 2, 3, 4, 5])
#
# print(max_pair(iterator))
#
# # TEST_3:
# iterator = iter([0, 0, 0, 0, 0, 0, 0, 0, 0])
#
# print(max_pair(iterator))
#
# # TEST_4:
# iterator = iter([10, 11])
#
# print(max_pair(iterator))
#
# # TEST_5:
# iterator = iter([5, 6, 4, 3, 2, 2])
#
# print(max_pair(iterator))
#
# # TEST_6:
# iterator = iter([10, 10, 10, 10, 10, 10, 10, 10, 10])
#
# print(max_pair(iterator))
#
# # TEST_7:
# iterator = iter([11, 10, 19, 1, 12, 100, 1, 13, 1])
#
# print(max_pair(iterator))
#
# # TEST_8:
# iterator = iter([11, 10, 19, 1, 12, 100, 1, 13, 107])
#
# print(max_pair(iterator))

# from itertools import tee, chain
#
# def ncycles(iterable, times):
#     return chain(*tee(iterable, times))
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# print(*ncycles([1, 2, 3, 4], 3))
#
# # TEST_2:
# iterator = iter('bee')
#
# print(*ncycles(iterator, 4))
#
# # TEST_3:
# iterator = iter([1])
#
# print(*ncycles(iterator, 10))
#
# # TEST_4:
# iterator = ncycles(iter('b'), 1)
#
# print(next(iterator))
#
# # TEST_5:
# iterator = ncycles(iter('g'), 3)
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
# # TEST_6:
# iterator = ncycles(iter([10, 10, 10, 10, 10]), 5)
#
# print(*iterator)
#
# # TEST_7:
# print(list(ncycles([], 5)))

# from itertools import zip_longest
#
# def grouper(iterable, n):
#     args = [iter(iterable)] * n
#     return zip_longest(*args, fillvalue=None)
#
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# numbers = [1, 2, 3, 4, 5, 6]
#
# print(*grouper(numbers, 2))
#
# # TEST_2:
# iterator = iter([1, 2, 3, 4, 5, 6, 7])
#
# print(*grouper(iterator, 3))
#
# # TEST_3:
# iterator = iter([1, 2, 3])
#
# print(*grouper(iterator, 5))
#
# # TEST_4:
# iterator = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#
# print(*grouper(iterator, 4))
#
# # TEST_5:
# iterator = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#
# print(*grouper(iterator, 5))
#
# # TEST_6:
# iterator = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#
# print(*grouper(iterator, 1))
#
# # TEST_7:
# iterator = iter('beegeek')
#
# print(*grouper(iterator, 5))
#
# # TEST_8:
# iterator = iter('beegeek')
#
# print(*grouper(iterator, 20))


# key_func = lambda x: x % 2

# print(key_func(4))

# from itertools import groupby

# groups = groupby('aaabbbcccaabb')

# key1, group1 = next(groups)
# key2, group2 = next(groups)

# print(key1, list(group1))


# from collections import namedtuple
# from itertools import groupby

# Person = namedtuple('Person', ['name', 'age', 'height'])

# persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
#            Person('Mark', 71, 172), Person('Alex', 45, 193),
#            Person('Jeff', 63, 193), Person('Ryan', 41, 184),
#            Person('Ariana', 28, 158), Person('Liam', 69, 193)]


# s_p = sorted(persons, key=lambda x: x.height)
# group_iter = groupby(s_p,key=lambda x: x.height)


# for k,data in group_iter:
#     print(f'{k}: {", ".join([i.name for i in sorted(data, key=lambda x: x.name)])}')




# from collections import namedtuple
# from itertools import groupby

# Student = namedtuple('Student', ['surname', 'name', 'grade'])

# students = [Student('Гагиев', 'Александр', 10), Student('Дедегкаев', 'Илья', 11), Student('Кодзаев', 'Георгий', 10),
#             Student('Набокова', 'Алиса', 11), Student('Кораев', 'Артур', 10), Student('Шилин', 'Александр', 11),
#             Student('Уртаева', 'Илина', 11), Student('Салбиев', 'Максим', 10), Student('Капустин', 'Илья', 11),
#             Student('Гудцев', 'Таймураз', 11), Student('Перчиков', 'Максим', 10), Student('Чен', 'Илья', 11),
#             Student('Елькина', 'Мария', 11),Student('Макоев', 'Руслан', 11), Student('Албегов', 'Хетаг', 11),
#             Student('Щербак', 'Илья', 10), Student('Идрисов', 'Баграт', 11), Student('Гапбаев', 'Герман', 10),
#             Student('Цивинская', 'Анна', 10), Student('Туткевич', 'Юрий', 11), Student('Мусиков', 'Андраник', 11),
#             Student('Гадзиев', 'Георгий', 11), Student('Белов', 'Юрий', 11), Student('Акоева', 'Диана', 11),
#             Student('Денисов', 'Илья', 11), Student('Букулова', 'Диана', 10), Student('Акоева', 'Лера', 11)]



# gr_st_name = groupby(sorted(students, key=lambda x: x.name), key=lambda x: x.name)


# l = []
# for k, data in gr_st_name:
#     l.append([k, len(list(i.name for i in data))])

# print(max(l, key=lambda x: x[1] )[0])


# group_iter = groupby(sorted(students, key=lambda x: x.name), key=lambda x: x.name)
# max_result = max(group_iter, key=lambda tpl: sum(1 for i in tpl[1]))
# print(max_result[0])

# from itertools import groupby

# def group_anagrams(words):
#     l = []
#     iter_g = groupby(sorted(words, key=sorted), key=sorted)
#     for k,v in iter_g:
#         yield tuple(v)

# from itertools import groupby

# def group_anagrams(words):
#     return (tuple(i) for _, i in groupby(sorted(words, key=sorted), key=sorted))







# # INPUT DATA:

# # TEST_1:
# groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])

# print(*groups)

# # TEST_2:
# groups = group_anagrams(['evil', 'father', 'book', 'stepik', 'beegeek'])

# print(*groups)

# # TEST_3:
# groups = group_anagrams(['крона', 'сеточка', 'тесачок', 'лучик', 'стоечка', 'норка', 'чулки'])

# print(*groups)

# # TEST_4:
# groups = group_anagrams(['чулки', 'чулки', 'чулки', 'чулки', 'чулки', 'чулки', 'чулки'])

# print(*groups)

# # TEST_5:
# groups = group_anagrams(['beegeek'])

# print(*groups)

# # TEST_6:
# groups = group_anagrams(['клоун', 'отсечка', 'кулон', 'уклон', 'чесотка', 'чулки', 'яяя', 'чулки', 'чесотка', 'яяя'])

# print(*groups)

# # TEST_7:
# groups = group_anagrams(['клоун', 'яяя', 'жжж', 'бббб', 'кулон'])

# print(*groups)

# # TEST_8:
# groups = group_anagrams(['катет', 'кета'])

# print(*groups)


# from itertools import groupby

# def ranges(numbers):
#     result = []
#     for _, group in groupby(numbers, key=lambda n: n - numbers.index(n)):
#         group = tuple(group)
#         group = group[0], group[-1]
#         result.append(group)
#     return result

# from itertools import groupby

# def ranges(numbers):
#     if not numbers:
#         return []

#     # Создаем список отрезков
#     result = []
    
#     # Группируем числа по их последовательности
#     for k, g in groupby(enumerate(numbers), lambda x: x[1] - x[0]):
#         group = list(g)
#         start = group[0][1]
#         end = group[-1][1]
#         result.append((start, end))
    
#     return result

# from itertools import permutations
#
#
# s = sorted(set(permutations(input())))
#
# for i in s:
#     print(*i, sep='')

#
# from itertools import combinations
#
# wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
#
# counter = 0
# for i in range(1, len(wallet)):
#     for j in set(combinations(wallet, i)):
#         if sum(j) == 100:
#             print(*j)
#             counter += 1
#
# print(counter)

