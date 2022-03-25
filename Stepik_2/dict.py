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

users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

