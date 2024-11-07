# def null_decorator(func):
#     return func


# def say():
#     print('Hello world')
#
#
# say = null_decorator(say)
#
# say()


# def sample_decorator(func):
#     def wrapper():
#         print('begin function')
#         func()
#         print('end function')
#     return wrapper
#
# def say():
#     print('hello world')


#
# print(say)
# say = sample_decorator(say)
# print(say)

# def null_decorator(func):
#     return func
#
# def say():
#     print('Привет Мир!')
#
# say = null_decorator(say)            # декорируем функцию
#
# say()


# def null_decorator(func):
#     return func
#
# @null_decorator                      # декорируем функцию
# def say():
#     print('Привет Мир!')
#
# say()


# def sample_decorator(func):          # определяем декоратор
#     def wrapper():
#         print('Начало функции')
#         func()
#         print('Конец функции')
#     return wrapper
#
# @sample_decorator                    # декорируем функцию
# def say():
#     print('Привет Мир!')
#
# say()

# def uppercase_decorator(func):
#     def wrapper():
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#
#     return wrapper
#
#
# @uppercase_decorator
# def greet():
#     return 'ща приду'
#
# print(greet())

# def bold(func):
#     def wrapper():
#         return '<b>' + func() + '</b>'
#     return wrapper
#
# def italic(func):
#     def wrapper():
#         return '<i>' + func() + '</i>'
#     return wrapper
#
# @italic
# @bold
# def greet():
#     return 'Hello world!'
#
# greet = bold(italic(greet))
#
# print(greet())

# def bold(func):
#     def wrapper(*args, **kwargs):
#         return '<b>' + func(*args, **kwargs) + '</b>'
#
#     return wrapper
#
#
# @bold
# def greet1(name):
#     return f'Hello {name}!'
#
# @bold
# def greet2():
#     return 'Hello world!'
#
# @bold
# def greet3(name, surname):
#     return f'Hello {name} {surname}!'
#
# print(greet1('Timur'))
# print(greet2())
# print(greet3('Timur', 'Guev'))

# def talk(func):
#     def wrapper(*args, **kwargs):
#         dash = '-' * 15
#         result = func(*args, **kwargs)
#         return dash + '\n' + result + '\n' + dash
#     return wrapper
#
#
# @talk
# def greet(name):
#     return f'Hello {name}!'
#
# print(greet('Timur'))


# def make_lower(func):
#     def wrapper():
#         return func().lower()
#
#     return wrapper
#
# def beegeek():
#     return 'BEEGEEK'
#
# beegeek = make_lower(beegeek)
#
# print(beegeek())

# def make_lower(func):
#     def wrapper():
#         return func().lower()
#
#     return wrapper
#
# def make_capitalize(func):
#     def wrapper():
#         return func().capitalize()
#
#     return wrapper
#
# def beegeek():
#     return 'BEEGEEK'
#
# beegeek = make_capitalize(make_lower(beegeek))
#
# print(beegeek())

# def double(func):
#     def wrapper():
#         return func() * 2
#
#     return wrapper
#
# def del_first_char(func):
#     def wrapper():
#         return func()[1:]
#
#     return wrapper
#
# @double
# @del_first_char
# def beegeek():
#     return 'beegeek'
#
# print(beegeek())

# def add_dollar_prefix(func):
#     def wrapper(*args, **kwargs):
#         result = str(func(*args, **kwargs))
#         return '$' + result
#
#     return wrapper
#
# @add_dollar_prefix
# def get_price(item):
#     prices = {'comic book': 5, 'puzzle': 20}
#     return prices[item]
#
# print(get_price(item='puzzle'))


# def sandwich(func):
#     def wrapper(*args, **kwargs):
#         up = f'---- Верхний ломтик хлеба ----'
#         down = f"---- Нижний ломтик хлеба ----"
#         print(up)
#         result = func(*args, **kwargs)
#         print(down)
#         return result
#
#     return wrapper
#
#
# @sandwich
# def add_ingredients(ingredients):
#     print(' | '.join(ingredients))
#
# add_ingredients(['томат', 'салат', 'сыр', 'бекон'])


# def decorator(func):
#     def wrapper(*args, sep=" ", end="\n"):
#         res = [c.upper() if type(c) == str else c for c in args]
#         end, sep = end.upper(), sep.upper()
#         result = func(*res, end=end, sep=sep)
#         return result
#
#     return wrapper


# def do_twice(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper
#
#
# # INPUT DATA:
#
# # TEST_1:
# @do_twice
# def beegeek():
#     print('beegeek')
#
#
# beegeek()
#
#
# # TEST_2:
# @do_twice
# def beegeek():
#     print('beegeek')
#
#
# print(beegeek())
#
#
# # TEST_3:
# @do_twice
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek())
#
#
# # TEST_4:
# @do_twice
# def beegeek():
#     print('beegeek')
#
#
# beegeek()
# beegeek()
# beegeek()
#
#
# # TEST_5:
# @do_twice
# def beegeek(a, b, sep):
#     print(a + b + sep)
#
#
# beegeek(1, 2, sep=10)
#
#
# # TEST_6:
# @do_twice
# def beegeek(*args, **kwargs):
#     print('beegeek' * sum(args + tuple(kwargs.values())))
#
#
# beegeek(1, 1, 1, sep=1, end=2, step=3)


# def reverse_args(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args[::-1], **kwargs)
#         return result
#     return wrapper

# def reverse_args(func):
#     def wrapper(*args, **kwargs):
#         result = func(*reversed(args), **kwargs)
#         return result
#     return wrapper


# INPUT DATA:

