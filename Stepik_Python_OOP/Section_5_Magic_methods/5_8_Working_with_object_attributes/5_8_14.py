
class Const:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, attr, value):
        if attr in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        object.__setattr__(self, attr, value)

    def __delattr__(self, item):
        raise AttributeError('Удаление атрибута невозможно')





videogame = Const(name='The Last of Us')

try:
    del videogame.name
except AttributeError as e:
    print(e)


class Const:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise AttributeError('Изменение значения атрибута невозможно')
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        raise AttributeError('Удаление атрибута невозможно')