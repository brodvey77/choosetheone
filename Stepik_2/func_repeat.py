# def matrix(n=1, m=None, value=0):
#     if m == None:
#         m = n
#     return [[value for i in range(m)] for j in range(n)]
#
# print(matrix())                   # матрица 1 × 1 из 0
# print(matrix(3))                  # матрица 3 × 3 из 0
# print(matrix(2, 5))               # матрица 2 × 5 из 0
# print(matrix(3, 4, 9))            # матрица 3 × 4 из 9


# def count_args(*args):
#     return len(args)
#
#
# print(count_args())
# print(count_args(10))
# print(count_args('stepik', 'beegeek'))
# print(count_args([], (''), 'a', 12, False))

# def sq_sum(*args):
#     return sum([i**2 for i in args])
#
#
# print(sq_sum())
# print(sq_sum(2))
# print(sq_sum(1.5, 2.5))
# print(sq_sum(1, 2, 3))
# print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# def mean(*args):
#     l = [i for i in args if type(i) in (int, float)]
#     if len(l) > 0:
#         return sum(l)/len(l)
#     else:
#         return 0.0
#
#
#
# print(mean())
# print(mean(7))
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))
# print(mean(-1, 2, 3, 10, ('5')))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# def greet(name, *args):
#     l = [name]
#     for i in args:
#         l.append(i)
#     return 'Hello, ' + ' and '.join(l) + '!'

# def greet(name, *args):
#     return f'Hello, {" and ".join((name,) + args)}!'
#
# print(greet('Timur'))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))

# def print_products(*args):
#     l = [i for i in args if type(i) == str and len(i) > 0]
#     for i in enumerate(l, 1):
#         print(*i)

# def print_products(*args):
#     l = [i for i in args if type(i) == str and len(i) > 0]
#     if len(l) == 0:
#         print('Нет продуктов')
#     else:
#         counter = 1
#         for i in l:
#             print(f'{counter}) {i}')
#             counter += 1
#
# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)


# def info_kwargs(**kwargs):
#     print(kwargs)
#     for k, v in sorted(kwargs.items()):
#         print(f'{k}: {v}')
#
#
#
# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')




