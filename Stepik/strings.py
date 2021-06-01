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


# l = len(text) + 1
# part_1 = text[0:l//2]
# part_2 = text[l//2:]
# print (part_1)
# print (part_2)

s = str(input())
l = len(s) + 1

part_1 = s[:l // 2]
part_2 = s[l // 2:]

print(part_2 + part_1)



