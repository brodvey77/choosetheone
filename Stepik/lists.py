# Суммы двух
# На вход программе подается натуральное число n≥2, а затем nn целых чисел. Напишите программу, которая создает
# из указанных чисел список, состоящий из сумм соседних чисел (00 и 11, 11 и 22, 22 и 33 и т.д.).

# Формат входных данных
# На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести список, состоящий из сумм соседних чисел.

# n = int(input())
# lst = []
# final_lst = []
#
# for i in range(n):
#     a = int(input())
#     lst.append(a)
#
# for i in range(len(lst) - 1):
#     final_lst.append(lst[0] + lst[1])
#     del lst[0]
#
# print(final_lst)

# На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая
# создает из указанных чисел список, затем удаляет все элементы стоящие по нечетным индексам, а затем
# выводит полученный список.
#
# Формат входных данных
# На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести список в соответствии с условием задачи.
#
# Примечание. Используйте оператор del.

# n = int(input())
# lst = []
#
# for i in range(n):
#     a = int(input())
#     lst.append(a)
#
# del lst[::2]
# print(lst)

# k-ая буква слова 🌶️🌶️
# На вход программе подается натуральное число n и n строк, а затем число k. Напишите программу, которая выводит
# kk-ую букву из введенных строк на одной строке без пробелов.
#
# Формат входных данных
# На вход программе подается натуральное число nn,  далее nn строк, каждая на отдельной строке. В конце вводится
# натуральное число kk – номер буквы (нумерация начинается с единицы).
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Если некоторые строки слишком короткие, и в них нет символа с заданным номером, то такие строки при
# выводе нужно игнорировать


# n = int(input())
# lst = []
# for i in range(1, n + 1):
#     a = str(input())
#     lst.append(a)
#
# k = int(input())
#
# text = ''
# for i in lst:
#     if len(i) < k:
#         continue
#     else:
#         text += i[k - 1]
# print(text)


# Символы всех строк
# На вход программе подается натуральное число nn, а затем nn строк. Напишите программу, которая создает список из
# символов всех строк, а затем выводит его.
#
# Формат входных данных
# На вход программе подаются натуральное число nn, а затем nn строк, каждая на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести список состоящий из символов всех введенных строк.
#
# Примечание. В результирующем списке могут содержаться одинаковые символы.

# n = int(input())
# a = []
#
# for i in range(1, n + 1):
#     a.extend(str(input()))
#
# print(a)

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# count = 0
# for i in numbers:
#     count += pow(i, 2)
# print(count)

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# print(sum([i**2 for i in numbers]))

# n = 5
# lst = []
# for i in range(1, n + 1):
#     x = lst.append(int(input()))
# for i in lst:
#     print(i)
# print()
# for i in lst:
#     print((i ** 2) + (i * 2) + 1)


# n = int(input())
#
# lst = []
#
# for i in range(n):
#     a = lst.append(int(input()))
# maximum = max(lst)
# minimum = min(lst)
#
# for i in lst:
#     if i == maximum:
#         lst.remove(i)
#     elif i == minimum:
#         lst.remove(i)
# for i in lst:
#     print(i)

# n = int(input())
# lst =[]
#
# for i in range(n):
#     a = lst.append(input())
# a = set(lst)
# print(*a, sep='\n')


# n = int(input())
# lst = []
# final_lst = []

# for i in range(n):
#     a = lst.append(input())
#
# for i in lst:
#     if i in final_lst:
#         continue
#     else:
#         final_lst.append(i)
# print(*final_lst)


# dat = []
# for _ in range(int(input())):
#     el = input()
#     if el not in dat:
#         dat.append(el)
#         print(el)


# n = int(input())
# lst = []
#
# for i in range(n):
#     a = lst.append(input())
#
# search = str.lower(input())
#
# for i in lst:
#     if search in i.lower():
#         print(i)


# n = int(input())
# lst = []
# search_array = []
#
# for i in range(n):
#     a = lst.append(input())
#
# k = int(input())
#
# for j in range(k):
#     search = search_array.append(str.lower(input()))


# n = 5
# lst = ['trac', 'Язык Python прекрасен', 'C# - отличный язык программирования', 'Stepik - отличная платформа',
#        'BEEGEEK FOREVER!', 'язык Python появился 20 февраля 1991', 'язык фывфывфыв',
#        'Язык выаываыва ваыва ываыв Python', 'язык Python ,kf', 'kf', 'Язык Python']
# search_array = ['язык', 'python']
# final = []
#
# final_lst = []
#
# for i in range(n):
#     a = lst.append(input())
#
# k = int(input())
#
# for j in range(k):
#     search = search_array.append(str.lower(input()))
#
# print(search_array[0])
#
# while len(lst) != 0:
#     for elem in lst:
#         if search_array[0] not in elem.lower():
#             lst.remove(elem)
#         else:
#             final_lst.append(elem)
#
# print(final_lst)


