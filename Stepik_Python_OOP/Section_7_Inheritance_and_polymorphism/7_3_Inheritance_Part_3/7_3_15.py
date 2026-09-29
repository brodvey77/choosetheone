class FuzzyString(str):
    def __eq__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        return self.lower() == other.lower()

    def __ne__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        return self.lower() != other.lower()

    def __lt__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        return self.lower() < other.lower()

    def __le__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        return self.lower() <= other.lower()

    def __gt__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        return self.lower() > other.lower()

    def __ge__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        return self.lower() >= other.lower()

    def __contains__(self, item):
        if not isinstance(item, str):
            return NotImplemented
        return item.lower() in self.lower()


s1 = FuzzyString('BeeGeek')
s2 = FuzzyString('beegeek')

print(s1 == s2)
print(s1 in s2)
print(s2 in s1)
print(s2 not in s1)


class FuzzyString(str):
    def __new__(cls, obj):
        instance = super().__new__(cls, obj)
        for oper in map(lambda s: f'__{s}__', ('eq', 'ne', 'lt', 'le', 'gt', 'ge', 'contains')):
            setattr(cls, oper, cls._comparator(oper))
        return instance

    @staticmethod
    def _comparator(oper):
        def _compare(self, other):
            if not isinstance(other, (str, self.__class__)):
                return NotImplemented
            return getattr(self.lower(), oper)(other.lower())

        return _compare
