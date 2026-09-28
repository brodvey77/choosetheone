

class UpperPrintString(str):
    def __new__(cls, value):
        instance = super().__new__(cls, value)
        return instance


    def __str__(self) -> str:
        return f'{super().__str__().upper()}'


s = UpperPrintString('beegeek')
print(s)
print(list(s))