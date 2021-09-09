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

# x = 5
#
# def add():
#     global x
#     x = 3
#     x = x + 5
#     print(x)
#
# add()
# print(x)

# def do_something(numbers):
#     result = 1
#     for i in numbers:
#         result *= i
#     return result
#
# print(do_something([2, 2, 2, 2]))

# def get_sum(x, y, z):
#     return x + y + z
#     print('Сумма равна', x + y + z)
#
#
# print(get_sum(1, 2, 3))

# объявление функции  мили = километры * 0.6214
# def convert_to_miles(km):
#     return round(num * 0.6214, 3)
#
# # считываем данные,
# num = int(input())
#
# # вызываем функцию
# print(convert_to_miles(num))

# # объявление функции
# def get_days(month):
#     if month in [1, 3, 5, 7, 8, 10, 12]:
#         return 31
#     elif month in [4, 6, 9, 11]:
#         return 30
#     else:
#         return 28
#
# num = int(input())
#
# print(get_days(num))

# def get_factors(num):
#     return [i for i in range(1, num + 1) if num % i == 0]
#
# n = int(input())
#
# print(get_factors(n))

# n = int(input())
# list = []
# for c in range(n):
#     list1 = [int(i) for i in input().split()]
#     list = quick_merge(list, list1)
#
# print(list)



# # объявление функции
# def find_all(target, symbol):
#     list = []
#     counter = 0
#     for i in s:
#         if i == symbol:
#             list.append(counter)
#         counter += 1
#     return list
#
#
# # считываем данные
# s = input()
# char = input()

# вызываем функцию
# print(find_all(s, char))

# def merge(list1, list2):
#     return sorted(list1 + list2)
#
#
# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
#
# # вызываем функцию
# print(merge(numbers1, numbers2))

# n = int(input())
#
# list = []
#
# for i in range(n):
#     list1 = [int(c) for c in input().split()]
#     list = sorted(list + list1)
#
# print(list)


# def quick_merge(list1, list2):
#     result = []
#     p1 = 0  # указатель на первый элемент списка list1
#     p2 = 0  # указатель на первый элемент списка list2
#     while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1
#     if p1 < len(list1):   # прицепление остатка
#         result += list1[p1:]
#     if p2 < len(list2):
#         result += list2[p2:]
#     return result
#
# n = int(input())
# numbers1 = [int(c) for c in input().split()]
# for _ in range(1, n):
#     numbers1 = quick_merge(numbers1, [int(c) for c in input().split()])
# print(*numbers1)


# def quick_merge(list1, list2):
#     result = []
#
#     p1 = 0  # указатель на первый элемент списка list1
#     p2 = 0  # указатель на первый элемент списка list2
#
#     while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1
#
#     if p1 < len(list1):  # прицепление остатка
#         result += list1[p1:]
#     if p2 < len(list2):
#         result += list2[p2:]
#
#     return result
#
# n = int(input())
#
# spisok = [int(c) for c in input().split()]
#
# for _ in range(n - 1):
#     spisok = quick_merge(spisok, [int(c) for c in input().split()])
#
# print(*spisok)


#  List creation
# s = list(map(int, input().split()))
#
# print(s)

# def is_valid_triangle(side_1, side_2, side_3):
#     if side_1 < side_2 + side_3 and side_2 < side_3 + side_1 and side_3 < side_1 + side_2:
#         return True
#     else:
#         return False
#
#
# a = int(input())
# b = int(input())
# c = int(input())
#
# print(is_valid_triangle(a, b, c))

# def is_prime(num):
#     flag = True
#     for i in range(2, num):
#         if num % i == 0:
#             flag = False
#     if num > 1 and flag == True:
#         return True
#     else:
#         return False
#
# phone_number = int(input())
#
#
# print(is_prime(phone_number))



# def is_prime(num):
#     flag = True
#     for i in range(2, num):
#         if num % i == 0:
#             flag = False
#     if num > 1 and flag == True:
#         return True
#     else:
#         return False
#
# def get_next_prime(num):
#     while is_prime(num + 1) == False:
#         num += 1
#     return num + 1
#
#
# phone_number = int(input())
#
# print(get_next_prime(phone_number))


# def is_lower(num):
#     flag = False
#     for i in num:
#         if i.isalpha() and i.islower():
#             flag = True
#     if flag == True:
#         return True
#     else:
#         return False
#
#
# def is_upper(num):
#     flag = False
#     for i in num:
#         if i.isalpha() and i.isupper():
#             flag = True
#     if flag == True:
#         return True
#     else:
#         return False
#
#
# def is_len_eight(num):
#     if len(num) >= int(8):
#         return True
#     else:
#         return False
#
#
# def is_digit(num):
#     flag = False
#     for i in num:
#         if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
#             flag = True
#             break
#     return flag
#
#
# def is_password_good(password):
#     if is_lower(password) == True and is_upper(password) == True and \
#             is_len_eight(password) == True and is_digit(password) == True:
#         return True
#     else:
#         return False
#
# txt = str(input())
#
#
# print(is_password_good(txt))


# объявление функции
# def is_one_away(word1, word2):
#     counter = 0
#     for i in range(len(word1)):
#         if word1[i] != word2[i]:
#             counter += 1
#     if len(word1) == len(word2) and counter == 1:
#         return True
#     else:
#         return False
#
# # считываем данные
# txt1 = input()
# txt2 = input()

# # вызываем функцию
# print(is_one_away(txt1, txt2))






# объявление функции
def is_palindrome(text):
    if text.lower()[::] == text.lower()[::-1]:
        print('YES')
    else:
        print('NO')

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))