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
from collections import defaultdict

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



from collections import defaultdict

staff_broken = [('Developing', 'Miguel Norris'), ('Sales', 'Connie Reid'), ('Sales', 'Joseph Lee'),
                ('Marketing', 'Carol Peters'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Ann Bell'),
                ('Marketing', 'Ralph Morgan'), ('Accounting', 'Gloria Higgins'), ('Developing', 'Wilma Woods'),
                ('Developing', 'Wilma Woods'), ('Marketing', 'Bernice Ramos'), ('Marketing', 'Joyce Lawrence'),
                ('Accounting', 'Craig Wood'), ('Developing', 'Nicole Watts'), ('Sales', 'Jose Taylor'),
                ('Accounting', 'Linda Hudson'), ('Accounting', 'Edna Cunningham'), ('Sales', 'Jose Taylor'),
                ('Marketing', 'Helen Taylor'), ('Accounting', 'Kimberly Reynolds'), ('Marketing', 'Mary King'),
                ('Sales', 'Joseph Lee'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Andrew Clark'),
                ('Accounting', 'John Watts'), ('Accounting', 'Rosemary Garcia'), ('Accounting', 'Steven Diaz'),
                ('Marketing', 'Mary King'), ('Sales', 'Gladys Taylor'), ('Developing', 'Thomas Porter'),
                ('Accounting', 'Brenda Davis'), ('Sales', 'Connie Reid'), ('Sales', 'Alicia Mendoza'),
                ('Marketing', 'Mario Reynolds'), ('Sales', 'John White'), ('Developing', 'Joyce Rivera'),
                ('Accounting', 'Steven Diaz'), ('Developing', 'Arlene Gibson'), ('Sales', 'Robert Barnes'),
                ('Sales', 'Charlotte Cox'), ('Accounting', 'Craig Wood'), ('Marketing', 'Carol Peters'),
                ('Marketing', 'Ralph Morgan'), ('Accounting', 'Kay Scott'), ('Sales', 'Evelyn Martin'),
                ('Marketing', 'Billy Lloyd'), ('Sales', 'Gladys Taylor'), ('Developing', 'Deborah George'),
                ('Sales', 'Charlotte Cox'), ('Marketing', 'Sam Davis'), ('Sales', 'John White'),
                ('Sales', 'Marie Cooper'), ('Marketing', 'John Gonzalez'), ('Sales', 'John Washington'),
                ('Sales', 'Chester Fernandez'), ('Sales', 'Alicia Mendoza'), ('Sales', 'Katie Warner'),
                ('Accounting', 'Jane Jackson'), ('Sales', 'Chester Fernandez'), ('Marketing', 'Charles Bailey'),
                ('Marketing', 'Gail Hill'), ('Accounting', 'Casey Jenkins'), ('Accounting', 'James Wilkins'),
                ('Accounting', 'Casey Jenkins'), ('Marketing', 'Mario Reynolds'), ('Accounting', 'Aaron Ferguson'),
                ('Accounting', 'Kimberly Reynolds'), ('Sales', 'Robert Barnes'), ('Accounting', 'Aaron Ferguson'),
                ('Accounting', 'Jane Jackson'), ('Developing', 'Deborah George'), ('Accounting', 'Michelle Wright'),
                ('Accounting', 'Dale Houston')]

d = defaultdict(list)

for key, value in staff_broken:
    d[key].append(value)

for k, v in sorted(d.items()):
    n_v = ', '.join(sorted(set(v)))
    print(f'{k}: {n_v}')






