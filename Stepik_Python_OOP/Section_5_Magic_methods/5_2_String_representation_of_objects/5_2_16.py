
class IPAddress:
    def __init__(self, ipaddress):
        if isinstance(ipaddress, str):
            self.ipaddress = ipaddress
        if isinstance(ipaddress, list|tuple):
            self.ipaddress = '.'.join(map(str, ipaddress))

    def __str__(self):
        return f"{self.ipaddress}"

    def __repr__(self):
        return f"IPAddress('{self.ipaddress}')"



ip = IPAddress('8.8.1.1')

print(str(ip))
print(repr(ip))

print('=' * 20)

ip = IPAddress((1, 1, 11, 11))

print(str(ip))
print(repr(ip))



from functools import singledispatchmethod


class IPAddress:
    @singledispatchmethod
    def __init__(self, ipaddress):
        self.ipaddress = ipaddress

    @__init__.register(list)
    @__init__.register(tuple)
    def _(self, ipaddress):
        self.ipaddress = '.'.join(map(str, ipaddress))

    def __str__(self):
        return self.ipaddress

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.ipaddress}')"




from functools import singledispatchmethod


class IPAddress:
    @singledispatchmethod
    def __init__(self, ipaddress):
        self.ipaddress = ipaddress

    @__init__.register(list | tuple)
    def _tuple__init__(self, ipaddress):
        self.ipaddress = '.'.join(map(str, ipaddress))

    def __str__(self):
        return self.ipaddress

    def __repr__(self):
        return f"IPAddress('{self.ipaddress}')"