# TEST_1:
# @reverse_args
# def power(a, n):
#     return a ** n
#
#
# print(power(2, 3))
#
#
# # TEST_2:
# @reverse_args
# def concat(a, b, c):
#     return a + b + c
#
#
# print(concat('apple', 'cherry', 'melon'))
#
#
# # TEST_3:
# @reverse_args
# def operation(a, b, c):
#     return a // b + c
#
#
# print(operation(10, 20, 80))
#
#
# # TEST_4:
# @reverse_args
# def operation(a, b):
#     return a // b
#
#
# print(operation(90, 0))
#
#
# # TEST_5:
# @reverse_args
# def operation(a, b):
#     return a // b
#
#
# try:
#     print(operation(0, 70))
# except ZeroDivisionError:
#     print('ZeroDivisionError')
#
#
# # TEST_6:
# @reverse_args
# def operation(a, b, name):
#     return a // b + name
#
#
# print(operation(10, 90, name=1))
#
#
# # TEST_7:
# @reverse_args
# def operation(a, b, value=10):
#     return a // b + value
#
#
# try:
#     print(operation(0, 70))
# except ZeroDivisionError:
#     print('ZeroDivisionError')
#
#
# # TEST_8:
# @reverse_args
# def operation(a, b, value=10):
#     return a // b - value
#
#
# print(operation(70, 70, value=70))

# def exception_decorator(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs), 'Функция выполнилась без ошибок'
#         except:
#             return None, 'При вызове функции произошла ошибка'
#
#     return wrapper


# def exception_decorator(func):
#     def wrapper(*args, **kargv):
#         try:
#             res, msg = func(*args, **kargv), 'Функция выполнилась без ошибок'
#         except:
#             res, msg = None, "При вызове функции произошла ошибка"
#         finally:
#             return res, msg
#
#     return wrapper

# # INPUT DATA:
#
# # TEST_1:
# @exception_decorator
# def f(x):
#     return x ** 2 + 2 * x + 1
#
#
# print(f(7))
# #
# # TEST_2:
# sum = exception_decorator(sum)
#
# print(sum(['199', '1', 187]))
#
#
# # TEST_3:
# @exception_decorator
# def f(x, y):
#     return x * y
#
#
# print(f('stepik', 10))


# TEST_4:
# @exception_decorator
# def f(x, y):
#     return x * y
#
#
# print(f('stepik', 'stepik'))


# TEST_5:
# @exception_decorator
# def f(*args, **kwargs):
#     return sum(args) + sum(kwargs.values())
#
#
# print(f(1, 2, 3, param1=4, param2=10))


# TEST_6:
# @exception_decorator
# def f(*args, **kwargs):
#     return sum(args) + sum(kwargs.values())
#
#
# print(f(1, 2, 3, param1=4, param2='10'))
# #
#


# def takes_positive(func):
#     def wrapper(*args, **kwargs):
#         if all(i > 0 and isinstance(i, int) for i in [*args, *kwargs.values()]):
#             return func(*args, **kwargs)
#         if any(not isinstance(i, int) for i in [*args, *kwargs.values()]):
#             raise TypeError
#         if any(i <= 0 for i in [*args, *kwargs.values()]):
#             raise ValueError
#
#     return wrapper
#
#
# def takes_positive(func):
#     def wrapper(*args, **kwargs):
#         for i in [*args, *kwargs.values()]:
#             if not type(i) is int:
#                 raise TypeError
#             elif i <= 0:
#                 raise ValueError
#         return func(*args, **kwargs)
#     return wrapper
#
# # all(i > 0 and isinstance(i, int) for i in args)
# # INPUT DATA:
#
# # TEST_1:
# @takes_positive
# def positive_sum(*args):
#     return sum(args)
#
#
# print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
#
#
# # TEST_2:
# @takes_positive
# def positive_sum(*args):
#     return sum(args)
#
#
# try:
#     print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
# except Exception as err:
#     print(type(err))
#
#
# # TEST_3:
# @takes_positive
# def positive_sum(*args):
#     return sum(args)
#
#
# try:
#     print(positive_sum('10', 20, 10))
# except Exception as err:
#     print(type(err))
#
#
# # TEST_4:
# @takes_positive
# def positive_sum(*args):
#     return sum(args)
#
#
# try:
#     print(positive_sum(10, 20, 16, 18, '10'))
# except Exception as err:
#     print(type(err))
#
#
# # TEST_5:
# @takes_positive
# def positive_sum(*args):
#     return sum(args)
#
#
# try:
#     print(positive_sum(10, 20, '16', 18, '10'))
# except Exception as err:
#     print(type(err))
#
#
# # TEST_6:
# @takes_positive
# def positive_sum(*args):
#     return sum(args)
#
#
# print(positive_sum(*range(10, 100)))
#
#
# # TEST_7:
# @takes_positive
# def positive_sum(*args):
#     return sum(args)
#
#
# try:
#     print(positive_sum(3, 2, 1, -8, 1, 2, 3))
# except Exception as err:
#     print(type(err))
#
#
# # TEST_8:
# @takes_positive
# def positive_sum(*args):
#     return sum(args)
#
#
# try:
#     print(positive_sum(*range(100, -1, -1)))
# except Exception as err:
#     print(type(err))
#
#
# # TEST_9:
# @takes_positive
# def positive_sum(*args, **kwargs):
#     return sum(args) + sum(kwargs.values())
#
#
# print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=4))
#
#
# # TEST_10:
# @takes_positive
# def positive_sum(*args, **kwargs):
#     return sum(args) + sum(kwargs.values())
#
#
# try:
#     print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=-40))
# except Exception as err:
#     print(type(err))
#
#
# # TEST_11:
# @takes_positive
# def positive_sum(*args, **kwargs):
#     return sum(args) + sum(kwargs.values())
#
#
# try:
#     print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep='40'))
# except Exception as err:
#     print(type(err))
#
#
# # TEST_12:
# @takes_positive
# def positive_sum(*args):
#     return sum(args)
#
#
# try:
#     print(positive_sum(11, 20.7, 10))
# except Exception as err:
#     print(type(err))
#
#
# # TEST_13:
# @takes_positive
# def power(a, n):
#     return a ** n
#
#
# try:
#     print(power(a="3", n="2"))
# except Exception as err:
#     print(type(err))

# def greet(name):
#     '''Функция приветствия пользователя.'''
#     return f'Hello {name}!'
#
# print(greet.__name__)
# print(greet.__doc__)

# def bold(func):
# #     def wrapper(*args, **kwargs):
# #         return '<b>' + func(*args, **kwargs) + '</b>'
# #     return wrapper
# #
# # @bold
# # def greet(name):
# #     '''Функция приветствия пользователя.'''
# #     return f'Hello {name}!'
# #
# # print(greet.__name__)
# # print(greet.__doc__)

