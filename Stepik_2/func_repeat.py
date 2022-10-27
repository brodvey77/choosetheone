# def matrix(n=1, m=None, value=0):
#     if m == None:
#         m = n
#     return [[value for i in range(m)] for j in range(n)]
#
# print(matrix())                   # матрица 1 × 1 из 0
# print(matrix(3))                  # матрица 3 × 3 из 0
# print(matrix(2, 5))               # матрица 2 × 5 из 0
# print(matrix(3, 4, 9))            # матрица 3 × 4 из 9
from functools import reduce

# def count_args(*args):
#     return len(args)
#
#
# print(count_args())
# print(count_args(10))
# print(count_args('stepik', 'beegeek'))
# print(count_args([], (''), 'a', 12, False))

# def sq_sum(*args):
#     return sum([i**2 for i in args])
#
#
# print(sq_sum())
# print(sq_sum(2))
# print(sq_sum(1.5, 2.5))
# print(sq_sum(1, 2, 3))
# print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# def mean(*args):
#     l = [i for i in args if type(i) in (int, float)]
#     if len(l) > 0:
#         return sum(l)/len(l)
#     else:
#         return 0.0
#
#
#
# print(mean())
# print(mean(7))
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))
# print(mean(-1, 2, 3, 10, ('5')))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# def greet(name, *args):
#     l = [name]
#     for i in args:
#         l.append(i)
#     return 'Hello, ' + ' and '.join(l) + '!'

# def greet(name, *args):
#     return f'Hello, {" and ".join((name,) + args)}!'
#
# print(greet('Timur'))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))

# def print_products(*args):
#     l = [i for i in args if type(i) == str and len(i) > 0]
#     for i in enumerate(l, 1):
#         print(*i)

# def print_products(*args):
#     l = [i for i in args if type(i) == str and len(i) > 0]
#     if len(l) == 0:
#         print('Нет продуктов')
#     else:
#         counter = 1
#         for i in l:
#             print(f'{counter}) {i}')
#             counter += 1
#
# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)


# def info_kwargs(**kwargs):
#     print(kwargs)
#     for k, v in sorted(kwargs.items()):
#         print(f'{k}: {v}')
#
#
#
# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')

# def start():
#     # тело функции start
#
#
# def stop():
#     # тело функции stop
#
#
# def pause():
#     # тело функции pause
#
#
# commands = {'start': start, 'stop': stop, 'pause': pause}  # словарь соответствия команда → функция
#
# command = input()        # считываем название команды
#
# commands[command]()      # вызываем нужную функцию через словарь по ключу

# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34),
#            (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4),
#            (90, 1, -45, -21)]
#
# def comparator(num):
#     return sum(num)/len(num)
#
# print(min(numbers, key=comparator))
# print(max(numbers, key=comparator))

# from statistics import mean
# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
#
# print(min(numbers, key=mean))
# print(max(numbers, key=mean))

#
# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
#
#
# def comparator(num):
#     return (num[0] ** 2 + num[1] ** 2) ** 0.5


# points.sort(key=comparator)

# print(sorted(points, key=comparator))



# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99),
#            (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
#
# def comparator(num):
#     return max(num) + min(num)
#
# print(sorted(numbers, key=comparator))


# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
#             ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
#
# def comparator(data):
#     return data[n-1]
#
#
# n = int(input())
# athletes.sort(key=comparator)
# for i in athletes:
#     print(*i)



# from math import sin
# n = int(input())
# f = input()
#
# d = {'квадрат': lambda x: x**2, 'куб': lambda x: x**3, 'корень': lambda x: x**0.5, 'модуль': lambda x: abs(x),
#      'синус': lambda x: sin(x)}
#
# print(d[f](n))

# def comparator(n):
#     return sum([int(i) for i in str(n)])
#
# numbers = [int(i) for i in input().split()]
#
# print(*sorted(numbers, key=comparator))


# def comparator(n):
#     return sum([int(i) for i in n])
#
# numbers = [i for i in input().split()]
#
# print(*sorted(numbers, key=comparator))


#
# def comparator(n):
#     return sum([int(i) for i in str(n)])
#
# numbers = sorted([int(i) for i in input().split()])
#
# print(*sorted(numbers, key=comparator))

# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
#
# def round_(n):
#     return round(n, 2)
#
#
#
# print(*map(round_, numbers), sep='\n')


# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434,
#            1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374,
#            1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98,
#            530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926,
#            175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120,
#            340, 963, 832, 1127]
#
#
# def delenie(n):
#     return n % 5 == 2
#
#
# def dlina(n):
#     if len(str(n)) == 3:
#         return n
#
#
# def cube(n):
#     return n ** 3
#
#
# print(*map(cube, filter(delenie, filter(dlina, numbers))))

# #
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35,
#            11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36,
#            72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35,
#            7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]

# def f(x, y):
#     return x + y**2
#
# print(reduce(f, numbers))
# #
# def square_num(x):
#     return x**2
# def summ_numbers(x, y):
#     return x + y
#
# # print(sum(map(kvadrat, numbers)))


# print(reduce(summ_numbers, map(square_num, numbers)))


