# text = input()
# counter = 0
#
# for a in range(len(text) - 1):
#     if text[a] == text[a + 1]:
#         counter += 1
# print(counter)

# text = input()
#
# vowel = 0
# consonant = 0
#
# for i in text.lower():
#     if i in 'ауоыиэяюёе':
#         vowel += 1
#     if i in 'бвгджзйклмнпрстфхцчшщ':
#         consonant += 1
# print('Количество гласных букв равно', vowel)
# print('Количество согласных букв равно', consonant)

# n = int(input())
# a = ''
#
# while n > 0:
#     a = str(n % 2) + a
#     n = n // 2
#
# print(a)

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::-1])

# text = str(input())
#
# if text[::] == text[::-1]:
#     print('YES')
# else:
#     print('NO')

# text = str(input())
#
# print(len(text))
# print(text * 3)
# print(text[0])
# print(text[:3])
# print(text[-3:])
# print(text[::-1])
# print(text[1:-1])

# text = str(input())
#
# print(text[2])
# print(text[-2])
# print(text[:5])
# print(text[:-2])
# print(text[::2])
# print(text[1::2])
# print(text[::-1])
# print(text[-1::-2])

# text = 'abcdefg'
# central = text[len(text) // 2]
# first_part = text[:len(text) // 2]
# second_part = text[-1:len(text) // 2:-1]
# second_part_chet = text[len(text) // 2:]
# right_second_part = second_part[-1::-1]
#
# if len(text) % 2 == 0:
#     print(second_part_chet + first_part)
# else:
#     print(right_second_part + central + first_part)
#
# # print(central)
# # print(first_part)
# # print(second_part)
# # print(second_part_chet)
# # print(right_second_part)


# text = 'abcdefg'
# central = text[len(text) // 2]
# first_part = text[:len(text) // 2]
# second_part = text[-1:len(text) // 2:-1]
# second_part_chet = text[len(text) // 2:]
# right_second_part = second_part[-1::-1]

# if len(text) % 2 == 0:
#     print(second_part_chet + first_part)
# else:
#     print(right_second_part + central + first_part)

# print(central)
# print(first_part)
# print(second_part)
# print(second_part_chet)
# print(right_second_part)

# s = 'foO BaR BAZ quX'
# print(s.capitalize())
# s = 'FOO Bar 123 baz qUX'
# print(s.swapcase())
# s = 'the sun also rises'
# print(s.title())

# s = 'FOO Bar 123 baz qUX'
# print(s.lower())

# s = 'FOO Bar 123 baz qUX'
# print(s.upper())

# capitalize — писать прописными буквами, закрепить.
# swapcase — обменять регистр. swap — гл. обмениваться, case — случай, регистр, падеж, дело, расследование...
# title — заголовок, титул.
# lower — нижний.
# upper — верхний.

# s = 'i Learn Python language'
# print(s.capitalize())
# s = 'i LEARN Python LAnguaGE'
# print(s.lower())
# s = '$12344%^$#@!'
# print(s.lower())
# s1 = 'a'
# s2 = s1.upper()
# print(s1, s2)

# s = 'i LEARN Python LAnguaGE'
# print(s.upper())
# s = 'i LEARN Python LAnguaGE'
# print(s.swapcase())

# text = input()
#
# if text == text.title():
#     print('YES')
# else:
#     print('NO')

# text = input()
#
# print(text.swapcase())

# text = input()
#
# if 'хорош' in text.lower():
#     print('YES')
# else:
#     print('NO')

# text = input()
# counter = 0
# for i in text:
#     if i != i.swapcase() and i == i.lower():
#         counter += 1
# print(counter)

# s = 'foo bar foo baz foo qux'
# print(s.find('foo'))
# print(s.find('bar'))
# print(s.find('qu'))
# print(s.find('python'))

# s = '     foo bar foo baz foo qux      '
# print(s.strip())

# s = 'foo bar foo baz foo qux'
# print(s.replace('foo', 'grault'))
# s = 'aabbAAccDDaa'
# s = s.lower()
# print(s.count('a'))


# s = 'www.stepik.org'
# print(s.endswith('.ru'))

# s = 'I learn Python language. Python - awesome!'
# print(s.find('Python'))
#
# s = '     I learn Python language               '
# print(s.strip())
#
# s = 'abcdababa'
# print(s.replace('ab', '123'))

# text = input()
# print(text.count(' ') + 1)

# text = input()
#
# a = 0
# g = 0
# c = 0
# t = 0
#
# for i in text.lower():
#     if i == 'a':
#         a += 1
#     elif i == 'г':
#         g += 1
#     elif i == 'ц':
#         c += 1
#     elif i == 'т':
#         t += 1
# print('Аденин:', a)
# print('Гуанин:', g)
# print('Цитозин:', c)
# print('Тимин:', t)

# text = input().lower()
# print('Аденин:', text.count('а'))
# print('Гуанин:', text.count('г'))
# print('Цитозин:', text.count('ц'))
# print('Тимин:', text.count('т'))

# n = int(input())
# counter = 0
#
# for i in range(1, n + 1):
#     text = str(input())
#     if text.count('11') >= 3:
#         counter += 1
# print(counter)

# text = str(input())
# counter = 0
# for i in text:
#     if i in '0123456789':
#         counter += 1
# print(counter)


# text = str(input())
#
# if text.endswith('.com') or text.endswith('.ru'):
#     print('YES')
# else:
#     print('NO')

# text = str(input())
# counter = 0
# letter = ''
#
# for i in text:
#     if text.count(i) >= counter:
#         counter = text.count(i)
#         letter = i
# print(letter)

# text = str(input())
#
# if text.count('f') == 1:
#     print(text.index('f'))
# elif text.count('f') > 1:
#     print(text.find('f'), text.rfind('f'))
# else:
#     print('NO')

