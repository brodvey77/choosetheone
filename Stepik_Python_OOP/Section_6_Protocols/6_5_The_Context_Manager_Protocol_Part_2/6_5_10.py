class Suppress:
    def __init__(self, *exceptions):
        self.exceptions = exceptions
        self.exception = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None and issubclass(exc_type, self.exceptions):
            self.exception = exc_value
            return True
        return False


class Suppress:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.exceptions:
            self.exception = exc_val
            return True
        self.exception = None
        return False




with Suppress(NameError):
    print('Этой переменной не существует -->', variable)

print('Завершение программы')

with Suppress(TypeError, ValueError) as context:
    number = int('я число')

print(context.exception)
print(type(context.exception))


with Suppress() as context:
    print('All success!')

print(context.exception)