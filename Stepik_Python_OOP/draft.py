# class PiggyBank:
#     def __init__(self, balance = 0, volume = 500) -> None:
#         self.balance = balance
#         self.volume = volume

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