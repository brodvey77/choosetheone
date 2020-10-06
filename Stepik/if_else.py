# language = input('input language >> ')
# if language == 'Python':
#     print('Yes')
# else:
#     print('No')

# number = int(input('input number two digit >> '))
# last_digit = number % 10
# first_digit = number // 10
# if last_digit == first_digit:
#     print('Yes')
# else:
#     print('No')

# number_1, number_2, number_3 = int(input()), int(input()), \
#                                int(input())
# counter = 0
# if number_1 % 2 == 0:
#     counter = counter + 1
# if number_2 % 2 == 0:
#     counter = counter + 1
# if number_3 % 2 == 0:
#     counter = counter + 1
# print(counter)

# password_1 = (input())
# password_2 = (input())
#
# if password_1 == password_2:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')

# print('Пароль принят' if input() == input() else 'Пароль не принят')

# number = int(input())
# if number % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')
# print('Четное' if not int(input()) % 2 else 'Нечетное')

# number = int(input())
# d = number % 10
# c = (number % 100) // 10
# b = (number % 1000) // 100
# a = number // 1000
# if a + d == b - c:
#     print('ДА')
# else:
#     print('НЕТ')

# age = int(input())
# if age >= 18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')
#
#
# print('Доступ разрешен' if  int(input()) >= 18 else 'Доступ запрещен')

# number_1 = int(input())
# number_2 = int(input())
# number_3 = int(input())
#
# if number_2 - number_1 == number_3 - number_2:
#     print('YES')
# else:
#     print('NO')

# number_1 = int(input())
# number_2 = int(input())
#
# if number_1 > number_2:
#     print(number_1)
# else:
#     print(number_2)

# a = int(input())
# b = int(input())
# print(a if a < b else b)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# min = a
#
# if min > b:
#     min = b
# if min > c:
#     min = c
# if min > d:
#     min = d
# print(min)

# age = int(input())
#
# if age in range(0, 14):
#     print('детство')
# elif age in range(14, 25):
#     print('молодость')
# elif age in range(25, 60):
#     print('зрелость')
# elif age >= 60:
#     print('старость')

# a = int(input())
# b = int(input())
# c = int(input())
#
# count = 0
# if a >= 0:
#     count = a
# if b >= 0:
#     count = count + b
# if c >= 0:
#     count = count + c
# if count < 0:
#     print(0)
# else:
#     print(count)