# def bold(func):
#     def wrapper(*args, **kwargs):
#         return '<b>' + func(*args, **kwargs) + '</b>'
#     wrapper.__name__ = func.__name__
#     wrapper.__doc__ = func.__doc__
#     return wrapper
#
# @bold
# def greet(name):
#     '''Функция приветствия пользователя.'''
#     return f'Hello {name}!'
#
# print(greet.__name__)
# print(greet.__doc__)


# import functools
#
# def bold(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         return '<b>' + func(*args, **kwargs) + '</b>'
#     return wrapper
#
# @bold
# def greet(name):
#     '''Функция приветствие пользователя.'''
#     return f'Hello {name}!'
#
# print(greet.__name__)
# print(greet.__doc__)

# Шаблон декоратора общего назначения
# Все декораторы в большинстве случаев делают примерно одно и то же. Наиболее частый шаблон декоратора выглядит следующим образом:

# import functools
#
# def decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         # Что-то выполняется до вызова декорируемой функции
#         value = func(*args, **kwargs)
#         # декорируется возвращаемое значение функции
#         # или что-то выполняется после вызова декорируемой функции
#         return value
#     return wrapper

# Декоратор измерения времени работы функции
# Следующий декоратор измеряет и выводит время выполнения декорируемой функции. Декоратор вычисляет время непосредственно перед запуском функции и сразу после ее завершения и выводит разницу подсчитанных времен.
#
# Приведенный ниже код:

# import functools, time
#
# def timer(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         val = func(*args, **kwargs)
#         end = time.perf_counter()
#         work_time = end - start
#         print(f'Время выполнения {func.__name__}: {round(work_time, 4)} сек.')
#         return val
#     return wrapper
#
# @timer
# def test(n):
#     return sum([(i/99)**2 for i in range(n)])
#
# @timer
# def sleep(n):
#     time.sleep(n)
#
# res1 = test(10000)
# res2 = sleep(4)
#
# print(f'Результат функции test = {res1}')
# print(f'Результат функции sleep = {res2}')

# Декоратор отслеживания количества вызовов функции
# Иногда полезно иметь декоратор, который может отслеживать состояние вызова функции. Создадим декоратор, который подсчитывает, сколько раз вызывается функция. Для сохранения состояния счетчика будем использовать пользовательский атрибут функции.
#
# Приведенный ниже код:

import functools

# def counter(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         wrapper.num += 1
#         print(f'Вызов {func.__name__}: {wrapper.num}')
#         val = func(*args, **kwargs)
#         return val
#     wrapper.num = 0
#     return wrapper
#
# @counter
# def greet(name):
#     return f'Hello {name}!'
#
# print(greet('Timur'))
# print(greet('Ruslan'))
# print(greet('Arthur'))
# print(greet('Gvido'))


# Декоратор замедления времени выполнения функции
# Иногда полезно иметь декоратор, который замедляет время выполнения функции.Создадим декоратор slow_down, который
# будет добавлять задержку выполнения программы в 1 секунду, прежде чем вызовет декорируемую
# функцию.
#
# Приведенный ниже код:

# import functools
# import time
#
#
# def slow_down(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         time.sleep(1)
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @slow_down
# def countdown(number):
#     if number < 1:
#         print('Конец!')
#     else:
#         print(number)
#         countdown(number - 1)
#
#
# countdown(5)

# import sys, time
#
#
# def teleprint(*args, delay=0.05, str_join=' '):
#     text = str_join.join(str(x) for x in args)
#     n = len(text)
#     for i, char in enumerate(text, 1):
#         if i == n:
#             char = f'{char}\n'
#         print(char, end='')
#         time.sleep(delay)
#
#
# teleprint('Привет Python!', 'Меня зовут Тимур', 'Beegeek = <3', str_join='*')
# teleprint('Привет Python!', 'Меня зовут Тимур', 'Beegeek = <3', str_join='*')

# import functools
#
# def make_capitalize(func):
#     @functools.wraps
#     def wrapper():
#         return func().capitalize()
#     return wrapper
#
# @make_capitalize
# def beegeek():
#     '''documentation'''
#     return 'beegeek'
#
# print(beegeek.__name__)
# print(beegeek.__doc__)


# import functools
#
# def square(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         val = func(*args, **kwargs)
#         return pow(val, 2)
#     return wrapper
#
#
# from functools import wraps
#
#
# def square(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs) ** 2
#
#     return wrapper
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# @square
# def add(a, b):
#     return a + b
#
# print(add(3, 7))
#
# # TEST_2:
# @square
# def add(a, b):
#     '''прекрасная функция'''
#     return a + b
#
# print(add(1, 1))
# print(add.__name__)
# print(add.__doc__)
#
# # TEST_3:
# @square
# def beegeek():
#     '''beegeek docs'''
#     return 99
#
# print(beegeek())
# print(beegeek.__name__)
# print(beegeek.__doc__)
#
# # TEST_4:
# @square
# def func(x):
#     '''classic f(x)'''
#     return (x + 1) ** 3
#
# print(func(7))
# print(func.__name__)
# print(func.__doc__)
#
# # TEST_5:
# @square
# def add(a, b, c, d, e):
#     return a + b + c + d + e
#
# print(add(1, 2, 3, 4, 5))
# print(add.__name__)
# print(add.__doc__)
#
# # TEST_6:
# @square
# def add(*args, **kwargs):
#     return sum([*args, *kwargs.values()])
#
# print(add(3, 7, x=10, y=30))


