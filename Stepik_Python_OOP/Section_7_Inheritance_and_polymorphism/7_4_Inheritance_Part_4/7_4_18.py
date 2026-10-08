
from collections import UserDict

class TwoWayDict(UserDict):
    def __setitem__(self, key, value):
        self.data[key] = value
        self.data[value] = key



from string import ascii_uppercase, ascii_lowercase

d = TwoWayDict()

for i in range(26):
    d[ascii_uppercase[i]] = ascii_lowercase[i]

print(d)



from collections import UserDict


class TwoWayDict(UserDict):
    def __setitem__(self, key, value):
        self.data |= {key: value, value: key}



from collections import UserDict

class TwoWayDict(UserDict):
    def __setitem__(self, k, v):
        super().__setitem__(k, v)
        super().__setitem__(v, k)



from collections import UserDict

class TwoWayDict(UserDict):
    def __setitem__(self, key, value):
        self.data.__setitem__(key, value)
        self.data.__setitem__(value, key)

