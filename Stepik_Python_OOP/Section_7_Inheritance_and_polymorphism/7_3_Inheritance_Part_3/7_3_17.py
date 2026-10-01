
class SuperInt(int):
    """наследник класса int, описывающий целое число с дополнительным функционалом"""

    def repeat(self, n=2):
        return SuperInt((-1 if self < 0 else 1) * int(str(abs(self)) * n))

    def to_bin(self):
        return SuperInt(f'{self:b}')

    def next(self):
        return SuperInt(self + 1)

    def prev(self):
        return SuperInt(self - 1)

    def __iter__(self):
        return iter(SuperInt(d) for d in str(abs(self)))



# TEST_7:
superint = SuperInt(30)

for i in range(10):
    superint = superint.prev()
    print(superint)

# TEST_8:
superint = SuperInt(50)

for i in range(0, 50, 3):
    superint = superint.next()
    print(superint.to_bin())

# TEST_9:
superint = SuperInt(-200)

for i in range(0, 100, 3):
    superint = superint.next()
    print(superint.to_bin())

# TEST_10:
superint = SuperInt(50)

for i in range(0, 50, 3):
    superint = superint.next()
    print(*superint)

# TEST_11:
superint = SuperInt(-200)

for i in range(0, 100, 3):
    superint = superint.next()
    print(*superint)

# TEST_12:
superint = SuperInt(100)
print(type(superint))
print(type(superint.next()))
print(type(superint.prev()))
print(type(superint.repeat()))

# TEST_13:
superint1 = SuperInt(2023)

for item in superint1:
    print(item, type(item))




class SuperInt(int):
    def repeat(self, n=2):
        digit = f"{'-' * (self < 0)}{f'{abs(self)}' * n}"
        return type(self)(digit)

    def to_bin(self):
        return f'{self:b}'

    def next(self):
        return type(self)(self + 1)

    def prev(self):
        return type(self)(self - 1)

    def __iter__(self):
        yield from map(SuperInt, str(abs(self)))





