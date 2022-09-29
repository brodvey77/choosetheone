# def matrix(n=1, m=None, value=0):
#     if m == None:
#         m = n
#     return [[value for i in range(m)] for j in range(n)]
from functools import reduce

# def f(n=3):
#     return n + 7
#
#
# print(f(f(f())))

# def func(*args):
#     return max(args) + min(args)
#
#
# print(func(10, 15, *[31, 42, 5, 1], *(17, 28, 19, 100), 13, 12))

# def count_args(*args):
# #     return len(args)
# #
# # print(count_args([], (''), 'a', 12, False))


# def sq_sum(*args):
#     return sum([i**2 for i in args])
#
# print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# def mean(*args):
#     l = [i for i in args if type(i) == int or type(i) == float]
#     if len(l) == 0:
#         return 0.0
#     else:
#         return sum(l)/len(l)
#
# print(mean())


# def greet(name, *args):
#     l = [name]
#     for i in args:
#         l.append(i)
#     return 'Hello, ' + ' and '.join(l) + '!'
#
#
# print(greet())


# def greet(name, *args):
#     return f'Hello, {" and ".join((name,) + args)}!'


# def print_products(*args):
#     counter = 1
#     l = [i for i in args if type(i) == str and len(i) > 1]
#     if len(l) > 0:
#         for j in l:
#             print(f'{counter}) {j}')
#             counter += 1
#     else:
#         print('Нет продуктов')
#
#
# print_products([4], {}, 1, 2, {'Beegeek'}, '')


# def info_kwargs(**kwargs):
#     for k, v in sorted(kwargs.items()):
#         print(f'{k}: {v}')
#
#
# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')


# commands = {'start': start, 'stop': stop, 'pause': pause}  # словарь соответствия команда → функция
#
# command = input()        # считываем название команды
#
# commands[command]()      # вызываем нужную функцию через словарь по ключу


# s1 = 'python'
# s2 = 'stepicon'
# s3 = 'beegeek'
#
# print(min(s1, s2, s3, key=len))
# print(max(s1, s2, s3, key=len))


# def f(x):
#     return x**2
#
#
# def g(x):
#     return x**3
#
#
# funcs = [f, g]
# print(funcs[0](5), funcs[1](5))


# def comparator(pair):
#     return pair[1]
#
#
# pairs = [(5, 4), (3, 2), (1, 7), (8, 2)]
# pairs.sort(key=comparator)
# print(pairs)

# def comparator(pair):
#     return pair[0] + pair[1]
#
#
# pairs = [(5, 4), (3, 2), (1, 7), (8, 2)]
# pairs.sort(key=comparator, reverse=True)
# print(pairs)

# def f1(x):
#     return 2*x+1
#
#
# def f2(x):
#     return x**2
#
#
# def f3(x):
#     return -x**2+1
#
#
# def f4(x):
#     return x-3
#
#
# funcs = [f1, f2, f3, f4]
# i = int(input())
# print(funcs[i](2))

# from statistics import mean
#
# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34),
#            (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6),
#            (-9, 8, 4), (90, 1, -45, -21)]
#
# print(min(numbers, key=mean))
# print(max(numbers, key=mean))


# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
# def comporant(num):
#     return sum(num) / len(num)
# print(min(numbers, key=comporant))
# print(max(numbers, key=comporant))

#
# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
# import math
# def distance(a):
#     return (math.pow(a[0], 2) + math.pow(a[1], 2))
#
# points.sort(key=distance)
# print(points)

# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34),
#            (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
#
# def sum_min_max(t):
#     return min(t) + max(t)
#
#
# numbers.sort(key=sum_min_max)
# print(numbers)

# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
#             ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]


# def choice_number(col):
#     return col[n - 1]
#
#
# n = int(input())
#
# names = sorted(athletes, key=choice_number)
# for i in names:
#     print(*i)

