# def my_pow(number, l = []):
#     for i in enumerate(str(number), 1):
#         l.append(int(i[1])**i[0])
#     print(sum(l))


# def my_pow(number):
#     return sum(int(c)**i for i, c in enumerate(str(numbe


# print(my_pow(139))


# names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
# budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
# box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]
#
#
#
#
# for n, b, bo in sorted(zip(names, budgets, box_offices)):
#     print(f'{n}: {bo - b}$')



# def zip_longest(*args, fill=None):
#     maximum = len(max(args, key=len))
#     for i in args:
#         while len(i) < maximum:
#             i.append(fill)
#     return list(zip(*args))
#
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))
# # [(1, 'a'), (2, 'b'), (3, 'c'), (4, '_'), (5, '_')]
#
# # TEST_2:
# data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
# print(zip_longest(*data))
#
# # TEST_3:
# data = [[1, 2, 3, 4, 5], ['one', 'two', 'three', 'four', 'five'], ['I', 'II', 'III', 'IV', 'V']]
# print(zip_longest(*data))
#
# # TEST_4:
# data = [[], ['one'], [], ['uno']]
# print(zip_longest(*data))
#
# # TEST_5:
# data = [[], ['one'], [], ['uno']]
# print(zip_longest(*data, fill='not known'))
#
# # TEST_6:
# data = [[]]
# print(zip_longest(*data, fill='not known'))
#
# # TEST_7:
# data = [[]]
# print(zip_longest(*data))
#
# # TEST_8:
# data = [[1, 2, 3, 4, 5], ['repeat', 'itertools', 'recursion'], [90, 100, 10, 40]]
# print(zip_longest(*data, fill='add'))
#
# # TEST_9:
# data = [[1, 2, 3, 4, 5], ['repeat', 'itertools', 'recursion'], [90, 100, 10, 40]]
# print(zip_longest(*data))
#
# # TEST_10:
# data = [['is_lower', 'is_upper'], [True, False, 'string', 'int', 'float', 'double', 'char', 'bool'], [False, False, True, True]]
# print(zip_longest(*data, fill='skip'))
#
# # TEST_11:
# data = [['is_lower', 'is_upper'], [True, False, 'string', 'int', 'float', 'double', 'char', 'bool'],
#         [False, False, True, True], [1, 5, 9, 9, 104, -24, 13.4, 'f']]
# print(zip_longest(*data, fill='skip'))

# def custom_sort(s):
#     # Разделяем символы на три категории
#     lower = sorted([c for c in s if c.islower()])  # строчные буквы
#     upper = sorted([c for c in s if c.isupper()])  # заглавные буквы
#     odd_digits = sorted([c for c in s if c.isdigit() and int(c) % 2 != 0])  # нечетные цифры
#     even_digits = sorted([c for c in s if c.isdigit() and int(c) % 2 == 0])  # четные цифры
#
#     # Объединяем отсортированные категории
#     return ''.join(lower + upper + odd_digits + even_digits)
#
#
# # Чтение входных данных
# input_string = input().strip()
# # Вывод результата
# print(custom_sort(input_string))

# print(hash(-1) == -1)
# print(hash(-2) == -2)

# def hash_as_key(objects):
#     d = {}
#     for i in objects:
#         d.setdefault(hash(i), []).append(i)
#     for k, v in d.items():
#         if len(v) == 1:
#             d[k] = d[k][0]
#     return d
#
#
# data = [1, 2, 3, 4, 5, 5]
# print(hash_as_key(data))
#
# data = [-1, -2, -3, -4, -5]
# print(hash_as_key(data))
#
# data = [(1, 2, 3), (1, 2, 3), (0, 0, 0), 10, (144, 75, 60), 20, 30]
# print(hash_as_key(data))


# expression1 = "print('Привет из функции eval()')"
# expression2 = "len([1, 1, 1, 1, 1])"
#
# result1 = eval(expression1)
# result2 = eval(expression2)

# print(result1)
# print(result2)

# code = 'print(100 + 10 + 1)'
#
# print(exec(code))

