from collections import OrderedDict as od

class PermaDict:
    def __init__(self, data=()):
        self._data = od(data)

    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        yield from self._data

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, key, value):
        if key in self._data:
            raise KeyError('Изменение значения по ключу невозможно')
        self._data[key] = value

    def __contains__(self, item):
        return item in self._data

    def __delitem__(self, key):
        self._data.pop(key)





permadict = PermaDict()
print('Keys:', *permadict.keys())
print('Values:', *permadict.values())
print('Items:', *permadict.items())



class PermaDict:
    def __init__(self, data=()):
        self._data = dict(data) or {}

    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self.keys())

    def __delitem__(self, key):
        del self._data[key]

    def __setitem__(self, key, value):
        if key in self.keys():
            raise KeyError('Изменение значения по ключу невозможно')
        self._data[key] = value

    def __getitem__(self, key):
        return self._data[key]





class PermaDict(dict):

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError('Изменение значения по ключу невозможно')
        self |= {key: value}
