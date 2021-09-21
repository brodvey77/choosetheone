# The Password Generator

import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''


n = int(input('Количество паролей генерации? '))
len_password = int(input('Какая длина пароля? '))
is_digits = input('Включать ли цифры 0123456789? y/n ')
is_lower_letters = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? y/n ')
is_upper_letters = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? y/n ')
is_punctuation = input('Включать ли символы !#$%&*+-=?@^_? y/n ')
is_not_beeee = input('Исключать ли неоднозначные символы il1Lo0O? y/n ')

if is_digits == 'y':
    chars += digits
if is_lower_letters == 'y':
    chars += lowercase_letters
if is_upper_letters == 'y':
    chars += uppercase_letters
if is_punctuation == 'y':
    chars += punctuation
if is_not_beeee == 'y':
    for i in 'il1Lo0O':
        chars.replace(i, '')



def generate_password(abc, len):
    return random.sample(abc, len)

for i in range(n):
    print(*generate_password(chars, len_password), sep='')