# s = eval(input())
#
# if isinstance(s, list):
#     print(s[-1])
# if isinstance(s, set):
#     print(len(s))
# if isinstance(s, tuple):
#     print((s[0]))

# import sys
#
# for i in sys.stdin:
#     print(eval(i))
#
# import sys
#
# print(max(map(eval, sys.stdin)))


# def my_pow(number):
#     return sum(int(c)**i for i, c in enumerate(str(number)))


# f = input()
# a, b = map(int, input().split(' '))
#
# l = [eval(f) for (x) in range(a, b + 1)]
#
# print(l)
#
# for i in range(1):
#     print(f'Минимальное значение функции {f} на отрезке [{a}; {b}] равно {min(l)}')
#     print(f'Максимальное значение функции {f} на отрезке [{a}; {b}] равно {max(l)}')


# # TEST_1:
# 2*x**2 + 5*x + 7
# -1 5
#
# # TEST_2:
# x + 1
# -999 999
#
# # TEST_3:
# x**3 + x**2 + x
# -100 100

# TEST_4:
# x**4 - 2 * x**2 - x**3 + x - 1
# -10 10

# # TEST_5:
# 15 * x**4 - x**5 - 2 * x**2 - x**3 + x - 1
# 0 15

# TEST_4:
# Минимальное значение функции x**4 - 2 * x**2 - x**3 + x - 1 на отрезке [-10; 10] равно -2
# Максимальное значение функции x**4 - 2 * x**2 - x**3 + x - 1 на отрезке [-10; 10] равно 10789
#
# # TEST_5:
# Минимальное значение функции 15 * x**4 - x**5 - 2 * x**2 - x**3 + x - 1 на отрезке [0; 15] равно -3811
# Максимальное значение функции 15 * x**4 - x**5 - 2 * x**2 - x**3 + x - 1 на отрезке [0; 15] равно 60203
#
# positive = [1, 2, 3, 4, 5]
# negative = [-1, -2, -3]
# combined = [1, 2, -3, 4]
#
# result = map(lambda a, b, c: a + b + c, positive, negative, combined)
#
# print(*result)

# result = (lambda x: x > 5)(3)
#
# print(result)

# data = ['Timur', -16.648911695768902, 'six', -202, 883.0093275936454, -765, (3, 4), -105.10718000213546, 976, -308.96857946288094, 458, ['one', 'two'], 479.92207220345927, -87, -71, 'twelve', 112, -621, -715.0179551194733, 'seven', 229, 729, -358, [1, 2, 3], -974, 882, -894.4709033242768, '', 323.7720806756133, 'beegeek', -224, 431, 170.6353248658936, -343.0016746052049, 'number', 104.17133679352878, [], -353.5964777099863, 'zero', -113, 288, None, -708.3036176571618]
#
# for i in map(int, filter(lambda x: isinstance(x, int) or isinstance(x, float), data)):
#     print(i)


# print(*[int(el) for el in data if isinstance(el, (int, float))], sep='\n')

# numbers = [4754, -4895, -364, -4764, 4683, 1639, -43, 228, -2701, -1503, 1223, 4340, -1296, 3939, -345, 623, -3275, 1003, 4367, -1739, 550, -1217, -1334, 1526, -4359, -3028, -4663, 3356, 3887, 4297, -1982, 1013, 3299, 3556, -3324, 417, 3531, -3134, 1782, 4439, 1652, -985, 4327, 1517, 1225, -915, 2808, -3851, -1005, 3396, 2842, -3879, -3824, -3805, 1609, -4741, -3072, 3573, 4680, 588, -1430, 2378, -1095, -343, 4357, -2164, -3304, 4354, 4926, -352, -1187, -3313, 2741, 4786, -2689, 741, 4558, 1442, 62, -1099, -2201, -16, -3115, 1862, 2384, 4072, -90, 204, 1158, -3134, -2512, 756, 4148, 4370, 1756, 3609, -1148, -3909, 4123, -2906, 69, 96, 1111]
#
# l = filter(lambda x: 9 < abs(x) < 100 and x % 9 == 0, numbers)
# f_l = map(lambda x: (x)**2, l)
#
# print(sum(f_l))

