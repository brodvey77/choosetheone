# for название_переменной_цикла in range(количество повторений):
#     блок кода
#
# for i in range(2):
#     print('Привет')
#
# for i in range(5):
#     num = int(input())
#     print('Квадрат вашего числа равен:', num * num)
# print('Цикл завершен')
#
# for i in range(10):
#     print('Python is awesome!')
#
# text = input()
# count = int(input())
#
# for i in range(count):
#     print(text)
#
# for i in range(6):
#     print('AAA')
# for i in range(5):
#     print('BBBB')
# print('E')
# for i in range(9):
#     print('TTTTT')
# print('G')
#
# n = int(input())
# if 1 <= n <= 20:
#     for i in range(n):
#         print('*' * 19)
# else:
#     print('Ваше число должно быть от 1 до 20')
#
#
# print('*******************\n' * int(input()))
#
# text = input()
#
# for i in range(10):
#     print(i, text)
#
# n = int(input())
#
# for i in range(n+1):
#     print('Квадрат числа', i, 'равен', i * i)
#
# n = int(input())
#
# if n >= 2:
#     for i in range(n):
#         print('*' * (n - i))
# else:
#     print('Число должно быть от 2 - ух и выше')
#
# m = int(input())
# p = int(input())
# n = int(input())
#
# for i in range(n):
#     print(i + 1, m * (p / 100 + 1) ** i)
#
# for i in range(10, 0, -2):
#         print(i)
#
# m = int(input())
# n = int(input())
# i = 0
#
# if m <= n:
#         for i in range(m, n + 1):
#                 print(i)
# else:
#         print('первое чило должно быть меньше либо равно второму числу')
#
# m = int(input())
# n = int(input())
#
# if m <= n:
#         for i in range(m, n + 1):
#                 print(i)
# else:
#         for i in range(m, n - 1, -1):
#                 print(i)
#
# m = int(input())
# n = int(input())
#
# if m > n:
#         for i in range(m, n - 1, -1):
#                 if i % 2 != 0:
#                         print(i)
# else:
#         print('Первое число должно быть больше второго числа')
#
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
#
#
# m, n = int(input()), int(input())
# for i in range(m, n + 1):
#     if i % 17 == 0 or i % 10 == 9 or i % 15 == 0:
#         print(i)
#
# n = int(input())
#
# for i in range(1, 11):
#     x = i * n
#     print(n, 'x', i, '=', x)
#
# counter = 0
# for i in range(10):
#     num = int(input())
#     if num > 10:
#         counter = counter + 1
# print('Было введено', counter, 'чисел, больших 10.')
#
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
#
# counter = 0
# for i in range(1, 101):
#     if i**2 % 10 == 4:
#         counter = counter + 1
# print(counter)
#
#
# total = 0
# for i in range(1, 101):
#     total = total + i
# print(total)
#
# total = 0
# for i in range(1, 6):
#     total += i
# print(total)
#
# total = 0
# for i in range(1, 6):
#     total += i
#     print(total, end='')
#
# list = ('Mast 13', 'Mast 12', 'Mast PRO 13', 'Mast PRO 12', 'Mast 22', 'Mast PRO 22', 'Mast 22', 'Coast 16',
#         'Coast 16 PRO', 'Coast 12', 'Coast 12 PRO', 'Coast 13', 'Coast 13 PRO', 'Coast 20', 'Coast 22 PRO',
#         'Coast 22', 'Coast 10', 'Coast 10 PRO', 'Coast 24', 'Coast 24 PRO', 'Mast 24', 'Mast 24 PRO')
# count = 0
# for i in list:
#     count += 1
#     print(count, i)
#
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
#
#
# n = int(input())
#
# count = 0
#
# for i in range(n):
#     count = int(input()) + count
# print(count)
#
# import math
#
# n = int(input())
# log = math.log(n)
# count = 0
# for i in range(1, n + 1):
#     count = count + 1 / i
# print(count - log)
#
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
#
# n = int(input())
# count = 1
#
# if n <= 12:
#     for i in range(1, n + 1):
#         count = count * i
# print(count)
#
# total = 1
# for i in range(3):
#     num = int(input())
#     if num != 0:
#         total *= num
# print(total)
#
#
# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         total += i
# print(total)
#
# n = int(input())
# total = 0
#
# for i in range(1, n+1):
#     if i % 2 == 0:
#         total -= i
#     else:
#         total += i
# print(total)
#
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
#
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
#
# flag = 'YES'
#
# for i in range(10):r
#     n = int(input())
#     if n % 2 != 0:
#         flag = 'NO'
# print(flag)
#
# n = int(input())
# big = 0
# biggest = 1
#
# #
# for i in range(n):
#     biggest, big = biggest + big, biggest
#
#     print(big, end=' ')
#
# text = str(input())
# while 'КОНЕЦ' != text != 'конец':
#     print(text)
#     text = str(input())
#
# стоп, хватит, достаточно
#
# text = str(input())
# total = 0
#
# while text != 'стоп' and text != 'хватит' and text != 'достаточно':
#     total += 1
#     text = str(input())
# print(total)
#
# num = int(input())
# while num % 7 == 0:
#     print(num)
#     num = int(input())
#
# num = int(input())
# total = 0
#
# while num > -1:
#     total += num
#     num = int(input())
# print(total)
#
# num = int(input())
# i = 0
#
# while 0 <= num < 6:
#     if num == 5:
#         i += 1
#     num = int(input())
# print(i)


