# class MyClass:
#     def __new__(cls, *args, **kwargs):
#         instance = object.__new__(cls)
#         return instance
#
#
# obj = MyClass()
#
# print(obj)
# print(type(obj))

class Cat:
    def __new__(cls, *args, **kwargs):
        print('1. Создание экземпляра класса Cat')
        instance = object.__new__(cls)
        return instance

    def __init__(self, name):
        print('2. Инициализация созданного экземпляра класса Cat')
        self.name = name


cat = Cat('Кемаль')

print(type(cat))
print(cat.name)