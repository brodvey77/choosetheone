
class NonNegativeInteger:
    def __init__(self, name, default=None):
        self._name = name
        self.default = default

    def __get__(self, obj, cls):
        if obj is None:
            return self

        if self._name in obj.__dict__:
            return obj.__dict__[self._name]

        if self.default is not None:
            return self.default

        raise AttributeError("Атрибут не найден")


    def __set__(self, obj, value):
        if isinstance(value, int) and value >= 0:
            obj.__dict__[self._name] = value
        else:
            raise ValueError('Некорректное значение')



class Student:
    score = NonNegativeInteger('score')

student = Student()

try:
    print(student.score)
except AttributeError as e:
    print(e)




class NonNegativeInteger:
    def __init__(self, name, default=None):
        self._attr = name
        self._default = default

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr not in obj.__dict__ and self._default is None:
            raise AttributeError('Атрибут не найден')
        return obj.__dict__.get(self._attr, self._default)

    def __set__(self, obj, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError('Некорректное значение')
        obj.__dict__[self._attr] = value