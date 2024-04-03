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

from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as file:
    data = pickle.load(file)

    for i in data:
        print(i)