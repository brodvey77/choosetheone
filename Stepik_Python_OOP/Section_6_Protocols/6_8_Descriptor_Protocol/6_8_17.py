class MaxCallsException(Exception):
    pass



class LimitedTakes:
    def __init__(self, times):
        self.times = times

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self.times < 1:
            raise MaxCallsException("Превышено количество доступных обращений")
        if self._attr in obj.__dict__:
            self.times -= 1
            return obj.__dict__[self._attr]
        else:
            raise AttributeError("Атрибут не найден")


    def __set__(self, obj, value):
        obj.__dict__[self._attr] = value



class Student:
    name = LimitedTakes(3)


student = Student()

for _ in range(100):
    student.name = 'Gwen'

print(student.name)



class MaxCallsException(Exception):
    pass


class LimitedTakes:
    def __init__(self, times):
        self._times = times

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._times:
            if self._attr in obj.__dict__:
                self._times -= 1
                return obj.__dict__[self._attr]
            raise AttributeError('Атрибут не найден')
        raise MaxCallsException('Превышено количество доступных обращений')

    def __set__(self, obj, value):
        obj.__dict__[self._attr] = value


class MaxCallsException(Exception):
    pass


class LimitedTakes:
    def __init__(self, times):
        self.times = times

    def __set_name__(self, cls, name):
        self.name = name

    def __set__(self, obj, value):
        obj.__dict__[self.name] = value

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self.name not in obj.__dict__:
            raise AttributeError("Атрибут не найден")
        if self.times:
            self.times -= 1
            return obj.__dict__[self.name]
        else:
            raise MaxCallsException('Превышено количество доступных обращений')