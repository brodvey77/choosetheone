
class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        self.__dict__.update(kwargs)

    def __getattr__(self, item):
        return self.default






god = DefaultObject(name='Ares', mythology='greek')

print(god.name)
print(god.mythology)
print(god.age)


class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.__setattr__(default, kwargs)

    def __setattr__(self, default, kwargs):
        self.__dict__['default'] = default
        self.__dict__.update(kwargs)

    def __getatribute__(self, name):
        return self.__getatribute__(self, name)

    def __getattr__(self, name):
        return self.default
