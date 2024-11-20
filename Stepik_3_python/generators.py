# def bee():
#     print('--')
#     yield 'b'
#     yield 'e'
#     yield 'e'
#     print('--')
#
# for elem in bee():
#     print(elem)


# def simple_sequence():
#     counter = 1
#     while True:
#         for i in range(counter):
#             yield counter
#         counter += 1
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# generator = simple_sequence()
#
# print(next(generator))
# print(next(generator))
#
# # TEST_2:
# generator = simple_sequence()
# numbers = [next(generator) for _ in range(10)]
#
# print(*numbers)
#
# # TEST_3:
# generator = simple_sequence()
#
# for _ in range(100):
#     print(next(generator))
#
# # TEST_4:
# generator = simple_sequence()
#
# for _ in range(1000):
#     next(generator)
#
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
#
# # TEST_5:
# generator = simple_sequence()
#
# for _ in range(10_000):
#     next(generator)
#
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
#
# # TEST_6:
# generator = simple_sequence()
#
# for _ in range(10_000_000):
#     next(generator)
#
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))


# def alternating_sequence(count=None):
#     c = range(1, 1_000_000_000_000_000_000)
#     if count == None:
#         while True:
#             for i in c:
#                 if i % 2 != 0:
#                     yield i
#                 else:
#                     yield '-' + str(i)
#     else:
#         for i in range(1, count + 1):
#             if i % 2 != 0:
#                 yield i
#             else:
#                 yield '-' + str(i)


# def alternating_sequence(count=None, n=0):
#     while n != count:
#         n += 1
#         yield n if n % 2 else -n










# INPUT DATA:

# TEST_1:
# generator = alternating_sequence()
#
# print(next(generator))
# print(next(generator))
#
# # TEST_2:
# generator = alternating_sequence(10)
#
# print(*generator)
#
# # TEST_3:
# generator = alternating_sequence(100)
#
# print(*generator)
#
# # TEST_4:
# generator = alternating_sequence(50)
#
# for _ in generator:
#     pass
#
# try:
#     next(generator)
# except StopIteration:
#     print('Error')
#
# # TEST_5:
# generator = alternating_sequence()
#
# for _ in range(10_000):
#     next(generator)
#
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
#
# # TEST_6:
# generator = alternating_sequence()
#
# for _ in range(10_124_421):
#     next(generator)
#
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
#
# # TEST_7:
# generator = alternating_sequence(1)
#
# try:
#     print(next(generator))
#     print(next(generator))
# except StopIteration:
#     print('Error')




# def primes(left, right):
#     for i in range(left, right + 1):
#         count = 0
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 count += 1
#         if count == 2:
#             yield i
#
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# generator = primes(1, 15)
#
# print(*generator)
#
# # TEST_2:
# generator = primes(6, 36)
#
# print(next(generator))
# print(next(generator))
#
# # TEST_3:
# generator = primes(37, 37)
#
# try:
#     print(next(generator))
#     print(next(generator))
# except StopIteration:
#     print('Error')
#
# # TEST_4:
# generator = primes(39, 83)
#
# print(*generator)
#
# # TEST_5:
# generator = primes(43, 79)
#
# print(*generator)
#
# # TEST_6:
# generator = primes(43, 72)
#
# print(*generator)
#
# # TEST_7:
# generator = primes(1000, 2000)
#
# print(*generator)
#
# # TEST_8:
# generator = primes(2000, 100000)
#
# for _ in range(1000):
#     next(generator)
#
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))




