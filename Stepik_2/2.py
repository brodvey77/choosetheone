# import math
# a, b = int(input()), int(input())
#
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(math.sqrt(a ** 10 + b ** 10))

# Body mass index

# weight, height = float(input('Input your weight in kg: ')), float(input('Input your height in m: '))
#
# body_mass_index = weight / height ** 2
#
# if body_mass_index < 18.5:
#     print('Недостаточная масса')
# elif body_mass_index > 25:
#     print('Избыточная масса')
# else:
#     print('Оптимальная масса')

# Line cost

# text = str(input())
# ruble = 0
# penny = 0
# counter = 0
#
#
# for i in text:
#     counter += 60
#     if counter > 100:
#         ruble += counter // 100
#         penny += counter % 100
#         counter = 0
#         if penny == 100:
#             ruble += penny //100
#             penny = 0
#     elif i == text[-1] and counter != 0:
#         penny += counter
#         if penny == 100:
#             ruble += penny //100
#             penny = 0
#
#
# print(f'{ruble} р. {penny} к.')


# string = input()
# price = 60 * len(string)
#
# print(f'{price // 100} р. {price % 100} коп.')


# print(len([i for i in str(input()).split()]))

# print(len(input().split()))

# year = int(input())
#
# list_of_enimals = ["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр",
#                    "Заяц"]
#
# list_of_years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011]
#
# if year in list_of_years:
#     print(list_of_enimals[list_of_years.index(year)])
#
# if year > 2000:
#     while year not in list_of_years:
#         year -= 12
#         if year in list_of_years:
#             print(list_of_enimals[list_of_years.index(year)])
#
# if year < 2000:
#     while year not in list_of_years:
#         year += 12
#         if year in list_of_years:
#             print(list_of_enimals[list_of_years.index(year)])


# year = int(input())
# animals = ['Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц', 'Дракон', 'Змея', 'Лошадь', 'Овца']
#
# print(animals[year % 12])

# number = int(input())
# list_digits = []
#
# while number != 0:
#     last_digit = number % 10
#     list_digits.append(last_digit)
#     number //= 10
#
# if len(list_digits) > 5:
#     list_digits.insert(0, list_digits[-1])
#     del list_digits[-1]
#
# for i in list_digits:
#     if list_digits[0] == 0:
#         del list_digits[0]
#
# print(*list_digits, sep='')

# n = int(input())
# print('{:,}'.format(n))


# n = int(input())
# list_d = []
# counter = 0
# while n != 0:
#     last_digit = n % 10
#     counter += 1
#     list_d.append(str(last_digit))
#     if counter == 3 and n != 1:
#         list_d.append(',')
#         counter = 0
#     n //= 10
#
# new = list_d[::-1]
# # if new[0] ==',':
# #     del new[0]
#
# print(*new, sep='', end='')


# The problem of Josephus Flavius

# n, k = int(input()), int(input())
# digit = 0
# for i in range(1, n + 1):
#     digit = (digit + k) % i
# print(digit + 1)


# n = int(input())
# numbers = []
# user_input = []
#
# for i in range(n):
#     user_input += input().split(' ')
#
#
# for i in user_input:
#     numbers.append(int(i))
#
# first = []
# second = []
# third = []
# forth = []
#
# flag = 0
#
# for i in numbers[flag::]:
#     x = numbers[flag]
#     y = numbers[flag + 1]
#     if x > 0 and y > 0:
#         first.append(1)
#     elif x < 0 and y > 0:
#         second.append(1)
#     elif x < 0 and y < 0:
#         third.append(1)
#     elif x > 0 and y < 0:
#         forth.append(1)
#     flag += 2
#     if len(numbers[flag::]) <= 0:
#         break
#
# print(f'Первая четверть: {len(first)}')
# print(f'Вторая четверть: {len(second)}')
# print(f'Третья четверть: {len(third)}')
# print(f'Четвертая четверть: {len(forth)}')

