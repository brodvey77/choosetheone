# import random
#
# n = int(input())    # количество попыток
#
# result = {1: 'Орел', 2: 'Решка'}
#
# for i in range(n):
#     print(result[random.randrange(1, 3)])

# import random
# n = int(input())    # количество попыток
# for i in range(n):
#     print(random.randint(1, 6))


# import random
#
# length = int(input())    # длина пароля
# my_list = []
# while len(my_list) != length:
#     v = random.randint(65, 122)
#     if v in [91, 92, 93, 94, 95, 96]:
#         continue
#     else:
#         my_list.append(chr(v))
#         print(chr(v), end='')


# import random
#
# length = int(input())    # длина пароля
# password = ''
# for i in range(length):
#     password += [chr(random.randint(65, 90)), chr(random.randint(97, 122))][random.randint(0, 1)]
# print(password)

# import random
#
# my_list = []
#
# while len(my_list) != 7:
#     v = random.randint(1, 49)
#     if v not in my_list:
#         my_list.append(v)
# for _ in sorted(my_list):
#     print(_, end=' ')

# import random
#
# s = set()
#
# while len(s) < 7:
#     s.add(random.randint(1, 49))
#
# print(*sorted(s))

# Приведенный ниже код:
#
# import string
#
# print(string.ascii_letters)
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.digits)
# print(string.hexdigits)
# print(string.octdigits)
# print(string.punctuation)
# print(string.printable)
# выводит:
#
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# abcdefghijklmnopqrstuvwxyz
# 0123456789
# 0123456789abcdefABCDEF
# 01234567
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ \t\n\r\x0b\x0c

# import random
# def generate_ip():
#     s = ''
#     for i in range(4):
#         s += str(random.randint(0, 255)) + '.'
#     return s[:-1]
#
# print(generate_ip())


# from random import randrange as r
#
# def generate_ip():
#     return f'{r(256)}.{r(256)}.{r(256)}.{r(256)}'

# from random import randrange as r
# import string
# from random import choice as ch
#
#
# def generate_index():
#     return ch(string.ascii_uppercase) + ch(string.ascii_uppercase) + str(r(100)) + '_' + str(r(100)) + ch(
#         string.ascii_uppercase) + ch(string.ascii_uppercase)
#
#
# print(generate_index())

# import random
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
#
# for i in matrix:
#     random.shuffle(i)


# import random
#
# matrix = [[int(random.randrange(10)) for i in range(7)] for _ in range(100)]
#
# for i in matrix:
#     while i[0] == 0:
#         random.shuffle(i)
#     for j in i:
#         print(j, end='')
#     print()


# from random import sample as r
#
# print(*r(range(int(1e6), int(1e7)), 100), sep='\n')


# from random import shuffle as sh
#
# s = list(input())
# sh(s)
# print(''.join(s))


# import random
#
# matrix = [[int(random.randrange(1, 76)) for i in range(5)] for _ in range(5)]
#
# for i in range(5):
#     for j in range(5):
#         if i == j and j == 5 - i - 1:
#             matrix[i][j] = 0
#         print(str(matrix[i][j]).ljust(3), end='')
#     print()

# import random
#
# my_list = [i for i in range(1, 76)]
# random.shuffle(my_list)
# c = 0
# matrix = []
# for i in range(len(my_list)):
#     if len(my_list[c:c + 5]) != 0:
#         matrix.append(my_list[c:c + 5])
#     c = c + 5
# for i in range(5):
#     for j in range(5):
#         if i == j and j == 5 - i - 1:
#             matrix[i][j] = 0
#         print(str(matrix[i][j]).ljust(3), end='')
#     print()

# from random import sample
#
# numbers = sample(list(range(1, 76)), 25)
# bingo = [numbers[i:i + 5] for i in range(0, 21, 5)]
# bingo[2][2] = 0
#
# for i in range(5):
#     for j in range(5):
#         print(str(bingo[i][j]).ljust(3), end=' ')
#     print()

