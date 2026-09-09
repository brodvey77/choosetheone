from keyword import kwlist

class NonKeyword:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self.name in obj.__dict__:
            return obj.__dict__[self.name]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if value not in kwlist:
            obj.__dict__[self.name] = value
        else:
            raise ValueError('Некорректное значение')




class NonKeywordData:
    obj = NonKeyword('obj')


data = [1, 2.3, [4, 5, 6], (7, 8, 9), {10: 11, 12: 13, 14: 15}, True, False, 'Mantrida']
nonkeyworddata = NonKeywordData()

for item in data:
    nonkeyworddata.obj = item
    print(nonkeyworddata.obj)