# n = int(input())
# count = [0, 0, 0, 0]
# names = ['Первая четверть:', 'Вторая четверть:',
#          'Третья четверть:', 'Четвертая четверть:']
#
# for _ in range(n):
#     x, y = [int(num) for num in input().split()]
#     if x > 0 and y > 0:
#         count[0] += 1
#     elif x < 0 and y > 0:
#         count[1] += 1
#     elif x < 0 and y < 0:
#         count[2] += 1
#     elif x > 0 and y < 0:
#         count[3] += 1
#
# for i in range(4):
#     print(names[i], count[i])

# text = [int(i) for i in input().split(' ')]
# counter = 0
# flag = text[0]
#
#
#
# for element in text:
#     if element > flag:
#         counter += 1
#     flag = element
#
# print(counter)

# text = [int(i) for i in input().split(' ')]
#
#
# new_list = []
#
# while len(text) > 1:
#     new_list.append(text[1])
#     new_list.append(text[0])
#     del text[0]
#     del text[0]
#
# if len(text) % 2 == 0:
#     print(*new_list)
# else:
#     print(*(new_list + text))

# text = [int(i) for i in input().split(' ')]
#
# text.insert(0, text.pop(-1))
#
# print(*text)


# text = [int(i) for i in input().split(' ')]
# text_2 = []
#
# for element in text:
#     if element in text_2:
#         continue
#     else:
#         text_2.append(element)
#
# print(*text_2)

# n = int(input())
# list_of_numbers = [int(input()) for i in range(n)]
# number_of_check = int(input())
# flag = 'НЕТ'
#
#
# for i in range(n - 1):
#     for j in list_of_numbers:
#         if j * list_of_numbers[i-1] == number_of_check:
#             flag = 'ДА'
#
# print(flag)

# t = str(input())
# r = str(input())
# bank = ['камень', 'ножницы', 'бумага']
#
# if r.lower() == t.lower():
#     print('ничья')
# elif t.lower() == bank[0] and r.lower() == bank[1]:
#     print('Тимур')
# elif t.lower() == bank[1] and r.lower() == bank[2]:
#     print('Тимур')
# elif t.lower() ==bank[2] and r.lower() == bank[0]:
#     print('Тимур')
# else:
#     print('Руслан')

# x, y = input(), input()
# var = ['камень', 'ножницы', 'бумага']
# ans = ['ничья', 'Руслан', 'Тимур']
# print(ans[var.index(x) - var.index(y)])

# num = input().split()
# c = 0
# for i in num:
#     c += int(i)
# print(c)

# a, b = map(int, input().split())
# print(a + b)

# s = int(input())
#
# p, c = int(s / 6), int(s / 6)
# k = int((p + c) * 2)
#
# print(p, k, c, sep=' ')

# x, y, z = map(int, input().split())
# karandash = 3
# pen = karandash + 2
# marker = pen + 7
#
# print((karandash * x) + (pen * y) + (marker * z))


# n, a, b = map(int, input().split())
#
# square = (a * b)*2
#
# print(square * n)
#
# print(*[2 * n * a * b for n, a, b in [map(int, input().split())]])


# a, b, c, d = map(int, input().split())
#
# print((a+b+c+d)/4)

# a, b = map(float, input().split())
#
# # if a >= 0 and b >= 0:
# #     if a > b:
# #         print(a - b)
# #     else:
# #         print(b - a)
# # elif a < 0 or b < 0:
# #     print(abs(a) + abs(b))
#
# print(abs(a - b))

# g, l = map(int, input().split())
#
# print(l - 1, g - 1)

# h1 = int(input())
# m1 = int(input())
# s1 = int(input())
# h2 = int(input())
# m2 = int(input())
# s2 = int(input())
#
# h_f = h2 - h1
# m_f = m2 - m1
# s_f = s2 - s1
#
# print((h_f*3600) +(m_f*60)+ s_f)

