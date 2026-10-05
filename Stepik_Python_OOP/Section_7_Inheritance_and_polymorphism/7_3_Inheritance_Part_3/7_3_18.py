
class RoundedInt(int):
    def __new__(cls, num, even=True):
        if even:
            return super().__new__(cls, num + num%2)
        else:
            return super().__new__(cls, num + (1-num%2))






roundedint1 = RoundedInt(7)
roundedint2 = RoundedInt(7, False)

print(roundedint1 + roundedint2)
print(roundedint1 + 1)
print(roundedint2 + 1)

print(type(roundedint1))
print(type(roundedint2))


class RoundedInt(int):
    def __new__(cls, value, even=True, *args, **kwargs):
        value += (value % 2 == 1) if even else (value % 2 == 0)
        instance = super().__new__(cls, value)
        return instance


class RoundedInt(int):
    def __new__(cls, num, even=True):
        return super().__new__(cls, num + (num % 2 == even))