# import random

# num1 = random.randint(1, 100)
# num2 = random.randint(-10, 150)
#
# print(num1, num2)


# for i in range(10):
#     print(random.randint(1, 100))

# num = random.uniform(1.34, 3.98)
# print(num)

# random.seed(12)   # явно устанавливаем начальное значение для генератора случайных чисел
#
# for _ in range(10):
#     print(random.randint(1, 100))
#
# import random
#
# again = 'д'
# while again.lower() == 'д':
#     print('Бросаем кубики... ')
#     print('Значения граней:')
#     print(random.randint(1, 6))
#     print(random.randint(1, 6))
#     again = input('Бросить кубики еще раз? (д = да, н = нет): ')

# for _ in range(10):
#     num = random.randint(0, 1)
#     if num == 0:
#         print('Орел')
#     else:
#         print('Решка')



# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# random.shuffle(numbers)
# print(numbers)

# print(random.choice('BEEGEEK'))
# print(random.choice([1, 2, 3, 4]))
# print(random.choice(['a', 'b', 'c', 'd']))

# import random
#
# numbers = [2, 5, 8, 9, 12]
#
# print(random.sample(numbers, 1))
# print(random.sample(numbers, 2))
# print(random.sample(numbers, 3))
# print(random.sample(numbers, 5))

# number = random.randint(1, 100)
#
# while True:
#     num_of_user = int(input('Введите число от 1 до 100: '))
#     if num_of_user > number:
#         print('Слишком много, попробуйте еще раз')
#         continue
#     elif num_of_user < number:
#         print('Слишком мало, попробуйте еще раз')
#         continue
#     else:
#         print('Вы угадали, поздравляем!')
#         break

# import math
# a = math.log2(12000000)
# print(math.ceil(a))


# Алгоритм угадывания

# left = 1
# right = 100
# middle = (left + right) // 2
# count = 0
# user_num = int(input())
#
# if middle == user_num:
#     print('YES')
# elif middle < user_num:
#     left = middle + 1
#     count += 1
# elif middle > user_num:
#     right = middle - 1
#     count += 1


# import math

# n = int(input())
# answer = math.ceil(math.log2(n))
# print(answer)

from random import randint

print('Добро пожаловать в числовую угадайку')
n = int(input('до какого числа выбрать диапозон? '))
num = randint(1, n)

def is_valid(text):
    if text.isdigit() and 1 <= int(text) <= n:
        return True
    else:
        return False

def input_digit():
    popitka = 1
    while True:
        user_num = input(f'Введите ваше число от 1 до {n}: ')
        if is_valid(user_num) == True:
            user_num = int(user_num)
            if user_num < num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                popitka += 1
                continue
            elif user_num > num:
                print('Ваше число больше загаданного, попробуйте еще разок')
                popitka += 1
                continue
            else:
                print(f'Вы угадали c {popitka} попытки, поздравляем!')
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                break

        else:
            print(f'А может быть все-таки введем целое число от 1 до {n}?')


input_digit()

while True:
    print('Хотите еще сыграть? ')
    answer = input('ДА или НЕТ')
    if answer.lower() == 'да':
        n = int(input('до какого числа выбрать диапозон? '))
        num = randint(1, n)
        input_digit()
    else:
        print('До свидания')
        break




