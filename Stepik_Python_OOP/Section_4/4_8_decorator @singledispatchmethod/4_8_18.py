from functools import singledispatchmethod

class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')


    @format.register
    @staticmethod
    def _from_int_or_float(data: int|float):
        if isinstance(data, int):
            print(f'Целое число: {data}')
        else:
            print(f'Вещественное число: {data}')

    @format.register
    @staticmethod
    def _from_tuple(data: tuple):
        print(f"Элементы кортежа: {', '.join(map(str, data))}")

    @format.register
    @staticmethod
    def _from_list(data: list):
        print(f"Элементы списка: {', '.join(map(str, data))}")

    @format.register
    @staticmethod
    def _from_dict(data: dict):
        print(f"Пары словаря: {','.join(str(item) for item in data.items())}")




# INPUT DATA:

# TEST_1:
Formatter.format(1337)
Formatter.format(20.77)

# TEST_2:
Formatter.format([10, 20, 30, 40, 50])
Formatter.format(([1, 3], [2, 4, 6]))

# TEST_3:
Formatter.format({'Cuphead': 1, 'Mugman': 3})
Formatter.format({1: 'one', 2: 'two'})
Formatter.format({1: True, 0: False})

# TEST_4:
try:
    Formatter.format('All them years, Dutch, for this snake?')
except TypeError as e:
    print(e)

# TEST_5:
not_supported = [str, type, bool, dict, tuple, list]

for item in not_supported:
    try:
        Formatter.format(item)
    except TypeError as e:
        print(e)