# from functools import wraps
#
# def returns_string(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         val = func(*args, **kwargs)
#         if isinstance(val, str):
#             return val
#         raise TypeError
#
#
#     return wrapper
#
#
# # INPUT DATA:
#
# # TEST_1:
# @returns_string
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek())
#
#
# # TEST_2:
# @returns_string
# def add(a, b):
#     return a + b
#
#
# try:
#     print(add(3, 7))
# except TypeError as e:
#     print(type(e))
#
#
# # TEST_3:
# @returns_string
# def beegeek():
#     '''documentation'''
#     return 'beegeek'
#
#
# print(beegeek.__name__)
# print(beegeek.__doc__)
#
#
# # TEST_4:
# @returns_string
# def nothing():
#     return
#
#
# print(nothing.__name__)
# print(nothing.__doc__)
#
# try:
#     nothing()
# except TypeError as e:
#     print(type(e))
#
#
# # TEST_5:
# @returns_string
# def add(a, b):
#     '''docs'''
#     return a + b
#
#
# print(add.__name__)
# print(add.__doc__)
#
# try:
#     add([1, 2], [3, 4])
# except TypeError as e:
#     print(type(e))
#
#
# # TEST_6:
# @returns_string
# def concat(a, b):
#     '''concat two strings'''
#     return a + b
#
#
# print(concat.__name__)
# print(concat.__doc__)
# print(concat('10', b='20'))
#
#
# # TEST_7:
# @returns_string
# def concat(*args, **kwargs):
#     return "".join([*args, *kwargs.values()])
#
#
# print(concat("Hello ", x="world", y="!!!"))


# from functools import wraps as wr
#
# def trace(func):
#     @wr(func)
#     def wrapper(*args, **kwargs):
#         print(f'TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}')
#         val = func(*args, **kwargs)
#         print(f'TRACE: возвращаемое значение {func.__name__}(): {repr(val)}')
#         return func(*args, **kwargs)
#     return wrapper
#
#
# # INPUT DATA:
#
# # TEST_1:
# @trace
# def say(name, line):
#     return f'{name}: {line}'
#
#
# say('Jane', 'Hello, World')
#
#
# # TEST_2:
# @trace
# def sub(a, b, c):
#     '''прекрасная функция'''
#     return a - b + c
#
#
# print(sub.__name__)
# print(sub.__doc__)
# sub(20, 5, c=10)
#
#
# # TEST_3:
# @trace
# def beegeek():
#     '''beegeek docs'''
#     return 'beegeek'
#
#
# print(beegeek())
# print(beegeek.__name__)
# print(beegeek.__doc__)
#
#
# # TEST_4:
# @trace
# def add(a, b, c):
#     '''docs'''
#     return a + b + c
#
#
# print(add(1, 2, 3))
# print(add.__name__)
# print(add.__doc__)
#
#
# # TEST_5:
# @trace
# def add(a, b, c):
#     '''docs'''
#     return a + b + c
#
#
# print(add(b=3, c=3, a=3))
# print(add.__name__)
# print(add.__doc__)
#
#
# # TEST_6:
# @trace
# def concat(a, b):
#     '''concat two strings'''
#     return a + b
#
#
# print(concat('bee', b='geek'))
# print(concat.__name__)
# print(concat.__doc__)
#
#
# # TEST_7:
# @trace
# def func(nums):
#     '''прекрасная функция'''
#     return list(i ** 2 for i in nums)
#
#
# print(func.__name__)
# print(func.__doc__)
# func([1, 2, 3, 4, 5, 6])
#
#
# # TEST_8:
# @trace
# def func(nums, degree=3):
#     '''прекрасная функция'''
#     return list(i ** degree for i in nums)
#
#
# print(func.__name__)
# print(func.__doc__)
# func([1, 2, 3, 4, 5, 6], degree=5)

# Декоратор delayed
# Реализуем декоратор delayed, который создает требуемую задержку выполнения кода. Такое поведение иногда требуется для мониторинга доступности какого-нибудь ресурса.

# import functools
# import time
#
# def delayed(delay=2):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             print(f'Спим {delay} сек.')
#             time.sleep(delay)
#             value = func(*args, **kwargs)
#             return value
#         return wrapper
#     return decorator
#
#
# @delayed(1)
# def countdown(number):
#     if number < 1:
#         print('Конец!')
#     else:
#         print(number)
#         countdown(number - 1)
#
#
# countdown(5)


# Декоратор timer
# Рассмотрим декоратор timer, который подсчитывает время выполнения функции. Для более точного подсчета декоратор принимает аргумент iters, который задает количество измерений.

# import functools, time
#
# def timer(iters=1):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             total = 0
#             for i in range(iters):
#                 start = time.perf_counter()
#                 value = func(*args, **kwargs)
#                 end = time.perf_counter()
#                 total += end - start
#             print(f'Среднее время выполнения {func.__name__}: {round(total/iters, 4)} сек.')
#             return value
#         return wrapper
#     return decorator
#
#
#
# @timer(iters=1000)
# def test(n):
#     return sum([(i/99)**2 for i in range(n)])
#
# @timer(iters=3)
# def sleep(n):
#     time.sleep(n)
#
# res1 = test(10000)
# res2 = sleep(4)
#
# print(f'Результат функции test = {res1}')
# print(f'Результат функции sleep = {res2}')


# Декоратор repeater
# Рассмотрим декоратор repeater, который вызывает декорируемую функцию переданное в качестве аргумента количество раз.

# import functools
#
# def repeater(repeat=1):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for i in range(1, repeat + 1):
#                 print(f'{i}-й запуск функции.')
#                 value = func(*args, **kwargs)
#             return value
#         return wrapper
#     return decorator
#
#
# @repeater(repeat=7)
# def beegeek():
#     print('beegeek')
#
# beegeek()


# def add_smiley_face(face):
#     def smiley_face_decorator(func):
#         def wrapper():
#             return func() + ' ' + face
#         return wrapper
#     return smiley_face_decorator
#
# @add_smiley_face('^~^')
# def beegeek():
#     return 'beegeek'
#
# print(beegeek())


