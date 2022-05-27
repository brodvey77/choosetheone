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