# import math
# def matematika(f, n):
#     return f(n)
#
# def sq(n):
#     return n * n
#
#
# def cube(n):
#     return n ** 3
#
#
# def root(n):
#     return n ** 0.5
#
#
# def module(n):
#     return abs(n)
#
#
# def sinus(n):
#     return math.sin(n)
#
#
# a = {'квадрат': sq, 'куб': cube, 'корень': root, 'модуль': module, 'синус': sinus}
#
# number = int(input())
# function = input()
#
# print(matematika(a[function], number))


# from math import sin
#
# def math_func(n, f):
#     return {'квадрат': n**2, 'куб': n**3, 'корень': n**0.5, 'модуль': abs(n), 'синус': sin(n)}[f]
#
# print(math_func(int(input()), input()))  # число, команда



# l = input().split()

# def sum_of_numbers(n):
#     f = []
#     for el in n:
#         f1 =[]
#         for d in el:
#             f1.append(int(d))
#         f.append(sum(f1))
#     x = sum(f)
#     return x


# l.sort(key=sum_of_numbers)

# print(*l)



# def comparator(n):
#     return sum([int(i) for i in str(n)])
#
# numbers = sorted([int(i) for i in input().split()])
#
# print(*sorted(numbers, key=comparator))
    

# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
# def predicate(word):
#     return word == word[::-1]
#
#
# words = ['abba', 'qwerty', 'python', 'a', 'deed', 'nun', 'level', 'language', 'deified', 'bbbbb', 'mother', 'sister', 'surface', '1234321']
# filtered = filter(predicate, words)
# print(len(filtered))


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
# numbers = [-2, 45, 45, -7, -45, 37, -42, 27, -58, -58, -12, -27, -49, -27, -56, 4, -99, -11, 86]
#
# var1 = max(numbers, key=abs)
# var2 = min(map(abs, numbers))
#
# print(var1 + var2)

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
# def round_(x):
#     return round(x, 2)
#
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
#
# print(*map(round_, numbers), sep='\n')



# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434,
#            1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374,
#            1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98,
#            530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926,
#            175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120,
#            340, 963, 832, 1127]
#
# def cube(x):
#     return x**3
#
#
# def ostatok(x):
#     return x % 5 == 2
#
#
# def digits_3(x):
#     return len(str(x)) == 3
#
#
# # z = map(cube, filter(ostatok, filter(digits_3, numbers)))
#
# print(*map(cube, filter(ostatok, filter(digits_3, numbers))), sep='\n')



# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
#
# def square_num(x):
#     return x**2
# def summ_numbers(x, y):
#     return x + y
#
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35,
#            11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36,
#            72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35,
#            7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
#
# # z = reduce(summ_numbers, map(square_num, numbers), 0)
# z = sum(map(square_num, numbers))
#
# print(z)


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# def num_two(x):
#     return len(str(abs(x))) == 2
# def num_7(x):
#     return x % 7 == 0
#
#
# def summ(x, y):
#     return x + y
#
#
# def square(x):
#     return x ** 2
#
#
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270,
#            219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35,
#            152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5,
#            187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35,
#            211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2,
#            79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234,
#            10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
#
# z = sum(map(square, filter(num_7, filter(num_two, numbers))))
#
# print(z)

# def func_apply(func, item):
#     result = []
#     for el in item:
#         result.append(func(el))
#     return result
#
# # def func_apply(func, arr):
# #     return [func(x) for x in arr]
#
# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
#
# print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
# print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
# print(func_apply(str, [1, 2, 3, 4, 5, 6]))

# list1 = list(map(len, ['this', 'is', 'a', 'test']))
# list2 = [len(word) for word in ['this', 'is', 'a', 'test']]
#
# print(list1 == list2)


# letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# filtered_vowels = filter(filter_vowels, letters)

# print(*filtered_vowels)

# random_list = [1, 'a', 0, False, True, '0', 7, '']
# filtered_list = list(filter(None, random_list))
# print(filtered_list)

# listA = [2, 3, 4]
# listB = [3, 2, 1]

# result = sum(map(pow, listA, listB))
# # print(result)
# from operator import mul
# from functools import reduce

