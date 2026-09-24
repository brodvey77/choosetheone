
class FieldTracker:
    def __init__(self):
        self._changed = {}

    def __setattr__(self, name, value):
        if name in getattr(self, 'fields', ()):
            if name in self.__dict__:
                current = self.__dict__[name]

                if current != value and name not in self._changed:
                    self._changed[name] = current

        object.__setattr__(self, name, value)

    def base(self, name):
        if name in self._changed:
            return self._changed[name]

        return getattr(self, name)

    def has_changed(self, name):
        return name in self._changed

    def changed(self):
        return self._changed.copy()

    def save(self):
        self._changed = {}







class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()

point = Point(1, 2, 3)

print(point.base('x'))
print(point.has_changed('x'))
print(point.changed())


class FieldTracker:
    fields = tuple()

    def __init__(self):
        self.dic = {k: self.__dict__[k] for k in self.fields}

    def base(self, name):
        return self.dic[name]

    def has_changed(self, name):
        return self.dic[name] != self.__dict__[name]

    def changed(self):
        return {k: self.dic[k] for k in self.fields if self.has_changed(k)}

    def save(self):
        self.dic = {k: self.__dict__[k] for k in self.fields}


