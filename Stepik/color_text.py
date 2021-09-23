# from colorama import init, Fore, Back, Style
#
# init(autoreset=True)
#
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print()
# print(Style.DIM + 'back to dim now')
# print(Style.BRIGHT + 'back to bright now')
# print(Style.NORMAL + 'back to normal now')


english_symbols_lower = 'abcdefghijklmnopqrstuvwxyz'
english_symbols_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
russian_symbols_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
russian_symbols_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
key = 2
#
# switch = input('Выберете шифровние (s) или дешифрование (d) ').lower()
# language = input('Какой язык выбрать? Английский (е) или Русский (r) ').lower()
# key = int(input('Какой применить шаг сдвига? '))

text = 'эюя'
final_text = ''

for i in text:
    if i in russian_symbols_lower:
        if russian_symbols_lower[russian_symbols_lower.index(i) + key] > len(russian_symbols_lower):

    else:
        print(russian_symbols_lower[russian_symbols_lower.index(i) + key], end='')
    if i in russian_symbols_upper:
        if
    else:
        print(russian_symbols_upper[russian_symbols_upper.index(i) + key], end='')





# sdvig = int(input())
# text = str(input())
# char = 0
# shifr = ''
#
# for i in text:
#     char = ord(i) - sdvig
#     if char < 97:
#         shifr = 122 - (96 - char)
#     else:
#         shifr = char
#     print(chr(shifr), end='')