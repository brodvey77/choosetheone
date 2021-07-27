# # объявление функции
# def draw_box():
#     print('*' * 10)
#     print('*        *')
#     print('*        *')
#     print('*        *')
#     print('*        *')
#     print('*        *')
#     print('*        *')
#     print('*        *')
#     print('*        *')
#     print('*        *')
#     print('*        *')
#     print('*        *')
#     print('*        *')
#     print('*' * 10)
#
# # основная программа
# draw_box()  # вызов функции

# объявление функции
# def draw_triangle():
#     for i in range(1, 11):
#         print('*' * i)
#
# # основная программа
# draw_triangle()  # вызов функции

# def draw_box(height, width):
#     for i in range(height):
#         print('*' * width)
#
# draw_box(5, 2)

# def print_number(a, b, c):
#     d = (a + c) // b
#     print(d)
#
# print_number(2, 3, 11)

# def change_us(a, b):
#     a = 0
#     b = 0
#     print(a, b)
#
# x = 1
# y = 7
# print(x, y)
# change_us(x, y)
# print(x, y)


# def print_text(text, num):
#     while num > 0:
#         print(text, end='')
#         num -= 1
#
# print_text('Python', 4)

# # объявление функции
# def draw_triangle(fill, base):
#     for i in range((base // 2) + 1):
#         for j in range(i):
#             print(fill, end='')
#         print(fill)
#     for i in range(base // 2, 0, -1):
#         for j in range(i - 1):
#             print(fill, end='')
#         print(fill)
#
# # считываем данные
# fill = input()
# base = int(input())
#
# # вызываем функцию
# draw_triangle(fill, base)

# # объявление функции
# def print_fio(name, surname, patronymic):
#     print(surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep='')
#
# # считываем данные
# name, surname, patronymic = input(), input(), input()
#
# # вызываем функцию
# print_fio(name, surname, patronymic)


# # объявление функции
# def print_digit_sum(num):
#     sum = 0
#     while num != 0:
#         last_digit = num % 10
#         sum += last_digit
#         num = num // 10
#     print(sum)
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print_digit_sum(n)

# def swap(a, b):
#     a, b = b, a
#
# a = 4
# b = 3
# swap(a, b)
# print(a - b)

# x = 5
#
# def add():
#     x = 3
#     x = x + 5
#     print(x)
#
# add()
# print(x)

x = 5

def add():
    global x
    x = 3
    x = x + 5
    print(x)

add()
print(x)