# import random
#
# n = int(input())
# list_1 = [input() for i in range(n)]
# list_2 = list_1.copy()
# flag = True
# s = 0
# while flag:
#     random.shuffle(list_2)
#     for i in range(len(list_1)):
#         if list_1[i] != list_2[i]:
#             s += 1
#         else:
#             s = 0
#     if s == len(list_1):
#         flag = False
#
# for i in range(len(list_1)):
#     print(f'{list_1[i]} - {list_2[i]}')

# from random import choice
#
# names, rel, tmp = {input() for _ in range(int(input()))}, {}, 0
# for name in names.copy():
#     if names == {name}:
#         rel[tmp], rel[name] = name, rel[tmp]
#     else:
#         rand_name = choice(list(names - {name}))
#         rel[name] = rand_name
#         names -= {rand_name}
#         tmp = name
# [print(k, '-', v) for k, v in rel.items()]
import random

# n, m = int(input()), int(input())
# l_list = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
#
# def generate_password(length):
#     return ''.join(random.sample(l_list, length))
#
# def generate_passwords(count, length):
#     for _ in range(count):
#         print(generate_password(length))
#
# generate_passwords(n, m)
#
#
#
# import string, random
#
# def generate_password(length):
#     symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits[2:]
#     symbols = ''.join([symbol for symbol in symbols if symbol not in "lIoO"])
#     return ''.join(random.sample(symbols, length))
#
# def generate_passwords(count, length):
#     return [generate_password(length) for _ in range(count)]
#
# n, m = int(input()), int(input())
# print(*generate_passwords(n, m), sep='\n')

# import string
#
# n, m = int(input()), int(input())
# l_list = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
# a = string.ascii_uppercase
# b = string.ascii_lowercase
# c = string.digits
#
#
# def gen(pasw):
#     counter = 0
#     counter_a = 0
#     counter_b = 0
#     counter_c = 0
#     for i in a:
#         if i in pasw:
#             counter_a += 1
#     for i in b:
#         if i in pasw:
#             counter_b += 1
#     for i in c:
#         if i in pasw:
#             counter_c += 1
#     if counter_a > 0:
#         counter_a = 1
#     if counter_b > 0:
#         counter_b = 1
#     if counter_c > 0:
#         counter_c = 1
#     counter = counter_a + counter_b + counter_c
#     return counter
#
#
# def generate_password(length):
#     s = ''.join(random.sample(l_list, m))
#     while gen(s) != 3:
#         s = ''.join(random.sample(l_list, m))
#     return s
#
#
# def generate_passwords(count, length):
#     for _ in range(count):
#         print(generate_password(length))
#
#
# generate_passwords(n, m)


# n = 10**6
# k = 0
# s0 = 16
# for _ in range(n):
#     x = random.uniform(-2, 2)
#     y = random.uniform(-2, 2)
#
#     if x**3 + y**4 + 2 >= 0 and 3*x + y**2 <= 2:
#         k += 1
#
# print((k/n)*s0)

# import random
# n = 10**6
# k = 0
# s0 = 4
# for _ in range(n):
#     x = random.uniform(-1, 1)
#     y = random.uniform(-1, 1)
#
#     if x**2 + y**2 <= 1:
#         k += 1
#
# print((k/n)*s0)


# BOGOSORT

# import random
#
# def is_sort(nums):                   # отсортирован ли список?
#     for i in range(len(nums) - 1):
#         if nums[i] > nums[i + 1]:
#             return False
#     return True
#
# def bogosort(nums):                  # реализация алгоритма болотной сортировки
#     while not is_sort(nums):
#         random.shuffle(nums)
#     return nums
#
# numbers = list(range(13))
# random.shuffle(numbers)              # перемешиваем начальный список
# print(numbers)                       # выводим начальный список
#
# sorted_numbers = bogosort(numbers)
#
# print(sorted_numbers)                # выводим отсортированный список


# num = 0.1 + 0.1 + 0.1
# eps = 0.000000001           # точность сравнения
#
# if abs(num - 0.3) < eps:    # число num отличается от числа 0.3 менее чем 0.000000001
#     print('YES')
# else:
#     print('NO')

# from decimal import *
#
# num = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
#
# if num == 0:
#     print('YES')
# else:
#     print('NO')

