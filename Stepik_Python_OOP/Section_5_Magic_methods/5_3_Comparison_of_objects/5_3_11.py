from functools import singledispatchmethod


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        if isinstance(other, tuple) and len(other) == 2:
            return self.x == other[0] and self.y == other[1]
        return NotImplemented



a = Vector(1, 2)
b = Vector(1, 2)

print(a == b)
print(a != b)

print('=' * 40)


a = Vector(1, 2)
pair1 = (1, 2)
pair2 = (3, 4)
pair3 = (5, 6, 7)
pair4 = (1, 2, 3, 4)
pair5 = (1, 4, 3, 2)

print(a == pair1)
print(a == pair2)
print(a == pair3)
print(a == pair4)
print(a == pair5)


from functools import singledispatchmethod

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    @singledispatchmethod
    def __eq__(self, other):
        return NotImplemented

    @__eq__.register(tuple)
    def _tuple__eq__(self, other):
        return (self.x, self.y) == other

@Vector.__eq__.register(Vector)
def _vector__eq__(self, other):
    return self.x == other.x and self.y == other.y