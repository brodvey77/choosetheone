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

# def bee(n):
#     if n > 1:
#         print((f'{n}' * ((5 - n) * 4)).center(16))
#         bee(n - 1)
#     print((f'{n}' * ((5 - n) * 4)).center(16))
#
#
# bee(4)


# def clock(start, end):
#     if start <= end:
#         print((f'{start}' * ((5 - start) * 4)).center(16))
#         clock(start + 1, end - 1)
#     print((f'{start}' * ((5 - start) * 4)).center(16))
#
#
#
#
# clock(1, 5)


# def print_digits(number):
#     if number % 10 != 0:
#         print(number % 10)
#         print_digits(number // 10)
#
#
# print_digits(6)

# def print_digits(number):
#     if number:
#         print_digits(number // 10)
#         print(number % 10)
#
# print_digits(2077)

# def factorial(n):
#     if n == 0:
#         return 1                        # базовый случай
#     else:
#         return n * factorial(n-1)       # рекурсивный случай
#
# print(factorial(4))


# def sum_to(n):
#     if n == 0:
#         return 0                       # базовый случай
#     else:
#         return n + sum_to(n - 1)       # рекурсивный случай

# def recursive_sum(nums):
#     if not nums:
#         return 0                                       # базовый случай
#     return nums[0] + recursive_sum(nums[1:])           # рекурсивный случай
#
# numbers = [1, 9, 2, 8, 7, 3]
#
# print(recursive_sum(numbers))


# def fib(n):
#     if n <= 2:
#         return 1                             # базовый случай
#     else:
#         return fib(n - 1) + fib(n - 2)       # рекурсивный случай
#
#
# print(fib(12))


# cache = {1: 1, 2: 1}                # ключ - номер числа, значение - число Фибоначчи
#
# def fib(n):
#     result = cache.get(n)
#     if result is None:
#         result = fib(n - 2) + fib(n - 1)
#         cache[n] = result
#     return result

# def qty_digits(number):
#     if number < 10:
#         return 1
#     return 1 + qty_digits(number // 10)
#
#
# print(qty_digits(122035))
#
#
# ndg = lambda x: 1 if x < 10 else ndg(x // 10) + 1
#
# print(ndg(int(input())))

# def qty_digits(number):
#     if number < 10:
#         return number
#     return number % 10 + qty_digits(number // 10)
#
#
# print(qty_digits(25))


# def qty_digits(number):
#     if number < 10:
#         return 1
#     return number % 10 + qty_digits(number // 10)
#
# print(qty_digits(int(input())))


# def number_of_frogs(year):
#     if year == 1:
#         return 77
#     return 3 * (number_of_frogs(year - 1) - 30)
#
#
# print(number_of_frogs(10))


# number_of_frogs = lambda year:  77  if year == 1 else 3 * (number_of_frogs(year - 1) - 30)

# def range_sum(numbers, start, end):
#     if start == end:
#         return numbers[start]
#     return numbers[start] + range_sum(numbers, start + 1, end)


#
# print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 22, 32))




# def get_pow(a, n):
#     if n == 0:
#         return 1
#     else:
#         return a * get_pow(a, n - 1)
#
#
#

# get_pow = lambda a, n: 1 if n == 0 else a*get_pow(a, n - 1)
#
# if __name__ == '__main__':
#
#     assert get_pow(5, 2) == 25
#
#     assert get_pow(2, 10) == 1024
#
#     assert get_pow(99, 0) == 1

def get_fast_pow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1: 
        return a * get_fast_pow(a, n - 1)
    else:
        return get_fast_pow(a *a,  n // 2)



print(get_fast_pow(2, 10))