# print(sum(map(lambda i: i**2 if abs(i) in range(10, 100) and i % 9 == 0 else 0, numbers)))

# names = ['ульяна', 'арина', 'Дмитрий', 'Сергей', 'Яна', 'мила', 'Ольга', 'софья', 'семён', 'Никита', 'маргарита', 'Василиса', 'Кирилл', 'александр', 'александра', 'Иван', 'андрей', 'Родион', 'максим', 'алиса', 'Артём', 'софия', 'владимир', 'дамир', 'Валерий', 'степан', 'Алексей', 'Марк', 'олег', 'ирина', 'Милана', 'мия', 'денис', 'Фёдор', 'Елизавета', 'айлин', 'Варвара', 'валерия', 'Алёна', 'Николь', 'юлия', 'Ксения', 'пётр', 'георгий', 'Мария', 'глеб', 'илья', 'Захар', 'Дарья', 'Евгения', 'матвей', 'Серафим', 'екатерина', 'Тимофей', 'виктор', 'Егор', 'Ника', 'анна', 'даниил', 'тихон', 'вера', 'кира', 'Эмилия', 'Виктория', 'Игорь', 'полина', 'алина', 'Давид', 'анастасия', 'Вероника', 'ярослав', 'Руслан', 'татьяна', 'Демид', 'амелия', 'Элина', 'Арсен', 'евгений', 'мадина', 'дарина', 'Савелий', 'Платон', 'Аделина', 'диана', 'Айша', 'павел', 'Стефания', 'Тимур', 'Ева', 'Елисей', 'Артемий', 'григорий', 'Мирон', 'Мирослава', 'Мира', 'Марат', 'Лилия', 'роман', 'владислав', 'Леонид']
#
# n = filter(lambda x: x[0].lower() == 'а' and len(x) > 4 or x[0].lower() == 'м' and len(x) > 4, names)
#
# print(*sorted(map(lambda x: x.capitalize(), n)))
#
# print(*sorted(map(str.title, filter(lambda x: x[0] in 'аАмМ' and len(x) > 4, names))))


# fib = lambda n: 1 if n <= 2 else fib(n - 1) + fib(n - 2)
# d = {1: 1, 2: 1}
# fib = lambda x: d[x] if x in d else d.setdefault(x, fib(x - 1) + fib(x - 2))
#
# print(fib(1))
#
# # 1
#
# print(fib(2))
#
# # 1
#
# print(fib(5))
#
# # 5

# def print_operation_table(operation, rows, cols):
#     for i in range(rows):
#         for j in range(cols):
#             print(operation(i + 1, j + 1), end=' ')
#         print()
#
#
#
#
# print_operation_table(lambda a, b: a * b, 5, 5)
# #
# # print_operation_table(pow, 5, 4)
#
# def print_operation_table(operation, rows, cols):
#     for i in range(1, rows + 1):
#         print(*map(operation, [i] * cols, range(1, cols + 1)))


