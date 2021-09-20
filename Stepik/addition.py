import random

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
