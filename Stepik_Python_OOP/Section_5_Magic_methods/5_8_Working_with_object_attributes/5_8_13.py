
class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


    def __getattr__(self, attr):
        if attr == 'attrs_num':
            return len(self.__dict__) + 1








music_group = AttrsNumberObject(name='Alexandra Savior', genre='dream pop')

print(music_group.attrs_num)
del music_group.genre
print(music_group.attrs_num)


class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.attrs_num = 1

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        self.__dict__["attrs_num"] = len(self.__dict__)

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __delattr__(self, name):
        object.__delattr__(self, name)
        self.__dict__["attrs_num"] = len(self.__dict__)
