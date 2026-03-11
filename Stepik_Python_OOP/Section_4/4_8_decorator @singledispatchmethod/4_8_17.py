from functools import singledispatchmethod

class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(bool)
    @staticmethod
    def _from_bool(data):
        if data:
            return False
        else:
            return True

    @neg.register(int|float)
    @staticmethod
    def _from_int_or_float(data):
        return -data



print(Negator.neg(11.0))
print(Negator.neg(-12))
print(Negator.neg(-0))
print(Negator.neg(True))
print(Negator.neg(False))

try:
    Negator.neg('number')
except TypeError as e:
    print(e)