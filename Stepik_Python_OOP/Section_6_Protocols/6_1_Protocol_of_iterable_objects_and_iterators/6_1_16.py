
class DevelopmentTeam:
    def __init__(self):
        self.juniors = []
        self.seniors = []

    def add_junior(self, *args):
        for i in args:
            self.juniors.append((i, 'junior'))

    def add_senior(self, *args):
        for i in args:
            self.seniors.append((i, 'senior'))

    def __iter__(self):
        yield from self.juniors
        yield from self.seniors






beegeek = DevelopmentTeam()
python = DevelopmentTeam()

beegeek.add_junior('Timur')
beegeek.add_senior('Rustam')

python.add_junior('Tim')
python.add_senior('Gvido')



print(*beegeek, sep='\n')
print(*python, sep='\n')


class DevelopmentTeam:
    def __init__(self):
        self._seniors = []
        self._juniors = []

    def add_junior(self, *juniors):
        self._juniors.extend(juniors)

    def add_senior(self, *seniors):
        self._seniors.extend(seniors)

    def __iter__(self):
        for junior in self._juniors:
            yield (junior, 'junior')
        for senior in self._seniors:
            yield (senior, 'senior')



import itertools as it


class DevelopmentTeam:
    def __init__(self):
        self.__juniors = []
        self.__seniors = []

    def add_junior(self, *names):
        self.__juniors.extend((name, 'junior') for name in names)

    def add_senior(self, *names):
        self.__seniors.extend((name, 'senior') for name in names)

    def __iter__(self):
        yield from it.chain(self.__juniors, self.__seniors)