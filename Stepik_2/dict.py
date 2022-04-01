# # Для вывода ключей словаря каждого на отдельной строке можно использовать следующий код:
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# for key in capitals:
#     print(key)
#
#
# # Для вывода значений словаря каждого на отдельной строке можно использовать следующий код:
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# for key in capitals:
#     print(capitals[key])
#
#
# # Для вывода элементов словаря каждого на отдельной строке можно использовать следующий код:
# capitals = {'Россия': 'Москва',
#             'Франция': 'Париж',
#             'Чехия': 'Прага'}
#
# for key in capitals:
#     print('Столица', key, '- это', capitals[key])

# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# for key in capitals.keys():     # итерируем по списку ['Россия', 'Франция', 'Чехия']
#     print(key)

# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# for value in capitals.values():     # итерируем по списку ['Москва', 'Париж', 'Прага']
#     print(value)


# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# for item in capitals.items():
#     print(item)

# РАСПАКОВКА

# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# for key, value in capitals.items():
#     print(key, '-', value)


# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# print(*capitals, sep='\n')


# capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}
#
# for key in sorted(capitals):
#     print(key)


# capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}
#
# for key, value in sorted(capitals.items(), key = lambda x: x[1]):
#     print(value)


# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# if 'Россия' in capitals:
#     print('В словаре есть ключ Россия')

#
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# if 'Париж' in capitals.values():
#     print('В словаре есть значение Париж')

# my_dict = {1: [0, 1], 2: [2, 3], 3: [4, 5]}
#
# for k in my_dict:
#     print(k)

# my_dict = {1: [0, 1], 2: [2, 3], 3: [4, 5]}
#
# for k in my_dict.values():
#     print(k)


# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# mylist = []
# for book in users:
#     for value in book['phone'][-1]:
#         if value == '8':
#             mylist.append(book['name'])
# print(*sorted(mylist))

# result = [user['name'] for user in users if user['phone'].endswith('8')]
#
# print(*sorted(result))

# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
#
#
# mylist = []
# for book in users:
#     if 'email' in book and book['email'] != '':
#         continue
#     else:
#         mylist.append(book['name'])
# print(*sorted(mylist))


# d = {
#     "0": "zero",
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine"
# }
# n = input()
#
# for k in n:
#     print(d[k], end=' ')

# print(*[d[key] for key in input()])


# course_dict = {
#     'CS101': '3004, Хайнс, 8:00',
#     'CS102': '4501, Альварадо, 9:00',
#     'CS103': '6755, Рич, 10:00',
#     'NT110': '1244, Берк, 11:00',
#     'CM241': '1411, Ли, 13:00'
# }
# key = input()
# print(f'{key}: {course_dict[key]}')

# text = input().lower().replace('"', '')
#
# digits = {
#     ".": '1', ",": '11', "?": '111', "!": '1111', ":": '11111',
#     "a": '2', "b": '22', "c": '222',
#     "d": '3', "e": '33', "f": '333',
#     "g": '4', "h": '44', "i": '444',
#     "j": '5', "k": '55', "l": '555',
#     "m": '6', "n": '66', "o": '666',
#     "p": '7', "q": '77', "r": '777', "s": '7777',
#     "t": '8', "u": '88', "v": '888',
#     "w": '9', "x": '99', "y": '999', "z": '9999',
#     " ": '0'
# }
#
# for i in text:
#     print(digits[i], end='')

# keyboard = {
#     "1": ".,?!:",
#     "2": "ABC",
#     "3": "DEF",
#     "4": "GHI",
#     "5": "JKL",
#     "6": "MNO",
#     "7": "PQRS",
#     "8": "TUV",
#     "9": "WXYZ",
#     "0": " "
# }
#
# for letter in input().upper():
#     for key, value in keyboard.items():
#         if letter in value:
#             print(key * (value.index(letter) + 1), end="")

# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# text = input()
# # my_dict = dict(zip(letters,morse))
# my_dict = {}
# for i in range(len(letters)):
#     my_dict[letters[i]] = morse[i]
# for k in text.upper():
#     if k in letters:
#         print(my_dict[k], end=' ')
#
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     if num not in result:
#         result[num] = 1
#     else:
#         result[num] += 1

# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     result[num] = result.get(num, 0) + 1