# def make_upper(func):
#     def wrapper():
#         return func().upper()
#     return wrapper
#
# def del_first_char(func):
#     def wrapper():
#         return func()[1:]
#     return wrapper
#
# def reverse(func):
#     def wrapper():
#         return func()[::-1]
#     return wrapper
#
# @reverse
# @del_first_char
# @make_upper
# def beegeek():
#     return 'beegeek'
#
# print(beegeek())
#
# import functools
# def prefix(string, to_the_end=False):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kwargs):
#             res = func(*args, **kwargs)
#             if to_the_end:
#                 return f'{res}{string}'
#             else:
#                 return f'{string}{res}'
#         return wrapper
#     return decorator
#
#
# import functools
#
# def prefix(string: str, to_the_end: bool=False):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             if to_the_end:
#                 return func(*args, **kwargs) + string
#             return string + func(*args, **kwargs)
#         return wrapper
#     return decorator
#
#
# # INPUT DATA:
#
# # TEST_1:
# @prefix('€')
# def get_bonus():
#     return '2000'
#
#
# print(get_bonus())
#
#
# # TEST_2:
# @prefix('$$$', to_the_end=True)
# def get_bonus():
#     return '2000'
#
#
# print(get_bonus())
#
#
# # TEST_3:
# @prefix(' online-school', to_the_end=True)
# def beegeek():
#     '''beegeek docs'''
#     return 'beegeek'
#
#
# print(beegeek.__name__)
# print(beegeek.__doc__)
# print(beegeek())
#
#
# # TEST_4:
# @prefix('online-school ')
# def beegeek():
#     '''beegeek docs'''
#     return 'beegeek'
#
#
# print(beegeek.__name__)
# print(beegeek.__doc__)
# print(beegeek())
#
#
# # TEST_5:
# @prefix('online-school ')
# def make_lower(string, lower=True):
#     '''makes string upper or lower'''
#     if lower:
#         return string.lower()
#     return string.upper()
#
#
# print(make_lower.__name__)
# print(make_lower.__doc__)
# print(make_lower('beegeek', False))
#
#
# # TEST_6:
# @prefix(' rocks', True)
# def make_lower(string, lower=True):
#     '''makes string upper or lower'''
#     if lower:
#         return string.lower()
#     return string.upper()
#
#
# print(make_lower.__name__)
# print(make_lower.__doc__)
# print(make_lower('Beegeek'))
#
#
# # TEST_7:
# @prefix('online-school ')
# def make_lower(string, lower=True):
#     if lower:
#         return string.lower()
#     return string.upper()
#
#
# print(make_lower('beegeek', lower=False))

# import functools
# def make_html(tag):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             return f'<{tag}>{func(*args, **kwargs)}</{tag}>'
#         return wrapper
#     return decorator
#
# from functools import wraps
#
# def make_html(tag):
#     return lambda fun : wraps(fun)(lambda *a, **k: f'<{tag}>{fun(*a, **k)}</{tag}>')
#
#
# # INPUT DATA:
#
# # TEST_1:
# @make_html('del')
# def get_text(text):
#     return text
#
#
# print(get_text('Python'))
#
#
# # TEST_2:
# @make_html('i')
# @make_html('del')
# def get_text(text):
#     return text
#
#
# print(get_text(text='decorators are so cool!'))
#
#
# # TEST_3:
# @make_html('small')
# @make_html('mark')
# @make_html('i')
# @make_html('del')
# def get_text(text):
#     return text
#
#
# print(get_text('ANRIANRIANRI'))
#
#
# # TEST_4:
# @make_html('mark')
# @make_html('mark')
# def get_text(text):
#     return text * 2
#
#
# print(get_text(text='doubleit'))
#
#
# # TEST_5:
# @make_html('mark')
# @make_html('mark')
# @make_html('mark')
# def beegeek():
#     '''beegeek docs'''
#     return 'beegeek'
#
#
# print(beegeek())
# print(beegeek.__name__)
# print(beegeek.__doc__)


# import functools
# def repeat(times):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for i in range(1, times + 1):
#                 val = func(*args, **kwargs)
#             return val
#         return wrapper
#     return decorator
#
#
# # INPUT DATA:
#
# # TEST_1:
# @repeat(3)
# def say_beegeek():
#     '''documentation'''
#     print('beegeek')
#
#
# say_beegeek()
#
#
# # TEST_2:
# @repeat(4)
# def say_beegeek():
#     '''documentation'''
#     print('beegeek')
#
#
# print(say_beegeek.__name__)
# print(say_beegeek.__doc__)
#
#
# # TEST_3:
# @repeat(1)
# def beegeek():
#     '''beegeek docs'''
#     print('beegeek')
#
#
# print(beegeek.__name__)
# print(beegeek.__doc__)
# beegeek()
#
#
# # TEST_4:
# @repeat(10)
# def beegeek():
#     '''beegeek docs'''
#     print('beegeek')
#
#
# print(beegeek.__name__)
# print(beegeek.__doc__)
# beegeek()
#
#
# # TEST_5:
# @repeat(10)
# def add(a, b):
#     '''sum of two numbers'''
#     return a + b
#
#
# print(add.__name__)
# print(add.__doc__)
# print(add(10, b=20))
#
# # TEST_6:
# counter = 0
#
#
# @repeat(11)
# def change_counter():
#     global counter
#     counter += 1
#     print(counter)
#
#
# print(change_counter.__name__)
# print(change_counter.__doc__)
# change_counter()
# print(counter)
#
#
# # TEST_7:
# @repeat(5)
# def say(word):
#     print(word)
#
#
# say(word="Hey!")

#
# import functools
#
# def strip_range(start, end, char='.'):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             val = func(*args, *kwargs)
#             if isinstance(val, str):
#                 return val[:start] + len(val[start:end]) * char + val[end:]
#             return val
#         return wrapper
#     return decorator


# from functools import wraps
#
# def strip_range(start, end, char='.'):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             return result[:start] + char * len(result[start:end]) + result[end:]
#         return wrapper
#     return decorator
#
#
# # INPUT DATA:
#
# # TEST_1:
# @strip_range(3, 5)
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek())
#
#
# # TEST_2:
# @strip_range(3, 20, '_')
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek())
#
#
# # TEST_3:
# @strip_range(20, 30)
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek())
#
#
# # TEST_4:
# @strip_range(1, 2, '-')
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek())
#
#
# # TEST_5:
# @strip_range(100, 200, '=')
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek())
#
#
# # TEST_6:
# @strip_range(0, 300, '=')
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek())
#
#
# # TEST_7:
# @strip_range(0, 4, '=')
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek())
#
#
# # TEST_8:
# @strip_range(0, 1)
# def beegeek(word, end=" "):
#     """This is... Requiem. What you are seeing is indeed the truth"""
#     return word + end
#
#
# print(beegeek("beegee", end="k"))
# print(beegeek.__name__)
# print(beegeek.__doc__)