# lst = ['Язык Python прекрасен', 'C# - отличный язык программирования', 'Stepik - отличная платформа',
#        'BEEGEEK FOREVER!', 'язык Python появился 20 февраля 1991']
#
# search_array = ['язык', 'python']
# new_lst = []
#
# while len(search_array) > 0:
#     for element in search_array:
#         for i in lst:
#             if element not in i.lower():
#                 lst.remove(i)
#                 print(lst)
#     del search_array[0]

# n = int(input())
# lst = []
# search_array = []
# final_lst = []
#
# for i in range(n):
#     a = lst.append(input())
#
# k = int(input())
#
# for j in range(k):
#     search = search_array.append(str.lower(input()))
#
# while len(search_array) > 0:
#     for element in search_array:
#         for i in lst:
#             if element not in i.lower():
#                 lst.remove(i)
#     del search_array[0]
#
# print(*lst, sep='\n')


# s = [input() for _ in range(int(input()))]
# d = [input() for _ in range(int(input()))]
# for i in s:
#     for j in d:
#         if j.lower() not in i.lower():
#             break
#     else:
#         print(i)

# n = int(input())
# lst = []
# minus = []
# zero = []
# plus = []
#
# for i in range(n):
#     digit = int(input())
#     if digit < 0:
#         minus.append(digit)
#     if digit == 0:
#         zero.append(digit)
#     if digit > 0:
#         plus.append(digit)
# lst = minus + zero + plus
#
# print(lst)

# ip = '192.168.1.24'
# numbers = ip.split('.')    # указываем явно разделитель
# print(numbers)

# words = ['Python', 'is', 'the', 'most', 'powerful', 'language']
# s = ' '.join(words)
# print(s)

# s = 'BEEGEEK'
# chars = list(s)
# s = '**'.join(chars)
# print(s)

# string = str(input())
# a = string.split()
# for i in a:
#     print(i)

# print('\n'.join(input().split()))
# print(*input().split(), sep='\n')

# string = str(input())
#
# lst = string.split()
#
# for i in lst:
#     print(i[0] + '.', end='')

# string = str(input())
# lst = string.split('\\')
# for i in lst:
#     print(i)

# string = input().split()
# print(type(string))
# for i in string:
#     print('+' * int(i))

# string = input().split('.')
# flag = 'YES'
# for i in string:
#     if int(i) > 255 or int(i) < 0:
#         flag = 'NO'
#         break
# print(flag)

# text = input()
# delimiter = input()
# print(delimiter.join(text))


# string = input()
# lst = string.split()
# counter = 0
#
# for i in lst[:-1]:
#     for j in lst[1:]:
#         if int(i) == int(j):
#             counter += 1
#     del lst[0]
# print(counter)

# colors = ['Orange']
# colors.append('Red')
# colors.append('Blue')
# colors.append('Green')
# colors.insert(0, 'Violet')
# colors.insert(2, 'Purple')
#
# print(colors)

# colors = ['Red', 'Blue', 'Green', 'Black', 'White']
# del colors[-1]
# colors.remove('Green')
#
# print(colors)


# Все сразу 2 🌶️
# Дополните приведенный код, чтобы он:
#
# Заменил второй элемент списка на 17; ok
# Добавил числа 4, 5 и 6 в конец списка; ok
# Удалил первый элемент списка; ok
# Удвоил список; ok
# Вставил число 25 по индексу 3; ok
# Вывел список, с помощью функции print().

# numbers = [8, 9, 10, 11]
# a = numbers.remove(9)
# b = numbers.insert(1, 17)
# c = numbers.append(4)
# d = numbers.append(5)
# e = numbers.append(6)
# for i in numbers:
#     if i == numbers[0]:
#         numbers.remove(i)
# numbers += numbers
# f = numbers.insert(3, 25)
#
# print(numbers)

# numbers = input().split()
#
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#
# maximum = numbers.index(max(numbers))
# minimum = numbers.index(min(numbers))
# numbers[maximum], numbers[minimum] = min(numbers), max(numbers)
#
# print(numbers)

# text = input()
# counter = 0
# for i in text.split():
#     if i.lower() in ['a', 'an', 'the']:
#         counter += 1
# print(f'Общее количество артиклей: {counter}')

