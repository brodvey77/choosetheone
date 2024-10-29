def null_decorator(func):
    return func


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
