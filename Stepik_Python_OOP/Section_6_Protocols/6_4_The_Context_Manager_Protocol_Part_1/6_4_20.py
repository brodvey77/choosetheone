# import os
#
# with os.scandir('.') as enries:
#     for entry in enries:
#         print(entry.name, '--->', entry.stat().st_size, 'bytes')
#
#
#
# from tempfile import TemporaryFile
#
# with TemporaryFile(mode='r+') as file:
#     file.write('Python generation!')
#     file.seek(0)
#     content = file.read()
#     print(content)


# class ContextManager:
#     def __enter__(self):
#         print('Вызов метода __enter__()')
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         print('Вызов метода __exit__()')
#
#
# with ContextManager() as manager:
#     print(manager)

# class ContextManager:
#     def __enter__(self):
#         print('Вызов метода __enter__()')
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         print('Вызов метода __exit__()')
#
#     def __str__(self):
#         return 'dsdssddsdsdsd'
#
#
# with ContextManager() as cm:
#     print(cm)


# class ContextManager:
#     def __enter__(self):
#         print('Вызов метода __enter__()')
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         print('Вызов метода __exit__()')
#         if isinstance(exc_value, ValueError):
#             print('Исключение ValueError обработано')
#             return True
#         return False
#
#
# try:
#     with ContextManager():
#         print('Выполнение блока with')
#         raise ValueError
# except ValueError:
#     print('Исключение обработано')


def is_context_manager(obj):
    if hasattr(obj, '__enter__') and hasattr(obj, '__exit__'):
        return True
    return False


# INPUT DATA:

# TEST_1:
print(is_context_manager(open('output.txt', mode='w')))

# TEST_2:
from tempfile import TemporaryFile

with TemporaryFile(mode='r+') as file:
    print(is_context_manager(file))

# TEST_3:
from threading import Lock

print(is_context_manager(Lock()))

# TEST_4:
print(is_context_manager(1992))
print(is_context_manager('beegeek'))
print(is_context_manager([1, 2, 3]))
print(is_context_manager({'one': 1, 'two': 2}))
print(is_context_manager(None))


# TEST_5:
class ContextManager:
    def __enter__(self):
        return 'beegeek'

    def __exit__(self, exc_type, exc_value, exc_tb):
        return True


print(is_context_manager(ContextManager()))


# TEST_6:
class ContextManager:
    def __init__(self):
        self.inside = False

    def __enter__(self):
        self.inside = True
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.inside = False
        return True


print(is_context_manager(ContextManager()))


# TEST_7:
class ContextManager:
    def __enter__(self):
        return 'beegeek'


print(is_context_manager(ContextManager()))


# TEST_8:
class ContextManager:
    def __init__(self):
        self.inside = False

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.inside = False
        return True


print(is_context_manager(ContextManager()))



def is_context_manager(obj):
    return hasattr(obj, '__enter__') and hasattr(obj, '__exit__')