# from decimal import Decimal as D
#
# s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 ' \
#     '5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 ' \
#     '9.60 8.86 2.73 5.83 6.50'
#
# numbers = [D(i) for i in s.split()]
#
# minimum = min(numbers)
# maximum = max(numbers)
#
# print(minimum + maximum)



# from decimal import *
#
# s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 ' \
#     '8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 ' \
#     '5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'
#
# numbers = sorted([Decimal(i) for i in s.split()], reverse=True)
#
# print(sum(numbers))
# print(*sorted(numbers[:5]))

# from decimal import *
#
# s = input()
# number = Decimal(s)
# num = list(number.as_tuple().digits)
# if '0' in s:
#     num.append(0)
# minimum = min(num)
# maximum = max(num)
# print(minimum + maximum)


# from decimal import Decimal
# d = Decimal(input())
# number = Decimal.exp(d) + Decimal.ln(d) + Decimal.log10(d) + Decimal.sqrt(d)
# print(number)


# from decimal import Decimal
# # d = Decimal(input())
# # print(d.exp() + d.ln() + d.log10() + d.sqrt())

#
# from fractions import *
#
# num = Fraction(7, 71)
#
# if num * 71 == 7:
#     print('YES')
# else:
#     print('NO')
#
# print(num * 71)
# print(num)


# from fractions import Fraction
#
# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67',
#            '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29',
#            '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75',
#            '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20',
#            '2.58', '2.46']

# s = [Fraction(i) for i in numbers]
#
# for i in range(len(numbers)):
#     print(f'{numbers[i]} = {s[i]}')


# for num in numbers:
#     print(f'{num} = {Fraction(num)}')


# from fractions import Fraction
#
# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 ' \
#     '1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 ' \
#     '0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
# numbers = [Fraction(i) for i in s.split()]
# minimum = min(numbers)
# maximum = max(numbers)
#
# print(min(numbers)+max(numbers))
# print(maximum, maximum)

# from fractions import Fraction as F
#
# n, m = int(input()), int(input())
#
# print(F(n)/F(m))


# from fractions import Fraction as F
# n, m = input(), input()
#
# print(f'{n} + {m} = {F(n) + F(m)}')
# print(f'{n} - {m} = {F(n) - F(m)}')
# print(f'{n} * {m} = {F(n) * F(m)}')
# print(f'{n} / {m} = {F(n) / F(m)}')

# from fractions import Fraction as F
# n = int(input())
# lst = [F(1, i)**2 for i in range(1, n + 1)]
#
# print(sum(lst))


# from fractions import Fraction as F
# from math import factorial as Fac
# n = int(input())
# lst = [F(1, Fac(i)) for i in range(1, n + 1)]
#
# print(sum(lst))

# from fractions import Fraction as F
# import math
# n = int(input())
# lst = [i for i in range(1, n + 1)]
# nums = []
# for i in lst:
#     for j in range(n, 1, -1):
#         if i + j == n and math.gcd(i, j) == 1 and i < j:
#             nums.append(F(i)/F(j))
# print(max(nums))

# from fractions import Fraction as F
# from math import gcd
#
# n = int(input())
# a = n // 2
# b = n - a
# while gcd(a, b) != 1:
#     a -= 1
#     b += 1
# print(F(a, b))


# from fractions import Fraction as F
# import math
# n = int(input())
# lst = [i for i in range(1, n + 1)]
# nums = []
# for i in lst:
#     for j in range(n, 1, -1):
#         if F(i) < F(j):
#             nums.append(F(i)/F(j))
# a = set(nums)
#
# print(*sorted(a), sep='\n')

# a, b = complex(input()), complex(input())
# print(f'{a} + {b} = {a + b}')
# print(f'{a} - {b} = {a - b}')
# print(f'{a} * {b} = {a * b}')

# numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j,
#            -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
# modules = {}
#
# for i in numbers:
#     modules[abs(i)] = i
# print(modules[max(modules)], max(modules), sep='\n')

# n = int(input())
# z1, z2 = complex(input()), complex(input())
#
# result = z1**n + z2**n + z1.conjugate()**(n) + z2.conjugate()**(n+1)
# print(complex(result))



