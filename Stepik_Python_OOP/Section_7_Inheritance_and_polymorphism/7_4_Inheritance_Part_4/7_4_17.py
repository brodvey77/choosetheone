
class EasyDict(dict):
    def __getattr__(self, item):
        return self[item]










easydict = EasyDict({'name': 'Artur', 'city': 'Almetevsk'})

easydict.age = 21
print(easydict)


class EasyDict(dict):
    __getattr__ = dict.__getitem__


class EasyDict(dict):
    def __getattr__(self, key):
        return super().__getitem__(key)






