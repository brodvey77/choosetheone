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

# def get_fast_pow(a, n):
#     if n == 0:
#         return 1
#     elif n % 2 == 1:
#         return a * get_fast_pow(a, n - 1)
#     else:
#         return get_fast_pow(a *a,  n // 2)
#
#
#
# print(get_fast_pow(2, 10))


# def recursive_sum(a, b):
#     if b == 0:
#         return a
#     else:
#         return recursive_sum(a + 1, b - 1)
#
#
# print(recursive_sum(10, 22))
# print(recursive_sum(99, 0))
# print(recursive_sum(0, 0))

# def is_power(number):
#     if number <= 2:
#         return True
#     elif number % 2 == 1:
#         return False
#     else:
#         return is_power(number / 2)
#
#
# if __name__ == "__main__":
#     assert is_power(512) == True
#     assert is_power(15) == False
#     assert is_power(1) == True
#     assert is_power(2)== True
#     assert is_power(100) == False
#     assert is_power(128) == True
#     assert is_power(1024) == True
#     assert is_power(1111111) == False
#
# def tribonacci(n):
#     cache = {1: 1, 2: 1, 3: 1}
#     def fib_rec(n):
#         result = cache.get(n)
#         if result is None:
#             result = fib_rec(n - 3) + fib_rec( n - 2) + fib_rec(n - 1)
#             cache[n] = result
#         return result
#     return fib_rec(n)
#
#
#
#
#
#
# # TEST_1:
# print(tribonacci(1))
#
# # TEST_2:
# print(tribonacci(7))
#
# # TEST_3:
# print(tribonacci(4))
#
# # TEST_4:
# print(tribonacci(3))
#
# # TEST_5:
# print(tribonacci(10))
#
# # TEST_6:
# print(tribonacci(2))
#
# # TEST_7:
# print(tribonacci(300))
#
# # TEST_8:
# print(tribonacci(100))


# def is_palindrome(string):
#     if len(string) <= 1:
#         return True
#     if string[0] != string[-1]:
#         return False
#     else:
#         return is_palindrome(string[1:-1])
#
# # TEST_1:
# print(is_palindrome('stepik'))
#
# # TEST_2:
# print(is_palindrome('level'))
#
# # TEST_3:
# print(is_palindrome('122333221'))
#
# # TEST_4:
# print(is_palindrome('b'))
#
# # TEST_5:
# print(is_palindrome('beegeek'))
#
# # TEST_6:
# print(is_palindrome('redivider'))
#
# # TEST_7:
# print(is_palindrome(''))
#
# # TEST_8:
# print(is_palindrome('aa'))
#
# # TEST_9:
# print(is_palindrome('ab'))
#
# # TEST_10:
# print(is_palindrome('abcca'))


# def to_binary(number):
#     if number == 0:
#         return "0"
#     if number == 1:
#         return "1"
#     else:
#         return to_binary(number // 2) + str(number % 2)
#
#
#
# # TEST_1:
# print(to_binary(15))
#
# # TEST_2:
# print(to_binary(0))
#
# # TEST_3:
# print(to_binary(1))
#
# # TEST_4:
# print(to_binary(256))
#
# # TEST_5:
# print(to_binary(2))
#
# # TEST_6:
# print(to_binary(1025))
#
# # TEST_7:
# print(to_binary(3427))
#
# # TEST_8:
# print(to_binary(131445))
#
# # TEST_9:
# print(to_binary(532))

# def play_digits(n):
#     if n > 0:
#         print(n)
#         play_digits(n - 5)
#     print(n)
#
#
#
#
#
# play_digits(16)







# print(play_digits(16))
# print(play_digits(10))
# print(play_digits(1))


# def get_all_str(data):
#     if type(data) == str:
#         print(data, end=' ')            # базовый случай
#     if type(data) == list:
#         for i in data:
#             get_all_str(i)              # рекурсивный случай
#
#
# numbers = ['1', ['2', '3', ['4'], ['5', ['6', '7']]]]
#
# get_all_str(numbers)

# def find_key(data, key):
#     if key in data:
#         return data[key]  # базовый случай
#
#     for v in data.values():
#         if type(v) == dict:
#             value = find_key(v, key)  # рекурсивный случай
#             if value is not None:
#                 return value
#
#
# info = {'name': 'Alyson',
#         'surname': 'Hannigan',
#         'birthday': {'day': 24, 'month': 'March', 'year': 1974},
#         'family': {'parents': {'mother': 'Emilie Posner', 'father': 'Alan Hannigan'}}}
#
# print(find_key(info, 'month'))
# print(find_key(info, 'mother'))

# Получить значение по умолчанию для максимальной глубины рекурсии можно с помощью функции getrecursionlimit() из модуля sys

# from sys import getrecursionlimit
#
# limit = getrecursionlimit()
#
# print(limit)

