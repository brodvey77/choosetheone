# def my_pow(number, l = []):
#     for i in enumerate(str(number), 1):
#         l.append(int(i[1])**i[0])
#     print(sum(l))


# def my_pow(number):
#     return sum(int(c)**i for i, c in enumerate(str(numbe


# print(my_pow(139))


# names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
# budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
# box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]
#
#
#
#
# for n, b, bo in sorted(zip(names, budgets, box_offices)):
#     print(f'{n}: {bo - b}$')



# def zip_longest(*args, fill=None):
#     maximum = len(max(args, key=len))
#     for i in args:
#         while len(i) < maximum:
#             i.append(fill)
#     return list(zip(*args))
#
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))
# # [(1, 'a'), (2, 'b'), (3, 'c'), (4, '_'), (5, '_')]
#
# # TEST_2:
# data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
# print(zip_longest(*data))
#
# # TEST_3:
# data = [[1, 2, 3, 4, 5], ['one', 'two', 'three', 'four', 'five'], ['I', 'II', 'III', 'IV', 'V']]
# print(zip_longest(*data))
#
# # TEST_4:
# data = [[], ['one'], [], ['uno']]
# print(zip_longest(*data))
#
# # TEST_5:
# data = [[], ['one'], [], ['uno']]
# print(zip_longest(*data, fill='not known'))
#
# # TEST_6:
# data = [[]]
# print(zip_longest(*data, fill='not known'))
#
# # TEST_7:
# data = [[]]
# print(zip_longest(*data))
#
# # TEST_8:
# data = [[1, 2, 3, 4, 5], ['repeat', 'itertools', 'recursion'], [90, 100, 10, 40]]
# print(zip_longest(*data, fill='add'))
#
# # TEST_9:
# data = [[1, 2, 3, 4, 5], ['repeat', 'itertools', 'recursion'], [90, 100, 10, 40]]
# print(zip_longest(*data))
#
# # TEST_10:
# data = [['is_lower', 'is_upper'], [True, False, 'string', 'int', 'float', 'double', 'char', 'bool'], [False, False, True, True]]
# print(zip_longest(*data, fill='skip'))
#
# # TEST_11:
# data = [['is_lower', 'is_upper'], [True, False, 'string', 'int', 'float', 'double', 'char', 'bool'],
#         [False, False, True, True], [1, 5, 9, 9, 104, -24, 13.4, 'f']]
# print(zip_longest(*data, fill='skip'))

# def custom_sort(s):
#     # Разделяем символы на три категории
#     lower = sorted([c for c in s if c.islower()])  # строчные буквы
#     upper = sorted([c for c in s if c.isupper()])  # заглавные буквы
#     odd_digits = sorted([c for c in s if c.isdigit() and int(c) % 2 != 0])  # нечетные цифры
#     even_digits = sorted([c for c in s if c.isdigit() and int(c) % 2 == 0])  # четные цифры
#
#     # Объединяем отсортированные категории
#     return ''.join(lower + upper + odd_digits + even_digits)
#
#
# # Чтение входных данных
# input_string = input().strip()
# # Вывод результата
# print(custom_sort(input_string))

# print(hash(-1) == -1)
# print(hash(-2) == -2)

# def hash_as_key(objects):
#     d = {}
#     for i in objects:
#         d.setdefault(hash(i), []).append(i)
#     for k, v in d.items():
#         if len(v) == 1:
#             d[k] = d[k][0]
#     return d
#
#
# data = [1, 2, 3, 4, 5, 5]
# print(hash_as_key(data))
#
# data = [-1, -2, -3, -4, -5]
# print(hash_as_key(data))
#
# data = [(1, 2, 3), (1, 2, 3), (0, 0, 0), 10, (144, 75, 60), 20, 30]
# print(hash_as_key(data))
