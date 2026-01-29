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
