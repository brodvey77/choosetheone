# class BlogPost:
#     def __init__(self,user_name, text, number_of_likes):
#         self.user_name = user_name
#         self.text = text
#         self.number_of_likes = number_of_likes
#
#     def change_number_of_likes(self, number_of_dislakes):
#         self.number_of_likes = number_of_dislakes
#
# post_about_history = BlogPost('Pistrushka', 'world war', 125)
# post_about_humor = BlogPost('Brodvey77', 'cumedy club', 259)
#
# print(post_about_history.number_of_likes)
# print(post_about_humor.number_of_likes)
# post_about_history.change_number_of_likes(1520)
# print(post_about_history.number_of_likes)
# post_about_humor.number_of_likes = 2000
# print(post_about_humor.number_of_likes)


# class BankAccount:
#
#     def __init__(self, client_id, client_first_name, client_last_name):
#         self.client_id = client_id
#         self.client_first_name = client_first_name
#         self.client_last_name = client_last_name
#         self.balance = 0.0
#
#     def add(self, amount):
#         self.balance += amount
#         print(self.client_first_name + ' Баланс равен = ' +  str(self.balance))
#
#     def withdraw(self, amount):
#         self.balance -= amount
#         print(self.client_first_name + ' Баланс равен = ' +  str(self.balance))
#
# sergey = BankAccount(406193,'Sergey', 'Romanov')
# victor = BankAccount(406194,'Victor', 'Selevanov')
#
# print((sergey.balance))
# print((victor.balance))
#
# sergey.add(10000)
# victor.add(10000)
# print((sergey.balance))
# print((victor.balance))
#
# sergey.withdraw(5000)
# victor.withdraw(6000)
# print((sergey.balance))
# print((victor.balance))

# class GameCharacter:
#
#     def __init__(self, name, health, level):
#         self.name = name
#         self.health = health
#         self.level = level
#
#     def speak(self):
#         print('Hi, my name is ' + self.name)
#
#
# class Villain(GameCharacter):
#     def __init__(self, name, health, level):
#         self.name = name
#         self.health = health
#         self.level = level
#
#     def speak(self):
#         print('Hi, my name is ' + self.name + 'and I will kill you')
#
#     def kill(self, other):
#         other.health = 0
#         print('Bang-bang, now you\'re dead')
#
# james = GameCharacter('James', 100, 1)
# jim = Villain('Jim', 100, 2)
#
# print(james.health)
# print(jim.health)
#
# james.speak()
# jim.speak()
# jim.kill(james)


# print(james.health)
# print(jim.health)

