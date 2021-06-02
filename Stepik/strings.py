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