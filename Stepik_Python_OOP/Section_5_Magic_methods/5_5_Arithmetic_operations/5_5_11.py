
class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return f"{self.string}"

    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return SuperString(self.string * other)
        return NotImplemented

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, int):
            return SuperString(self.string[:len(self.string)//other])
        return NotImplemented

    def __lshift__(self, other):
        if isinstance(other, int):
            if other == 0:
                return self.__class__(self.string)
            else:
                return self.__class__(self.string[:-other])

        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            if other == 0:
                return self.__class__(self.string)
            else:
                return self.__class__(self.string[other:])
        return NotImplemented



s = SuperString('beegeek')
for i in range(9):
    print(f'{s} << {i} =', s << i)

print('=' * 40)

superstring = SuperString('bee')
print(superstring.__add__([]))
print(superstring.__mul__(()))
print(superstring.__truediv__({}))
print(superstring.__lshift__(set()))
print(superstring.__rshift__('geek'))

print('+' * 40)

# TEST_8:
superstring = SuperString('bee')
print(superstring.__add__([]))
print(superstring.__mul__(()))
print(superstring.__truediv__({}))
print(superstring.__lshift__(set()))
print(superstring.__rshift__('geek'))