# import turtle
#
# turtle.Screen().addshape('rocketship.gif')  # регистрируем изображение
# turtle.shape('rocketship.gif')              # устанавливаем изображение
#
#
# for _ in range(4):
#   turtle.forward(150)
#   turtle.left(90)
# for i in range(10):
#     turtle.forward(10)
#     for _ in range(360):
#         turtle.left(1)
#         turtle.forward(1)
#     turtle.right(36)


# def rectangle(width, height):
#     turtle.forward(width)
#     turtle.left(90)
#     turtle.forward(height)
#     turtle.left(90)
#     turtle.forward(width)
#     turtle.left(90)
#     turtle.forward(height)
#     turtle.left(90)
#
# w, h = int(input()), int(input())
# rectangle(w, h)

# import turtle
# def triangle(side):
#     for i in range(3):
#         turtle.forward(side)
#         turtle.left(120)
#
# n = int(input('Input your side >> '))
# triangle(n)
#
# import turtle
#
# def square(side):
#     a = 10
#     for _ in range(3):
#         turtle.setheading(a)
#         for i in range(4):
#             turtle.forward(side)
#             turtle.left(90)
#         a += 10
#
# n = int(input('Input ypu side: '))
# square(n)

# import turtle
#
# def square(side):
#     a = 45
#     for _ in range(8):
#         turtle.setheading(a)
#         for i in range(4):
#             turtle.forward(side)
#             turtle.left(90)
#         a += 45
#
# n = int(input('Input your side: '))
# square(n)

# import turtle as t
#
# def hexagon(side):
#     for i in range(6):
#         t.forward(side)
#         t.left(60)
#
#
# l = int(input('Input your length side'))
# hexagon(l)

# import turtle as t

# def hexagon(side):
#     for i in range(7):
#         t.forward(side)
#         t.left(60)
#     t.right(120)


# l = int(input('Input your length side'))
# for i in range(6):
#     hexagon(l)

# import turtle as t

# def rectangle(width, height):
#   for i in range(2):
#     t.forward(width)
#     t.right(90)
#     t.forward(height)
#     t.right(90)
#
# a, b = int(input()), int(input())
#
# rectangle(a, b)
# import turtle as t

# import turtle as t
# def triangle(side):
#   for i in range(3):
#     t.forward(side)
#     t.left(60)
#
#
# leight = int(input())
#
# triangle(leight)

# import turtle as t
#
# def square(side):
#   t.left(75)
#   for i in range(3):
#     t.left(30)
#     for i in range(4):
#         t.forward(side)
#         t.right(90)
#
#
# length = int(input())
#
# square(length)



# import turtle as t
#
# def square(side):
#   for i in range(8):
#     t.right(45)
#     for i in range(4):
#       t.forward(side)
#       t.right(90)
#
#
# length = int(input())
#
# square(length)

# import turtle as t
# def triangle(side):
#   for i in range(6):
#     t.forward(side)
#     t.left(60)
#
#
# leight = int(input())
#
# triangle(leight)

# import turtle as t
# def triangle(side):
#   for i in range(6):
#     t.forward(50)
#     t.left(60)


import turtle as t

# for i in range(6):
#   t.forward(30)
#   t.left(60)
# t.right(120)
# for i in range(6):
#   for i in range(5):
#     t.forward(30)
#     t.left(60)

# import turtle as t
# def romb(side):
#   t.forward(100)
#   t.right(60)
#   t.forward(100)
#   t.right(120)
#   t.forward(100)
#   t.right(60)
#   t.forward(100)
#
# def star():
#   for i in range(10):
#     romb(length)
#     t.right(85)
#
# length = int(input())
#
# star()


# import turtle as t
#
# def get_line():
#   t.forward(50)
#   t.backward(100)
#   t.forward(50)
#
#
# for i in range(6):
#   get_line()
#   t.left(60)


# import turtle as t
#
# def star():
#   for i in range(5):
#     t.right(144)
#     t.forward(100)

# s = 10
# for _ in range(10):
#   for i in range(4):
#     t.forward(s)
#     t.left(90)
#   s += 5

