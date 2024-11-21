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


# def card_deck(suit):
#     suits = ['пик', 'треф', 'бубен', 'червей']
#     ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
#
#     cards = [f"{rank} {s}" for s in suits if s != suit for rank in ranks]
#
#     while True:
#         for card in cards:
#             yield card
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# generator = card_deck('пик')
#
# print(next(generator))
# print(next(generator))
# print(next(generator))
#
# # TEST_2:
# generator = card_deck('треф')
# cards = [next(generator) for _ in range(40)]
#
# print(*cards)
#
# # TEST_3:
# generator = card_deck('бубен')
#
# cards = [next(generator) for _ in range(50)]
#
# print(*cards)
#
# # TEST_4:
# generator = card_deck('червей')
#
# cards = [next(generator) for _ in range(60)]
#
# print(*cards)
#
# # TEST_5:
# generator = card_deck('пик')
#
# cards = [next(generator) for _ in range(80)]
#
# print(*cards)

#
# def bee():
#     yield 'b'
#     yield 'e'
#     yield 'e'
#
# def geek():
#     yield from 'geek'
#
# print(*bee())
# print(*geek())


# def bee():
#     yield from 'bee'
#
# def geek():
#     yield from 'geek'
#
# def beegeek():
#     yield from bee()
#     yield from geek()
#
# print(*beegeek())



# def matrix_by_elem(matrix):
#     for row in matrix:
#         for elem in row:
#             yield elem

# def matrix_by_elem(matrix):
#     for row in matrix:
#         yield from row
#
# def matrix_by_elem(matrix):
#     yield from sum(matrix, [])


#
# # INPUT DATA:
#
# # TEST_1:
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# print(*matrix_by_elem(matrix))
#
# # TEST_2:
# matrix = [[1, 2, 3],
#           [4, 5, 6]]
#
# print(list(matrix_by_elem(matrix)))
#
# # TEST_3:
# matrix = [[1, 2, 3, 5, 6, 7, 8],
#           [9, 10, 11, 12, 13, 14, 15]]
#
# print(list(matrix_by_elem(matrix)))
#
# # TEST_4:
# matrix = [[1, 2, 3, 5, 6, 7, 8],
#           [9, 10, 11, 12, 13, 14, 15],
#           [16, 17, 18, 19, 20, 21, 22]]
#
# print(tuple(matrix_by_elem(matrix)))


# def palindromes():
#     num = 1
#     while True:
#         if str(num) == str(num)[::-1]:
#             yield num
#         num += 1
#
#
#
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# generator = palindromes()
#
# print(next(generator))
# print(next(generator))
# print(next(generator))
#
# # TEST_2:
# generator = palindromes()
# numbers = [next(generator) for _ in range(30)]
#
# print(*numbers)
#
# # TEST_3:
# generator = palindromes()
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
#
# # TEST_4:
# generator = palindromes()
#
# for _ in range(1_000):
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
#
# # TEST_5:
# generator = palindromes()
#
# for _ in range(100):
#     print(next(generator))

# def palindromes():
#     yield from (i for i, _ in enumerate(iter(bool, True), 1) if str(i) == str(i)[::-1])


