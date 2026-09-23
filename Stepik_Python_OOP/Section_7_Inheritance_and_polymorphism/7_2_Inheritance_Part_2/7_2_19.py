
class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        self.value = max(self.value - n, 0)


class DoubledCounter(Counter):
    def __init(self, start=0):
        super().__init__(start)
        self.value = start

    def inc(self, n=1):
        self.value += n
        self.value += n

    def dec(self, n=1):
        self.value = max(self.value - n, 0)
        self.value = max(self.value - n, 0)



digits = [122, 48, 122, 180, 176, 148, 104, 70, 168, 128, 129, 120, 63, 172, 101, 132, 195, 139, 164, 163, 196, 132,
          110, 42, 183, 49, 50, 193, 198, 187, 172, 52, 113, 164, 196, 48, 114, 186, 78, 105, 82, 142, 97, 194, 74, 115,
          107, 160, 119, 82]

counter = DoubledCounter(10)

pos = True

for digit in digits:
    if pos:
        counter.inc(digit)
    else:
        counter.dec(digit)
    pos = not pos

print(counter.value)



class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        self.value = max(self.value - n, 0)


class DoubledCounter(Counter):
    def inc(self, n=1):
        super().inc(n * 2)

    def dec(self, n=1):
        super().dec(n * 2)


class Counter:
    def __init__(self, start=0, repeat=1):
        self.value = start
        self.repeat = repeat

    def inc(self, n=1):
        self.value += n * self.repeat

    def dec(self, n=1):
        self.value = max(self.value - (n * self.repeat), 0)


class DoubledCounter(Counter):
    def __init__(self, start=0, repeat=2):
        super().__init__(start, repeat)