# from functools import wraps
# def returns(datatype):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             val = func(*args, **kwargs)
#             if isinstance(val, datatype):
#                 return val
#             raise TypeError
#         return wrapper
#     return decorator
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# @returns(int)
# def add(a, b):
#     return a + b
#
# print(add(10, 5))
#
# # TEST_2:
# @returns(int)
# def add(a, b):
#     return a + b
#
# try:
#     print(add('199', '1'))
# except TypeError as e:
#     print(type(e))
#
# # TEST_3:
# @returns(list)
# def beegeek():
#     '''beegeek docs'''
#     return 'beegeek'
#
# print(beegeek.__name__)
# print(beegeek.__doc__)
#
# try:
#     print(beegeek())
# except TypeError as e:
#     print(type(e))
#
# # TEST_4:
# @returns(list)
# def append_this(li, elem):
#     '''append_this docs'''
#     return li + [elem]
#
# print(append_this.__name__)
# print(append_this.__doc__)
# print(append_this([1, 2, 3], elem=4))
#
# # TEST_5:
# @returns(tuple)
# def append_this(li, elem):
#     '''append_this docs'''
#     return li + [elem]
#
# print(append_this.__name__)
# print(append_this.__doc__)
#
# try:
#     print(append_this([1, 2, 3], [4, 5, 6]))
# except TypeError as e:
#     print(type(e))
#
# # TEST_6:
# @returns(int)
# def add(a, b):
#     return a + b
#
# print(add(a=10, b=5))

import functools
import sys
# def takes(*args_t):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args_w, **kwargs):
#             flag = True
#             for a in args_w:
#                 if type(a) in args_t:
#                     flag = True
#                 else:
#                     raise TypeError
#             for k in kwargs.values():
#                 if type(k) in args_t:
#                     flag = True
#                 else:
#                     raise TypeError
#             return func(*args_w, **kwargs)
#         return wrapper
#     return decorator
#
#
# import functools
#
# def takes(*datatypes):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, ** kwargs):
#             if any(type(i) not in datatypes for i in (*args, *kwargs.values())):
#                 raise TypeError
#             return func(*args, ** kwargs)
#         return wrapper
#     return decorator
#
#
# # INPUT DATA:
#
# # TEST_1:
# @takes(int, str)
# def repeat_string(string, times):
#     return string * times
#
#
# print(repeat_string('bee', 3))
#
#
# # TEST_2:
# @takes(list, bool, float, int)
# def repeat_string(string, times):
#     return string * times
#
#
# try:
#     print(repeat_string('bee', 4))
# except TypeError as e:
#     print(type(e))
#
#
# # TEST_3:
# @takes(list)
# def append_this(li, elem):
#     '''append_this docs'''
#     return li + [elem]
#
#
# print(append_this.__name__)
# print(append_this.__doc__)
#
# try:
#     print(append_this([1, 2], [3, 4]))
# except TypeError as e:
#     print(type(e))
#
#
# # TEST_4:
# @takes(list)
# def append_this(li, elem):
#     '''append_this docs'''
#     return li + [elem]
#
#
# print(append_this.__name__)
# print(append_this.__doc__)
#
# try:
#     print(append_this([1, 2], 3))
# except TypeError as e:
#     print(type(e))
#
#
# # TEST_5:
# @takes(str, int, list)
# def add(a, b):
#     '''add docs'''
#     return a + b
#
#
# print(add.__name__)
# print(add.__doc__)
#
# try:
#     print(add('a', 'b'))
# except TypeError as e:
#     print(type(e))
#
#
# # TEST_6:
# @takes(list, int, tuple, str)
# def add(a, b):
#     '''add docs'''
#     return a + b
#
#
# print(add.__name__)
# print(add.__doc__)
#
# try:
#     print(add(a='a', b='c'))
# except TypeError as e:
#     print(type(e))
#
#
# # TEST_7:
# @takes(list, int, tuple, str)
# def add(a, b):
#     '''add docs'''
#     return a + b
#
#
# print(add.__name__)
# print(add.__doc__)
#
# try:
#     print(add(1, b=2))
# except TypeError as e:
#     print(type(e))
#
#
# # TEST_8:
# @takes(list, int, float, str)
# def add(a, b):
#     '''add docs'''
#     return a + b
#
#
# print(add.__name__)
# print(add.__doc__)
#
# try:
#     print(add((1, 2), (3, 4, 5)))
# except TypeError as e:
#     print(type(e))
#
#
# # TEST_9:
# @takes()
# def beegeek():
#     '''beegeek docs'''
#     return 'beegeek'
#
#
# print(beegeek())
#
#
# # TEST_10:
# @takes(str)
# def beegeek(word):
#     return word
#
#
# print(beegeek(word="beegeek"))
#
#
# # TEST_11:
# @takes(str)
# def beegeek(word, repeat):
#     return word * repeat
#
#
# try:
#     print(beegeek('beegeek', repeat=2))
# except TypeError as e:
#     print(type(e))



# import functools
# def add_attrs(*args_a, **kwargs_a):
#     def decorator(func):
#         for k,v in kwargs_a.items():
#             func.__dict__[k] = v
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             return func(*args, **kwargs)
#
#         return wrapper
#     return decorator
#
#
# # INPUT DATA:
#
# # TEST_1:
# @add_attrs(attr1='bee', attr2='geek')
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek.attr1)
# print(beegeek.attr2)
#
#
# # TEST_2:
# @add_attrs(attr2='geek')
# @add_attrs(attr1='bee')
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek.attr1)
# print(beegeek.attr2)
# print(beegeek.__name__)
#
#
# # TEST_3:
# @add_attrs(attr1='bee', attr2='geek', attr3='stepik')
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek.attr1)
# print(beegeek.attr2)
# print(beegeek.attr3)
# print(beegeek.__name__)
# print(beegeek.__doc__)
#
#
# # TEST_4:
# @add_attrs(at1=10, at2=20, at3=30, at4=40, atf=50)
# def add(a, b):
#     '''add docs'''
#     return a + b
#
#
# print(add.at1)
# print(add.at2)
# print(add.at3)
# print(add.__name__)
# print(add.__doc__)
# print(add(1, 2))
# print(add(b=12, a=13))
# print(add.at4)
# print(add.atf)
#
#
# # TEST_5:
# @add_attrs(func_attr='i am attribute')
# def func(a, b):
#     '''func docs'''
#     return
#
#
# print(func.func_attr)

