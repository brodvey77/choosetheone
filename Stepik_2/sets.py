import math
#
# x = 36
# y = 4
#
# a = math.sqrt(x / y)
# b = math.sqrt(x * y)
# c = math.sqrt(x - y)
# d = math.sqrt(x + y)
#
# print(a)
# print(b)
# print(c)
# print(d)

# c = int(input())
# b = int(input())
#
# a = math.sqrt(c**2 - b**2)
#
# print(a)


# n, m, k, x, y, z = 25, 20, 7, 8, 3, 10
#
# clear_n = n - x
# clear_m = m - x - y
# clear_k = k - y
# al = clear_n + x + clear_m + y + clear_k + z
#
# print(al)

# n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]
#
# n_m = n + m - x
# m_k = m + k - y
# k_n = k + n - z
# only_n = n - (n_m - t) - (k_n - t) - t
# only_m = m - (n_m - t) - (m_k - t) - t
# only_k = k - (k_n - t) - (m_k - t) - t
# only_one = only_k + only_n + only_m
# only_two = (n_m - t) + (m_k - t) + (k_n - t)
# not_read = a - (only_one + (n_m -t) + (m_k - t) + (k_n - t) + t)
# print(only_one, only_two, not_read, sep='\n')

# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
# fruits_sorted = sorted(fruits, reverse=True)
# print(*fruits_sorted, sep='\n')

# print(len(set(input())))

# numbers = input()
# if len(numbers) == len(set(numbers)):
#     print('YES')
# else:
#     print('NO')

# s1 = input()
# s2 = input()
# s3 = s1 + s2
# if len(set(s3)) != 10:
#     print('NO')
# else:
#     print('YES')

# numbers = set(input() + input())
# print('YES' if len(numbers) == 10 else 'NO')


# a = input()
# b = input()
#
# if set(a) == set(b):
#     print('YES')
# else:
#     print("NO")

# print('YES' if set(input()) == set(input()) else 'NO')

# text = input().split()
# if set(text[0]) == set(text[1]) == set(text[2]):
#     print('YES')
# else:
#     print("NO")

# myset = set()
# for i in range(10):
#     if i % 2 == 0:
#         myset.add('even')
#     else:
#         myset.add('odd')
# print(myset)
# print(len(myset))

# n = int(input())
# my_list = []
#
# for i in range(n):
#     my_list.append(input().lower())
#
# for i in my_list:
#     print(len(set(i)))

# for _ in range(int(input())):
#     print(len(set(input().lower())))

# n = int(input())
# myset = set()
# for i in range(n):
#     myset.update(input().lower())
# print(len(myset))

# n = int(input())
# symbols = set()
#
# for _ in range(n):
#     for c in input().lower():
#         symbols.add(c)
#
# print(len(symbols))

# text = input().lower().split()
# text_2 = ''
# for word in text:
#     for sym in word:
#         if sym in '.,;:-?!':
#             continue
#         text_2 += sym
#     text_2 += ' '
# text_2 = text_2.split()
# print(len(set(text_2)))


# words = [word.lower().strip('.,;:-?!') for word in input().split()]
#
# print(len(set(words)))


# numbers = input().split()
# my_set = set()
# for num in numbers:
#     if int(num) not in my_set:
#         print('NO')
#         my_set.add(int(num))
#     else:
#         print('YES')



# set1 = {'a', 'b', 'c', 'd', 'h'}
# set2 = {'b', 'd', 'f', 'h'}
#
# set3 = set1 - set2 & set1
#
# print(set3)

# 231 1234 6754 7 78 56 34 890
# 1234 6754 7 3456 890


# num = set(input().split()) - set(input().split())
# numbers = sorted([int(i) for i in num])
# print(*numbers)



# my_list = [{int(i) for i in input()} for j in range(int(input()))]
# my_set = set(my_list[0])
#
# for i in my_list:
#     my_set &= i
#
# print(*sorted(my_set))

# set1 = {10, 20, 30, 40}
# set2 = set(range(50))
# print(set1.issubset(set2))

# set1 = set('Stepik')
# set2 = set('stepik')
#
# print(set1.issubset(set2))

# word = 'beegeek'
# set1 = set(word*3)
# set2 = set(word[::-1]*2 + 'stepik')
#
# print(set1)
# print(set2)
#
#
# print(set2 < set1)

# set1 = {1, 2, 3, 4, 5, 6, 7, 8}
# list1 = [1, 2, 3, 4, 5]
#
# print(set1.issuperset(list1))

