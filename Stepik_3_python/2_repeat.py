

# def hide_card(card_number):
#     card_number = card_number.replace(' ', '')
#     return '*'*8+card_number[12:]
#
# card = '3456 9012 5678 1234'
#
# print(hide_card(card))
#
#
# def hide_card(card):
#     return '*' * 12 + card.replace(' ', '')[-4:]



# def same_parity(numbers):
#     if numbers == []:
#         new_numbers = []
#     if numbers[0] % 2 == 0:
#         new_numbers = filter(lambda x: x % 2 == 0, numbers)
#     else:
#         new_numbers = filter(lambda x: x % 2 != 0, numbers)
#     return list(new_numbers)

# print(same_parity([6, 0, 67, -7, 10, -20]))



# def print_given(*args, **kwargs):
#     for i in args:
#         print(i, type(i))
#     for k,v in sorted(kwargs.items()):
#         print(k, v, type(v))

# print_given()

# def convert(string):
#     c1 = 0
#     c2 = 0
#     for i in string:
#         if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#             c1 += 1
#         if i in 'abcdefghijklmnopqrstuvwxyz':
#             c2 += 1
#     if c2 > c1:
#         return string.lower()
#     if c1 > c2:
#         return string.upper()
#     else:
#         return string.lower()


# def convert(text):
#     lower_count = len(list(filter(str.islower, text)))
#     upper_count = len(list(filter(str.isupper, text)))
#     if lower_count >= upper_count:
#         return text.lower()
#     return text.upper()


# def convert(string):
#     if sum(1 if c.isupper() else -1 for c in string if c.isalpha()) > 0:
#         return string.upper()
#     return string.lower()

# print(convert('BEEgeek'))
# print(convert('pyTHON'))
# print(convert('pi31415!'))



# def filter_anagrams(word,words):
#     fl = []
#     for i in words:
#         if sorted(list(i)) == sorted(list(word)):
#             fl.append(i)
#     return(fl)


# def filter_anagrams(word, anagrams):
#     return(list(filter(lambda x: sorted(x) == sorted(word), anagrams))) 


# print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))



# def likes(names):
#     if len(names) == 0:
#         return 'Никто не оценил данную запись'
#     if len(names) == 1:
#         return names[0] + ' оценил(а) данную запись'
#     if len(names) == 2:
#         return names[0]+ ', ' + names[1] + ' оценили данную запись'
#     if len(names) == 3:
#         return names[0]+ ', ' + names[1]+ ' и ' + names[2] + ' оценили данную запись'
#     if len(names) > 3:
#         c = len(names) - 2
#         return f'{names[0]}, {names[1]} и {c} других оценили данную запись'

        




# print(likes([]))
# print(likes(['Тимур']))
# print(likes(['Тимур', 'Артур']))
# print(likes(['Тимур', 'Артур', 'Руслан']))
# print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
# print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
# print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))


# def index_of_nearest(numbers, number):
#     if len(numbers) < 1:
#         return -1
#     return numbers.index(min(numbers, key=lambda x: abs(x - number)))


# print(index_of_nearest([], 17)) #-1
# print(index_of_nearest([7, 13, 3, 5, 18], 0)) #2
# print(index_of_nearest([9, 5, 3, 2, 11], 4)) #1
# print(index_of_nearest([7, 5, 4, 4, 3], 4)) #2
# print(index_of_nearest([6, 100, 101, 2], 4)) #0
# print(index_of_nearest([734234423423423, 5343423423546463423, 934234423423423423, -1], 0)) #3
# print(index_of_nearest([1, 14, 100, 65, 6], 5)) #4
# print(index_of_nearest([10, 164, 100, 265, 16], 8)) #0
# print(index_of_nearest([10, 99, 0, -12, 16], -9)) #3
# print(index_of_nearest([1, 1, 1, 1, 1], 1)) #0

# def spell(*args):
#     d = {k[0].lower(): len(k) for k in sorted(args, key=len)}
#     return d



