import sys


# class UpperPrint:
#     def __enter__(self):
#         # Сохраняем оригинальный метод write
#         self.original_write = sys.stdout.write
#         # Переопределяем метод write
#         sys.stdout.write = self.upper_write
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         # Восстанавливаем оригинальный метод write
#         sys.stdout.write = self.original_write
#
#     def upper_write(self, text):
#         # Записываем текст в верхнем регистре
#         self.original_write(text.upper())
#
#
# import sys


class UpperPrint:
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = lambda text: self.original_write(text.upper())
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.original_write



print('Если жизнь одаривает вас лимонами — не делайте лимонад')
print('Заставьте жизнь забрать их обратно!')

with UpperPrint():
    print('Мне не нужны твои проклятые лимоны!')
    print('Что мне с ними делать?')

print('Требуйте встречи с менеджером, отвечающим за жизнь!')