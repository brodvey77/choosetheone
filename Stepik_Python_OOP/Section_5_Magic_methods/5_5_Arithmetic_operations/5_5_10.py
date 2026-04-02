#
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}({self.x}, {self.y})"
#
#     def __add__(self, other):
#         if isinstance(other, Vector):
#             return Vector(self.x + other.x, self.y + other.y)
#         return NotImplemented
#
#     def __sub__(self, other):
#         if isinstance(other, Vector):
#             return Vector(self.x - other.x, self.y - other.y)
#         return NotImplemented
#
#     def __mul__(self, other):
#         if isinstance(other, int|float):
#             return Vector(self.x * other, self.y * other)
#         return NotImplemented
#
#     def __rmul__(self, other):
#         if isinstance(other, int|float):
#             return self.__mul__(other)
#         return NotImplemented
#
#     def __truediv__(self, other):
#         if isinstance(other, int|float):
#             return Vector(self.x / other, self.y / other)
#         return NotImplemented

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int|float):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    __rmul__ = __mul__


    def __truediv__(self, other):
        if isinstance(other, int|float):
            return Vector(self.x / other, self.y / other)
        return NotImplemented

    __rtruediv__ = __truediv__





a = Vector(3, 4)

print(a * 2)
print(2 * a)
print(a / 2)