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