# t = str(input())
# r = str(input())
# bank = ['камень', 'ножницы', 'бумага', 'ящерица', 'Спок']
#
# if r.lower() == t.lower():
#     print('ничья')
# elif t.lower() == bank[0].lower() and r.lower() == bank[3].lower():
#     print('Тимур')
# elif t.lower() == bank[0].lower() and r.lower() == bank[1].lower():
#     print('Тимур')
# elif t.lower() == bank[1].lower() and r.lower() == bank[2].lower():
#     print('Тимур')
# elif t.lower() == bank[1].lower() and r.lower() == bank[3].lower():
#     print('Тимур')
# elif t.lower() == bank[2].lower() and r.lower() == bank[0].lower():
#     print('Тимур')
# elif t.lower() == bank[2].lower() and r.lower() == bank[4].lower():
#     print('Тимур')
# elif t.lower() == bank[3].lower() and r.lower() == bank[4].lower():
#     print('Тимур')
# elif t.lower() == bank[3].lower() and r.lower() == bank[2].lower():
#     print('Тимур')
# elif t.lower() == bank[4].lower() and r.lower() == bank[1].lower():
#     print('Тимур')
# elif t.lower() == bank[4].lower() and r.lower() == bank[0].lower():
#     print('Тимур')
# else:
#     print('Руслан')

# text = input()
# counter = 0
# flag = 'О'
# maximum = 0
#
# for i in text:
#     if i == 'Р':
#         flag = 'Р'
#         counter += 1
#         if counter > maximum:
#             maximum = counter
#     else:
#         flag = 'О'
#         counter = 0
#
# print(maximum)


# s = input().split('О')
# print(len(max(s)))

# Кремниевая долина 🌶️🌶️

# text = 'oantoooooooooooooooooooooooooooooooooooooooooooooooooooon'
# start = ''
# finish = ''
# reserve_list = ''
# new_list = ''
# flag = False


# import re
#
# lst = []
# regex = ''.join(f'.*?{i}' for i in 'anton')
# for i in range(int(input('N: '))):
#     if re.search(regex, input()):
#         lst.append(i + 1)
# print(*lst)


# otvet=[]
# for s in range(int(input())):
#     a=input()
#     for i in 'anton':
#         if i in a:
#             a=a[a.find(i):]
#         else:
#             break
#     else:
#         otvet.append(s+1)
# print(*otvet)

# for i in range(int(input())):
#     s, virus, x = input(), 'anton', 0
#     for sym in s:
#         if sym == virus[x]:
#             x += 1
#         if x == 5:
#             print(i + 1, end=' ')
#             break

# s = input()
# res = 'запретил букву'
# n = len(set(s + res.replace(' ', '')))
# text, x = sorted(set(s + res.replace(' ', ''))), 0
#
# print(text)
#
# for _ in range(n):
#     string = (s + ' ' + res + ' ' + text[x]).strip().replace('  ',' ')
#     print(string)
#     s = s.replace(text[x], '').lstrip()
#     res = res.replace(text[x], '').rstrip()
#     x += 1
#
#
# word = input() + ' запретил букву'
# alpha = [chr(i) for i in range(1072, 1104)]
#
# for letter in alpha:
#     if letter in word:
#         print(word, letter)
#         word = word.replace(letter, '').replace('  ', ' ').strip()

# numbers = [-6, -8, 0, 1, 3, 8, -7, 12, 17, 24, 25, 3, 5, 1]
# res = 0
# for num in numbers:
#     res += (num % 2 == 1) and (num > 1)
# print(res)

# def is_even(num):
#     return num % 2 == 0
#
# print(is_even(2))

# print(isinstance(3, int))
# print(isinstance(3.5, float))
# print(isinstance('Beegeek', str))
# print(isinstance([1, 2, 3], list))
# print(isinstance(True, bool))


# # объявление функции
# def func(num1, num2):
#     return num1 % num2 == 0
#
# # считываем данные
# num1, num2 = int(input()), int(input())
#
# # вызываем функцию
# if func(num1, num2):
#     print('делится')
# else:
#     print('не делится')

