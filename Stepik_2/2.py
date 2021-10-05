# import math
# a, b = int(input()), int(input())
#
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(math.sqrt(a ** 10 + b ** 10))

# Body mass index

# weight, height = float(input('Input your weight in kg: ')), float(input('Input your height in m: '))
#
# body_mass_index = weight / height ** 2
#
# if body_mass_index < 18.5:
#     print('Недостаточная масса')
# elif body_mass_index > 25:
#     print('Избыточная масса')
# else:
#     print('Оптимальная масса')

# Line cost

# text = str(input())
# ruble = 0
# penny = 0
# counter = 0
#
#
# for i in text:
#     counter += 60
#     if counter > 100:
#         ruble += counter // 100
#         penny += counter % 100
#         counter = 0
#         if penny == 100:
#             ruble += penny //100
#             penny = 0
#     elif i == text[-1] and counter != 0:
#         penny += counter
#         if penny == 100:
#             ruble += penny //100
#             penny = 0
#
#
# print(f'{ruble} р. {penny} к.')


# string = input()
# price = 60 * len(string)
#
# print(f'{price // 100} р. {price % 100} коп.')


# print(len([i for i in str(input()).split()]))

# print(len(input().split()))

year = int(input())