# s = 2
#
# for i in range(10):
#   t.left(90)
#   t.forward(s)
#   s *=2
#
# t.dot(10)
# t.forward(100)
# t.left(90)
# t.dot(10)
# t.forward(60)
# t.left(90)
# t.dot(10)
# t.forward(100)
# t.left(90)
# t.dot(10)
# t.forward(60)

# import turtle
#
# for _ in range(2):
#   for side in (150, 75):
#    turtle.dot(10)
#    turtle.forward(side)
#    turtle.left(90)


# import turtle as t
#
# def chaos(n):
#     t.shape('triangle')
#     t.dot(15)
#     for i in range(n):
#         t.forward(100)
#         t.stamp()
#         t.backward(100)
#         t.left(360 / n)
#
#
# chaos(int(input()))

# import turtle as t
#
#
# def chaos(n):
#     t.shape('turtle')
#     t.stamp()
#     for i in range(n):
#         t.penup()
#         t.forward(100)
#         t.stamp()
#         t.penup()
#         t.backward(100)
#         t.left(360 / n)
#
#
# q = int(input())
# chaos(q)


# chaos(int(input()))


# import turtle as t
#
# t.Screen().bgcolor(25, 160, 200)
# def chaos(n):
#     t.shape('turtle')
#     t.stamp()
#     t.pensize(5)
#     for i in range(n):
#         t.penup()
#         t.forward(70)
#         t.pendown()
#         t.forward(15)
#         t.penup()
#         t.forward(15)
#         t.stamp()
#         t.penup()
#         t.backward(100)
#         t.left(360 / n)
#
#
# q = int(input())
# chaos(q)

# import turtle as t
# t.penup()
# t.Screen().bgcolor('lightgreen')
# t.shape('turtle')
# for i in range(43):
#   t.stamp()
#   t.right(19)
#   t.forward(5+i)


# import turtle as t
#
# colors = ('blue', 'yellow', 'green', 'purple', 'orange', 'red')
#
# for i in range(44):
#     t.left(45)
#     t.pencolor(colors[i % 6])
#     t.pensize(i * 0.5 + 1)
#     t.forward(i * 2.5 + 5)

# import turtle
#
# turtle.goto(100, 150)
# position = turtle.pos()
# print(position)

# import turtle
#
# turtle.goto(200, -150)
# x = turtle.xcor()
# y = turtle.ycor()
# print(x)
# print(y)

# import turtle as t
# t.hideturtle()
# t.penup()
# t.goto(-150, -60)
# t.pendown()
# t.forward(300)
# t.goto(0, 150)
# t.goto(-150, -60)
#
# t.penup()
# t.goto(-150, 60)
# t.pendown()
# t.forward(300)
# t.goto(0, -150)
# t.goto(-150, 60)


# import turtle
# x = -100
# y = -100
# turtle.hideturtle()
# for i in range(10):
#     turtle.dot(10, 'red')
#     turtle.pencolor('lightgreen')
#     turtle.goto(x, y)
#     turtle.dot(10, 'blue')
#     x += 20
#     turtle.goto(0, 0)


# import turtle
#
# turtle.pensize(10)
# turtle.penup()
# turtle.setpos(-200, 100)
# turtle.pendown()
# turtle.color('blue')
# turtle.circle(80)
# turtle.penup()
#
# turtle.setpos(-75, 100)
# turtle.pendown()
# turtle.color('black')
# turtle.circle(80)
# turtle.penup()
#
# turtle.setpos(60, 100)
# turtle.pendown()
# turtle.color('red')
# turtle.circle(80)
# turtle.penup()
#
# turtle.setpos(-140, 25)
# turtle.pendown()
# turtle.color('yellow')
# turtle.circle(80)
# turtle.penup()
#
# turtle.setpos(-5, 25)
# turtle.pendown()
# turtle.color('green')
# turtle.circle(80)

# from turtle import *
# colors = ('dodgerblue3', 'darkgoldenrod3', 'black', 'chartreuse4', 'firebrick')
# pensize(20), penup(), goto(-300, 0)
# for c in range(5):
#     pencolor(colors[c])
#     pendown()
#     circle(100)
#     next_x, next_y = xcor() + 120, ycor() - 100 * (-1)**(c % 2)
#     if c:
#         penup()
#         goto(xcor() - 120, ycor() - 100 * (-1)**(c % 2))
#         pencolor(colors[c - 1])
#         for i in range(6):
#             penup()
#             if c % 2 == i % 2:
#                 pendown()
#             circle(100, 60)
#     penup()
#     goto(next_x, next_y)
# done()