# letters = ['a', 'b', 'c', 'd']
#
# new_letters = list(letters)
# new_letters = letters.copy()
# new_letters = letters[:]

# numbers = [1, 2, 3, 4, 5, 6, 7]
# new_numbers = [2 * x for x in numbers]
# print(new_numbers)

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
#
# print(list1)


# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
#
# for i in list1:
#     if max(i) > maximum:
#         maximum = max(i)
#
# print(maximum)


# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
#
# for i in list1:
#     i.reverse()
#
# print(list1)


# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
#
# for element in list1:
#     counter += len(element)
#     total += sum(element)
#
# print(total/counter)

# n, m = int(input()), int(input())    # считываем значения n и m
# my_list = []
#
# for _ in range(n):
#     my_list.append([0] * m)
#
# print(my_list)

# n, m = int(input()), int(input())    # считываем значения n и m
# my_list = [0] * n
#
# for i in range(n):
#     my_list[i] = [0] * m
#
# print(my_list)
#
# n, m = int(input()), int(input())    # считываем значения n и m
#
# my_list = [[0] * m for _ in range(n)]
#
# print(my_list)

# n = 4                                          # количество строк (элементов)
# my_list = []
#
# for _ in range(n):
#     elem = [int(i) for i in input().split()]   # создаем список из элементов строки
#     my_list.append(elem)
# print(my_list)

# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         print(my_list[i][j], end=' ')   # используем необязательный параметр end
#     print()                             # перенос на новую строку


# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for row in my_list:
#     for elem in row:
#         print(elem, end=' ')
#     print()

# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         print(my_list[j][i], end=' ')    # выводим my_list[j][i] вместо my_list[i][j]
#     print()

# Используем два вложенных цикла для подсчета суммы всех чисел в списке:

# my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]
#
# total = 0
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         total += my_list[i][j]
# print(total)

# my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]
#
# total = 0
# for row in my_list:
#     for elem in row:
#         total += elem
# print(total)

# Подсчет суммы с помощью функции sum() выглядит так:

# my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]
#
# total = 0
# for row in my_list:      # в один цикл
#     total += sum(row)
# print(total)

# list1 = [[1, 2, 3], [4, 5]]
# list2 = list1
#
# list1[0].append(7)
#
# print(list2)

# my_list = [[1], [2, 3], [4, 5, 6]]
# total = 0
#
# for row in my_list:
#     total += sum(row)
#
# print(total)
# print(type(row))

# my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]
#
# maximum = my_list[0][0]
# minimum = my_list[0][0]
#
# for row in my_list:
#     if max(row) > maximum:
#         maximum = max(row)
#     if min(row) < minimum:
#         minimum = min(row)
#
# print(maximum + minimum)

# n = int(input())
# my_list = [[int(i) for i in range(1, n + 1)] for i in range(1, n + 1)]
# for element in my_list:
#     print(element)
#
# n = int(input())
# result = []
#
# for _ in range(n):
#     result.append(list(range(1, n + 1)))
#
# print(*result, sep='\n')

# def pascal(n):
#     my_list = []
#     for i in range(1, n + 1):
#         my_list.append(i)
#         print(my_list)
#
# n = int(input())
#
# print(pascal(n))

# import speedtest
#
# speed = speedtest.Speedtest()
# download_speed = speed.download()
# upload_speed = speed.upload()
# print(f'The download speed is {download_speed}')
# print(f'The upload speed is {upload_speed}')

# Треугольник Паскаля 1

# n = int(input())
# p = []
#
# for i in range(n + 1):
#     row = [1] * (i + 1)
#     for j in range(i + 1):
#         if j != 0 and j != i:
#             row[j] = p[i - 1][j - 1] + p[i - 1][j]
#     p.append(row)
#
# counter = 0
# flag = n
# for r in p:
#     if counter != flag:
#         counter += 1
#         continue
#     print(r)


