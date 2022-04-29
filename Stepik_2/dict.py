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

# n = int(input())   # input digit(quantity of sentences)
# list_of_sentences = [input() for _ in range(n)] # create list of sentences
# dict_of_words = {} # create empty dict
#
# for word in list_of_sentences:
#     dict_of_words.setdefault(word[:word.find(':')].lower(), []).append(word[word.find(':') + 1:].lstrip())
#
# m = int(input())  # input digit(quantity of search words)
#
# for i in range(m):
#     m_i = input().lower()
#     if m_i in dict_of_words:
#         print(*dict_of_words[m_i])
#     else:
#         print('Не найдено')

# mydict = {}
#
# for _ in range(int(input())):
#     key, value = input().split(': ')
#     mydict[key.lower()] = value
#
# for _ in range(int(input())):
#     print(mydict.get(input().lower(), 'Не найдено'))

# a, b = input(), input()
# a_d = {}
# b_d = {}
#
# for r in a:
#     a_d[r] = a_d.get(r, 0) + 1
# for c in b:
#     b_d[c] = b_d.get(c, 0) + 1
#
# print('YES' if a_d == b_d else "NO")

# a, b = input().lower(), input().lower()
# a_d, b_d = {}, {}
#
# for r in a:
#     a_d[r.strip('.,!?:;-'' ')] = a_d.get(r, 0) + 1
# for c in b:
#     b_d[c.strip('.,!?:;-'' ')] = b_d.get(c, 0) + 1
#
# print('YES' if a_d == b_d else "NO")


# dict_senses = {}
# for _ in range(int(input())):
#     key, value = input().split()
#     dict_senses[key] = value
#
# word = input()
#
# for k,v in dict_senses.items():
#     if k == word:
#         print(v)
#     elif v == word:
#         print(k)

# words = {}
# for _ in range(int(input())):
#     a, b = input().split()
#     words[a], words[b] = b, a
# print(words[input()])

# a, b = input().split()
# print(a, b)

# slovar = {}
# for _ in range(int(input())):
#     key, value = input().split()
#     slovar[key] = value
#     slovar[value] = key
# print(slovar[input()])

# n = int(input())
# cities = {}
#
# list_of_cities = [input().split() for _ in range(n)]
#
# for c in list_of_cities:
#     cities.setdefault(c[0], c[1:])
# print(cities)
#
# def my_dict(w):
#     for k, v in cities.items():
#         if w in v:
#             print(k)
#
#
# for i in range(int(input())):
#     my_dict(input())


# d = {}
# for _ in range(int(input())):
#     country, *cities = input().split()
#     d.update(dict.fromkeys(cities, country))
# for _ in range(int(input())):
#     print(d[input()])

# for _ in range(int(input())):
#     key, value = input().split(': ')
#     mydict[key.lower()] = value
#
# for _ in range(int(input())):
#     print(mydict.get(input().lower(), 'Не найдено'))
# for i in range(m):
#     m_i = input().lower()
#     if m_i in dict_of_words:
#         print(*dict_of_words[m_i])
#     else:
#         print('Не найдено')

# list1 = [input().split() for i in range(int(input()))]
# d = {}
# for i in list1:
#     d.setdefault(i[1].lower(), []).append(i[0])
#
# for i in range(int(input())):
#     print(d.get(input().lower(), ['абонент не найден']))


# dct = {}
# for _ in range(int(input())):
#     phone, name = input().lower().split()
#     dct.setdefault(name, []).append(phone)
# for _ in range(int(input())):
#     print(*dct.get(input().lower(), ['абонент не найден']))


# s = input()
# n = int(input())
# word = {}
# d = {}
#
# for i in s:
#     word[i] = str(word.get(i, 0) + 1)
#
# for i in range(n):
#     letter, qty = input().split(': ')
#     d[letter] = qty
#
# new_dicts = {v: k for k,v in word.items()}
#
# for k, v in d.items():
#     d[k] = new_dicts[v]
#
# d = {v: k for k,v in word.items()}
#
# for _ in s:
#     print(d[_])


# info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
#         'emp2': {'name': 'Ruslan', 'job': 'Developer'},
#         'emp3': {'name': 'Rustam', 'job': 'Tester'}}
#
# info = dict(emp1 = {'name': 'Timur', 'job': 'Teacher'},
#             emp2 = {'name': 'Ruslan', 'job': 'Developer'},
#             emp3 = {'name': 'Rustam', 'job': 'Tester'})