# money = int(input())
# coin_25 = 0
# coin_10 = 0
# coin_5 = 0
# coin_1 = 0
#
# while money >= 25:
#     coin_25 = money // 25
#     money = money - coin_25 * 25
# while money >= 10:
#     coin_10 = money // 10
#     money = money - coin_10 * 10
# while money >= 5:
#     coin_5 = money // 5
#     money = money - coin_5 * 5
# while money >= 1:
#     coin_1 = money // 1
#     money = money - coin_1 * 1
# print(coin_25 + coin_10 + coin_5 + coin_1)

# num = 123456789
# total = 0
# while num != 0:
#     last_digit = num % 10
#     if last_digit > 4:
#         total += 1
#     num = num // 10
# print(total)

# num = int(input())
#
# while num != 0:
#     print(num % 10)
# num = num // 10

# num = int(input())
# while num != 0:
#     last_digit = num % 10
#     num = num // 10
#     print(last_digit, end='')

# num = int(input())
# largest = 0
# smallest = 9
#
# while num != 0:
#     last_digit = num % 10
#     if last_digit > largest:
#         largest = last_digit
#     if last_digit < smallest:
#         smallest = last_digit
#     num = num // 10
# print('Максимальная цифра равна', largest)
# print('Минимальная цифра равна', smallest)


# num = int(input())
# sum_of_digit = 0
# multiplication = 1
# total_digit = 0
# average = 0
# first_digit = 0
# last_digit = 0
# sum_of_last_anf_first_digit = 0
#
# while num != 0:
#     digit = num % 10
#     total_digit += 1
#     sum_of_digit += digit
#     multiplication *= digit
#     first_digit = num % 10
#     if total_digit == 1:
#         last_digit = digit
#     num = num // 10
#
# print(sum_of_digit)
# print(total_digit)
# print(multiplication)
# print(sum_of_digit / total_digit)
# print(first_digit)
# print(first_digit + last_digit)


# num = int(input())
# last = 0
# pre_last = 0
#
#
# while num != 0:
#     last_digit = num % 10
#     last, pre_last = last_digit, last
#     num = num // 10
# print(pre_last)

# num = int(input())
# tank = num % 10
# flag = 'YES'
#
# while num != 0:
#     digit = num % 10
#     if digit != tank:
#         flag = 'NO'
#     num = num // 10
# print(flag)

# num = int(input())
# tank = num % 10
# flag = 'YES'
#
# while num != 0:
#     digit = num % 10
#     if digit < tank:
#         flag = 'NO'
#     else:
#         tank = digit
#     num = num // 10
#
# print(flag)

# mult = 1
# for i in range(1, 11):
#    if i % 2 == 0:
#       continue
#    if i % 9 == 0:
#       break
#    mult *= i
# print(mult)

# num = int(input())
#
# for i in range(1, num + 1):
#     if num % i == 0 and i > 1:
#         print(i)
#         break

# num = int(input())
#
# for i in range(1, num + 1):
#     if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
#         continue
#     print(i)

# n = 0
# while n < 10:
#     n += 2
#     if n == 8:
#         break
#     print(n)
# else:
#     print('Цикл завершен.')


# count = 0
# p = 1
# for i in range(1, 11):
#     x = int(input())
#     if x >= 0:
#         p *= x
#         count += 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')

# mx = 0
# s = 0
# for i in range(11):
#     x = int(input())
#     if x < 0:
#         s = x
#     if x > mx:
#         mx = x
# print(s)
# print(mx)


# mx = -10 ** 6
# s = 0
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         s += x
#     if mx < x < 0:
#         mx = x
# if s < 0:
#     print(s)
#     print(mx)
# else:
#     print('NO')

# s = 1
# for i in range(1, 7):
#     n = input()
#     if i % 2 == 0:
#         s = s + n
# print(s)

# s = 0
#
# for i in range(1, 8):
#     n = int(input())
#     if n % 2 == 0:
#         s += n
# else:
#     print(s)


# n = int(input())
# max_digit = n % 10
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit < max_digit:
#             digit = max_digit
#     n = n % 10
# if max_digit == 0:
#     print('NO')
# else:
#     print(max_digit)

# n = int(input())
# max_digit = -1
#
# while n != 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_digit:
#             max_digit = digit
#     n = n // 10
# if max_digit == -1:
#     print('NO')
# else:
#     print(max_digit)

# n = int(input())
# while n > 0:
#     n %= 10
# print(n)

# n = int(input())
# while n != 0:
#     l = n % 10
#     n = n // 10
# print(l)

# n = input()
# product = n % 10
# while n >= 10:
#     digit = n % 10
#     product = product * digit
#     n //= 10
# print(product)

# n = int(input())
# product = 1
#
# while n != 0:
#     digit = n % 10
#     product = product * digit
#     n = n // 10
# print(product)