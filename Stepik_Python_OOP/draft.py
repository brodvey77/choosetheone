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
#
#     def paint(self, new_color):
#         self.color = new_color
#
#     def add_rooms(self, n):
#         self.rooms += n
#
#
#
# house = House('white', 4)
#
# house.paint('black')
# house.add_rooms(1)
#
# print(house.color)
# print(house.rooms)

# from math import pi
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#         self.area = pi*(radius**2)
#         self.diameter = radius*2
#
#
# circle = Circle(5)
#
# print(circle.radius)
# print(circle.diameter)
# print(circle.area)