# import turtle
# turtle.speed(8)
# turtle.hideturtle()
# turtle.penup()
# turtle.goto(0, -200)
# turtle.pendown()
# x = 100
# for i in range(2):
#     turtle.circle(x)
#     x -= 35
# turtle.penup()
# turtle.goto(0, -165)
# turtle.pendown()
# turtle.goto(0, -110)
# turtle.circle(10)
# turtle.penup()
# turtle.goto(-50, -70)
# turtle.pendown()
# turtle.dot(20)
# turtle.penup()
# turtle.goto(50, -70)
# turtle.pendown()
# turtle.dot(20)
# turtle.penup()
# turtle.goto(50, -70)
# turtle.pendown()
# turtle.dot(20)
#
# turtle.penup()
# turtle.goto(-94, -36)
# turtle.pendown()
# turtle.circle(35)
# turtle.penup()
# turtle.goto(94, -36)
# turtle.pendown()
# turtle.circle(35)

# import turtle
# import random
#
# turtle.Screen().setup(500, 500)
# colors = ('blue', 'yellow', 'green', 'purple', 'orange', 'red')
# turtle.pensize(3)
# turtle.speed(0)
#
# # function draw of  the snowflake
# def get_skelet_snowflake(size):
#     turtle.color(random.choice(colors))
#     for j in range(6):
#         for i in range(3):
#             turtle.forward(size / 4)
#             turtle.right(360 / 6)
#             turtle.forward(size / 4)
#             turtle.backward(size / 4)
#             turtle.left(360 / 3)
#             turtle.forward(size / 4)
#             turtle.backward(size / 4)
#             turtle.right(360 / 6)
#             if i == 2:
#                 turtle.forward(size/4)
#         turtle.backward(size)
#         turtle.right(360/6)
#     turtle.dot(10)
#
# # function of penup, pendown
# def uppen():
#     turtle.penup()
#     turtle.goto(random.randint(-300, 300), random.randint(-300, 300))
#     turtle.pendown()
#     get_skelet_snowflake(random.randint(10, 70))
#
# for i in range(30):
#     uppen()


# import turtle
# turtle.fillcolor('lightblue')
# turtle.begin_fill()
# for i in range(4):
#     turtle.forward(100)
#     turtle.left(90)
#     x = turtle.pos()
# turtle.end_fill()
#
#
# turtle.penup()
# turtle.goto(-25, 100)
# turtle.pendown()
#
# turtle.fillcolor('brown')
# turtle.begin_fill()
# for i in range(3):
#     turtle.forward(150)
#     turtle.left(120)
# turtle.end_fill()


# import turtle
#
# turtle.fillcolor('black')
# turtle.begin_fill()
# for i in range(2):
#     turtle.forward(70)
#     turtle.left(90)
#     turtle.forward(150)
#     turtle.left(90)
# turtle.end_fill()
#
# turtle.penup()
# turtle.goto(35, 105)
# turtle.pendown()
#
# turtle.fillcolor('red')
# turtle.begin_fill()
# turtle.circle(20)
# turtle.end_fill()
#
# turtle.penup()
# turtle.goto(35, 55)
# turtle.pendown()
#
# turtle.fillcolor('yellow')
# turtle.begin_fill()
# turtle.circle(20)
# turtle.end_fill()
#
# turtle.penup()
# turtle.goto(35, 5)
# turtle.pendown()
#
# turtle.fillcolor('green')
# turtle.begin_fill()
# turtle.circle(20)
# turtle.end_fill()

