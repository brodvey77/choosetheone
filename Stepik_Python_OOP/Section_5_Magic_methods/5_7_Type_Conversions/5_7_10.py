from math import sqrt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __int__(self):
        return int(abs(sqrt(self.x**2 + self.y**2)))

    def __float__(self):
        return float(abs(sqrt(self.x**2 + self.y**2)))

    def __complex__(self):
        return complex(self.x, self.y)



print(bool(Vector(1, 2)))
print(bool(Vector(1, 0)))
print(bool(Vector(0, 1)))
print(bool(Vector(0, 0)))


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __float__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __int__(self):
        return int(float(self))

    def __complex__(self):
        return complex(self.x, self.y)

