# def matrix(n=1, m=None, value=0):
#     if m == None:
#         m = n
#     return [[value for i in range(m)] for j in range(n)]
#
# print(matrix())                   # матрица 1 × 1 из 0
# print(matrix(3))                  # матрица 3 × 3 из 0
# print(matrix(2, 5))               # матрица 2 × 5 из 0
# print(matrix(3, 4, 9))            # матрица 3 × 4 из 9
# from functools import reduce
import operator
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

#
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270,
#            219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260,
#            -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60,
#            254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29,
#            148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278,
#            26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219,
#            57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
#
# def two(x):
#     if len(str(abs(x))) == 2 and x % 7 == 0:
#         return x
#
# def kvadrat(x):
#     return x**2
#
# print(sum(map(kvadrat, filter(two, numbers))))



# def func_apply(func, args):
#     return list(map(func, args))
#
#
#
# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
# print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
# print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
# print(func_apply(str, [1, 2, 3, 4, 5, 6]))

from functools import reduce

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

# Cities: Beijing, Buenos Aires, ...

# a = map(lambda x: x[0], sorted(filter(lambda x: x[1] > 10000000 and x[2] == 'primary', data), key=lambda x: x[0]))
#
# print('Cities: ' + reduce(lambda x, y: x + ', ' + y, a))

######## EXAM ##########

# To: <mail>
# Приветствую, <name>!
# Вам назначен экзамен, который пройдет <date>, в <time>.
# По адресу: <place>.
# Экзамен будет проводить <teacher> в кабинете <number>.
# Желаем удачи на экзамене!
#
# def generate_letter(mail, name, date, time, place, teacher=' Тимур Гуев', number=17):
#         return f'''To: {mail}\nПриветствую, {name}!\nВам назначен экзамен, который пройдет {date}, в {time}.\nПо адресу: {place}.\nЭкзамен будет проводить {teacher} в кабинете {number}.\nЖелаем удачи на экзамене!'''
#
#
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
# print()
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00',
#                       'Часова 23, корпус 2', 'Василь Ярошевич', 23))



# def pretty_print(objects, side='-', delimiter='|'):
#     line = f'{delimiter} {(" " + delimiter + " ").join(str(item) for item in objects)} {delimiter}'
#     print(f' {side * (len(line) - 2)}')
#     print(line)
#     print(f' {side * (len(line) - 2)}')
#
# pretty_print([1, 2, 10, 23, 123, 3000])
# pretty_print(['abc', 'def', 'ghi', '12345'])
# pretty_print(['abc', 'def', 'ghi'], side='*')
# pretty_print(['abc', 'def', 'ghi'], delimiter='#')
# pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')


# print((lambda x: (x + 3) * 5 / 2)(3))

# data = [['p', 'y', 't', 'h', 'o', 'n'], ['s', 't', 'e', 'p', 'i', 'k']]
# result = list(map(lambda x: '.'.join(x), data))
# print(result[1])


# result = list(filter(str.isalpha, ['a', '1', 'b', '2']))
#
# print(result)

# result = list(filter(str.swapcase, ['a', '1', '', 'b', '2']))
#
# print(result)

# files = ['duwwouy440.py', 'crocst0sse.cs', 'j9t7ga2s6x.java', 'jk4nnes4tp.py', '2spc9uqzhu.doc',
#          'qi0ujxe0c7.png', 'z5x7l1j1d8.jpg', 'i5wtdxh366.geo', 'h53s2m2p73.py', 'ojty11f02d.sx',
#          'jyjuwlvwb3.st', 'gv4940lf8m.txt', 'op38fy9m9x.docx', 'o02ltr8vbp.xlsx', 'la97gc4js4.html',
#          'lcihrp8c6l.py', 'z66y7dgfo1.py', 'ckoks0849e.csv']
#
# result = list(filter(lambda s: s.endswith('.py'), files))
#
# print(len(result))

# print(list(filter(None, ['', 1, 7, 'beegeek', None, False, 0])))


# from functools import reduce
#
# words = ['beegeek', 'stepik', 'python', 'iq-option']
# result = reduce(lambda a, b: a if len(a) > len(b) else b, words)
# print(result)


# from functools import reduce
#
# result = reduce(lambda s, x: s + str(x), [1, 2, 3, 4, 5], '+')
# print(result)

# from functools import reduce
# import operator
#
# def flatten(data):
#     return reduce(operator.concat, data, [])
#
# result = flatten([[1, 2], [3, 4], [], [5]])
#
# print(result)
# from functools import reduce
# def concat(*args, sep=' '):
#     return reduce(lambda x, y: str(x) + sep + str(y), args)
#
#
#
#
# print(concat('hello', 'python', 'and', 'stepik'))
# print(concat('hello', 'python', 'and', 'stepik', sep='*'))
# print(concat('hello', 'python', sep='()()()'))
# print(concat('hello', sep='()'))
# print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))


# def product_of_odds(data):   # data - список целых чисел
#     result = 1
#     for i in data:
#         if i % 2 == 1:
#             result *= i
#     return result

# def product_of_odds(data):
#         return reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 1, data), 1)
#
#
# print(product_of_odds(range(1, 11)))


# words = 'the world is mine take a look what you have started'.split()
#
# print(*map(lambda x: f'"{x}"', words))

# x!=x[::-1]

# numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
# print(*filter(lambda x: x != x[::-1], map(lambda x: str(x), numbers)))

# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
#
# sorted_numbers = sorted(numbers, key=lambda x: sum(x)/len(x), reverse=True)
#
# print(sorted_numbers)

# def mul7(x):
#     return x * 7
#
#
# def add2(x, y):
#     return x + y
#
#
# def add3(x, y, z):
#     return x + y + z
#
#
# def call(f, *args):
#     return f(*args)
#
#
# print(call(mul7, 10))
# print(call(add2, 2, 7))
# print(call(add3, 10, 30, 40))
# print(call(bool, 0))



# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
#
# def compose(f, g):
#     return lambda x: f(g(x))
#
#
#
# print(compose(mul7, add3)(1))
# print(compose(add3, mul7)(2))
# print(compose(mul7, str)(3))
# print(compose(str, mul7)(5))

# def arithmetic_operation(op):
#         if op == '+':
#                 return lambda x, y: x + y
#         elif op == '-':
#                 return lambda x, y: x - y
#         elif op == '*':
#                 return lambda x, y: x * y
#         elif op == '/':
#                 return lambda x, y: x / y
#         else:
#                 return lambda x, y: print('bad operation!')


# from operator import *
#
# def arithmetic_operation(operation):
#     oper = {
#         '+': add,
#         '-': sub,
#         '*': mul,
#         '/': truediv
#     }
#     return oper[operation]
#
# add = arithmetic_operation('+')
# div = arithmetic_operation('/')

# print(add(10, 20))
# print(div(20, 5))

from functools import reduce
# text = 'cate Frog cat FROGs bee CATERS mouse cATwalk dolphin mOus Cats CatAlo'
#
# print(*sorted(input().split(), key=lambda x: x.lower()))

# n = int(input())

# def preobrazovanie(spisok):
#     return sorted(map(lambda a: int(a), map(lambda b: b.replace('.', ''), spisok)))
#
# l = [input() for i in range(int(input()))]
#
#
# print(preobrazovanie(l))


# ip_adresses = [input() for _ in range(int(input()))]
#
# low = lambda ip: list(map(int, ip.split('.')))
# print(*sorted(ip_adresses, key=low), sep='\n')


import ipaddress

# print(*sorted(l, key=ipaddress.IPv4Address))


