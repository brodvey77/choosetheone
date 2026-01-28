class PiggyBank:
    def __init__(self, balance = 0) -> None:
        self.balance = balance

    def add_coins(self,coins):
        self.balance += coins

    def remove_coins(self, coins):
        self.balance -= coins
