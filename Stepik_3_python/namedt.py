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


import csv
from collections import namedtuple

l = []
with open('meetings.csv', encoding='utf-8') as file:
    rows = csv.reader(file, delimiter=',')
    for i in rows:
        headers = i
        break

    Friend = namedtuple('Friend', headers)

    for f in rows:
        friend = Friend._make(f)
        l.append(friend)

    for _ in l:
        print(_)