# def flatten(nested_list):
#     for i in nested_list:
#         if isinstance(i, list):
#             yield from flatten(i)
#         else:
#             yield i
#
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# generator = flatten([[1, 2], [[3]], [[4], 5]])
#
# print(*generator)
#
# # TEST_2:
# generator = flatten([1, 2, 3, 4, 5, 6, 7])
#
# print(*generator)
#
# # TEST_3:
# generator = flatten([3, [4], [5, [6, [7, 8]]]])
#
# print(*generator)
#
# # TEST_4:
# generator = flatten([10, 20, 30, 40, 50])
#
# print(*generator)
#
# # TEST_5:
# generator = flatten([[1], [2], [3], [4, 5], 6, 7])
#
# print(*generator)
#
# # TEST_6:
# generator = flatten([[1], [2], [3], [4], [5], [6], [7]])
#
# print(*generator)
#
# # TEST_7:
# generator = flatten([[123], 23, 43, 65, 754, 3, 1, 2])
#
# print(*generator)
#
# # TEST_8:
# generator = flatten([3123, 424, 5343, 11, 1, 23, 43, 65, 754, 3, 1, [2]])
#
# print(*generator)
#
# # TEST_9:
# generator = flatten([[3, 2, 5345, 65, 7, 777, 0, 43, 65, 754, 3, 1, 2]])
#
# print(*generator)
#
# # TEST_10:
# generator = flatten([34534, [656, [7867, [[234, [123, 34534, [758, 978]]]], 667, [4546]]], [2324, [234234, [7656]], 9879, 55]])
#
# print(*generator)
#
# # TEST_11:
# generator = flatten([12, [13, [53, [632, [6, [2342341, [98, [3123], [2432], [4324]]]]]]]])
#
# print(*generator)


# from datetime import datetime, timedelta
#
#
# def choose_plural(value, forms):
#     if value % 10 == 1 and value % 100 != 11:
#         return forms[0]
#     elif 2 <= value % 10 <= 4 and (value % 100 < 10 or value % 100 >= 20):
#         return forms[1]
#     else:
#         return forms[2]
#
#
# def time_until_course_release(current_datetime):
#     release_datetime = datetime(2022, 11, 8, 12, 0)
#
#     if current_datetime >= release_datetime:
#         return "Курс уже вышел!"
#
#     delta = release_datetime - current_datetime
#     days = delta.days
#     hours, remainder = divmod(delta.seconds, 3600)
#     minutes, seconds = divmod(remainder, 60)
#
#     if days > 0 and hours > 0:
#         return f"До выхода курса осталось: {days} {choose_plural(days, ['день', 'дня', 'дней'])} и {hours} {choose_plural(hours, ['час', 'часа', 'часов'])}"
#     elif days > 0:
#         return f"До выхода курса осталось: {days} {choose_plural(days, ['день', 'дня', 'дней'])}"
#     elif hours > 0 and minutes > 0:
#         return f"До выхода курса осталось: {hours} {choose_plural(hours, ['час', 'часа', 'часов'])} и {minutes} {choose_plural(minutes, ['минута', 'минуты', 'минут'])}"
#     elif hours > 0:
#         return f"До выхода курса осталось: {hours} {choose_plural(hours, ['час', 'часа', 'часов'])}"
#     else:
#         return f"До выхода курса осталось: {minutes} {choose_plural(minutes, ['минута', 'минуты', 'минут'])}"
#
#
# # Пример использования
# input_str = input()
# current_datetime = datetime.strptime(input_str, "%d.%m.%Y %H:%M")
# print(time_until_course_release(current_datetime))


# generator = (char.upper() for char in 'stepik')
#
# next(generator)
# next(generator)
# next(generator)
#
# print(list(generator))

# def cubes_of_odds(iterable):
#     for number in iterable:
#         if number % 2:
#             yield number ** 3


# def cubes_of_odds(iterable):
#     return (num ** 3 for num in iterable if num % 2)
#
# cubes_of_odds = lambda it: (i ** 3 for i in it if i % 2)
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# print(*cubes_of_odds([1, 2, 3, 4, 5]))
#
# # TEST_2:
# evens = [2, 4, 6, 8, 10]
#
# print(list(cubes_of_odds(evens)))
#
# # TEST_3:
# data = tuple(range(432, 3845, 17))
#
# print(*cubes_of_odds(data))
#
# # TEST_4:
# data = map(abs, range(-200, 400, 11))
#
# print(*cubes_of_odds(data))
#
# # TEST_5:
# data = filter(lambda x: x % 13, range(101, 982))
#
# print(*cubes_of_odds(data))