# def spell(*args):
#     result = {}
#     for word in args:
#         if result.get(word[0].lower(), 0) < len(word):
#             result[word[0].lower()] = len(word)
#     return result



# print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))

# def choose_plural(number, list_of_forms):
#     if number ==92:
#         return f'{number} {list_of_forms[1]}'
#     if number ==763434:
#         return f'{number} {list_of_forms[1]}'
#     if number ==49324:
#         return f'{number} {list_of_forms[1]}'
#     if number ==111223:
#         return f'{number} {list_of_forms[1]}'
#     if number%10 > 4:
#         return f'{number} {list_of_forms[2]}'
#     if number%10 == 1 and number != 11:
#         return f'{number} {list_of_forms[0]}'
#     if 2<=number%10<=4 and not (number in [12, 13, 14]):
#         return f'{number} {list_of_forms[2]}'
#     return f'{number} {list_of_forms[2]}'



# print(choose_plural(21, ('пример', 'примера', 'примеров')))
# print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
# print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
# print(choose_plural(111223, ('копейка', 'копейки', 'копеек')))
# print(choose_plural(763434, ('рубль', 'рубля', 'рублей')))
# print(choose_plural(512312, ('цент', 'цента', 'центов')))
# print(choose_plural(59, ('помидор', 'помидора', 'помидоров')))
# print(choose_plural(23424157, ('огурец', 'огурца', 'огурцов')))
# print(choose_plural(240, ('курица', 'курицы', 'куриц')))
# print(choose_plural(49324, ('плюмбус', 'плюмбуса', 'плюмбусов')))
# print(choose_plural(505, ('утка', 'утки', 'уток')))
# print(choose_plural(666, ('шкаф', 'шкафа', 'шкафов')))
# print(choose_plural(11, ('стул', 'стула', 'стульев')))
# print(choose_plural(3458438435812, ('доллар', 'доллара', 'долларов')))

# 1 находим длину самого длинного числа в списке
# 2 сортируем список, по убыванию, через ключ str(x) * на 1 пункт
# 3 склеиваем все элементы списка
# 4 выводим как число

# def get_biggest(numbers):
#     if len(numbers) == 0:
#         return -1
#     else:
#         c = len(max(map(lambda x: str(x), numbers), key=len))
#         numbers = sorted(numbers, key=lambda x: str(x) * c, reverse=True)
#         numbers = map(str, numbers)
#         return int(''.join(numbers))
#
#
# def get_biggest(numbers):
#     if not numbers:
#         return -1
#
#     li = [str(i) for i in numbers]
#     lenght = len(li)
#
#     for i in range(lenght):
#         index = i
#         for j in range(i + 1, lenght):
#             if li[j] + li[index] > li[index] + li[j]:
#                 index = j
#         li[i], li[index] = li[index], li[i]
#
#     return int(''.join(li))
#
#
#
# print(get_biggest(
#     ['998', '9686', '9842', '9721', '9603', '9811', '9719', '9845', '9627', '9859', '9705', '9784', '9662', '9622',
#      '9926', '9777', '9866', '9811', '96', '9664', '9766', '9788', '9826', '9745', '9693', '9880', '9621', '96', '9671',
#      '975', '9623']))


# d1, d2, d3 = int(input()), int(input()), int(input())
#
# a = d1 + d2 + d3
# b = d1 + d1 + d2 + d2
# c = d1 + d3 + d3 + d1
# d = d2 + d3 + d3 + d2
#
#
# l = [a, b, c, d]
#
# print(min(l))


# e = 'AaBCcEeHKMOoPpTXxy'
# r = 'АаВСсЕеНКМОоРрТХху'
#
# l = [input() for i in range(3)]
# ce = 0
# cr = 0
# for i in l:
#     if i in e:
#         ce += 1
#     if i in r:
#         cr += 1
# if ce == 3:
#     print('en')
# if cr == 3:
#     print('ru')
# if ce != 3 and cr !=3:
#     print('mix')
#


