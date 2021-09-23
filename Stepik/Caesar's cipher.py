# Caesar's cipher
import time

english_symbols_lower = 'abcdefghijklmnopqrstuvwxyz'
english_symbols_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
russian_symbols_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
russian_symbols_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


switch = input('Выберете шифровние (s) или дешифрование (d) ').lower()
time.sleep(0.5)
language = input('Какой язык выбрать? Английский (е) или Русский (r) ').lower()
time.sleep(0.5)
key = int(input('Какой применить шаг сдвига? '))
time.sleep(0.5)


final_text = ''
for i in text:
    if i in russian_symbols_upper:
        final_text += i[russian_symbols_upper] + key

    if i in russian_symbols_lower:
        final_text += i[russian_symbols_lower] + key






# if switch == 's':
#     text = input('Введите текст для шифрования: ')
#     print(func_of_cipfer(text, language, key))
# if switch == 'd':
#     text = input('Введите текст для расшифровки: ')
#     print(func_of_decipher(text, language, key))