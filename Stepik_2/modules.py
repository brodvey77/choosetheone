# import random
#
# n = int(input())    # количество попыток
#
# result = {1: 'Орел', 2: 'Решка'}
#
# for i in range(n):
#     print(result[random.randrange(1, 3)])

# import random
# n = int(input())    # количество попыток
# for i in range(n):
#     print(random.randint(1, 6))


# import random
#
# length = int(input())    # длина пароля
# my_list = []
# while len(my_list) != length:
#     v = random.randint(65, 122)
#     if v in [91, 92, 93, 94, 95, 96]:
#         continue
#     else:
#         my_list.append(chr(v))
#         print(chr(v), end='')


# import random
#
# length = int(input())    # длина пароля
# password = ''
# for i in range(length):
#     password += [chr(random.randint(65, 90)), chr(random.randint(97, 122))][random.randint(0, 1)]
# print(password)




