# def product(n, func):
#     result = 1
#     for number in range(1, n):
#         result *= func(number)
#     return  result
#
# def square(x):
#     return x * x
#
# print(product(4, square))
#
# def cube(x):
#     return x * x * x
#
# print(product(4, cube))

# def my_function(a, b, func):
#     result = func([a, b])
#     return result
#
# print(my_function(7, 3, sum))

# using nested function
from random import choice

# def make_color():
#     def get_color():
#         colors = ('red', 'green', 'yellow')
#         color = choice(colors)
#         return color
#     return get_color
#
# my_color = make_color()
# print(my_color())
#
# second_color = make_color()
# print(second_color())
#
# third_color = make_color()
# print(third_color())


# inner funcrtion can access outer function scope
# def colorize1(thing):
#     def get_color():
#         colors = ('red', 'green', 'yellow')
#         color = choice(colors)
#         return color + ' ' + thing
#
#     return get_color
#
# print(colorize1('apple')())
#
# colorize_dog = colorize1('dog')
# print(colorize_dog())

# DECORATIONS

# def simple_function():
#     print('Simple function code')
#
# simple_function()

# def decorator_function(original_function):
#     def wrap_function():
#         print('Some code before old cod')
#         original_function()
#         print('Some code after old cod')
#     return wrap_function

# decorated_function = decorator_function(simple_function)
#
# decorated_function()
#
# @decorator_function
# def simple_function():
#     print('Simple function code')
#
# simple_function()

def make_complement(func):
    def wrapper(*args, **kwargs):
        print('Nice to meet you')
        func(*args, **kwargs)
        print('You look great!')
    return wrapper


@make_complement
def ask_name():
    print('What is your name?')

ask_name()

@make_complement
def say_name(name):
    print('My name is ' + name)

say_name('Jack')

@make_complement
def order(food, drink):
    print(f'Give me {food}, and {drink}')

order(food='Chips', drink='kola')




