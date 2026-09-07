import sys
from contextlib import contextmanager

@contextmanager
def reversed_print():
    standart_output = sys.stdout.write
    sys.stdout.write = lambda text: standart_output(text[::-1])
    yield
    sys.stdout.write = standart_output

import sys
from contextlib import contextmanager


@contextmanager
def reversed_print():
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield
    sys.stdout.write = original_write






print('Если жизнь одаривает вас лимонами — не делайте лимонад')
print('Заставьте жизнь забрать их обратно!')

with reversed_print():
    print('Мне не нужны твои проклятые лимоны!')
    print('Что мне с ними делать?')

print('Требуйте встречи с менеджером, отвечающим за жизнь!')