#
# import functools
# def ignore_exception(*args):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*aargs, **kkwargs):
#             try:
#                 return func(*aargs, **kkwargs)
#             except (args) as e:
#                 print(f'Исключение {e.__class__.__name__} обработано')
#
#
#         return wrapper
#     return decorator
#
#
# # INPUT DATA:
#
# # TEST_1:
# @ignore_exception(ZeroDivisionError, TypeError, ValueError)
# def f(x):
#     return 1 / x
#
#
# f(0)
#
# # TEST_2:
# min = ignore_exception(ZeroDivisionError)(min)
#
# try:
#     print(min(1, '2', 3, [4, 5]))
# except Exception as e:
#     print(type(e))
#
#
# # TEST_3:
# @ignore_exception()
# def func():
#     '''func docs'''
#     raise ValueError
#
#
# try:
#     func()
# except Exception as e:
#     print(type(e))
#
#
# # TEST_4:
# @ignore_exception(TypeError)
# def func():
#     '''func docs'''
#     raise ValueError
#
#
# try:
#     func()
# except Exception as e:
#     print(type(e))
#
#
# # TEST_5:
# @ignore_exception(ValueError, TypeError, NameError)
# def func():
#     '''func docs'''
#     raise ValueError
#
#
# print(func.__name__)
# print(func.__doc__)
#
# try:
#     func()
# except Exception as e:
#     print(type(e))
#
#
# # TEST_6:
# @ignore_exception(ValueError, TypeError, NameError)
# def func():
#     '''func docs'''
#     raise NameError
#
#
# try:
#     func()
# except Exception as e:
#     print(type(e))
#
#
# # TEST_7:
# @ignore_exception(ValueError, TypeError, ZeroDivisionError, NameError)
# def func():
#     '''func docs'''
#     raise ZeroDivisionError
#
#
# try:
#     func()
# except Exception as e:
#     print(type(e))
#
#
# # TEST_8:
# @ignore_exception(ValueError, NameError, ZeroDivisionError, TypeError)
# def func(a, b, c):
#     '''func docs'''
#     raise NameError
#
#
# try:
#     func(1, 2, c=10)
# except Exception as e:
#     print(type(e))
#
#
# # TEST_9:
# @ignore_exception(ValueError, TypeError, ZeroDivisionError, NameError)
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek())


# import functools
#
# class MaxRetriesException(Exception):
#     pass
#
# def retry(times):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for i in range(1, times +1):
#                 try:
#                     return func(*args, **kwargs)
#                 except: pass
#             raise MaxRetriesException
#
#
#         return wrapper
#     return decorator
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# @retry(3)
# def no_way():
#     raise ValueError
#
# try:
#     no_way()
# except Exception as e:
#     print(type(e))
#
# # TEST_2:
# @retry(8)
# def beegeek():
#     beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
#     if beegeek.calls < 5:
#         raise ValueError
#     print('beegeek')
#
# beegeek()
#
# # TEST_3:
# @retry(6)
# def beegeek():
#     beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
#     if beegeek.calls < 7:
#         raise ValueError
#     print('beegeek')
#
# try:
#     beegeek()
# except Exception as e:
#     print(type(e))
#
# # TEST_4:
# @retry(7)
# def beegeek():
#     beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
#     if beegeek.calls < 7:
#         raise ValueError
#     print('beegeek')
#
# try:
#     beegeek()
# except Exception as e:
#     print(type(e))
#
# # TEST_5:
# @retry(5)
# def beegeek():
#     beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
#     if beegeek.calls < 7:
#         raise ValueError
#     print('beegeek')
#
# try:
#     beegeek()
# except Exception as e:
#     print(type(e))
#
# # TEST_6:
# @retry(5)
# def beegeek():
#     beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
#     if beegeek.calls < 7:
#         raise ValueError
#     print('beegeek')
#
# try:
#     beegeek()
# except Exception as e:
#     print(type(e))
#
# # TEST_7:
# @retry(9)
# def add(a, b):
#     add.calls = add.__dict__.get('calls', 0) + 1
#     if add.calls < 10:
#         raise ValueError
#     return a + b
#
# try:
#     print(add(10, 20))
# except Exception as e:
#     print(type(e))
#
# # TEST_8:
# @retry(10)
# def add(a, b):
#     add.calls = add.__dict__.get('calls', 0) + 1
#     if add.calls < 10:
#         raise ValueError
#     return a + b
#
# try:
#     print(add(10, 30))
# except Exception as e:
#     print(type(e))
#
# # TEST_9:
# @retry(100)
# def add(a, b):
#     add.calls = add.__dict__.get('calls', 0) + 1
#     if add.calls < 10:
#         raise ValueError
#     return a + b
#
# try:
#     print(add(40, 10))
# except Exception as e:
#     print(type(e))
#
# # TEST_10:
# @retry(1)
# def add(a, b):
#     add.calls = add.__dict__.get('calls', 0) + 1
#     if add.calls < 10:
#         raise ValueError
#     return a + b
#
# try:
#     print(add(40, 20))
# except Exception as e:
#     print(type(e))
#
# # TEST_11:
# @retry(10)
# def calculate(a, b, c):
#     calculate.calls = calculate.__dict__.get('calls', 0) + 1
#     if calculate.calls < 4:
#         raise ValueError
#     return a + b + c
#
# try:
#     print(calculate(1, 2, c=3))
# except Exception as e:
#     print(type(e))
#
# # TEST_12:
# @retry(3)
# def calculate(a, b, c):
#     calculate.calls = calculate.__dict__.get('calls', 0) + 1
#     if calculate.calls < 4:
#         raise ValueError
#     return a + b + c
#
# try:
#     print(calculate(b=1, a=2, c=3))
# except Exception as e:
#     print(type(e))
#
# # TEST_13:
# @retry(4)
# def calculate(a, b, c):
#     calculate.calls = calculate.__dict__.get('calls', 0) + 1
#     if calculate.calls < 4:
#         raise ValueError
#     return a + b + c
#
# try:
#     print(calculate(b=2, a=2, c=3))
# except Exception as e:
#     print(type(e))
#
# # TEST_14:
# @retry(99)
# def calculate(a, b, c):
#     calculate.calls = calculate.__dict__.get('calls', 0) + 1
#     if calculate.calls < 4:
#         raise ValueError
#     return a + b + c
#
# try:
#     print(calculate(10, b=1, c=2))
# except Exception as e:
#     print(type(e))
#
# # TEST_15:
# @retry(99)
# def calculate(a, b, c):
#     """Calculate something"""
#     calculate.calls = calculate.__dict__.get('calls', 0) + 1
#     if calculate.calls < 4:
#         raise ValueError
#     return a + b + c
#
# print(calculate.__name__)
# print(calculate.__doc__)
# try:
#     print(calculate(2000, b=1, c=4))
# except Exception as e:
#     print(type(e))