# Мы также можем явно установить значение максимальной глубины рекурсии. Для этого используется функция setrecursionlimit() из модуля sys.
#
# Приведенный ниже код:

# import sys
#
# limit = sys.getrecursionlimit()
# print(limit)
#
# sys.setrecursionlimit(6000)
# new_limit = sys.getrecursionlimit()
# print(new_limit)

# import sys
#
# print(sys.getrecursionlimit())


# def recursive_sum(nested_lists):
#     total = 0
#     for element in nested_lists:
#         if isinstance(element, list):
#             total += recursive_sum(element)  # Рекурсивный вызов для вложенного списка
#         else:
#             total += element  # Суммируем целое число
#     return total


# def recursive_sum(nested_lists):
#     if nested_lists == []:
#         return 0
#     elif isinstance(nested_lists, int):
#         return nested_lists
#     elif isinstance(nested_lists, list):
#         return recursive_sum(nested_lists[0]) + recursive_sum(nested_lists[1:])
#
# def recursive_sum(nested_lists):
#     if type(nested_lists) == int:
#         return nested_lists
#     if type(nested_lists) == list:
#         total = 0
#         for i in nested_lists:
#             total += recursive_sum(i)
#         return  total
#
# #
# my_list = [1, [4, 4], 2, [1, [2, 10]]]
# print(recursive_sum(my_list))
#
# my_list = []
# print(recursive_sum(my_list))


# def linear(nested_lists):
#     total = []
#     for element in nested_lists:
#         if isinstance(element, list):
#             total.extend(linear(element))
#         else:
#             total.append(element)
#     return total
#
#
# # TEST_1:
# my_list = [3, [4], [5, [6, [7, 8]]]]
#
# print(linear(my_list))
#
# # TEST_2:
# my_list = [10, 20, 30, 40, 50]
#
# print(linear(my_list))
#
# # TEST_3:
# my_list = [[1], [2], [3], [4, 5], 6, 7]
#
# print(linear(my_list))
#
# # TEST_4:
# my_list = [[123], 23, 43, 65, 754, 3, 1, 2]
#
# print(linear(my_list))
#
# # TEST_5:
# my_list = [3123, 424, 5343, 11, 1, 23, 43, 65, 754, 3, 1, [2]]
#
# print(linear(my_list))
#
# # TEST_6:
# my_list = [[3, 2, 5345, 65, 7, 777, 0, 43, 65, 754, 3, 1, 2]]
#
# print(linear(my_list))
#
# # TEST_7:
# my_list = [34534, [656, [7867, [[234, [123, 34534, [758, 978]]]], 667, [4546]]], [2324, [234234, [7656]], 9879, 55]]
#
# print(linear(my_list))
#
# # TEST_8:
# my_list = [12, [13, [53, [632, [6, [2342341, [98, [3123], [2432], [4324]]]]]]]]
#
# print(linear(my_list))
#
# # TEST_9:
# my_list = [3, [4], [5, [6, [7, 8]]]]
# print(linear(my_list))
#
# my_list = [3, [4], [5, [6, [7, 8]]]]
# print(linear(my_list))


# def get_all_values(nested_dicts, key):
#     if key in nested_dicts:
#         return nested_dicts.get(key)
#     for v in nested_dicts.values():
#         if isinstance(v, dict):
#             value = get_all_values(v, key)
#             if value is not None:
#                 return value


# def get_all_str(data):
#     result = []
#
#     def wrapper(elemnt):
#         if isinstance(elemnt, str):
#             result.append(elemnt)
#
#         elif isinstance(elemnt, list):
#             for item in elemnt:
#                 wrapper(item)
#
#     wrapper(data)
#     return result
#
#
# numbers = ['1', ['2', '3', ['4'], ['5', [['6', []], '7']]]]
# print(get_all_str(numbers))

