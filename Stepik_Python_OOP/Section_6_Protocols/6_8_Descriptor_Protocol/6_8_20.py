
# class Versioned:
#     def __set_name__(self, cls, attr):
#         self._attr = attr
#         self.d = []
#
#     def __get__(self, obj, cls):
#         if obj is None:
#             return self
#         if self._attr not in object.__dict__:
#             return obj.__dict__[self._attr]
#         else:
#             raise AttributeError("Атрибут не найден")
#
#     def __set__(self, obj, value):
#         self.d.append(value)
#         obj.__dict__[self._attr] = value
#
#     def get_version(self, obj, n:int):
#         return self.d[n-1]
#
#
#     def set_version(self, obj, n:int):
#         obj.__dict__[self._attr] = self.d[n-1]


class Versioned:
    def __set_name__(self, owner, name):
        self.name = name
        self.history_name = f'_{name}_history'
        self.current_name = f'_{name}_current'

    def __get__(self, instance, owner):
        if instance is None:
            return self

        if not hasattr(instance, self.history_name):
            raise AttributeError('Атрибут не найден')

        return getattr(instance, self.current_name)

    def __set__(self, instance, value):
        if not hasattr(instance, self.history_name):
            setattr(instance, self.history_name, [])

        history = getattr(instance, self.history_name)
        history.append(value)
        setattr(instance, self.current_name, value)

    def get_version(self, instance, n):
        return getattr(instance, self.history_name)[n - 1]

    def set_version(self, instance, n):
        value = getattr(instance, self.history_name)[n - 1]
        setattr(instance, self.current_name, value)



class Student:
    name = Versioned()

student = Student()

try:
    print(student.name)
except AttributeError as e:
    print(e)


class Versioned:
    def __init__(self):
        self._history = {}

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if obj not in self._history:
            raise AttributeError('Атрибут не найден')
        version = self._history[obj][0]
        values = self._history[obj][1]
        return values[version]

    def __set__(self, obj, value):
        values = self._history.setdefault(obj, [-1, []])[1]
        values.append(value)

    def get_version(self, obj, n):
        values = self._history[obj][1]
        return values[n - 1]

    def set_version(self, obj, n):
        self._history[obj][0] = n - 1