# import string
#
#
# def verification(login, password, success, failure):
#     if not any(c in string.ascii_letters for c in password):
#         failure(login, 'в пароле нет ни одной буквы')
#     elif not any(c.isupper() and c in string.ascii_uppercase for c in password):
#         failure(login, 'в пароле нет ни одной заглавной буквы')
#     elif not any(c.islower() and c in string.ascii_lowercase for c in password):
#         failure(login, 'в пароле нет ни одной строчной буквы')
#     elif not any(c.isdigit() for c in password):
#         failure(login, 'в пароле нет ни одной цифры')
#     else:
#
#         success(login)
#
#
#
#
# def verification(login, password, success, failure):
#     vd = {str.isalpha: 'в пароле нет ни одной буквы',
#           str.islower: 'в пароле нет ни одной строчной буквы',
#           str.isupper: 'в пароле нет ни одной заглавной буквы',
#           str.isdigit: 'в пароле нет ни одной цифры'}
#     for f in vd:
#         if not any(f(i) for i in password):
#             return failure(login, vd[f])
#     success(login)
#
#
# # INPUT DATA:
#
# # TEST_1:
# def success(login):
#     print(f'Привет, {login}!')
#
# def failure(login, text):
#     print(f'{login}, попробуйте снова. Ошибка: {text}')
#
# verification('timyrik20', 'Beegeek314', success, failure)
#
# # TEST_2:
# def success(login):
#     print(f'Здравствуйте, {login}!')
#
# def failure(login, text):
#     print(f'{login}, попробуйте снова. Текст ошибки: {text}')
#
# verification('Ruslan_Chaniev', 'stepikstepik2', success, failure)
#
# # TEST_3:
# def success(login):
#     print(f'Здравствуйте, {login}!')
#
# def failure(login, text):
#     print(f'{login}, попробуйте снова. Текст ошибки: {text}')
#
# verification('Arthur_Davletov', 'HELLO_WORLD', success, failure)
#
# # TEST_4:
# def success(login):
#     print(f'Здравствуйте, {login}!')
#
#
# def failure(login, text):
#     print(f'{login}, попробуйте снова. Текст ошибки: {text}')
#
#
# verification('Arthur_Davletov', '797777777777', success, failure)
#
# # TEST_5:
# def success(login):
#     print(f'Здравствуйте, {login}!')
#
#
# def failure(login, text):
#     print(f'{login}, попробуйте снова. Текст ошибки: {text}')
#
#
# verification('Arthur_Davletov', 'Python777', success, failure)
#
# # TEST_6:
# def success(login):
#     print(f'Здравствуйте, {login}!')
#
#
# def failure(login, text):
#     print(f'{login}, попробуйте снова. Текст ошибки: {text}')
#
#
# verification('Arthur_Davletov', 'qwerty', success, failure)
#
# # TEST_7:
# def success(login):
#     print(f'Здравствуйте, {login}!')
#
#
# def failure(login, text):
#     print(f'{login}, попробуйте снова. Текст ошибки: {text}')
#
#
# verification('Arthur_Davletov', 'мойпароль123', success, failure)
#
# # TEST_8:
# def success(login):
#     print(f'Здравствуйте, {login}!')
#
#
# def failure(login, text):
#     print(f'{login}, попробуйте снова. Текст ошибки: {text}')
#
#
# verification('Arthur_Davletov', 'мойпарольbee123', success, failure)
#
# # TEST_9:
# def success(login):
#     print(f'Здравствуйте, {login}!')
#
#
# def failure(login, text):
#     print(f'{login}, попробуйте снова. Текст ошибки: {text}')
#
#
# verification('Arthur_Davletov', 'мойпарольBEE123', success, failure)

# def my_func():
# #     return 17
# #
# # input = my_func
# # num = input()
# # print(num)


# def func(name, language='Python', year=1992):
#     pass
#
# print(func.__name__)          # имя функции
# print(func.__doc__)           # строка документации
# print(func.__defaults__)      # кортеж с аргументами по умолчанию
#
# print(abs.__doc__)
# print(str.lower.__doc__)

# def bee():
#     '''bee docstring'''
#     return 'bee'
#
#
# def geek():
#     return 'geek'
#     '''geek docstring'''
#
#
# print(bee.__doc__)
# print(geek.__doc__)

# def ru_greeting(name):
#     print('Привет,', name)
#
#
# def en_greeting(name):
#     print('Hello,', name)
#
#
# greeting = {'ru': ru_greeting,
#             'en': en_greeting}
#
# greeting['ru']('Тимур')


# def add_name(name, names=[]):
#     names.append(name)
#
# add_name('Timur')
# add_name('Arthur')
# add_name('Dima')
#
# print(*add_name.__defaults__)

# def numbers_sum(*args):
#     """Принимает список и возвращает сумму его чисел (int, float),
# игнорируя нечисловые объекты. 0 - если в списке чисел нет."""
#     return sum(filter(lambda x: isinstance(x, (int, float)), *args))
#
#
#
#
# print(numbers_sum([1, '2', 3, 4, 'five']))
# print(numbers_sum(['beegeek', 'stepik', '100']))
# print(numbers_sum.__doc__)
#
# print(numbers_sum([10, 100, 1000, 10000]))
#
# print(numbers_sum(['beegeek', 11, 'stepik', 28.5, '100', 11.2]))