# n = int(input())
# p = []
#
# for i in range(n):
#     row = [1] * (i + 1)
#     for j in range(i + 1):
#         if j != 0 and j != i:
#             row[j] = p[i - 1][j - 1] + p[i - 1][j]
#     p.append(row)
#
# for k in p:
#     print(k)


# Упаковка дубликатов 🌶️


# s = input()
# counter = 0
# l = []
# for i in range(2, len(s), 2):
#     if s[i] != s[i-2]:
#         l.append(s[counter:i].split())
#         counter = i
# l.append(s[counter:].split())
# print(l)

# res = []
#
# for el in input().split():
#     if res and el in res[-1]:
#         res[-1].append(el)
#     else:
#         res.append([el])
#
# print(res)

# a, s, x = input().split(), [], ''
# for i in a:
#     if x != i:
#         s.append(list(i))
#     else:
#         s[-1].append(i)
#     x = i
# print(s)

# from itertools import groupby
#
# s = 'w w w o r l d g g g g r e a t t e c c h e m g g p w w'
# res = [list(v) for k, v in groupby(s.split())]
# print(res)

# import pyspeedtest

# st = pyspeedtest.SpeedTest()
# st.download()
# st.upload()
# st.ping()

# s = input().split()            # vvod stroki
# l = []                         # create empty list
# x = ''                         # create auxiliary element
#
# for i in s:
#     if x != i:
#         l.append(list(i))     # if element different add new list
#     else:
#         l[-1].extend(i)       # if element same extend previous list
#     x = i                     # auxiliary element = current value
# print(l)





# def chunked(s, n):
#     c = 0
#     l = []
#     for i in range(len(s)):
#         if len(s[c:c + n]) != 0:
#             l.append(s[c:c + n])
#         c = c + n
#     return l
#
# s, n = input().split(), int(input())
#
# print(chunked(s, n))


# def chunked(symbols, n):
#     result = []
#     for i in range(0, len(symbols), n):
#         result.append(symbols[i:i + n])
#     return result
#
# symbols = input().split()
# n = int(input())
#
# print(chunked(symbols, n))


# Подсписки списка 🌶️🌶️

# s = input().split()                         # get input list
#
# l = [[]]                                    # create empty list in list
#
# for index_list in range(len(s)):
#     for i in range(len(s) - index_list):
#         l.append(s[i:i + index_list + 1])
#
# print(l)

# def get_sublists(symbols, n):
#     sublists = []
#     for i in range(len(symbols) - n + 1):
#         sublists.append(symbols[i:i + n])
#     return sublists
#
#
# symbols = input().split()
# result = [[]]
#
# for i in range(1, len(symbols) + 1):
#     result.extend(get_sublists(symbols, i))
#
# print(result)

# rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов
#
# matrix  = [[2, 3, 1, 0],
#            [9, 4, 6, 8],
#            [4, 7, 2, 7]]
#
# for r in range(rows):
#     for c in range(cols):
#         print(matrix[r][c], end=' ')
#     print()

# rows, cols = 3, 4                # rows - количество строк, cols - количество столбцов
#
# matrix  = [[277, -930, 11, 0],
#            [9, 43, 6, 87],
#            [4456, 8, 290, 7]]
#
# for r in range(rows):
#     for c in range(cols):
#         print(str(matrix[r][c]).ljust(9), end='')
#     print()

# n = 4
# matrix = [[0]*n for _ in range(n)]    # создаем квадратную матрицу размером 8×8
#
# for i in range(n):                     # заполняем главную диагональ 1-цами, а побочную 2-ками
#     matrix[i][i] = 1
#     matrix[i][n-i-1] = 2
#
# for r in range(n):                     # выводим матрицу
#     for c in range(n):
#         print(matrix[r][c], end=' ')
#     print()


