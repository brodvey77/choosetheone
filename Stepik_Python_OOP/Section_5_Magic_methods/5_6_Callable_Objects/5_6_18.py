
class SortKey:
    def __init__(self, *args):
        self.args = args

    def __call__(self, obj):
        # print('Экземпляр класса -->', obj)
        # print('Словарь с атрибутами -->', obj.__dict__)
        # print('Название/я атрибута --->>>', tuple(i for i in obj.__dict__))
        # print('Значение/я атрибута/ов переданных в key=SortKey(...,...))) СПОСОБ №1 --->>>', tuple(obj.__getattribute__(i) for i in self.args))
        # print("Значение/я атрибута/ов переданных в key=SortKey(...,...))) СПОСОБ №2  --->>>", tuple(obj.__dict__[i] for i in self.args))
        # print('=' * 40)
        return tuple(obj.__dict__[i] for i in self.args)


class SortKey:
    def __init__(self, *attributes):
        self.attributes = attributes

    def __call__(self, instance):
        return [getattr(instance, attribute) for attribute in self.attributes]


