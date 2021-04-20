# a = float(input())
# b = float(input())
#
# s = 1 / 2 * a * b
#
# print(s)


# s = float(input())
# v1 = float(input())
# v2 = float(input())
#
# t = s / (v1 + v2)
#
# print(t)

# num = float(input())
#
# if num == 0:
#     print('Обратного числа не существует')
# else:
#     print(num ** -1)

# f = float(input())
#
# c = 5 / 9 * (f - 32)
#
# print(c)


# f = int(input())
# age = 0
#
# if f <= 1:
#     age = f * 10.5
# elif f == 2:
#     age = int(f * 10.5)
# else:
#     age = (f - 2) * 4 + 21
#
# print(age)


# num = float(input())
# num2 = int(num * 10)
# num2 = num2 % 10
#
# print(num2)


# num = float(input())
# num2 = num % 1
#
# print(num2)

# a = float(input())
# b = int(a)
# print(a - b)

# num = max(1, 3, -5, 7) + min(-3, 6, -8, -1) + abs(-17)
# print(num)


# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())
# num5 = int(input())
#
# min_num = min(num1, num2, num3, num4, num5)
# max_num = max(num1, num2, num3, num4, num5)
#
# print('Наименьшее число = ', min_num)
# print('Наибольшее число = ', max_num)


# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
#
# n3 = min(num1, num2, num3)
# n1 = max(num1, num2, num3)
#
# sum_num = num1 + num2 + num3
#
# n2 = sum_num - n3 - n1
#
# print(n1)
# print(n2)
# print(n3)


# num = int(input())
#
# n3 = num % 10
# n2 = num % 100 // 10
# n1 = num % 1000 // 100
#
# max_num = max(n1, n2, n3)
# min_num = min(n1, n2, n3)
#
# average = n1 + n2 + n3 - max_num - min_num
#
# if max_num - min_num == average:
#     print('Число интересное')
# else:
#     print('Число неинтересное')

# a1 = float(input())
# a2 = float(input())
# a3 = float(input())
# a4 = float(input())
# a5 = float(input())
#
# if a1 < 0:
#     a1 = abs(a1)
# if a2 < 0:
#     a2 = abs(a2)
# if a3 < 0:
#     a3 = abs(a3)
# if a4 < 0:
#     a4 = abs(a4)
# if a5 < 0:
#     a5 = abs(a5)
#
# sum_a = a1 + a2 + a3 + a4 + a5
# print(sum_a)

# a = abs(float(input()))
# b = abs(float(input()))
# c = abs(float(input()))
# x = abs(float(input()))
# y = abs(float(input()))
#
# print(a + b + c + x + y)


# p1 = int(input())
# p2 = int(input())
# q1 = int(input())
# q2 = int(input())
#
# print(abs(p1 - q1) + abs(p2 - q2))

# from  math import *
#
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
# s = sqrt((x1-x2)**2 + (y1 - y2)**2)
# print(s)

# from math import pi
#
# r = float(input())
#
# s = pi * (r ** 2)
# c = (2 * pi) * r
#
# print(s)
# print(c)

# from math import *
#
# a = float(input())
# b = float(input())
#
#
# arif = (a + b) / 2
# geom = sqrt(a * b)
# garm = ((2 * a) * b) / (a + b)
# qvad = sqrt((a ** 2 + b ** 2) / 2)
#
# print(arif)
# print(geom)
# print(garm)
# print(qvad)

# from math import *
# x = float(input())
#
# r = radians(x)
# r = (x * pi) / 180
#
# result = sin(r) + cos(r) + (tan(r) ** 2)
#
# print(result)


# from math import ceil, floor
# x = float(input())
#
# result = ceil(x) + floor(x)
# print(result)


# from math import pow, sqrt
#
# a = float(input())
# b = float(input())
# c = float(input())
#
# d = pow(b, 2) - 4 * a * c
#
# if d < 0:
#     print('Нет корней')
# elif d == 0:
#     x = -b / (2 * a)
#     print(x)
# elif d > 0:
#     x1 = (-b + sqrt(d)) / (2 * a)
#     x2 = (-b - sqrt(d)) / (2 * a)
#     print(min(x1, x2))
#     print(max(x1, x2))

# from math import tan, pi
#
# n = int(input())
# a = float(input())
#
# s = n * (a ** 2) / (4 * tan(pi / n))
#
# print(s)


# city_1, city_2, city_3 = input(), input(), input()
# min_city = 0
# max_city = 0
#
# if len(city_2) > len(city_1) < len(city_3):
#     min_city = city_1
# elif len(city_1) > len(city_2) < len(city_3):
#     min_city = city_2
# elif len(city_1) > len(city_3) < len(city_2):
#     min_city = city_3
#
# print(min_city)
#
# if len(city_2) < len(city_1) > len(city_3):
#     max_city = city_1
# elif len(city_1) < len(city_2) > len(city_3):
#     max_city = city_2
# elif len(city_1) < len(city_3) > len(city_2):
#     max_city = city_3
#
# print(max_city)

# s1 = input()
# s2 = input()
# s3 = input()
# print(min([s1, s2, s3], key=len))
# print(max([s1, s2, s3], key=len))

# a = len(input())
# b = len(input())
# c = len(input())
#
# if ((2 *b) - c -a) * ((2 * c) - b - a) * ((2 * a) - b - c) == 0:
#     print('YES')
# else:
#     print('NO')

# text = input()
# if 'синий' in text or 'воскресенье' in text:
#     print('YES')
# else:
#     print('NO')


# text = input()
#
# if '@' in text and '.' in text:
#     print('YES')
# else:
#     print('NO')