# Примечание 2. Используйте функцию print_matrix() для вывода квадратной матрицы размерности n:
#
# def print_matrix(matrix, n, width=1):
#     for r in range(n):
#         for c in range(n):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()
# Примечание 3. Для считывания матрицы из n строк, заполненной числами, удобно использовать следующий код:
#
# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)


# n = 3
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# for i in range(n):
#     for j in range(n):
#         print(a[i][j], end=' ')
#     print()


# n = 3
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# for i in range(n):
#     for j in range(n):
#         print(a[n - i - 1][n - j - 1], end=' ')
#     print()


# n = 5
# a = [[19, 21, 33, 78, 99],
#      [41, 53, 66, 98, 76],
#      [79, 80, 90, 60, 20],
#      [33, 11, 45, 67, 90],
#      [45, 67, 12, 98, 23]]
#
# maximum = -1
# minimum = 100
#
# for i in range(n):
#     if a[i][i] > maximum:
#         print('максимум - ', a[i][i])
#         maximum = a[i][i]
#     if a[i][n - i - 1] < minimum:
#         print('минимум - ', a[i][n - i - 1])
#         minimum = a[i][n - i - 1]
# print(minimum + maximum)


# rows, cols = int(input()), int(input())
# l = []
# new_list = []
#
# for i in range(rows * cols):
#     l.append(input())
#     if len(l) == cols:
#         print(*l)
#         l.clear()



# n, m = int(input()), int(input())
# matrix = []
#
# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(input())
#     matrix.append(row)
#
#
# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end=' ')
#     print()






# def matrix(n, m):
#     matrix = []
#     for i in range(n):
#         row = []
#         for j in range(m):
#             row.append(input())
#         matrix.append(row)
#
#
#     for i in range(n):
#         for j in range(m):
#             print(matrix[i][j], end=' ')
#         print()
#
#     print()
#
#     for j in range(m):
#         for i in range(n):
#             print(matrix[i][j], end=' ')
#         print()
#
# n, m = int(input()), int(input())
#
# matrix(n, m)


# n = int(input())
# matrix = []
#
# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append(int(input()))
#     matrix.append(row)
#
#
# def sum_of_matrix(matrix):
#     sum = 0
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 sum += matrix[i][j]
#     print(sum)


# n = int(input())
# sum = 0
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             sum += matrix[i][j]
# print(sum)


# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# counter = 0
#
# for r in range(n):
#     average = sum(matrix[r]) / len(matrix[r])
#     for c in range(n):
#         if matrix[r][c] > average:
#             counter += 1
#         if c == (n - 1):
#             print(counter)
#             counter = 0


# n = int(input())
# matrix = []
#
# for _ in range(n):
#     row = [int(i) for i in input().split()]
#     matrix.append(row)
#
# for i in range(n):
#     counter = 0
#     average = sum(matrix[i]) / n
#     for j in range(n):
#         if matrix[i][j] > average:
#             counter += 1
#     print(counter)


# n = int(input())
# matrix = []
# l = []
#
# for _ in range(n):
#     row = [int(i) for i in input().split()]
#     matrix.append(row)
#
# for i in range(n):
#     for j in range(n):
#         if i < j and i >= n - 1 - j:
#             l.append(matrix[i][j])
#         if i > j and i <= n - 1 - j:
#             l.append(matrix[i][j])
#         if i == j:
#             l.append(matrix[i][j])
#
# print(max(l))

# n = int(input())
# matrix = []
#
# for _ in range(n):
#     row = [int(i) for i in input().split()]
#     matrix.append(row)
#
# largest = matrix[0][0]
#
# for i in range(n):
#     for j in range(n):
#         if (i >= j and i + j + 1 <= n) or (i <= j and i + j + 1 >= n):
#             if matrix[i][j] > largest:
#                 largest = matrix[i][j]
#
# print(largest)