# set1 = {'q', 'w', 'e', 'r', 't', 'y'}
# list1 = ['y', 'w', 'r']
#
# print(set1 >= list1)

# set1 = set(range(1, 10))
# set2 = set(range(10, 20))
#
# print(set1.isdisjoint(set2))

# a = set(input())
# b = set(input())
#
# if a.isdisjoint(b):
#     print('NO')
# else:
#     print('YES')

# a = set(input())
# b = set(input())
#
# if b.issubset(a):
#     print('YES')
# else:
#     print('NO')

# n = set(input().split()) & set(input().split()) - set(input().split())
# result = sorted([int(i) for i in n], reverse=True)
# print(*result)

# n1 = set(int(i) for i in input().split())
# n2 = set(int(i) for i in input().split())
# n3 = set(int(i) for i in input().split())

#
# result = sorted((n1 | n2 | n3) - (n1 & n2 & n3))
#
# print(*result)


# n1 = set(int(i) for i in input().split())
# n2 = set(int(i) for i in input().split())
# n3 = set(int(i) for i in input().split())
# new_set = set(int(i) for i in range(0, 11))
#
# result = sorted(new_set - (n1 | n2 | n3))
# print(*result)
#
# set1 = set(int(i) for i in input().split())
# set2 = set(int(i) for i in input().split())
# set3 = set(int(i) for i in input().split())
#
# print(*sorted(set(range(11)) - set1 - set2 - set3))

# n, m, k, p = [int(input()) for i in range(4)]
# result = n - m -k + p
# print(result)

# n = [int(i) for i in input().split()]
# myset = set(n)
# print(len(n) - len(myset))
# sunrise = input().split()
#
# print(len(sunrise) - len(set(sunrise)))
#
# n = int(input())
# myset = {input() for i in range(n)}
# city = input()
# if city in myset:
#     print('REPEAT')
# else:
#     print('OK')

# set_set = {input() for _ in range(int(input()))}
# print('REPEAT' if input() in set_set else 'OK')

# m = int(input())
# n = int(input())
# home = {input() for _ in range(m)}
# work = [input() for _ in range(n)]
#
# for book in work:
#     if book in home:
#         print('YES')
#     else:
#         print('NO')

# a = set(int(i) for i in input().split())
# b = set(int(i) for i in input().split())
# myset = a | b
# if len(myset) == 0:
#     print('BAD DAY')
# else:
#     print(*sorted(myset, reverse=True))

# set1 = {int(i) for i in input().split()}
# set2 = {int(i) for i in input().split()}
#
# if set1.isdisjoint(set2):
#     print('BAD DAY')
# else:
#     print(*sorted(set1 & set2, reverse=True))

# set_of_numbers = {int(i) for i in input().split()}
# numbers = {int(i) for i in input().split()}
#
# if set_of_numbers == numbers:
#     print('YES')
# else:
#     print('NO')

# m, n = int(input()), int(input())
# mathematic = {input() for _ in range(m)}
# informatic = {input() for _ in range(n)}
# counter = mathematic ^ informatic
# if len(counter) != 0:
#     print(len(counter))
# else:
#     print('NO')

# ruk = input().split()
# pomruk = input().split()
# result = sorted(set(ruk) | set(pomruk))
# print(*result)




# if len(first) - len(set(first)) == 0:
#     print('NO')
# else:
#     print(len(first) - (len(first) - len(set(first)) * 2))


# n = int(input()) + int(input())
# s = {input() for _ in range(n)}
# k = 2 * len(s) - n
# print(k if k else 'NO')

# m = int(input())
# print(set.intersection(*({input() for _ in range(int(input()))} for _ in range(m))), sep="\n")
# #
#
#
# m = int(input()) # Считываем число листков M
# print(* # Оператор разыменовывания итератора полученного пересечения множеств (блоков строчек)
#     set.intersection( # Выводим построчно пересечение следующих множеств:
#     * # Оператор разыменовывания итератора генерируемых множеств (блоков строчек)
#     (
#         # Считываем очередной блок фамилий во множество:
#         {input() # Считываем очередную фамилию в блоке (после того, как считали количество фамилий в блоке)
#         for _ in range(int(input())) # Считываем количество фамилий в блоке, затем итерируем N строк
#         } # Ввод окончен
#         for _ in range(m) # Итерируем M блоков
#     )), sep="\n" # Наш сепаратор - перевод строки
# )
#
# n = int(input())
# result = {input() for _ in range(int(input()))}
#
# for _ in range(n - 1):
#     result &= {input() for _ in range(int(input()))}
#
# print(*sorted(result), sep='\n')