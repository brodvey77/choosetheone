# sentence = 'In the face of ambiguity refuse the temptation to guess'
#
# filter_iterator = filter(lambda word: len(word) > 4, sentence.split())   # фильтруем
# map_iterator = map(lambda word: word.upper(), filter_iterator)           # преобразовываем
# enumerate_iterator = enumerate(map_iterator, 1)                          # нумеруем
#
# for index, value in enumerate_iterator:                                  # выводим
# #     print(f'{index}. {value}')
# for i in enumerate('beegeek'):
#     print(i)
#
# for i in [1, 2, 3, 4, 5]:
#     print(i)
#
# for i in 'beegeek':
#     print(i)
#
# for i in range(10):
#     print(i)
#
# for i in map(str.upper, 'beegeek'):
#     print(i)
#
#
#
# for i in (1, 2, 3, 4, 5):
#     print(i)
#
# for i in filter(None, '11010111'):
#     print(i)
#
#
# for i in {'bee': 1, 'geek': 2}:
#     print(i)
#
#
# for i in {1, 2, 3, 4, 5}:
#     print(i)
#
#
# for i in zip('bee', 'geek'):
#     print(i)


# print(next(enumerate('beegeek')))
#
# # print(next([1, 2, 3, 4, 5]))
# # print(next('beegeek'))
# print(next(range(10)))
# print(next(map(str.upper, 'beegeek')))
# # print(next((1, 2, 3, 4, 5)))
# print(next(filter(None, '11010111')))
# # print(next({'bee': 1, 'geek': 2})
# # print(next({1, 2, 3, 4, 5}))
# print(next(zip('bee', 'geek')))

# from sys import getsizeof
#
# numbers1 = range(10)
# numbers2 = range(10000000)
#
# size1 = getsizeof(numbers1)
# size2 = getsizeof(numbers2)
#
# print(size1 == size2)


# numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64, -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88, -11, 16, -22]
#
# a = iter(numbers)
#
# for i in range(3):
#     next(a)
#
#
# print(next(a))