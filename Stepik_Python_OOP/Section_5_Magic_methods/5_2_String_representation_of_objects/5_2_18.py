
class AnyClass:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


    def __repr__(self):
        attrs = []
        for k,v in self.__dict__.items():
            if isinstance(v, str):
                attrs.append(f"{k}='{v}'")
            else:
                attrs.append(f"{k}={v}")
        return f"AnyClass({', '.join(attrs)})"


    def __str__(self):
        attrs = []
        for k, v in self.__dict__.items():
            if isinstance(v, str):
                attrs.append(f"{k}='{v}'")
            else:
                attrs.append(f"{k}={v}")
        return f"AnyClass: {', '.join(attrs)}"









any = AnyClass()

print(str(any))
print(repr(any))

print('=' * 30)

cowboy = AnyClass(name='John', surname='Marston')

print(str(cowboy))
print(repr(cowboy))
print('=' * 30)

obj = AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)

print(str(obj))
print(repr(obj))