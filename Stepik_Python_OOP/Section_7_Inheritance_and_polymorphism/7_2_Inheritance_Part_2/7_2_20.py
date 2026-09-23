from functools import reduce

class Summator:
    def total(self, n):
        return reduce(lambda x,y: x+y, range(1, n+1))

class SquareSummator(Summator):
    def total(self, n):
        return n * (n + 1) * (2 * n + 1) // 6

class QubeSummator(Summator):
    def total(self, n):
        return int((n * (n + 1) / 2) ** 2)

class CustomSummator(Summator):
    def __init__(self, m):
        self.m = m
    def total(self, n):
        return sum(i**self.m for i in range(1, n+1))




for i in range(5, 50):
    summator = CustomSummator(i)
    print(summator.total(10))





class Summator:
    def transform(self, n):
        return n

    def total(self, n):
        return sum(self.transform(i) for i in range(1, n + 1))


class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2


class QubeSummator(Summator):
    def transform(self, n):
        return n ** 3


class CustomSummator(Summator):
    def __init__(self, power):
        self.power = power

    def transform(self, n):
        return n ** self.power


class Summator:
    def __init__(self, m=1):
        self.m = m

    def total(self, n):
        return sum(map(lambda x: x ** self.m, range(1, n + 1)))


class SquareSummator(Summator):
    def __init__(self):
        super().__init__(2)


class QubeSummator(Summator):
    def __init__(self):
        super().__init__(3)


class CustomSummator(Summator):
    def __init__(self, m):
        super().__init__(m)
