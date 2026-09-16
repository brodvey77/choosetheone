
class Validator:
    def __init__(self, obj):
        self.obj = obj

    def is_valid(self):
        return None

class NumberValidator(Validator):
    def __init__(self, obj):
        Validator.__init__(self, obj)

    def is_valid(self):
        if isinstance(self.obj, int | float):
            return True
        else:
            return False


validator1 = Validator('beegeek')
validator2 = Validator(1)
validator3 = Validator(1.1)

print(validator1.is_valid())
print(validator2.is_valid())
print(validator3.is_valid())


class Validator:
    def __init__(self, obj):
        self._obj = obj

    def is_valid(self):
        pass


class NumberValidator(Validator):
    def is_valid(self):
        return isinstance(self._obj, (int, float))