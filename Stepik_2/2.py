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
