# class PiggyBank:
#     def __init__(self, balance = 0, volume = 500) -> None:
#         self.balance = balance
#         self.volume = volume
from itertools import cycle

from numpy.ma.core import argsort

#     def add_coins(self,coins):
#         if self.balance + coins > self.volume:
#             raise ValueError('Копилка слишком мала')
#         else:
#             self.balance += coins

#     def remove_coins(self, coins):
#         if self.balance - coins < 0:
#             raise ValueError('В копилке недостаточно монет')
#         else:
#             self.balance -= coins



# piggybank = PiggyBank(0, 10)

# print(piggybank.balance)

# piggybank.remove_coins(20)                            # пробуем из пустой копилки вынуть 20 монет
# piggybank.add_coins(20)                               # пробуем добавить избыточное количество монет

# print(piggybank.balance)




# class Gun():
#     def __init__(self) -> None:
#         pass

#     def shoot(self):
#         print('pif')


# gun = Gun()

# gun.shoot()
# gun.shoot()
# gun.shoot()

# class User:
#     def __init__(self, name, friends = 0):
#         self.name = name
#         self.friends = friends

#     def add_friends(self, n):
#         self.friends += n


# user = User('Arthur')

# print(user.friends)


# class House:
#     def __init__(self, color, rooms) -> None:
#         self.color = color
#         self.rooms = rooms

#     def paint(self, new_color):
#         self.color = new_color

#     def add_rooms(self, n):
#         self.rooms += n



# house = House('white', 4)

# house.paint('black')
# house.add_rooms(1)

# print(house.color)
# # print(house.rooms)
#
# class Bee:
#     def __init__(self, x=0, y=0) -> None:
#         self.x = x
#         self.y = y
#
#     def move_up(self, n):
#         self.y += n
#
#     def move_down(self, n):
#         self.y -= n
#
#     def move_right(self, n):
#         self.x += n
#
#     def move_left(self, n):
#         self.x -= n
#
#
#
# bee = Bee()
#
# bee.move_right(2)
# bee.move_right(2)
# bee.move_up(3)
# bee.move_left(1)
# bee.move_down(1)
#
# print(bee.x, bee.y)


# from itertools import cycle
#
# class Gun():
#     def __init__(self):
#         self.sounds = cycle(['pif', 'paf'])
#
#     def shoot(self):
#         print(next(self.sounds))
#
#
# gun = Gun()
#
# gun.shoot()
# gun.shoot()
# gun.shoot()
# gun.shoot()

#
# class Gun():
#     def __init__(self):
#         self.sounds = cycle(('pif', 'paf'))
#         self.counter = 0
#
#     def shoot(self):
#         print(next(self.sounds))
#         self.counter += 1
#
#     def shots_count(self):
#         return self.counter
#
#
#     def shots_reset(self):
#         self.counter = 0
#         self.sounds = cycle(('pif', 'paf'))
#
#
#
#
# gun = Gun()
#
# gun.shoot()
# print(gun.shots_count())
# gun.shots_reset()
# print(gun.shots_count())
# gun.shoot()
# gun.shoot()


# TEST_7:
# pif
# 1
# 0
# pif
# paf

# class Scales():
#     def __init__(self):
#         self.weight = 0
#
#     def add_right(self, weight):
#         self.weight += weight
#
#     def add_left(self, weight):
#         self.weight -= weight
#
#     def get_result(self):
#         if self.weight > 0:
#             return 'Правая чаша тяжелее'
#         if self.weight < 0:
#             return 'Левая чаша тяжелее'
#         else:
#             return 'Весы в равновесии'
#
#
# scales = Scales()
#
# scales.add_right(2)
# scales.add_left(1)
#
# print(scales.get_result())

# import math
#
# class Vector:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def abs(self):
#         return math.sqrt(self.x **2  + self.y ** 2)
#
#
#
# vector = Vector(3, 4)
#
# print(vector.x, vector.y)
# print(vector.abs())


# class Numbers:
#     def __init__(self):
#         self.l = []
#
#     def add_number(self, num):
#         self.l.append(num)
#
#     def get_even(self):
#         return list(filter(lambda x: x % 2 == 0, self.l))
#
#     def get_odd(self):
#         return list(filter(lambda x: x % 2 != 0, self.l))
#
#
#
# numbers = Numbers()
#
# print(numbers.get_even())
# print(numbers.get_odd())

# class TextHandler:
#     def __init__(self):
#         self.l = []
#
#
#     def add_words(self, text):
#         for i in text.split():
#             self.l.append(i)
#
#     def get_shortest_words(self):
#         return list(filter(lambda x: len(x) == len(min(self.l, key=len)), self.l))
#
#     def get_longest_words(self):
#         return list(filter(lambda x: len(x) == len(max(self.l, key=len)), self.l))



#
# texthandler = TextHandler()
#
# texthandler.add_words('The world will hold my trial for your sins')
# texthandler.add_words('Never meant to see the sky never meant to live')
#
# print(texthandler.get_shortest_words())
# print(texthandler.get_longest_words())


# class Todo:
#     def __init__(self):
#         self.things = []
#         self.maximum = []
#         self.minimum = []
#
#     def add(self, name, rang):
#         self.things.append((name, rang))
#
#     def get_by_priority(self, n: int):
#         return list(map(lambda x: x[0], filter(lambda x: x[1] == n, self.things)))
#
#     def get_low_priority(self):
#         for i in self.things:
#             if i[1] == min(list(map(lambda x: x[1], self.things))):
#                 self.minimum.append(i[0])
#         return self.minimum
#
#     def get_high_priority(self):
#         for i in self.things:
#             if i[1] == max(list(map(lambda x: x[1], self.things))):
#                 self.maximum.append(i[0])
#         return self.maximum
#
#
#
#
# todo = Todo()
#
# print(todo.things)
# print(todo.get_by_priority(1))
# print(todo.get_low_priority())
# print(todo.get_high_priority())


class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street, house, flat):
        self.delivery_data.append((street, house, flat))

    def get_houses_for_street(self, street):
        return list(dict.fromkeys(map(lambda x: x[1], list(filter(lambda x: x[0] == street, self.delivery_data)))))

    def get_flats_for_house(self, street, house):
        return list(dict.fromkeys(map(lambda x: x[2], list(filter(lambda x: x[0] == street and x[1] == house, self.delivery_data)))))



postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)


print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))
