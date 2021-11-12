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

t = str(input())
r = str(input())
bank = ['камень', 'ножницы', 'бумага', 'ящерица', 'Спок']

if r.lower() == t.lower():
    print('ничья')
elif t.lower() == bank[0] and r.lower() == bank[3]:
    print('Тимур')
elif t.lower() == bank[0] and r.lower() == bank[1]:
    print('Тимур')
elif t.lower() == bank[1] and r.lower() == bank[2]:
    print('Тимур')
elif t.lower() == bank[1] and r.lower() == bank[3]:
    print('Тимур')
elif t.lower() == bank[2] and r.lower() == bank[0]:
    print('Тимур')
elif t.lower() == bank[2] and r.lower() == bank[4]:
    print('Тимур')
elif t.lower() == bank[3] and r.lower() == bank[4]:
    print('Тимур')
elif t.lower() == bank[3] and r.lower() == bank[2]:
    print('Тимур')
elif t.lower() == bank[4] and r.lower() == bank[1]:
    print('Тимур')
elif t.lower() == bank[4] and r.lower() == bank[0]:
    print('Тимур')
else:
    print('Руслан')