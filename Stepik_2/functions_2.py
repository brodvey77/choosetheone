# def matrix(n=1, m=None, value=0):
#     if m == None:
#         m = n
#     return [[value for i in range(m)] for j in range(n)]


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

import math
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


