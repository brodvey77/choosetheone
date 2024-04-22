# from collections import namedtuple
#
# Fruit = namedtuple('Fruit', ['name', 'color', 'vitamins'])
#
# print(Fruit)


# from collections import namedtuple
#
# Game = namedtuple('Game', 'name developer publisher')
#
# ExtendedGame = namedtuple('ExtendedGame', [*Game._fields, 'release_date', 'price'])
#
# game = Game('GENERALS', 'Серёга', 'HDD')
# print(game)
# game2 = ExtendedGame('GENERALS', 'Серёга', 'HDD', '250565', 250000)
# print(game2)

# from collections import namedtuple
# import pickle
#
# Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
#
# with open('data.pkl', 'rb') as file:
#     data = pickle.load(file)
#
#     for i in data:
#         dct = i._asdict()
#         for k,v in dct.items():
#             print(f'{k}: {v}')
#         print()


# from collections import namedtuple
#
# User = namedtuple('User', ['name', 'surname', 'email', 'plan'])
#
# users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
#          User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
#          User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
#          User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
#          User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
#          User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
#          User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
#          User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
#          User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
#          User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
#          User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
#          User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
#          User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
#          User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
#          User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]
#
# for el in sorted(users, key=lambda x: (('Gold', 'Silver', 'Bronze', 'Basic').index(x.plan), x.email)):
#     print(f'{el.name} {el.surname}')
#     print(f'  Email: {el.email}')
#     print(f'  Plan: {el.plan}')
#     print()


# import csv
# from collections import namedtuple
# from datetime import datetime
#
# friends = []
# with open('meetings.csv', encoding='utf-8') as file:
#     rows = csv.reader(file, delimiter=',')
#     for i in rows:
#         headers = i
#         break
#
#     Friend = namedtuple('Friend', headers)
#
#     for f in rows:
#         friends.append(Friend._make(f))
#
# friends_s = sorted(friends, key=lambda x: (datetime.strptime(x.meeting_date,'%d.%m.%Y' ), datetime.strptime(x.meeting_time, '%H:%M')))
#
# for i in friends_s:
#     print(i.surname, i.name)




# import csv
# from collections import namedtuple
# from datetime import datetime
#
# with open('meetings.csv', encoding='u8') as fi:
#     rows = csv.DictReader(fi)
#     Friend = namedtuple('Friend', rows.fieldnames)
#     meetings = [Friend(**row) for row in rows]
#
# meetings.sort(key=lambda item: datetime.strptime(f'{item.meeting_date} {item.meeting_time}', '%d.%m.%Y %H:%M'))
# for meeting in meetings:
#     print(meeting.surname, meeting.name)


# from datetime import datetime as dt
#
# with open('meetings.csv', encoding='utf-8') as file:
#     data, s = __import__('csv').DictReader(file), '%d.%m.%Y %H:%M'
#     for i in sorted(data, key=lambda x: dt.strptime(f'{x["meeting_date"]} {x["meeting_time"]}', s)):
#         print(i['surname'], i['name'])

# from collections import defaultdict

# from collections import defaultdict
#
# data = defaultdict(list)
# print(data['key1'])
#
# data.default_factory = dict
# print(data['key2'])
#
# data.default_factory = tuple
# print(data['key3'])

#
# from collections import defaultdict

# data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061), ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041), ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729), ('Tutorials', 977), ('Books', 656)]
#
# d = {}
#
# for i in data:
#     d[i[0]] = d.get(i[0], 0) + i[1]
#
# for k,v in sorted(d.items()):
#     print(f'{k}: ${v}')

# from collections import defaultdict
#
# data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061), ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041), ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729), ('Tutorials', 977), ('Books', 656)]
#
# result = defaultdict(int)
#
# for key, value in data:
#     result[key] += value
#
# for key, value in sorted(result.items()):
#     print(f'{key}: ${value}')

