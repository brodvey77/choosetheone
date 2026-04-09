from random import randint


class Dice:
    def __init__(self, sides: int):
        self.sides = sides

    def __call__(self):
        return randint(1, self.sides)


kingdice = Dice(20)
print(callable(kingdice))