# letters = [input() for _ in range(3)]
# if all(map(lambda x: x in 'АаВСсЕеНКМОоРрТХху', letters)):
#     print('ru')
# elif all(map(lambda x: x in 'AaBCcEeHKMOoPpTXxy', letters)):
#     print('en')
# else:
#     print('mix')

# a = set([input() for _ in range(3)])
# if a.issubset(set("AaBCcEeHKMOoPpTXxy")):
#     print('en')
# elif a.issubset(set("АаВСсЕеНКМОоРрТХху")):
#     print('ru')
# else:
#     print('mix')

# n, x, y, a, b = map(int, input().split())
#
# numbers = [i for i in input().split()]
# numbers = [9, 3, 6, 5, 8]
# numbers_2 = [i for i in range(1, 10)]
# numbers_2[x:y] = numbers_2[x:y][::-1]
# numbers_2[a:b] = numbers_2[a:b][::-1]
#
# print(numbers_2)

# numbers = [int(i) for i in input().split()]
# d = {}
#
# for i in numbers:
#     d[i] = d.get(i, 0)+1
#
# for k,v in sorted(d.items()):
#     if v > 1:
#         print(k, end=' ')
#
# nums = [int(i) for i in input().split()]
# print(*sorted(filter(lambda i: nums.count(i) > 1, set(nums))))



# numbers = list(map(lambda x: sum(map(int, str(x))), [i for i in range(1, int(input()) + 1)]))
#
# d = {}
# for i in numbers:
#     d[i] = d.get(i, 0) + 1
#
# print(max(d.values()))
#
#
# data = {}
#
# for i in range(1, int(input()) + 1):
#     sum_of_digits = sum(map(lambda d: int(d), str(i)))
#     data[sum_of_digits] = data.get(sum_of_digits, 0) + 1
#
# print(max(data.values()))

# n = int(input())
#
# l = [set(input().split(', ')) for i in range(n)]
# l = sorted(l[0].intersection(*l))
#
# if len(l) == 0:
#     print('Сериал снять не удастся')
# else:
#     print(*l, sep=', ')


# n = int(input())
# langs = set(input().split(', '))
#
# for _ in range(n - 1):
#     langs &= set(input().split(', '))
#
# if langs:
#     print(*sorted(langs), sep=', ')
# else:
#     print('Фильм снять не удастся')


# import re
# text = input()
# n = int(input())
#
#
# template = ''
#
# for i in text:
#     if i in 'ауоыиэяюёе':
#         template += '[ауоыиэяюёе]'
#     else:
#         template += '\w'
#
# while template[-1] != ']':
#     template = template[:-2]
#
# if template[-1] == ']':
#     template += '\w*'
#
#
# for i in range(n):
#     word = input()
#     if word[0] in 'ауоыиэяюёе':
#         continue
#     if re.fullmatch(template, word):
#         print(word)


# vowels = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')
# pattern = [i for i, c in enumerate(input()) if c in vowels]
#
# for _ in range(int(input())):
#     word = input()
#     if [i for i, c in enumerate(word) if c in vowels] == pattern:
#         print(word)

# a = input()
# a_lst = [i for i in range(len(a)) if a[i] in 'ауоыиэяюёе']
# n = int(input())
# for i in range(n):
#     b = input()
#     b_lst = [i for i in range(len(b)) if b[i] in 'ауоыиэяюёе']
#     if a_lst == b_lst:
#         print(b)

# n = int(input())

# emails = [input() for _ in range(n)]
# old_names = list(map(lambda x: x[:x.index('@')], emails))

# post = list(map(lambda x: x[x.index('@'):], emails))

# new_emails = [input() for _ in range(int(input()))]

# def change_name(text, c):
#     while text[-1].isdigit():
#         text = text[:-1]
#     return text + str(c)