# import turtle
# turtle.hideturtle()
# cor = []
# # рисуем треугольник
# turtle.pensize(3)
# for i in range(3):
#     turtle.forward(300)
#     turtle.left(120)
#
# cir1 = turtle.Turtle()
# cir1.hideturtle()
# cir1.penup()
# cir1.goto(-10, 100)
# cir1.pendown()
# cir1.fillcolor('black')
# cir1.begin_fill()
# cir1.circle(50)
# cir1.end_fill()
#
# cir2 = turtle.Turtle()
# cir2.hideturtle()
# cir2.penup()
# cir2.goto(300, 100)
# cir2.pendown()
# cir2.fillcolor('black')
# cir2.begin_fill()
# cir2.circle(50)
# cir2.end_fill()
#
# cir3 = turtle.Turtle()
# cir3.hideturtle()
# cir3.penup()
# cir3.goto(150, -155)
# cir3.pendown()
# cir3.fillcolor('black')
# cir3.begin_fill()
# cir3.circle(50)
# cir3.end_fill()
#
# turtle.penup()
# turtle.goto(0, 150)
# turtle.pendown()
#
# # рисуем обратный треугольник белый
# turtle.pencolor('white')
# turtle.fillcolor('white')
# turtle.begin_fill()
# for i in range(3):
#     turtle.forward(300)
#     turtle.right(120)
# turtle.end_fill()



# import turtle
# turtle.speed(5)
#
# for _ in range(3):
#     turtle.forward(90)
#     turtle.left(120)
#
# turtle.penup()
# turtle.goto(0, 60)
#
# turtle.color('white')
# turtle.fillcolor('white')
# turtle.begin_fill()
# for _ in range(3):
#     turtle.forward(90)
#     turtle.color('black')
#     turtle.dot(30)
#     turtle.color('white')
#     turtle.right(120)
#
# turtle.end_fill()

# import turtle
#
# colors = ("#FF0000", "#FFA600", "#FFFF00", "#62FF00", "#89F590", "#69C5FF",
#           "#1E56FC", "#4800FF", "#CC00FF", "#FF5099")
#
# y = 0
# r = 100
#
# for i in range(10):
#     turtle.fillcolor(colors[i])
#     turtle.begin_fill()
#     turtle.circle(r - (i * 10))
#     y += 10
#     turtle.penup()
#     turtle.goto(0, y)
#     turtle.pendown()
#     turtle.end_fill()

# import turtle
# turtle.pencolor('darkblue')
# turtle.Screen().bgcolor('darkblue')
# turtle.fillcolor('orange')
# turtle.begin_fill()
# turtle.circle(100)
# turtle.end_fill()
# turtle.penup()
# turtle.goto(40, 0)
# turtle.pendown()
#
# turtle.fillcolor('darkblue')
# turtle.begin_fill()
# turtle.circle(100)
# turtle.end_fill()


# from turtle import *
# bgcolor('darkblue'), penup(), speed(0)  # Настройка основных значений
# dot(200, 'orange'), forward(200)  # Рисование луны
# shape('circle'), shapesize(10), color('darkblue')  # Настройка вида черепашки
# while True:  # Цикл прохода черепашки справа налево
#     for _ in range(400):
#         backward(1)
#     forward(400)

# import turtle
#
# turtle.Screen().bgcolor('DarkBlue')
# turtle.hideturtle()
# turtle.pencolor('orange')
# turtle.dot(200)
#
# while True:
#     da = turtle.Turtle()
#     da.hideturtle()
#     da.pencolor('DarkBlue')
#     for i in range(200, -201, -1):
#          da.penup()
#          da.goto(i, 0)
#          da.dot(200)
#          da.tracer(6, 0)
#          da.clear()
#          da.dot(200)

# import turtle
# import random as r
# turtle.colormode(255)
# turtle.speed(0)
#
# turtle.Screen().setup(640, 480)
# turtle.bgcolor('black')
#
# def get_star(size):
#     color = (r.randrange(250), r.randrange(250), r.randrange(250))
#     turtle.pencolor(color)
#     turtle.penup()
#     turtle.goto(r.randrange(-320, 321), r.randrange(-240, 241))
#     turtle.right(r.randrange(360))
#     turtle.pendown()
#     turtle.fillcolor(color)
#     turtle.begin_fill()
#     for i in range(5):
#         turtle.forward(size)
#         turtle.left(144)
#     turtle.end_fill()
#
#
# for i in range(50):
#     get_star(r.randrange(5, 100))

import turtle

turtle.circle(80, steps=5)