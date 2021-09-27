# Caesar's cipher
# import time
#
# english_symbols_lower = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
# english_symbols_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
# russian_symbols_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
# russian_symbols_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
#
# switch = input('Выберете шифровние (s) или дешифрование (d) ').lower()
# time.sleep(0.5)
# language = input('Какой язык выбрать? Английский (е) или Русский (r) ').lower()
# time.sleep(0.5)
# key = int(input('Какой применить шаг сдвига? '))
# time.sleep(0.5)
#
#
# def eng_lang(text, key):
#     final_text = ''
#     for i in text:
#         if i.isupper():
#             now = english_symbols_upper.find(i)
#             final = now + key
#             final_text += english_symbols_upper[final]
#         if i.islower():
#             now = english_symbols_lower.find(i)
#             final = now + key
#             final_text += english_symbols_lower[final]
#         if i not in english_symbols_lower and i not in english_symbols_upper:
#             final_text += i
#     return final_text
#
#
# def rus_eng(text, key):
#     final_text = ''
#     for i in text:
#         if i.isupper():
#             now = russian_symbols_upper.find(i)
#             final = now + key
#             final_text += russian_symbols_upper[final]
#         if i.islower():
#             now = russian_symbols_lower.find(i)
#             final = now + key
#             final_text += russian_symbols_lower[final]
#         if i not in russian_symbols_lower and i not in russian_symbols_upper:
#             final_text += i
#     return final_text
#
#
# if switch == 's':
#     user_input = input('Введите текст для шифрования: ')
#     if language == 'e':
#         print(eng_lang(user_input, key))
#     else:
#         print(rus_eng(user_input, key))
# if switch == 'd':
#     user_input = input('Введите текст для расшифровки: ')
#     if language == 'e':
#         print(eng_lang(user_input, -key))
#     else:
#         print(rus_eng(user_input, -key))


english_symbols_lower = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
english_symbols_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

input_text = input('Input your text here: ')
text = input_text.split(' ')
new_text = []

for i in text:
    new_text.append(i.replace(',', '').replace('.', '').replace('"', '').replace('!', '').replace('?', ''))


def decoder(text, key):
    final_text = ''
    for i in text:
        if i.isupper():
            now = english_symbols_upper.find(i)
            final = now + key
            final_text += english_symbols_upper[final]
        if i.islower():
            now = english_symbols_lower.find(i)
            final = now + key
            final_text += english_symbols_lower[final]
        if i not in english_symbols_lower and i not in english_symbols_upper:
            final_text += i
        return final_text