# text = str(input())
# print(text[:text.find('h')] + text[text.rfind('h') + 1:])

# s1 = 'abc123'
# s2 = 'abc$*123'
# s3 = ''
#
# print(s1.isalnum())
# print(s2.isalnum())
# print(s3.isalnum())

# s1 = 'ABCabc'
# s2 = 'abc123'
# s3 = ''
#
# print(s1.isalpha())
# print(s2.isalpha())
# print(s3.isalpha())

# s1 = '1234567'
# s2 = 'abc123'
# s3 = ''
#
# print(s1.isdigit())
# print(s2.isdigit())
# print(s3.isdigit())

# s1 = 'abc'
# s2 = 'abc1$d'
# s3 = 'Abc1$D'
#
# print(s1.islower())
# print(s2.islower())
# print(s3.islower())

# s1 = 'ABC'
# s2 = 'ABC1$D'
# s3 = 'Abc1$D'
#
# print(s1.isupper())
# print(s2.isupper())
# print(s3.isupper())
#
# s = 'aabbAA111ccDDaa'
# print(s.isalnum())
# print(s.isalpha())
# print(s.isdigit())

# s = 'aabb!@#$11cc'
# print(s.islower())

# s = 'AAb!@#$11CC'
# print(s.isupper())

# In 2010, someone paid 10k Bitcoin for two pizzas.

# year = 2010
# amount = '10K'
# currency = 'Bitcoin'
#
# print(f'In {year}, someone paid {amount} {currency} for two pizzas.')

# num1 = ord('A')
# num2 = ord('B')
# num3 = ord('a')
# print(num1, num2, num3)

# chr1 = chr(65)
# chr2 = chr(75)
# chr3 = chr(2344)
# print(chr1, chr2, chr3)

# for i in range(26):
#     print(chr(ord('A') + i))

# print(ord('foo'))

# a, b = int(input()), int(input())
#
# for i in range(a, b + 1):
#     print(chr(i), end=' ')

# text = str(input())
#
# for i in text:
#     print(ord(i), end=' ')

# sdvig = int(input())
# text = str(input())
# char = 0
# shifr = ''
#
# for i in text:
#     char = ord(i) - sdvig
#     if char < 97:
#         shifr = 122 - (96 - char)
#     else:
#         shifr = char
#     print(chr(shifr), end='')

# a = 'asdsadasdsasdas&'
#
# print(a.isletters())

# s = str(input())
# to_print = ''
#
# for i in range(len(s)):
#     if i % 3 != 0:
#         print(s[i], end='')

# text = str(input())
#
# for i in text:
#     if i == '1':
#         i = 'one'
#     print(i, end='')

# print(text.replace('1', 'one'))


# text = str(input())
# count = 0
# text_2 = text.replace('f', 'a', 1)
# text_3 = text_2.find('f')
# # print(text_3)
#
# for i in text:
#     if i == 'f':
#         count += 1
#
# if count <= 0:
#     print('-2')
# else:
#     print(text_3)

# text = 'qwertyhasdfghzxcvb'
# print(text.find('h'))
# print(text.rfind('h'))
# text_2 = text[text.find('h') + 1:text.rfind('h')]
# print(text_2[::-1])
#
# print(text[text.rfind('h'):])

# print(text[:text.find('h')+1] + text_2[::-1] + text[text.rfind('h'):])

# names = ['Michael', 'John', 'Freddie']
# print(names)

# num = int(input())
#
# print(list(range(1, num + 1)))

# num = int(input())
# first = 96
# alphabet = ''
# for i in range(1, num + 1):
#     first += 1
#     alphabet += chr(first)
# print(list(alphabet))


# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
#
# print(primes[16])

# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
# maximum = max(numbers)
# minimum = min(numbers)
# print(sum([max(numbers), min(numbers)]))

# evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# average = sum(evens)/len(evens)
#
# print(average)

# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[3], rainbow[-1] = 'Зеленый', 'Фиолетовый'
#
# print(rainbow)

# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese',
#              'Lahnda']
#
# print(languages[::-1])

# [1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13]
# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
#
# print(numbers1 * 2 + numbers2 * 9 + numbers3)

# Вывел длину списка; ok
# Вывел последний элемент списка; ok
# Вывел список в обратном порядке (вспоминаем срезы); ok
# Вывел YES если список содержит числа 5 и 17, и NO в противном случае; ok
# Вывел список с удаленным первым и последним элементами. ok

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14,
#            8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
#
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
#
# if 5 and 17 in numbers:
#     print('YES')
# else:
#     print('NO')
# del numbers[0]
# del numbers[-1]
# print(numbers)

# n = int(input())
# spisok = []
# for i in range(n):
#     word = input()
#     spisok.append(word)
#
# print(spisok)

# n = int(input())
# lst = [input() for _ in range(n)]
# print(lst)

# Напишите программу, выводящую следующий список:
#
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]

# lst = []
# counter = 1
# for i in range(97, 123):
#     lst.append(chr(i) * counter)
#     counter += 1
# print(lst)

# На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая создает из
# указанных чисел список их кубов.
#
# Формат входных данных
# На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести список, состоящий из кубов указанных чисел.

# num = int(input())
# lst = []
#
# for i in range(num):
#     a = int(input())
#     lst.append(pow(a, 3))
# print(lst)

# На вход программе подается натуральное число n. Напишите программу, которая создает список
# состоящий из делителей введенного числа.
#
# Формат входных данных
# На вход программе подается натуральное число n.
#
# Формат выходных данных
# Программа должна вывести список, состоящий из делителей введенного числа.

# n = int(input())
# lst = []
#
# for i in range(1, n + 1):
#     if n % i == 0:
#         lst.append(i)
# print(lst)