# print(int('123'))
# print(int('123', base=5))
# print(int('1001', base=2))
# print(int('A12B', base=16))


# from functools import partial
#
# basetwo = partial(int, base=2)
#
# print(basetwo('101'))
# print(basetwo('1000'))
# print(basetwo('11111'))


# from functools import partial
#
# def pretty_print(text, symbol, count):
#     print(symbol * count)
#     print(text)
#     print(symbol * count)
#
# star_pretty_print = partial(pretty_print, 'Hi!!!', symbol='*')
#
# star_pretty_print(count=7)
#
# print(star_pretty_print.args)
# print(star_pretty_print.keywords)
#
# star_pretty_print.func('Исходная функция', symbol='~', count=20)

#
# from functools import partial
#
# def add(a, b):
#     return a + b
#
# add_one = partial(add, 1)
#
# print(add_one(2, 3))

# from functools import partial
#
# def add(a, b):
#     '''documentation'''
#     return a + b
#
# add_one = partial(add, 1)
#
# print(add_one.__name__)
# print(add_one.__doc__)

# from functools import partial
#
# def add(a, b):
#     return a + b
#
# add_one = partial(add, 1)
#
# print(add_one.func.__name__)
# print(add_one.func(2, 3))


# from functools import partial, update_wrapper
#
# def add(a, b):
#     '''documentation'''
#     return a + b
#
# add_one = partial(add, 1)
# update_wrapper(add_one, add)
#
# print(add_one.__name__)
# print(add_one.__doc__)


# from functools import partial
#
# beegeek = partial(print, 'beegeek')
#
# beegeek('stepik', 'python')

# from functools import partial
#
# beegeek = partial(print, 'bee', 'geek', end='!')
#
# print(beegeek.args)
# print(beegeek.keywords)


# from functools import partial
#
# beegeek = partial(print, 'beegeek', sep=', ')
#
# beegeek('stepik', 'python')

# from functools import partial
#
# beegeek = partial(print, sep=', ')
#
# beegeek('beegeek', 'stepik', 'python', sep='-')


# from functools import partial
#
# def send_email(name, email_address, text):
#     return f'В письме для {name} по электроному адресу {email_address} нписано так - {text}'
#
#
# to_Timur = partial(send_email, 'Тимур',  'timyrik20@beegeek.ru')
#
# send_an_invitation = partial(send_email, text='Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....')
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# print(to_Timur('когда курс?'))
#
# # TEST_2:
# print(to_Timur('Тимур, привет, я на егэ, помоги решить 13 задачу'))
#
# # TEST_3:
# print(to_Timur('хочу курс по искусственным интеллектам и криптовалютам бесплатно и завтра'))
#
# # TEST_4:
# try:
#     to_Timur()
# except:
#     print('ok')
#
# # TEST_5:
# try:
#     to_Timur('первое', 'второе')
# except:
#     print('ok')
#
# # TEST_6:
# try:
#     to_Timur('первое', 'второе', 'третье')
# except:
#     print('ok')
#
# # TEST_7:
# try:
#     to_Timur('beegeek')
#     print('ok')
# except:
#     print('ne ok')
#
# # TEST_8:
# print(send_an_invitation("Тимур", "timyrik20@beegeek.ru"))
#
# # TEST_9:
# try:
#     print(send_an_invitation("Тимур"))
# except:
#     print("Ошибка, и где же? Хм-м-м")
#
# # TEST_10:
# print(to_Timur('Здравствуйте! Я Таня из компании Орифлэйм. Хочу предложить вам новую линейку курсов от Поколения Python'))
#
# # TEST_11:
# print(to_Timur('This is... Requiem. What you are seeing is indeed the truth.'))


# from functools import lru_cache
#
#
# @lru_cache()
# def add_one(number):
#     print(number + 1, end=' ')
#
#
# numbers = [1, 2, 3, 1, 3, 4, 4, 1]
#
# for i in numbers:
#     add_one(i)


# from functools import lru_cache
#
# @lru_cache()
# def average(numbers):
#     return sum(numbers) / len(numbers)
#
# numbers = [1, 2, 3, 4, 5]
#
# print(average(numbers))
# print(average(numbers))

# from functools import lru_cache
#
# @lru_cache(typed=True)
# def return_this(a, b):
#     return a, b
#
# print(return_this(1, 1))
# print(return_this(True, True))
# print(return_this(1.0, 1.0))


# import sys
# from functools import lru_cache
#
#
# def dima(x):
#     print(''.join(sorted(x)))
#
#
# for i in sys.stdin:
#     dima(i.strip())

# import sys
# from functools import lru_cache
#
# @lru_cache()
# def sorting_string(text: str) -> str:
#     return ''.join(sorted(text))
#
#
# for i in sys.stdin:
#     print(sorting_string(i.strip()))
#
#
#
# a = 'tutorial'
# print(sorting_string(a))