# n = int(input())
# matrix = []
#
# for _ in range(n):
#     row = [int(_) for _ in input().split()]
#     matrix.append(row)
#
# sum1 = 0
# sum2 = 0
# sum3 = 0
# sum4 = 0
#
# for i in range(n):
#     for j in range(n):
#         if i == j or j == n - i - 1:
#             continue
#         if i < j and i < n - 1 - j:
#             sum1 += matrix[i][j]
#         if i < j and i > n - 1 - j:
#             sum2 += matrix[i][j]
#         if i > j and i > n - 1 - j:
#             sum3 += matrix[i][j]
#         if i > j and i < n - 1 - j:
#             sum4 += matrix[i][j]
#
# print(f'Верхняя четверть: {sum1}')
# print(f'Правая четверть: {sum2}')
# print(f'Нижняя четверть: {sum3}')
# print(f'Левая четверть: {sum4}')


# n = int(input())
# matrix = []
# quadrants = [['Верхняя четверть:', 0],
#              ['Правая четверть:', 0],
#              ['Нижняя четверть:', 0],
#              ['Левая четверть:', 0]]
#
# for _ in range(n):
#     row = [int(i) for i in input().split()]
#     matrix.append(row)
#
# for i in range(n):
#     for j in range(n):
#         if i < j and i + j + 1 < n :
#             quadrants[0][1] += matrix[i][j]
#         elif i < j and i + j + 1 > n:
#             quadrants[1][1] += matrix[i][j]
#         elif i > j and i + j + 1 > n:
#             quadrants[2][1] += matrix[i][j]
#         elif i > j and i + j + 1 < n:
#             quadrants[3][1] += matrix[i][j]
#
# for i in range(4):
#     print(quadrants[i][0], quadrants[i][1])


# p = 5
# y = 7
# w = p + y
# w = w + 1
# p = y
# y = 10
# p = 2 + w + y
#
# print(p)
#
# a, b = int(input()), int(input())
# print(abs(a) + abs(b))


# s = map(int, input().split())
# print(max(s))

# n = float(input())
# print(round(n, 2), round(n, 3))


# n, m = int(input()), int(input())
#
# mult = []
#
# # for _ in range(n):
# #     mult.append([_] * m)
#
# for i in range(n):
#     for j in range(m):
#         if j != m - 1:
#             print(str((i * j)).ljust(2), end=' ')
#         else:
#             print(str((i * j)), end='')
#     print()

# print(mult)

# n, m = int(input()), int(input())
# matrix = []
#
# for i in range(n):
#     row = [int(i) for i in input().split()]
#     matrix.append(row)
#
# maximum = matrix[0][0]
# a = 0
# b = 0
#
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] > maximum:
#             maximum = matrix[i][j]
#             a = i
#             b = j
# print(a, b)


# n, m = int(input()), int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# row, col = 0, 0
#
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] > matrix[row][col]:
#             row, col = i, j
#
# print(row, col)


# n, m = int(input()), int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# a, b = map(int, input().split())
# counter = 0
#
# for j in range(m):
#     for i in range(n):
#         if j == a:
#             matrix[i][j], matrix[i][b] = matrix[i][b], matrix[i][j]
#
# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end=' ')
#     print()

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# flag = 'YES'
# for i in range(n):
#     for j in range(n):
#         if i != j:
#             if matrix[i][j] != matrix[j][i]:
#                 flag = 'NO'
#                 break
# print(flag)


# n = int(input())
# matrix = [input().split() for _ in range(n)]
# result = 'YES'
#
# for i in range(n):
#     for j in range(i + 1, n):
#         if matrix[i][j] != matrix[j][i]:
#             result = 'NO'
#             break
#     if result == 'NO':
#         break
#
# print(result)



# n = int(input())
# matrix = [input().split() for _ in range(n)]
#
# for i in range(n):
#     matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]
#
# for r in range(n):
#     for c in range(n):
#         print(matrix[r][c], end=' ')
#     print()



# n = int(input())
# matrix = [input().split() for _ in range(n)]
# matrix.reverse()
# # for i in range(n // 2):
# #     matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
# for row in matrix:
#     print(*row)