# from collections import defaultdict
#
# staff = [('Sales', 'Robert Barnes'), ('Developing', 'Thomas Porter'), ('Accounting', 'James Wilkins'), ('Sales', 'Connie Reid'), ('Accounting', 'Brenda Davis'), ('Developing', 'Miguel Norris'), ('Accounting', 'Linda Hudson'), ('Developing', 'Deborah George'), ('Developing', 'Nicole Watts'), ('Marketing', 'Billy Lloyd'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Bernice Ramos'), ('Sales', 'Jose Taylor'), ('Sales', 'Katie Warner'), ('Accounting', 'Steven Diaz'), ('Accounting', 'Kimberly Reynolds'), ('Accounting', 'John Watts'), ('Accounting', 'Dale Houston'), ('Developing', 'Arlene Gibson'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Rosemary Garcia'), ('Marketing', 'Ralph Morgan'), ('Marketing', 'Sam Davis'), ('Marketing', 'Gail Hill'), ('Accounting', 'Michelle Wright'), ('Accounting', 'Casey Jenkins'), ('Sales', 'Evelyn Martin'), ('Accounting', 'Aaron Ferguson'), ('Marketing', 'Andrew Clark'), ('Marketing', 'John Gonzalez'), ('Developing', 'Wilma Woods'), ('Sales', 'Marie Cooper'), ('Accounting', 'Kay Scott'), ('Sales', 'Gladys Taylor'), ('Accounting', 'Ann Bell'), ('Accounting', 'Craig Wood'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Mario Reynolds'), ('Marketing', 'Helen Taylor'), ('Marketing', 'Mary King'), ('Accounting', 'Jane Jackson'), ('Marketing', 'Carol Peters'), ('Sales', 'Alicia Mendoza'), ('Accounting', 'Edna Cunningham'), ('Developing', 'Joyce Rivera'), ('Sales', 'Joseph Lee'), ('Sales', 'John White'), ('Marketing', 'Charles Bailey'), ('Sales', 'Chester Fernandez'), ('Sales', 'John Washington')]
#
# d = defaultdict(int)
#
# for key, value in staff:
#     d[key] += 1
#
# for k,v in sorted(d.items()):
#     print(f'{k}: {v}')



# from collections import defaultdict
#
# staff_broken = [('Developing', 'Miguel Norris'), ('Sales', 'Connie Reid'), ('Sales', 'Joseph Lee'),
#                 ('Marketing', 'Carol Peters'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Ann Bell'),
#                 ('Marketing', 'Ralph Morgan'), ('Accounting', 'Gloria Higgins'), ('Developing', 'Wilma Woods'),
#                 ('Developing', 'Wilma Woods'), ('Marketing', 'Bernice Ramos'), ('Marketing', 'Joyce Lawrence'),
#                 ('Accounting', 'Craig Wood'), ('Developing', 'Nicole Watts'), ('Sales', 'Jose Taylor'),
#                 ('Accounting', 'Linda Hudson'), ('Accounting', 'Edna Cunningham'), ('Sales', 'Jose Taylor'),
#                 ('Marketing', 'Helen Taylor'), ('Accounting', 'Kimberly Reynolds'), ('Marketing', 'Mary King'),
#                 ('Sales', 'Joseph Lee'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Andrew Clark'),
#                 ('Accounting', 'John Watts'), ('Accounting', 'Rosemary Garcia'), ('Accounting', 'Steven Diaz'),
#                 ('Marketing', 'Mary King'), ('Sales', 'Gladys Taylor'), ('Developing', 'Thomas Porter'),
#                 ('Accounting', 'Brenda Davis'), ('Sales', 'Connie Reid'), ('Sales', 'Alicia Mendoza'),
#                 ('Marketing', 'Mario Reynolds'), ('Sales', 'John White'), ('Developing', 'Joyce Rivera'),
#                 ('Accounting', 'Steven Diaz'), ('Developing', 'Arlene Gibson'), ('Sales', 'Robert Barnes'),
#                 ('Sales', 'Charlotte Cox'), ('Accounting', 'Craig Wood'), ('Marketing', 'Carol Peters'),
#                 ('Marketing', 'Ralph Morgan'), ('Accounting', 'Kay Scott'), ('Sales', 'Evelyn Martin'),
#                 ('Marketing', 'Billy Lloyd'), ('Sales', 'Gladys Taylor'), ('Developing', 'Deborah George'),
#                 ('Sales', 'Charlotte Cox'), ('Marketing', 'Sam Davis'), ('Sales', 'John White'),
#                 ('Sales', 'Marie Cooper'), ('Marketing', 'John Gonzalez'), ('Sales', 'John Washington'),
#                 ('Sales', 'Chester Fernandez'), ('Sales', 'Alicia Mendoza'), ('Sales', 'Katie Warner'),
#                 ('Accounting', 'Jane Jackson'), ('Sales', 'Chester Fernandez'), ('Marketing', 'Charles Bailey'),
#                 ('Marketing', 'Gail Hill'), ('Accounting', 'Casey Jenkins'), ('Accounting', 'James Wilkins'),
#                 ('Accounting', 'Casey Jenkins'), ('Marketing', 'Mario Reynolds'), ('Accounting', 'Aaron Ferguson'),
#                 ('Accounting', 'Kimberly Reynolds'), ('Sales', 'Robert Barnes'), ('Accounting', 'Aaron Ferguson'),
#                 ('Accounting', 'Jane Jackson'), ('Developing', 'Deborah George'), ('Accounting', 'Michelle Wright'),
#                 ('Accounting', 'Dale Houston')]
#
# d = defaultdict(list)
#
# for key, value in staff_broken:
#     d[key].append(value)
#
# for k, v in sorted(d.items()):
#     n_v = ', '.join(sorted(set(v)))
#     print(f'{k}: {n_v}')



