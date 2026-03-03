
class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    @classmethod
    def from_iterable(cls, object):
        return cls(object[0], object[1], object[2])

    @classmethod
    def from_str(cls, s):
        l = [float(i) for i in s.split(' ')]
        print(l)
        return cls(l[0], l[1], l[2])



polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')

print(polynom.a)
print(polynom.b)
print(polynom.c)
print(polynom.a + polynom.b + polynom.c)


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    @classmethod
    def from_iterable(cls, iterable):
        return cls(*iterable)

    @classmethod
    def from_str(cls, string):
        iterable = (float(digit) for digit in string.split())
        return cls.from_iterable(iterable)