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


# def reverse(sequence):
#     for i in sequence[::-1]:
#         yield i
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# print(*reverse([1, 2, 3, 4, 5]))
#
# # TEST_2:
# generator = reverse('beegeek')
#
# print(type(generator))
# print(*generator)
#
# # TEST_3:
# generator = reverse('stepik')
#
# print(type(generator))
#
# try:
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
# except StopIteration:
#     print('Error')
#
# # TEST_4:
# generator = reverse(list(range(123, 5453, 3)))
#
# print(type(generator))
# print(*generator)
#
# # TEST_5:
# generator = reverse(tuple('HFJDHFjdhfjhfdJSHFJDHF'))
#
# print(type(generator))
#
# try:
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
# except StopIteration:
#     print('Error')
#
# # TEST_6:
# generator = reverse(list('HFJDHFjd23423i942313223hfjhfdJSHFJD656754964HF'))
#
# print(type(generator))
# print(*generator)
#
# # TEST_7:
# generator = reverse([1])
#
# print(type(generator))
# print(*generator)
#
# # TEST_8:
# print(list(reverse([])))

from datetime import date, timedelta


# def dates(start, count=None):
#     current = start
#     delta = timedelta(days=1)
#     try:
#         if count is None:
#             while current.year <= 9999:
#                 yield current
#                 current += delta
#         else:
#             for _ in range(count):
#                 if current.year > 9999:
#                     raise StopIteration
#                 yield current
#                 current += delta
#     except:
#         return


# from datetime import date, timedelta
#
#
# def dates(start, count=None):
#     count = count or (date.max - start).days + 1
#     for i in range(count):
#         yield start + timedelta(days=i)
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# generator = dates(date(2022, 3, 8))
#
# print(next(generator))
# print(next(generator))
# print(next(generator))
#
# # TEST_2:
# generator = dates(date(2022, 3, 8), 5)
#
# print(*generator)
#
# # TEST_3:
# generator = dates(date(2025, 9, 11), 99)
#
# print(*generator)
#
# # TEST_4:
# generator = dates(date(2024, 9, 13), 1)
#
# try:
#     d = next(generator)
#     print(type(d))
#     print(d)
#     next(generator)
# except StopIteration:
#     print('Error')
#
# # TEST_5:
# generator = dates(date(2049, 1, 7))
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
# print(next(generator))
#
# # TEST_6:
# generator = dates(date(9999, 1, 7))
#
# for _ in range(348):
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
# print(next(generator))
#
# try:
#    print(next(generator))
# except StopIteration:
#     print('Error')