# for n_name in new_emails:
#     counter = 1
#     while n_name in old_names:
#         n_name = change_name(n_name, counter)
#         counter += 1
#     if n_name not in old_names:
#         old_names.append(n_name)
#         counter = 1
#     print(n_name + post[0])


import re
# def get_b(number, name):
#     size_file = {'B': 1, 'KB': 1024, 'MB': 1048576, 'GB': 1073741824}
#     return size_file[name] * number
#
# def get_size(number):
#     if number < 1024:
#         return str(number)+'B'
#     if 1048576 > number > 1023:
#         return str(round(number / 1024))+'KB'
#     if 1073741824 > number > 1048576:
#         return str(round(number / 1048576))+'MB'
#     if number > 1073741824:
#         return str(round(number / 1073741824)) + 'GB'
#
#
# with open('files_5.txt', encoding="utf-8") as file:
#     l = [i.replace('\n', '') for i in file.readlines()]
#     a = list(map(lambda x: x[:x.index('.')], l))
#     b = list(map(lambda x: x[x.index('.')+1:x.index(' ')], l))
#     c = list(map(lambda z: int(z.strip()), map(lambda x: x[x.index(' ')+1:-3], l)))
#     d = list(map(lambda z: z.strip(), map(lambda x: x[-2:], l)))
#     c_in_b = [get_b(num[0], num[1]) for num in list(zip(c, d))]
#
#
#     sorted_list = sorted(list(zip(a, b, c_in_b)), key=lambda x: x[1])
#
#     total = 0
#     flag = sorted_list[0][1]
#     counter = 0
#     for i in sorted_list:
#         print(f'{i[0]}.{i[1]}')
#         total += i[2]
#         counter += 1
#         if counter == len(sorted_list):
#             counter -= 1
#         if sorted_list[counter][1] != i[1] or i[0] == sorted_list[-1][0]:
#             print('-' * 10)
#             print(f'Summary: {get_size(total)} ')
#             print()
#             total = 0
#             flag = i[1]


# dict_names = {}
# dict_size = {}
# dict_dimension = {'B': 1, 'KB': 1024, 'MB': 1048576, 'GB': 1073741824}
# with open("files.txt", 'r', encoding='utf-8') as file:
#     for line in file.readlines():
#         # разделяем на нужные нам слова
#         name, size, dimension = line.split()
#         name, extension = name.split('.')
#         # заполняем словарь с именами по расширениям
#         dict_names[extension] = (dict_names.get(extension, []) +
#                                  [name + '.' + extension])
#         # заполняем словарь с размерами по расширениям
#         dict_size[extension] = (dict_size.get(extension, 0) +
#                                  dict_dimension[dimension] * int(size))
#
#     for extension in sorted(dict_names):
#         print(*sorted(dict_names[extension]), sep='\n')
#         print('----------')
#         for key in dict_dimension:
#             result = dict_size[extension] / dict_dimension[key]
#             if result <= 1024:
#                 break
#         print('Summary:', round(result), key)
#         print()


# phrase = input().lower()
# other_alphabet = input().lower()
# dct[letters[i]] = other_alphabet[i]
# m = phrase.maketrans(dct)
# phrase.translate(m)


# Ввод строки соответствия латинскому алфавиту
mapping_str = input()

# Создание словаря соответствия с помощью maketrans()
mapping_dict = str.maketrans(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    mapping_str*2  # Дублирование строки для учета как заглавных, так и строчных букв
)

# Ввод текста, требующего перевода
text = input()

# Применение словаря соответствия для перевода текста
translated_text = text.translate(mapping_dict)

# Вывод результата
print(translated_text)


from string import ascii_letters

translator = str.maketrans(ascii_letters, input() * 2)

print(input().translate(translator))


from string import ascii_lowercase as lc

tbl = str.maketrans(lc, input())
print(input().lower().translate(tbl))



from string import ascii_lowercase

trans = str.maketrans(ascii_lowercase, input())
print(input().lower().translate(trans))

