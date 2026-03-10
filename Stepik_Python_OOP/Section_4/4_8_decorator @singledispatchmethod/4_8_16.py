
# class Processor:
#     @staticmethod
#     def process(data):
#         if isinstance(data, (int, float)):
#             return data * 2
#         elif isinstance(data, str):
#             return data.upper()
#         elif isinstance(data, list):
#             return sorted(data)
#         elif isinstance(data, tuple):
#             return tuple(sorted(data))
#         raise TypeError('Аргумент переданного типа не поддерживается')

from functools import singledispatchmethod

class Processor:
    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')


    @process.register(int|float)
    @staticmethod
    def _from_int_or_float(data):
        return data * 2

    @process.register(str)
    @staticmethod
    def _from_string(self):
        return self.upper()


    @process.register(list)
    @staticmethod
    def _from_list(data):
        return sorted(data)


    @process.register(tuple)
    @staticmethod
    def _from_tuple(data):
        return tuple(sorted(data))


    # def process(data):
    #     if isinstance(data, (int, float)):
    #         return data * 2
    #     elif isinstance(data, str):
    #         return data.upper()
    #     elif isinstance(data, list):
    #         return sorted(data)
    #     elif isinstance(data, tuple):
    #         return tuple(sorted(data))
    #     raise TypeError('Аргумент переданного типа не поддерживается')

print(Processor.process(10))
print(Processor.process(5.2))
print(Processor.process('hello'))
print(Processor.process((4, 3, 2, 1)))
print(Processor.process([3, 2, 1]))

try:
    Processor.process({1, 2, 3})
except TypeError as e:
    print(e)