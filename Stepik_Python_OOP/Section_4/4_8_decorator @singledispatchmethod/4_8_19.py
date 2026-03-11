import datetime
from datetime import date, timedelta
from functools import singledispatchmethod

def current_age(birth_date, current_date=None):
    if current_date is None:
        current_date = date.today()
    age = current_date.year - birth_date.year
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    @__init__.register(date)
    def _from_date(self, birth_date):
        self.birth_date = birth_date

    @__init__.register(str)
    def _from_str(self, birth_date):
        try:
            self.birth_date = date.fromisoformat(birth_date)
        except ValueError:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(list)
    def _from_list(self, birth_date):
        self._from_sequence(birth_date)

    @__init__.register(tuple)
    def _from_tuple(self, birth_date):
        self._from_sequence(birth_date)

    def _from_sequence(self, birth_date):
        # Проверка длины
        if len(birth_date) != 3:
            raise TypeError('Аргумент переданного типа не поддерживается')

        # Проверка, что все элементы - целые числа
        for x in birth_date:
            if not isinstance(x, int):
                raise TypeError('Аргумент переданного типа не поддерживается')

        try:
            self.birth_date = date(birth_date[0], birth_date[1], birth_date[2])
        except (ValueError, TypeError):
            raise TypeError('Аргумент переданного типа не поддерживается')




# TEST_8:
birth_dates = [
    [2020],
    (2020,),
    [2020, 1],
    [2020, 1, '1'],
    (2020, 1),
    (2020, 1, '1'),
    [2020, 1, 1, 1],
    (2020, 1, 1, 1),
    [2020, '1', '1'],
    [2020, '1', 1],
]

for birth_date in birth_dates:
    try:
        birthinfo = BirthInfo(birth_date)
    except TypeError as e:
        print(e)


print('test 9')
# TEST_9:
birth_dates = [
    ['2020', 1, 1],
    ['2020', '1', '1'],
    (2020, '1', '1'),
    ('2020', '1', '1'),
    (2020, '1', 1),
    ('2020', 1, 1),
    [2020, 1, 32],
    [2020, 13, 1],
    (2020, 1, 32),
    (2020, 13, 1)
]

for birth_date in birth_dates:
    try:
        birthinfo = BirthInfo(birth_date)
    except TypeError as e:
        print(e)