# n = input()
# n = int(n.lstrip('#'))
#
# for i in range(1, n + 1):
#     string = str(input())
#     if '#' in string:
#         string = string[:string.index('#')]
#         string = string.rstrip()
#     print(string)

# numbers = [4, 2, 8, 6, 5, 3, 10, 4, 100, 1, -7]
# numbers.sort()
# del numbers[0]
# del numbers[-1]
# numbers.sort(reverse=True)
# print(numbers)

# numbers = input().split()
#
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# print(numbers)
# numbers.sort()
# print(*numbers)
# numbers.sort(reverse=True)
# print(*numbers)

# n = input().split()
# n.sort(key=int)
# print(*n)
# n.sort(reverse=True, key=int)
# print(*n)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
#             'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
#             'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [m[1:] for m in keywords]
#
# print(new_keywords)


# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
#             'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
#             'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [c for c in keywords if len(c) >= 5]
#
# print(new_keywords)


# palindromes = [p for p in range(101, 1000) if p // 100 == p % 10]
#
# print(palindromes)

# for i in range(100, 1000):
#     if i // 100 == i % 10:
#         print(i)

# import emoji
#
# print(emoji.emojize('hello world :red_heart:', variant='emoji_type'))

# n = int(input())
#
# list = [i ** 2 for i in range(1, n + 1)]
#
# print(*list, sep='\n')

# n = str(input())
#
# list =[pow(int(i), 3) for i in n.split()]
#
# print(*list)

# string = str(input())
# list = [i for i in string.split()]
#
# print(*list, sep='\n')

# string = str(input())
#
# # list = [int(element) for element in string if element in '0123456789']
# list = [int(element) for element in string if element.isdigit()]
#
# print(*list, sep='')

# string = str(input())
#
# list = [pow(int(i), 2) for i in string.split() if int(i) % 2 == 0 and pow(int(i), 2) % 10 != 4]
#
# print(*list)

# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# n = len(a)
#
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:                  # если порядок элементов пары неправильный
#             a[j], a[j + 1] = a[j + 1], a[j]  # меняем элементы пары местами
#
# print('Отсортированный список:', a)


# a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]
#
# n = len(a)
#
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#
# print(a)

# a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]
#
# n = len(a)
#
# for i in range(n - 1):
#     flag = True
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             flag = False
#     if flag:
#         break
# print(a)





# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96,
# -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67,
# 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52,
# 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
#
# n = len(a)
#
# for i in range(n):
#     minimum = i
#     for j in range(i + 1, n):
#         if a[j] < a[minimum]:
#             minimum = j
#     a[minimum], a[i] = a[i], a[minimum]
#
# print(a)

# a = [88, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# n = len(a)
#
# for i in range(1, n):
#     elem = a[i]  # первый элемент из неотсортированной части списка
#     j = i
#     while j >= 1 and a[j - 1] > elem:
#         a[j] = a[j - 1]
#         j -= 1
#     a[j] = elem
#
# print(f'Отсортированный список: {a}')



# names = ['Джим', 'Джилл', 'Джон', 'Джасмин']
# if 'Джасмин' not in names:
#     print ('Не могу найти Джасмин.')
# else:
#     print('Ceмья Джасмин: ', end='')
#     print(names)

# n = int(input())
#
# list = [i for i in range(2, n + 1) if i % 2 == 0]
# print(list)
import smtplib

# l = str(input())
# m = str(input())
#
#
# list_l = [int(i) for i in l.split()]
# list_m = [int(i) for i in m.split()]
# list_f =[]
# for i in range(len(list_l)):
#     list_f = list_l[0] + list_m[0]
#     del list_l[0]
#     del list_m[0]
#     print(list_f, end=' ')

# string = str(input())
# list = [i for i in string.split()]
# sum_list = sum([int(i) for i in string.split()])
# print('+'.join(list), '=', sum_list, sep='')

# stroka = str(input())
#
# list = [i for i in stroka.split('-')]
#
# if list[0] == '7':
#     del list[0]
#
# if ''.join(list).isdigit():
#     list_2 = [int(i) for i in list]
#     if 99 < list_2[0] <= 999 and 99 < list_2[1] <= 999 and 999 < list_2[2] <= 9999:
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')

# spisok1=[i for i in input().split('-')]
# spisok2=[len(i) for i in spisok1 if i.isdigit()]
# print('YES' if spisok2==[1, 3, 3, 4] and spisok1[0]=='7' or spisok2==[3, 3, 4] else 'NO')

# string = str(input())
#
# list = [len(i) for i in string.split()]
#
# print(max(list))

# string = str(input())
#
# list = [i[1:] + i[0] + 'ки' for i in string.split()]
#
# print(list)

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



