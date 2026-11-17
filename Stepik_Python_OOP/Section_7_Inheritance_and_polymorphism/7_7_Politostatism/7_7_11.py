from abc import ABC, abstractmethod


class Stat(ABC):
    def __init__(self, iterable=None):
        self.iterable = list(iterable) if iterable is not None else []

    def add(self, number):
        self.iterable.append(number)


    @abstractmethod
    def result(self):
        pass


    def clear(self):
        self.iterable.clear()

class MinStat(Stat):


    def result(self):
        if self.iterable:
            return min(self.iterable)
        else:
            return None


class MaxStat(Stat):

    def result(self):
        if self.iterable:
            return max(self.iterable)
        else:
            return None


class AverageStat(Stat):

    def result(self):
        if self.iterable:
            return sum(self.iterable) / len(self.iterable)
        else:
            return None




minstat = MinStat([1, 2, 4])
maxstat = MaxStat([1, 2, 4])
averagestat = AverageStat([1, 2, 4])

minstat.add(5)
maxstat.add(5)
averagestat.add(5)

print(minstat.result())
print(maxstat.result())
print(averagestat.result())



import statistics
from abc import ABC, abstractmethod


class Stat(ABC):
    def __init__(self, iterable=()):
        self.data = list(iterable)

    def add(self, n):
        self.data.append(n)

    def clear(self):
        self.data.clear()

    @abstractmethod
    def result(self):
        pass


class MinStat(Stat):
    def result(self):
        return min(self.data, default=None)


class MaxStat(Stat):
    def result(self):
        return max(self.data, default=None)


class AverageStat(Stat):
    def result(self):
        return statistics.fmean(self.data) if self.data else None