# ids = ['emp1', 'emp2', 'emp3']
#
# emp_info = [{'name': 'Timur', 'job': 'Teacher'},
#             {'name': 'Ruslan', 'job': 'Developer'},
#             {'name': 'Rustam', 'job': 'Tester'}]
#
# info = dict(zip(ids, emp_info))


# info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
#         'emp2': {'name': 'Ruslan', 'job': 'Developer'},
#         'emp3': {'name': 'Rustam', 'job': 'Tester'}}
#
# info['emp1']['job'] = 'Manager'
#
# print(info['emp1'])

# info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
#         'emp2': {'name': 'Ruslan', 'job': 'Developer'},
#         'emp3': {'name': 'Rustam', 'job': 'Tester'}}
#
# for emp in info:
#     print('Employee ID:', emp)
#     for key in info[emp]:
#         print(key + ':', info[emp][key])
#     print()

# info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
#         'emp2': {'name': 'Ruslan', 'job': 'Developer'},
#         'emp3': {'name': 'Rustam', 'job': 'Tester'}}
#
# for emp, inf in info.items():
#     print('Employee ID:', emp)
#     for key in inf:
#         print(key + ':', inf[key])
#     print()

# ГЕНЕРАТОР СЛОВАРЕЙ

# squares = {i: i**2 for i in range(6)}
# print(squares)

# {ключ: значение for переменная in последовательность}
# где переменная — имя некоторой переменной, последовательность — последовательность значений, которые она принимает
# (любой итерируемый объект), ключ: значение — некоторое выражение, как правило, зависящее от использованной в списочном
# выражении переменной, которой будут заполнены элементы словаря.

# dict1 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
# selected_keys = [0, 2, 5]
#
# dict2 = {k: dict1[k] for k in selected_keys}
#
# print(dict2)

# squares = {i: {j: j**2 for j in range(i + 1)} for i in range(5)}
#
# for value in squares.values():
#     print(value)

# marks = {
#    'class':{
#       'student':{
#          'name':'Rosaly',
#          'marks':{
#             'physics':70,
#             'history':80
#          }
#       }
#    }
# }
#
# print(marks['class']['student']['marks']['history'])


# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
# result = {i: numbers[i] ** 2 for i in range(len(numbers))}
#
# print(result)


# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62,
#                     'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654,
#                     'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271,
#                     'anna': 55, 'madlen': 876}
#
# result = {k: v for k, v in favorite_numbers.items() if 10 <= v <= 99}
#
# print(result)
#
# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
#           9: 'September', 10: 'October', 11: 'November', 12: 'December'}
#
# result = {k: v for v, k in months.items()}
#
# print(result)
# import time
# start = time.time()
# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
#
# # result = {int(k[:k.find(':')]): k[k.find(':')+1:] for k in s.split()}
# # result = {int(k):v for k, v in [l.split(':') for l in s.split()]}
# end = time.time()
#
# print(start - end)

# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
#
# result = {k: [v for v in range(1, k + 1) if k % v == 0] for k in numbers}
#
# print(result)

# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
#
# result = {k: [ord(v) for v in k] for k in words}
#
# print(result)

# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
#
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
#
# result = {k: v for k, v in letters.items() if k not in remove_keys}
#
# print(result)


# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50),
#             'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78),
#             'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80),
#             'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
#
# result = {k: v for k, v in students.items() if v[0] > 167 and v[1] < 75}
#
# print(result)

# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24),
#           (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
#
# result = {k[0]: tuple(k[1:]) for k in tuples}
#
# print(result)

# [{'S001': {'Camila Rodriguez': 86}}, {'S002': {'Juan Cruz': 98}},...]

# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
#
# result = [{k: {v: c}} for k, v, c in zip(student_ids, student_names, student_grades)]
# result =  [{student_ids[i]:{student_names[i]:student_grades[i]}} for i in range (len(student_ids))]
#
# print(result)



# list_text = [i for i in input().split()]
# dict_text = {}
#
# for k in list_text:
#     dict_text[k] = dict_text.get(k, -1) + 1
#     print(dict_text[k], end=' ')



# my_dict = {}
# for _ in range(int(input())):
#     k, v = input().split()
#     my_dict[k] = v
# z = input()
# for a, b in my_dict.items():
#     if z == b:
#         print(a)
#     elif z == a:
#         print(b)
#
# n = int(input())
# d = {}
# for i in range(n):
#     first, second = input().split()
#     d[first] = second
#     d[second] = first
# print(d[input()])

# my_dict = {}
# for _ in range(int(input())):
#     president, vote = input().split()
#     my_dict[president] = my_dict.get(president, 0) + int(vote)
#
#
#
# for k, v in sorted(my_dict.items()):
#     print(k, v)






