from functools import total_ordering

@total_ordering
class Word:
    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return f"Word('{self.word}')"

    def __str__(self):
        return f"{self.word.capitalize()}"

    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        return NotImplemented





print(Word('bee') == Word('hey'))
print(Word('bee') < Word('geek'))
print(Word('bee') > Word('geek'))
print(Word('bee') <= Word('geek'))
print(Word('bee') >= Word('gee'))

print('=' * 25)

words = [Word('python'), Word('bee'), Word('geek')]

print(sorted(words))
print(min(words))
print(max(words))

print('=' * 25)

word = Word('Beegeek')
not_supported = [range(10), iter([1, 2, 3]), True, False, 85.34, {'Erich Gamma', 'Richard Helm', 'Ralph Johnson', 'John Matthew Vlissides'}]

for obj in not_supported:
    print(word == obj)

print('=' * 25)

word = Word('Beegeek')

print(word.__eq__(1))
print(word.__ne__(1.1))
print(word.__gt__(range(5)))
print(word.__lt__([1, 2, 3]))
print(word.__ge__({4, 5, 6}))
print(word.__le__({1: 'one'}))

from functools import total_ordering
import re


@total_ordering
class Word:
    def __init__(self, word):
        if Word.is_correct(word):
            self.word = word

    @staticmethod
    def is_correct(word):
        if re.fullmatch(r"[A-Za-z]+", word):
            return True
        return False

    def __str__(self):
        return f"{str(self.word).capitalize()}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.word}')"

    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        return NotImplemented