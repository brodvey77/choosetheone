#
# class BankAccount:
#     def __init__(self, balance=0):
#         self._balance = balance
#
#
#     def get_balance(self):
#         return self._balance
#
#     def deposit(self, amount):
#         self._balance += amount
#
#     def withdraw(self, amount):
#         if amount <= self._balance:
#             self._balance -= amount
#         else:
#             raise ValueError('На счете недостаточно средств')
#
#     def transfer(self, account, amount):
#         if amount > self._balance:
#             raise ValueError('На счете недостаточно средств')
#         else:
#             account._balance += amount
#             self._balance -= amount
#
#
#
# account1 = BankAccount(100)
# account2 = BankAccount(200)
#
# print(account1.get_balance())
# print(account2.get_balance())
#
# account1.transfer(account2, 50)
#
# print(account1.get_balance())
# print(account2.get_balance())
#
# account1.transfer(account2, 50)
#
# print(account1.get_balance())
# print(account2.get_balance())
#
# account2.transfer(account1, 50)
#
# print(account1.get_balance())
# print(account2.get_balance())