# def get_all_values(nested_dicts, key):
#     result = []
#     def gav_rec(element):
#         if key in element:                 # base case
#             result.append(element.get(key))
#
#         for v in element.values():         # recursive case
#             if isinstance(v, dict):
#                 value = gav_rec(v)
#                 if value is not None:
#                     return value
#
#     gav_rec(nested_dicts)
#     return set(result)
#
#
# def get_all_values(data, key):
#     values = set()
#     if key in data:
#         values.add(data[key])
#     for item in data.values():
#         if isinstance(item, dict):
#             values |= get_all_values(item, key)
#     return values
#
#
# # TEST_1:
# my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
# result = get_all_values(my_dict, 'top_grade')
#
# print(*sorted(result))
#
# # TEST_2:
# my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
# result = get_all_values(my_dict, 'hobby')
#
# print(*sorted(result))
#
# # TEST_3:
# my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
# result = get_all_values(my_dict, 'top_grade')
#
# print(len(sorted(result)))
#
# # TEST_4:
# my_dict = {
#            'Arthur': {'hobby': 'videogames', 'drink': 'cacao'},
#            'Timur': {'hobby': 'math'},
#            'Dima': {
#                    'hobby': 'CS',
#                    'sister':
#                        {
#                          'name': 'Anna',
#                          'hobby': 'TV',
#                          'age': 14
#                        }
#                    }
#            }
#
# result = get_all_values(my_dict, 'hobby')
# print(*sorted(result))
#
# # TEST_5:
# my_dict = {
#            'Arthur': {'hobby': 'videogames', 'drink': 'cacao'},
#            'Timur': {'hobby': 'math'},
#            'Dima': {
#                    'hobby': 'CS',
#                    'sister':
#                        {
#                          'name': 'Anna',
#                          'hobby': 'TV',
#                          'age': 14
#                        }
#                    }
#            }
#
# result = get_all_values(my_dict, 'age')
# print(*result)
#
# # TEST_6:
# my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
# result = get_all_values(my_dict, 'top_grade')
#
# print(*sorted(result))
# print(type(result))
#
# my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
# result = get_all_values(my_dict, 'hobby')
#
# print(*sorted(result))

# def get_all_values(data, key):
#     s = set()
#     if key in data:
#         s.add(data[key])
#     for k, v in data.items():
#         if isinstance(v, dict):
#             s.update(get_all_values(v, key))
#     return s

# def get_all_values(data, key):
#     values = set()
#     if key in data:
#         values.add(data[key])
#     for item in data.values():
#         if isinstance(item, dict):
#             values |= get_all_values(item, key)
#     return values

# def dict_travel(nested_dicts, parent_key=''):
#     items = []
#     for k, v in sorted(nested_dicts.items()):
#         new_key = f"{parent_key}.{k}" if parent_key else k
#         if isinstance(v, dict):
#             items.extend(dict_travel(v, new_key).items())
#         else:
#             items.append((new_key, v))
#     return dict(items)
#
#
# data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}
# result = dict_travel(data)
#
# for key, value in result.items():
#     print(f"{key}: {value}")





# def sec():
#     result = dict_travel(data)
#     return result
#
# def dict_travel(nested_dicts, i=''):
#     for k,v in sorted(nested_dicts.items()):
#         if isinstance(v, dict):
#             dict_travel(v, i + f'{k}.')
#         else:
#             print(f'{i}{k}: {v}')
#
#
#
# data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}
# dict_travel(data)
#
#
# data = {'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}
# dict_travel(data)
#
#
# data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}
# dict_travel(data)
#
#
# data = {'firstname': 'Alyson', 'lastname': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}
# dict_travel(data)
#
#
# data = {'firstname': 'Тимур', 'lastname': 'Гуев', 'birthdate': {'day': 10, 'month': 'October', 'year': 1993},'address': {'streetaddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityname': 'Москва'}, 'postalcode': '125315'}}
# dict_travel(data)

# def custom_isinstance(objects, typeinfo):
#     s = 0
#     for element in objects:
#         if isinstance(element, typeinfo):
#             s += 1
#     return s
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
# print(custom_isinstance(numbers, int))
#
# # TEST_2:
# numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
# print(custom_isinstance(numbers, (int, float)))
#
# # TEST_3:
# numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
# print(custom_isinstance(numbers, list))
#
# # TEST_4:
# numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
# print(custom_isinstance(numbers, (set, tuple)))
#
# # TEST_5:
# objects = [{2, 3, 4}, (5, 7, 1243), ["Hello World", "Тимур"]]
# print(custom_isinstance(objects, (tuple, list)))
#
# def custom_isinstance(objects, typeinfo):
#     return sum(isinstance(i, typeinfo) for i in objects)

# numbers = [-7724, 5023, 3197, -102, -4129, -880, 5857, -2866, -8913, 1195, 9809, 5347, -8071, 903, 3030, -4347, -3354, 1024, 8670, 4210, -5228, 8900, 4823, -2002, 4900, 9520, -3658, 1104, -9554, 3064, 9632, -8701, 3384, 4370, 2034, 7822, -9694, 3347, 7440, -8459, 3238, -5193, -3381, 5281, 9022, 5559, 7593, -6540, -6204, -2483, 8729, 5810, -8254, -9846, -1801, 4882, 3838, -3140, 7609, -3325, 6026, 2994, -1677, 1266, -1893, -4408, -5722, -2841, 9812, 5837, -7474, 4624, -664, 6998, 7888, -971, 8810, 3812, -5396, 2593, 512, -4634, 9735, -3062, 9031, -9300, 3657, 6332, 7552, 8125, -725, 4392, 1727, 8194, -2828, -4314, -8967, -7912, -1363, -5957]
#
# print(max(enumerate(numbers), key=lambda x: x[1])[0])

# print(numbers.index(max(numbers)))

from operator import attrgetter
# print(max(enumerate(numbers), key=itemgetter(1))[0])