# from collections import defaultdict
#
# def wins(pairs):
#     d = defaultdict(set)
#     for key, value in pairs:
#         d[key].add(value)
#     return d
#
#
# result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Артур', 'Дима')])
#
# for winner, losers in sorted(result.items()):
#     print(winner, '->', *sorted(losers))


# from collections import defaultdict
#
# def flip_dict(d):
#     flipped_dict = defaultdict(list)
#     for key, values in d.items():
#         for value in values:
#             flipped_dict[value].append(key)
#     return flipped_dict
#
# data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'], 'Anri': ['juice', 'coffee']}
#
# for key, values in flip_dict(data).items():
#     print(f'{key}: {", ".join(values)}')
#
#
#
# from collections import defaultdict
#
# def flip_dict(data):
#     fliped_data = defaultdict(list)
#     for key, values in data.items():
#         for value in values:
#             fliped_data[value].append(key)
#     return fliped_data

#
# from collections import defaultdict
#
# def best_sender(messages, senders):
#     d = defaultdict(list)
#     d_2 = defaultdict(int)
#     for s, m in zip(senders, messages):
#         d[s].extend(m.split())
#     for k, v in d.items():
#         d_2[k] = len(v)
#
#     return max(sorted(d_2, reverse=True), key=d_2.get)
#
#
# # TEST_3:
# messages = ['Hello userTwooo', 'Hi userThree', 'Wonderful day Alice', 'Nice day userThree']
# senders = ['Alice', 'userTwo', 'userThree', 'Alice']
#




# from collections import defaultdict
#
# def best_sender(messages, senders):
#     result = defaultdict(int)
#     for sender, message in zip(senders, messages):
#         result[sender] += len(message.split())
#     return max(result, key=lambda p: (result[p], p))


# from collections import defaultdict
#
#
# def best_sender(messages, senders):
#     result_dict = defaultdict(int)
#     for i in range(len(senders)):
#         result_dict[senders[i]] += len(messages[i].split())
#     return max(result_dict.items(), key=lambda x: (x[1], x[0]))[0]

# from collections import OrderedDict
#
# a = OrderedDict()
# b = OrderedDict(name='Timur', surname='Guev', hobby='math')
# c = OrderedDict({'name': 'Timur', 'surname': 'Guev', 'hobby': 'math'})
# d = OrderedDict((['name', 'Timur'], ['surname', 'Guev'], ['hobby', 'math']))
# e = OrderedDict(int, ['name': 'Timur', 'surname': 'Guev', 'hobby': 'math'])
# f = OrderedDict.fromkeys(('name', 'surname', 'hobby'), 'Empty')
#
#
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# # print(type(e))
# print(type(f))



# from collections import OrderedDict
#
# data = OrderedDict(key1='value1')
#
# data['key2'] = 'value2'
# data['key3'] = 'value3'
#
# for key, value in data.items():
#     print(f'{key} -> {value}')

# from collections import OrderedDict
#
# cloth = OrderedDict({'name': 'pants', 'size': 'm', 'color': 'grey'})
#
# cloth['name'] = 'shirt'
# cloth.update(size='s')
#
# for key, value in cloth.items():
#     print(f'{key}: {value}')

#
# country1 = dict(name='Finland', capital='Helsinki', currency='euro')
# country2 = dict(capital='Helsinki', name='Finland', currency='euro')
#
# print(country1 == country2)

# from collections import OrderedDict
#
# country1 = OrderedDict(name='Finland', capital='Helsinki', currency='euro')
# country2 = OrderedDict(name='Finland', capital='Helsinki', currency='euro')
#
# country2.move_to_end('name')
#
# print(country1 == country2)


