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

# num1 = 34
# num2 = 81
# if num1 // 9 == 0 or num2 % 9 == 0:
#     print('число', num1, 'выиграло')
# else:
#     print('число', num2, 'выиграло')
#
# print(num1 // 9 )
# print(num2 % 9)

# a = int(input())
# if a >= 2 and a <= 17:
#     b = 3
#     p = a * a + b * b
# else:
#     b = 5
# p = (a + b) * (a + b)
# print(p)

# a = 7
# print(a <= 17)
# if a >= 2 and a <= 17:

# a = int(input())
# if a >= 2 and a <= 17:
#     b = 3
#     p = a * a + b * b
# else:
#     b = 5
# p = (a + b) * (a + b)
# print(p)

# x = int(input())
#
# if -30 < x <= -2 or 7 < x <= 25:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')


# number = int(input())
#
# if 999 < number <= 9999 and (number % 7 == 0 or number % 17 == 0):
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# b = int(input())
# c = int(input())
#
# if a < b + c and b < c + a and c < a + b:
#     print('YES')
# else:
#     print('NO')

# year = int(input())
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# if a == c or b == d:
#     print('YES')
# else:
#     print('NO')
#
# for a in range(0, 101):
#     if a % 5 == 0:
#         print(a)


# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
#
# if (x2 == x1 or x2 == x1 + 1 or x2 == x1 - 1) and (y2 == y1 or y2 == y1 + 1 or y2 == y1 - 1):
#     print('YES')
# else:
#     print('NO')


# n = int(input('Speed Zum >> '))
# k = int(input('Speed Flash >> '))
#
# if n > k:
#     print('NO')
# elif n< k:
#     print('YES')
# else:
#     print('Don\'t know')

# a = int(input())
# b = int(input())
# c = int(input())
#
# if a == b == c:
#     print('Равносторонний')
# elif a == b != c or a != b == c or a == c:
#     print('Равнобедренный')
# else:
#     print('Разносторонний')


# a = int(input())
# b = int(input())
# c = int(input())
#
# if b < a < c or c < a < b:
#     print(a)
# elif a < b < c or c < b < a:
#     print(b)
# else:
#     print(c)


# month = int(input())
#
# if month % 2 != 0 and month != 9 and month != 11 or month == 8 or month == 10 or month == 12:
#     print(31)
#
# elif month == 2:
#     print(28)
#
# else:
#     print(30)

# elif month()

# month = int(input())
#
# if month == 2:
#     print(28)
# else:
#     if month <= 7:
#         print(month % 2 + 30)
#     else:
#         print(31 - month % 2)


# weight = int(input())
#
# if weight < 60:
#     print('Легкий вес')
# elif 60 <= weight < 64:
#     print('Первый полусредний вес')
# else:
#     print('Полусредний вес')

# number_1 = int(input())
# number_2 = int(input())
# operator = str(input())
#
# # if number_2 == 0 and operator == '/':
# #     print('На ноль делить нельзя!')
# if operator == '+':
#     print(number_1 + number_2)
# elif operator == '-':
#     print(number_1 - number_2)
# elif operator == '*':
#     print(number_1 * number_2)
# elif 0!= operator == '/':
#     print(number_1 / number_2)
# else:
#     print('Неверная операция')


# color_1 = str(input())
# color_2 = str(input())
#
# if color_1 == 'красный' and color_2 == 'синий' or color_2 == 'красный' and color_1 == 'синий':
#     print('фиолетовый')
# elif color_1 == 'красный' and color_2 == 'желтый' or color_2 == 'красный' and color_1 == 'желтый':
#     print('оранжевый')
# elif color_1 == 'синий' and color_2 == 'желтый' or color_2 == 'синий' and color_1 == 'желтый':
#     print('зеленый')
# elif color_1 == 'красный' and color_2 == 'красный':
#     print('красный')
# elif color_1 == 'синий' and color_2 == 'синий':
#     print('синий')
# elif color_1 == 'желтый' and color_2 == 'желтый':
#     print('желтый')
# else:
#     print('ошибка цвета')

# number = int(input())
#
# if number == 0:
#     print('зеленый')
# elif 1 <= number <= 10 and number % 2 != 0:
#     print('красный')
# elif 1 <= number <= 10 and number % 2 == 0:
#     print('черный')
# elif 11 <= number <= 18 and number % 2 != 0:
#     print('черный')
# elif 11 <= number <= 18 and number % 2 == 0:
#     print('красный')
# elif 19 <= number <= 28 and number % 2 != 0:
#     print('красный')
# elif 19 <= number <= 28 and number % 2 == 0:
#     print('черный')
# elif 29 <= number <= 36 and number % 2 != 0:
#     print('черный')
# elif 29 <= number <= 36 and number % 2 == 0:
#     print('красный')
# else:
#     print('ошибка ввода')

# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())
#
# if a1 < a2 and b1 > b2:
#     print(a2, b2)
# elif a1 < a2 and b1 == b2:
#     print(a2, b2)
# elif a1 == a2 and b1 > b2:
#     print(a1, b2)
# elif a1 == a2 and b1 == b2:
#     print(a1, b2)
#
# elif a1 == a2 and b1 < b2:
#     print(a1, b1)
# elif a1 > a2 and b1 == b2:
#     print(a1, b1)
# elif a1 > a2 and b1 < b2:
#     print(a1, b1)
#
# elif a1 < a2 == b1 and b1 < b2:
#     print(b1)
# elif a1 > a2 and b1 > b2 and a1 == b2:
#     print(a1)
# elif a1 < a2 < b1 < b2:
#     print(a2, b1)
# elif a2 < a1 < b2 < b1:
#     print(a1, b2)
# else:
#     print('пустое множество')


# экзамен

# year = int(input())
#
# if year % 10 == 0 and year % 100 // 10 == 0:
#     print('YES')
# else:
#     print('NO')


# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
#
# if (x1 + y1 + x2 + y2) % 2 == 0:
#     print('YES')
# else:
#     print('NO')


# age = int(input())
# pol = str(input())
#
# if 10 <= age <= 15 and pol == 'f':
#     print('YES')
# else:
#     print('NO')


# digit = int(input())
#
# if digit == 1:
#     print('I')
# elif digit == 2:
#     print('II')
# elif digit == 3:
#     print('III')
# elif digit == 4:
#     print('IV')
# elif digit == 5:
#     print('V')
# elif digit == 6:
#     print('VI')
# elif digit == 7:
#     print('VII')
# elif digit == 8:
#     print('VIII')
# elif digit == 9:
#     print('IX')
# elif digit == 10:
#     print('X')
# else:
#     print('ошибка')


# digit = int(input())
#
# if digit % 2 != 0:
#     print('YES')
# elif digit % 2 == 0 and 2 <= digit <= 5:
#     print('NO')
# elif digit % 2 == 0 and 6 <= digit <= 20:
#     print('YES')
# elif digit % 2 == 0 and digit > 20:
#     print('NO')


# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
#
# if abs(x1 - x2) == abs(y1 - y2):
#     print('YES')
# else:
#     print('NO')
#
# print(str(x1 - x2))
# print(str(y1 - y2))
#
#
# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# if  (a-c)**2==(b-d)**2:
#     print ("YES")
# else:
#     print ("NO")

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# dx = abs(x1 - x2)
# dy = abs(y1 - y2)
# if dx == 1 and dy == 2 or dx == 2 and dy == 1:
#     print('YES')
# else:
#     print('NO')

# Ход Ферзя

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
#     print('YES')
# else:
#     print('NO')