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


english_symbols_lower = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
english_symbols_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
russian_symbols_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
russian_symbols_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
key = -3
#
# switch = input('Выберете шифровние (s) или дешифрование (d) ').lower()
# language = input('Какой язык выбрать? Английский (е) или Русский (r) ').lower()
# key = int(input('Какой применить шаг сдвига? '))

user_input = input('input your text here: ')


def eng_lang(text):
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


print(eng_lang(user_input))


# for i in text:
#     if i.isupper():
#         now = english_symbols_upper.find(i)
#         final = now + key
#         final_text = english_symbols_upper[final]
#     if i.islower():
#         now = english_symbols_lower.find(i)
#         final = now + key
#         final_text = english_symbols_lower[final]
#     if i not in english_symbols_lower and i not in english_symbols_upper:
#         final_text = i
#
#     print(final_text, end='')



# for i in text:
#     now = english_symbols_lower.find(i)
#     final = now + key
#     final_text = english_symbols_lower[final]
#     if i not in english_symbols_lower:
#         final_text = i
#     print(final_text, end='')
#
#
# for i in text:
#     now = russian_symbols_lower.find(i)
#     final = now + key
#     final_text = russian_symbols_lower[final]
#     if i not in russian_symbols_lower:
#         final_text = i
#     print(final_text, end='')





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