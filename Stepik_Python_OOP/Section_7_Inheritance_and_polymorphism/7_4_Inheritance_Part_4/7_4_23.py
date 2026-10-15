from collections import UserString

class MutableString(UserString):

    def lower(self):
        self.data = self.data.lower()


    def upper(self):
        self.data = self.data.upper()


    def sort(self, key=None, reverse=False):
        self.data = ''.join(sorted(self.data, key=key, reverse=reverse))

    def __setitem__(self, index, value):
        data = list(self.data)
        data[index] = value
        self.data = ''.join(data)

    def __delitem__(self, index):
        data = list(self.data)
        del data[index]
        self.data = ''.join(data)



# mutablestring = MutableString('Beegeek')
# mutablestring.lower()
# print(mutablestring)
# mutablestring.upper()
# print(mutablestring)
# mutablestring.sort()
# print(mutablestring)


mutablestring = MutableString('beegeek')
print(mutablestring)
mutablestring[0] = 'B'
mutablestring[-4] = 'G'
print(mutablestring)