# num = int(input())
#
# description = {1: 'One', 2: 'Two', 3: 'Three'}
#
# print(description.get(num, 'Unknown'))


# dct = {'понедельник': 1, 'вторник': 2, 'среда': 3}
#
# print(dct.get('понедельник', 'Не найдено'))

# dct = {'понедельник': 1, 'вторник': 2, 'среда': 3}
#
# print(dct.get('пятница', 'Не найдено'))


# result = {}
# for i in range(1, 16):
#     result[i] = result.get(i, i**2)
#
# print(result)


# result = {i: i**2 for i in range(1, 16)}

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# result = dict1.copy()
#
# for k, v in dict2.items():
#     result[k] = result.get(k, 0) + v

# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
#
# result = {}
# for i in text:
#     result[i] = result.get(i, 0) + 1
#
# print(result)

# {value:key for key, value in dict.items()} меняет местами ключ и значение в словаре.

# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange ' \
#     'barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry ' \
#     'apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana ' \
#     'melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry ' \
#     'apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit ' \
#     'banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

# result = {}
#
# for i in s.split():
#     result[i] = result.get(i, 0) + 1
# flag = max(result.values())
#
# for k, v in sorted(result.items()):
#     if v == flag:
#         print(k)
#         break

#
# text = 'ballboy'
# for i in text:
#         if text.index(i) == 0:
#                 print(i, end=' ')




# Вам доступен список pets, содержащий информацию о собаках и их владельцах.  Каждый элемент списка – это кортеж вида
# (кличка собаки, имя владельца, фамилия владельца, возраст владельца).
#
# Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого владельца будут
# перечислены его собаки. Ключом словаря должен быть кортеж (имя, фамилия, возраст владельца), а значением – список
# кличек собак (сохранив исходный порядок следования).
#
# Примечание 1. Не забывайте: кортежи являются неизменяемыми, поэтому могут быть ключами словаря.
#
# Примечание 2. Обратите внимание, что у некоторых владельцев по несколько собак.
#
# Примечание 3. Выводить содержимое словаря result не нужно.

# sample: {('Josh', 'King', 25): ['Rusty', 'Balto', 'Barry', 'Lassie']}

# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# result = {}
#
# for pet in pets:
#     result.setdefault(pet[1:], []).append(pet[0])
# print(result)

# Самое редкое слово 🌶️
# На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего,
# без учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести слово (в нижнем регистре), встречаемое реже всего.
#
# Примечание 1. Программа не должна быть чувствительной к регистру, слова apple и Apple должна воспринимать как
# одинаковые.
#
# Примечание 2. Слово — последовательность букв. Кроме слов в тексте могут присутствовать пробелы и знаки
# препинания .,!?:;-, которые нужно игнорировать. Других символов в тексте нет.
# lower().strip('.,;:-?!')

# text = input().lower().strip('.,;:-?!').split()
#
# result = {}
#
# for word in sorted(text):
#     result[word.lower().strip('.,;:-?!')] = result.get(word, 0) + 1
# flag = min(result.values())
#
# for k, v in result.items():
#     if v == flag:
#         print(k)
#         break


# Исправление дубликатов 🌶️
# На вход программе подается строка, содержащая строки-идентификаторы. Напишите программу, которая исправляет их так,
# чтобы в результирующей строке не было дубликатов. Для этого необходимо прибавлять к повторяющимся идентификаторам
# постфикс _n, где n – количество раз, сколько такой идентификатор уже встречался.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая строки-идентификаторы, разделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести исправленную строку, не содержащую дубликатов сохранив при этом исходный порядок.

# text = 'a b c a a d c'.split()
# result = {}
#
# for word in text:
#     result[word] = result.get(word, -1) + 1
#     if result[word] > 0:
#         print(word + '_' + str(result[word]))
#     else:
#         print(word)



# lst = input().split()
# res = {}
# for c in lst:
#     if c in res:
#         print(f'{c}_{res[c]}', end=' ')
#     else:
#         print(c, end=' ')
#     res[c] = res.get(c, 0) + 1

# d, res = {}, []
# for w in input().split():
#     n = d[w] = d.get(w, -1) + 1
#     res.append(f'{w}_{n}' if n > 0 else w)
# print(*res)