# result = reduce(mul, range(1, 6))
# print(result)
# from operator import add

# result = list(map(add, 'abc', '1234'))
# print(result)

# from operator import mul

# result = list(map(mul, ['a', 'b', 'c'], [1, 2, 3]))
# print(result)

# from operator import add
# from functools import reduce

# result = reduce(add, [[1, 2, 3], [4,  -, 6], [7, 8, 9]])
# print(result)

# funcs = [lambda x: x ** 0.5, lambda x: x ** 2, lambda x: x ** 3]
# print(funcs[1](9))

# from functools import reduce

# numbers = range(10)
# obj = map(lambda x: x + 1, numbers)
# obj = list(filter(lambda x: x % 2 == 1, obj))
# result = reduce(lambda x, y: x + y, obj, 0)

# print(result)
# high_ord_func = lambda x, func: x + func(x)

# result = high_ord_func(2, lambda x: x * x) + high_ord_func(5, lambda x: x + 3)
# print(high_ord_func(5, lambda x: x + 3))

# print(result)


# dict1 = {'x': 1}
# dict2 = {'y': 2}
# dict3 = {'x': 3, 'y': 4}

# result = list(filter(lambda d: 'x' in d.keys(), [dict1, dict2, dict3]))

# print(result)

# from functools import reduce
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result_1 = list(map(lambda num: num**2, floats))
# map_result = list(map(lambda num: round(num, 1), map_result_1))
#
# filter_result_1 = list(filter(lambda name: len(name) > 4, words))
# filter_result = list(filter(lambda name: name == name[::-1], filter_result_1))
#
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)


# from functools import reduce
#
# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
#
# final_list = list(map(lambda c: c[0], sorted(list(filter(lambda z: z[1] > 10000000 and z[2] == 'primary', data)))))
#
# print(reduce(lambda x, y: f'{x} {y},', final_list, 'Cities:').strip(','))


# numbers = [1, 2, 5, 3, 4]
# numbers.sort(key=lambda x: -x)
# print(numbers)

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# result = list(filter(lambda x: True, primes))
# print(result)

# full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
# print(full_name('ben', 'affleck'))

# func = lambda x: x % 19 == 0 or x % 13 == 0
#
#
# print(func(19))
# print(func(13))
# print(func(20))
# print(func(15))
# print(func(247))

# func = lambda text: text[0].lower() == 'a' and text[-1].lower() == 'a'
#
# print(func('abcd'))
# print(func('bcda'))
# print(func('abcda'))
# print(func('Abcd'))
# print(func('bcdA'))
# print(func('abcdA'))

# is_num = lambda num: num.replace('.','', 1).replace('-', '', 1).isdigit() and  num.rfind('-') <= 0
#
# print(is_num('10.34ab'))
# print(is_num('10.45'))
# print(is_num('-18'))
# print(is_num('-34.67'))
# print(is_num('987'))
# print(is_num('abcd'))
# print(is_num('123.122.12'))
# print(is_num('-123.122'))
# print(is_num('--13.2'))
# print(is_num('.-95.'))
# print(is_num('1-1'))


# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able',
#          'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound',
#          'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday',
#          'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry',
#          'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
#
# a = list(filter(lambda x: len(x) == 6, words))
#
# print(*sorted(a))

# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80,
#            93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27,
#            57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29,
#            88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
#
# numbers = list(filter(lambda x: not(x%2 and x > 47), numbers))
# b = list(map(lambda num: num // 2 if num % 2 == 0 else num, numbers))
# print(*b)

# print(*map(lambda x: [x // 2, x][x % 2], filter(lambda x: x < 48 or not x % 2, numbers)))

# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'),
#         (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'),
#         (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'),
#         (7029917, 'Massachusetts'), (6910840, 'Tennessee')]

# a = sorted(data, key=lambda x: x[1][-1], reverse=True)
# for i in a:
#         print(i[1] + ':', i[0])
#
# for pop, city in sorted(data, key=lambda x: x[1][-1], reverse=True):
#     print(f'{city}: {pop}')