# from collections import OrderedDict
#
# country1 = dict(name='Finland', capital='Helsinki', currency='euro')
# country2 = OrderedDict(currency='euro', capital='Helsinki', name='Finland')
#
# print(country1 == country2)


# from collections import OrderedDict
#
# planets1 = OrderedDict(Mercury=None, Venues=2, Earth=None, Mars=4, Jupiter=5)
# planets2 = OrderedDict(Mercury=1, Saturn=6, Uranus=7, Neptune=8, Earth=3)
#
# solar_system = planets1 | planets2
#
# print(*solar_system)

# from collections import OrderedDict
#
# flower = OrderedDict([('name', 'Rose'), ('family', 'Rosaceae'), ('kingdom', 'Plantae')])
#
# flower.move_to_end('family')
#
# for key, value in flower.items():
#     print(f'{key}: {value}')


# from collections import OrderedDict
#
# flower = OrderedDict([('name', 'Viola'), ('family', 'Violaceae'), ('kingdom', 'Plantae')])
#
# flower.move_to_end('kingdom', last=False)
#
# for key, value in flower.items():
#     print(f'{key}: {value}')


# from collections import OrderedDict
#
# grades = OrderedDict(Timur=100, Arthur=84, Anri=94, Dima=98)
# new_grades = OrderedDict()
#
# for rule in (True, False, False, True):
#     name, grade = grades.popitem(last=rule)
#     new_grades[name] = grade
#
# print(*new_grades)


# from collections import OrderedDict
#
# vector = OrderedDict(x=3, y=4, module=5)
#
# print(*reversed(vector))

# from collections import OrderedDict
#
# data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
# print(OrderedDict(reversed(data.items())))


# from collections import OrderedDict
#
# from collections import OrderedDict
# data = OrderedDict(key1='value1', key2='value2', key3='value3', key4='value4')
# # data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
# new_data = OrderedDict()
#
# for rule in [False if i % 2 == 0 else True for i in range(len(data))]:
#     name, grade = data.popitem(last=rule)
#     new_data[name] = grade
#
# print(new_data)

# from collections import OrderedDict
#
# def custom_sort(ordered_dict, by_values=False):
#     if by_values:
#         for key in sorted(ordered_dict,key=lambda x: ordered_dict[x]):
#             ordered_dict.move_to_end(key)
#     else:
#         for key in sorted(ordered_dict):
#             ordered_dict.move_to_end(key)
#
#
# data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
# custom_sort(data, by_values=True)
#
# print(*data.items())
#
# # ('Mercury', 1) ('Venus', 2) ('Earth', 3) ('Mars', 4)

# from collections import Counter
#
# print(Counter('Sandy Cheeks'))
# print(Counter('Sandy Cheeks'.split()))
# print(Counter(Sandy=1.5, Cheeks=-3))
# print(Counter())
# print(Counter({'S': 1, 'a': 5, 'n': 3, 'd': 9, 'y': 7}))
# print(Counter(Sandy='2', Cheeks='4'))
# print(Counter({'S': '1', 'a': '5', 'n': '3', 'd': '9', 'y': '7'}))
# print(Counter.fromkeys('Sandy', 1))

# from collections import Counter
#
# browsers = Counter(['Firefox', 'Chrome', 'Edge', 'Edge' 'Chrome', 'Firefox', 'Opera', 'Yandex', 'Chrome'])
#
# print(browsers['Firefox'])

# from collections import Counter

# counter = Counter.fromkeys('abcd', 1)

# print(*counter.keys(), sum(counter.values()))


# from collections import Counter

# counter = Counter({1: 11, 2: 22, 3: 33})

# print(max(counter.keys()) + min(counter.values()))

# from collections import Counter

# pets = Counter(cat=3, dog=3, fox=2, hamster=1)

# print(pets['elephant'])
# print(*pets)





# from collections import Counter
#
#
# letters = Counter(set('Beautiful is better than ugly'))
#
# print(letters['t'])

# from collections import Counter
#
# clothes = Counter([('shirt', 3), ('dress', 1), ('shirt', 3)])
#
# print(clothes['shirt'])
#
# print(clothes)

# from collections import Counter
#
# letters1 = Counter('abcd')
# letters2 = Counter('abcd')
#
# letters2.update(e=0)
#
# print(letters1 == letters2)