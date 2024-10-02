# def message():
#     print('Это рекурсивная функция')
#     message()
#
# message()

# def bee(n):
#     if n > 0:
#         print(n)
#         bee(n - 1)
#
# bee(3)

# def bee(n):
#     if n > 0:
#         bee(n - 1)
#         print(n)
#
# bee(3)

# def bee(n):
#     if n > 0:
#         print(n)
#         bee(n - 1)
#         print(n)
#
# bee(2)


# def bee(n):
#     if n > 0:
#         print(n)
#         bee(n - 1)
#     print(n)
#
# bee(2)


# def bee(n):
#     print(n)
#     if n > 0:
#         print(n)
#         bee(n - 1)
#
# bee(2)

# def beegeek(n):
#     if n > 0:
#         print('bee')
#         beegeek(n - 1)
#     else:
#         print('geek')
#
# beegeek(3)


# def bee(n):
#     if n >= 777:
#         print('bee')
#     else:
#         bee(n + 1)
#
# bee(666)


# def bee(n):
#     if n >= 7:
#         print('bee')
#     else:
#         print(n)
#         bee(n + 1)
#
#
# bee(4)

# def bee(n):
#     if n >= 7:
#         print('bee')
#     else:
#         bee(n + 1)
#         print(n)
#
#
# bee(4)

# def draw_rect(width, height, step):
#     if step < height:
#         print('*' * width)
#         draw_rect(width, height, step + 1)
#
# draw_rect(4, 3, 0)
# print()
# draw_rect(6, 6, 0)
# print()
# draw_rect(10, 2, 0)

# def draw_rect(width, height, step=0):
#     if step < height:
#         print('*' * width)
#         draw_rect(width, height, step + 1)

# def draw_rect(width, height):
#     def rec(step):
#         if step < height:
#             print('*' * width)
#             rec(step + 1)
#     rec(0)

# def bee(n):
#     if n < 5:
#         bee(n + 1)
#     else:
#         print(n)
#
# bee(0)


# def traffic(n):
#     while n > 0:
#         print('Не парковаться')
#         n -= 1


# def traffic(n):
#     if n > 0:
#         print('Не парковаться')
#         traffic(n - 1)


# def number_arr():
#     def num(number):
#         if number < 101:
#             print(number)
#             num(number + 1)
#
#     num(1)
#
#
# number_arr()


# numbers = [243, -279, 395, 130, 89, 269, 861, 669, 939, 367, -46, 710, 841, -280, -244, 274, -132, 273, 418, 432, -341, 437, 360, 960, 195, 792, 106, 461, -35, 980, -80, 540, -358, 69, -26, -416, 597, 96, 533, 232, 755, 894, 331, 323, -383, -386, 231, 436, 553, 967, 166, -151, 772, 434, 325, 301, 275, 431, 556, 728, 558, 702, 463, 127, 984, 212, 876, -287, -16, -177, 577, 604, 116, 500, 653, 669, 916, 802, 817, 762, -210, -353, 144, -351, 777, 805, 692, 22, -303, 249, 190, 411, 236, -274, 174, 380, 71, 124, -85, 430]
#
# def get_elements(n):
#     def res(a):
#         if a < 100:
#             print(f'Элемент {a}: {n[a]}')
#             res(a + 1)
#
#     res(0)
#
#
#
#
# get_elements(numbers)


# l = []
# def get_numbers(n):
#     if n > 0:
#         l.append(n)
#         get_numbers(int(input()))
#     else:
#         l.append(0)
#         print(*l[::-1], sep='\n')
#
#
# get_numbers(int(input()))


# def recursion():
#     digit = int(input())
#     if digit != 0:
#         recursion()
#     print(digit)
#
# recursion()


# def triangle(h):
#     if h != 0:
#         print('*' * h)
#         triangle(h - 1)
#
# triangle(5)


# def triangle(h):
#     if h != 1:
#         triangle(h - 1)
#     print(h * '*')
#
#
#
# triangle(5)

