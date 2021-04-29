# for название_переменной_цикла in range(количество повторений):
#     блок кода

# for i in range(2):
#     print('Привет')

# for i in range(5):
#     num = int(input())
#     print('Квадрат вашего числа равен:', num * num)
# print('Цикл завершен')

# for i in range(10):
#     print('Python is awesome!')

# text = input()
# count = int(input())
#
# for i in range(count):
#     print(text)

# for i in range(6):
#     print('AAA')
# for i in range(5):
#     print('BBBB')
# print('E')
# for i in range(9):
#     print('TTTTT')
# print('G')

# n = int(input())
# if 1 <= n <= 20:
#     for i in range(n):
#         print('*' * 19)
# else:
#     print('Ваше число должно быть от 1 до 20')


# print('*******************\n' * int(input()))

# text = input()
#
# for i in range(10):
#     print(i, text)

# n = int(input())
#
# for i in range(n+1):
#     print('Квадрат числа', i, 'равен', i * i)

# n = int(input())
#
# if n >= 2:
#     for i in range(n):
#         print('*' * (n - i))
# else:
#     print('Число должно быть от 2 - ух и выше')

# m = int(input())
# p = int(input())
# n = int(input())
#
# for i in range(n):
#     print(i + 1, m * (p / 100 + 1) ** i)

# for i in range(10, 0, -2):
#         print(i)

# m = int(input())
# n = int(input())
# i = 0
#
# if m <= n:
#         for i in range(m, n + 1):
#                 print(i)
# else:
#         print('первое чило должно быть меньше либо равно второму числу')

# m = int(input())
# n = int(input())
#
# if m <= n:
#         for i in range(m, n + 1):
#                 print(i)
# else:
#         for i in range(m, n - 1, -1):
#                 print(i)

# m = int(input())
# n = int(input())
#
# if m > n:
#         for i in range(m, n - 1, -1):
#                 if i % 2 != 0:
#                         print(i)
# else:
#         print('Первое число должно быть больше второго числа')

# m = int(input())
# n = int(input())
#
# if m <= n:
#         for i in range(m, n + 1):
#                 if i % 17 == 0:
#                         print(i)
#                 elif i % 10 == 9:
#                         print(i)
#                 elif i % 3 == 0 and i % 5 == 0:
#                         print(i)


# m, n = int(input()), int(input())
# for i in range(m, n + 1):
#     if i % 17 == 0 or i % 10 == 9 or i % 15 == 0:
#         print(i)

# n = int(input())
#
# for i in range(1, 11):
#     x = i * n
#     print(n, 'x', i, '=', x)

# counter = 0
# for i in range(10):
#     num = int(input())
#     if num > 10:
#         counter = counter + 1
# print('Было введено', counter, 'чисел, больших 10.')

# counter1 = 0
# counter2 = 0
# for i in range(10):
#     num = int(input())
#     if num > 10:
#         counter1 = counter1 + 1
#     if num == 0:
#         counter2 = counter2 + 1
# print('Было введено', counter1, 'чисел, больших 10.')
# print('Было введено', counter2, 'нулей.' )

# counter = 0
# for i in range(1, 101):
#     if i**2 % 10 == 4:
#         counter = counter + 1
# print(counter)


# total = 0
# for i in range(1, 101):
#     total = total + i
# print(total)

# total = 0
# for i in range(1, 6):
#     total += i
# print(total)

# total = 0
# for i in range(1, 6):
#     total += i
#     print(total)

# list = ('Mast 13', 'Mast 12', 'Mast PRO 13', 'Mast PRO 12', 'Mast 22', 'Mast PRO 22', 'Mast 22', 'Coast 16',
#         'Coast 16 PRO', 'Coast 12', 'Coast 12 PRO', 'Coast 13', 'Coast 13 PRO', 'Coast 20', 'Coast 22 PRO',
#         'Coast 22', 'Coast 10', 'Coast 10 PRO', 'Coast 24', 'Coast 24 PRO', 'Mast 24', 'Mast 24 PRO')
# count = 0
# for i in list:
#     count += 1
#     print(count, i)

# a = int(input())
# b = int(input())
#
# count = 0
# if a <= b:
#     for i in range(a, b + 1):
#         if (i ** 3) % 10 == 4 or (i ** 3) % 10 == 9:
#             count += 1
#     print(count)
# else:
#     print('Первое число должно быть меньше или равно второму числу')


# n = int(input())
#
# count = 0
#
# for i in range(n):
#     count = int(input()) + count
# print(count)

# import math
#
# n = int(input())
# log = math.log(n)
# count = 0
# for i in range(1, n + 1):
#     count = count + 1 / i
# print(count - log)

# n = int(input())
# counter = 0
#
# for i in range(1, n + 1):
#     if (i * i) % 10 == 2 or (i * i) % 10 == 5 or \
#             (i * i) % 10 == 8:
#         counter = counter + i
# if counter != 0:
#     print(counter)
# else:
#     print(0)

# n = int(input())
# count = 1
#
# if n <= 12:
#     for i in range(1, n + 1):
#         count = count * i
# print(count)

# total = 1
# for i in range(3):
#     num = int(input())
#     if num != 0:
#         total *= num
# print(total)


# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         total += i
# print(total)

# n = int(input())
# total = 0
#
# for i in range(1, n+1):
#     if i % 2 == 0:
#         total -= i
#     else:
#         total += i
# print(total)

# n = int(input())
# bigest = 0
# big = 0
#
# if n >= 2:
#     for i in range(n):
#         n = int(input())
#         if n > bigest:
#             big = bigest
#             bigest = n
#         else:
#             if n < bigest and n > big:
#                 big = n
# print(bigest)
# print(big)

# even_number = 0
#
# for i in range(10):
#     n = int(input())
#     if n % 2 == 0:
#         even_number += 1
#         if even_number == 10:
#             print('YES')
# if even_number != 10:
#     print('NO')

# flag = 'YES'
#
# for i in range(10):
#     n = int(input())
#     if n % 2 != 0:
#         flag = 'NO'
# print(flag)

# n = int(input())
# big = 0
# biggest = 1
#
# #
# for i in range(n):
#     biggest, big = biggest + big, biggest
#
#     print(big, end=' ')