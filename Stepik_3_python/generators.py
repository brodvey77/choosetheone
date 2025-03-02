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

# def is_prime(number):
#     if number < 2:
#         return False
#     return all(number % i != 0 for i in range(2, int(number**0.5) + 1))



# def count_iterable(iterable):
#     return sum(1 for i in iterable)
#
#
# # INPUT DATA:
#
# # TEST_1:
# print(count_iterable([1, 2, 3, 4, 5]))
#
# # TEST_2:
# numbers = iter([1, 2, 3, 4, 5, 6, 7])
#
# print(count_iterable(numbers))
#
# # TEST_3:
# data = tuple(range(432, 3845, 17))
#
# print(count_iterable(data))
#
# # TEST_4:
# data = map(abs, range(-200, 400, 11))
#
# print(count_iterable(data))
#
# # TEST_5:
# data = filter(lambda x: x % 13, range(101, 982))
#
# print(count_iterable(data))
#
# # TEST_6:
# data = zip('beegeek', 'stepik')
#
# print(count_iterable(data))
#
# # TEST_7:
# data = zip('', '')
#
# print(count_iterable(data))
#
# # TEST_8:
# data = filter(None, range(100_000_001))
#
# print(count_iterable(data))


# def all_together(*args):
#     return (j for i in args for j in i)



# # INPUT DATA:

# # TEST_1:
# objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]

# print(*all_together(*objects))

# # TEST_2:
# objects = [[1, 2, 3], [(0, 0), (1, 1)], {'geek': 1}]

# print(*all_together(*objects))

# # TEST_3:
# print(list(all_together()))

# # TEST_4:
# objects = [iter('bee'), [[1, 2], [3, 4], [5, 6]], {'geek': 1, 'bee': 2}]

# print(*all_together(*objects))

# # TEST_5:
# _map = map(str.upper, 'beegeek')
# _filter = filter(str.islower, 'BEEgeek')
# _zip = zip('bee', '123')

# print(*all_together(_map, _filter, _zip))

# # TEST_6:
# _map = map(str.upper, 'stepik')
# _filter = filter(str.islower, 'beeGEEK')
# _zip = zip('zip', '321')
# _reversed = reversed([1, 2, 3, 4])
# _enumerate = enumerate('bee')

# print(*all_together(_map, _filter, _zip, _reversed, _enumerate))



# def interleave(*args):
#     return (j for i in zip(*args) for j in i)
#
#
#     # for i in zip(*args):
#     #     for j in i:
#     #         yield j
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# print(*interleave('bee', '123'))
#
# # TEST_2:
# numbers = [1, 2, 3]
# squares = [1, 4, 9]
# qubes = [1, 8, 27]
#
# print(*interleave(numbers, squares, qubes))
#
# # TEST_3:
# numbers1 = tuple(range(10))
# numbers2 = list(range(10, 20))
# numbers3 = tuple(range(20, 30))
# numbers4 = tuple(range(30, 40))
#
# print(*interleave(numbers1, numbers2, numbers3, numbers4))
#
# # TEST_4:
# string = str(range(10, 50))
#
# print(*interleave(string))
#
# # TEST_5:
# numbers1 = tuple(range(38, 99, 7))
# numbers2 = tuple(range(65, 114, 6))
# string1 = 'BEEGEEKbe'
# string2 = 'STEPIKste'
# numbers3 = list(range(1, 170, 19))
# numbers4 = list(range(2, 175, 20))
#
# print(*interleave(numbers3, string2, numbers4, string1, numbers2, numbers1))



# from collections import namedtuple
#
# Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])
#
# persons = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
#            Person('Goran Aslin', 'Swedish', 'male', 1980, 0),
#            Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
#            Person('Genevieve Asse', 'French', 'female', 1949, 0),
#            Person('Irene Adler', 'Swedish', 'female', 2005, 0),
#            Person('Sergio Asti', 'Italian', 'male', 1926, 0),
#            Person('Olof Backman', 'Swedish', 'male', 1999, 0),
#            Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
#            Person('Dana Atchley', 'American', 'female', 1941, 2000),
#            Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
#            Person('Shura_Stone', 'Russian', 'male', 2000, 0),
#            Person('Jon Bale', 'Swedish', 'male', 2000, 0)]
#
#
# alive = (i for i in persons if i.death == 0)
# man = (i for i in alive if i.sex == 'male')
# national = (i for i in man if i.nationality == 'Swedish')
# result = max((i for i in national), key=lambda x: x.birth)
#
# print(result.name)


# def parse_ranges(ranges):
#     for range_str in ranges.split(','):
#         a, b = map(int, range_str.split('-'))
#         for number in range(a, b + 1):
#             yield number
#
#
#
# def parse_ranges(ranges):
#     return (j
#             for i in ranges.split(',')
#             for a, b in [i.split('-')]
#             for j in range(int(a), int(b) + 1))
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# print(*parse_ranges('1-2,4-4,8-10'))
#
# # TEST_2:
# print(*parse_ranges('1-10,2-10'))
#
# # TEST_3:
# print(*parse_ranges('7-32'))
#
# # TEST_4:
# print(*parse_ranges('8-8,8-8,8-8,8-8,8-8'))
#
# # TEST_5:
# print(*parse_ranges('10-10,11-11,12-12'))
#
# # TEST_6:
# print(*parse_ranges('10-15,1-4,4-5,5-5,1-10,1-15'))
#
# # TEST_7:
# numbers = parse_ranges('1-3')
#
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
#
# # TEST_8:
# numbers = parse_ranges('1-3,4-5,10-32,32-32,32-40,1-2,2-32,10-11,67-199')
#
# print(*numbers)

#
# def filter_names(names: list, ignore_char: str, max_names: int):
#     start_char = (i for i in names if i[0].lower() != ignore_char.lower())
#     consist_of_digit = (i for i in start_char if not any(j.isdigit() for j in i))
#     return (i[0] for i in zip(consist_of_digit, range(max_names)))
#
#
# def filter_names(names, ignore_char, max_names):
#     ignore_char = ignore_char.lower()
#     filtred_char = (name for name in names if not name.lower().startswith(ignore_char))
#     filtred_dig = (name for name in filtred_char if name.isalpha())
#     return (name for idx, name in enumerate(filtred_dig) if idx < max_names)
#
#
# def filter_names(names, char, n):
#     for i in names:
#         if i[0].lower() != char.lower() and i.isalpha() and n:
#             yield i
#             n -= 1
#
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
#
# print(*filter_names(data, 'D', 3))
#
# # TEST_2:
# data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
#
# print(*filter_names(data, 't', 20))
#
# # TEST_3:
# data = ['Di6ma', 'Ti4mur', 'Ar5thur', 'Anri7620', 'Ar3453ina', '345German', 'Ruslan543', 'Soslanfsdf123', 'Geo000000r']
#
# print(*filter_names(data, 'A', 100))
#
# # TEST_4:
# data = ['Arthur', 'Anri', 'Arina', 'Albert', 'Angel', 'Ariel']
#
# print(*filter_names(data, 'F', 6))
#
# # TEST_5:
# data = ['Arthur', 'Anri', 'Arina', 'Albert', 'Angel', 'Ariel']
#
# print(*filter_names(data, 'A', 22))
#
# # TEST_6:
# data = ['Arthur', 'Anri', 'Arina', 'Albert', 'Angel', 'Ariel']
#
# print(next(filter_names(data, 'R', 1)))
#
# # TEST_7:
# data = ['Barry']
#
# print(*filter_names(data, 'B', 1))
#
# # TEST_8:
# data = ['Dima1', 'Timur2', 'Arthur', 'Anri', 'Arina', '3German', '4Ruslan']
#
# print(*filter_names(data, 'a', 20))
#
# # TEST_9:
# data = ['Dima', 'Timur2', 'Arthur', 'Anri', 'Arina', '3German', '4Ruslan']
#
# print(*filter_names(data, 'A', 1))
#
# # TEST_10:
# data = ['1Dima', 'Timur2', 'Arthur', 'Anri', 'Arina', '3German', 'Ruslan']
#
# print(*filter_names(data, 'A', 1))
#
# # TEST_11:
# data = []
#
# print(list(filter_names(data, 'B', 1)))
#
# # TEST_12:
# data = ['Dima', 'Timur', 'Arthur', 'Anri', 'Arina', 'German', 'Ruslan', 'Roma5', 'Jenya', 'Anna']
#
# print(*filter_names(data, 'A', 8))



# with open('data_n.csv', 'r', encoding='utf-8') as file:
#     file_lines = (line for line in file)
#     line_values = (line.rstrip().split(',') for line in file_lines)
#     file_headers = next(line_values)
#     line_dicts = (dict(zip(file_headers, data)) for data in line_values)
#     r_a = (i for i in line_dicts if i['round'] == 'a')
#     result = (int(i['raisedAmt']) for i in r_a)
#     print(sum(result))

# from datetime import date, datetime
#
# def years_days(y: int):
#     first_date = date(year=y, month=1, day=1)
#     last_date = date(year=y, month=12, day=31)
#     return (date.fromordinal(i) for i in range(first_date.toordinal(), last_date.toordinal() + 1))
#
# from datetime import date, timedelta
# from calendar import isleap
#
# def years_days(year):
#     n_days = 365 + isleap(year)
#     return (date(year, 1, 1) + timedelta(days=i) for i in range(n_days))
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# dates = years_days(2022)
#
# print(next(dates))
# print(next(dates))
# print(next(dates))
# print(next(dates))
#
# # TEST_2:
# dates = years_days(2077)
#
# print(*dates)
#
# # TEST_3:
# dates = years_days(2000)
#
# print(*dates)
#
# # TEST_4:
# dates = years_days(1900)
#
# print(*dates)

# def nonempty_lines(file):
#     with open(file, 'r', encoding='utf-8') as f:
#         for line in f:
#             line = line.strip('\n')
#             if line:
#                 if len(line) > 25:
#                     yield '...'
#                 else:
#                     yield line
#
#
# def nonempty_lines(file):
#     with open(file, encoding='utf-8') as f:
#         yield from ('...' if len(i.strip()) > 25 else i.strip() for i in f if i.strip() != '')
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# lines = nonempty_lines('file1.txt')
#
# print(next(lines))
# print(next(lines))
# print(next(lines))
# print(next(lines))
#
# # TEST_2:
# print(*nonempty_lines('file2.txt'))
#
# # TEST_3:
# print(*nonempty_lines('file3.txt'))
#
# # TEST_4:
# print(*nonempty_lines('file4.txt'))
#
# # TEST_5:
# print(*nonempty_lines('file5.txt'))


# def txt_to_dict():
#     with open('planets.txt', 'r', encoding='utf-8') as file:
#         d = {}
#         file_lines = (line.strip().split(' = ') for line in file)
#         for line in file_lines:
#             if line !=['']:
#                 d[line[0]] = line[1]
#             else:
#                 yield d
#                 d = {}
#         yield d
#
#
# def txt_to_dict():
#     with open('planets.txt', 'r', encoding='utf-8') as file:
#         items = (i.split('\n') for i in file.read().split('\n\n'))
#         return (dict(i.split(' = ') for i in planet) for planet in items)
#
# def txt_to_dict():
#     with open('planets.txt', encoding='utf-8') as fi:
#         # генератор объектов вида:
#         # ['Name = Mercury', 'Diameter = 4879.4', 'Mass = 3.302×10^23', 'OrbitalPeriod = 0.241']
#         planets = (planet.split('\n') for planet in fi.read().split('\n\n'))
#
#         # генератор объектов вида:
#         # [['Name', 'Mercury'], ['Diameter', '4879.4'], ['Mass', '3.302×10^23'], ['OrbitalPeriod', '0.241']]
#         planets_info = ((p.split(' = ') for p in planet) for planet in planets)
#
#     # преобразование объектов генератора в словари согласно условию
#     for planet in planets_info:
#         yield dict(planet)
#
#
#
#
# # print(*txt_to_dict())
#
# # INPUT DATA:
#
# # TEST_1:
# planets = txt_to_dict()
#
# print(next(planets))
#
# # TEST_2:
# planets = txt_to_dict()
#
# print(*planets)


# from collections import Counter
# def unique(iterable):
#     c = Counter(iterable)
#     return (i for i in c)
#
# # INPUT DATA:
#
# # TEST_1:
# numbers = [1, 2, 2, 3, 4, 5, 5, 5]
#
# print(*unique(numbers))
#
# # TEST_2:
# iterator = iter('111222333')
# uniques = unique(iterator)
#
# print(next(uniques))
# print(next(uniques))
# print(next(uniques))
#
# # TEST_3:
# data = map(abs, range(-100, 100))
#
# print(*unique(data))
#
# # TEST_4:
# data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')
#
# print(*unique(data))
#
# # TEST_5:
# data = 'JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'
#
# print(*unique(data))
#
# # TEST_6:
# data = map(str.lower, 'STEPIK')
#
# print(*unique(data))
#
# # TEST_7:
# data = map(str.lower, 'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')
#
# print(*unique(data))
#
# # TEST_8:
# data = ['bee', 'geek', 'stepik', 'python']
#
# print(*unique(data))
#
# # TEST_9:
# print(list(unique([])))

# def stop_on(iterable, obj):
#     i_o = (i for i in iterable)
#     for i in i_o:
#         if i != obj:
#             yield i
#         else:
#             break
#
#
# def stop_on(iterable, obj):
#     it = iter(iterable)
#     return iter(lambda: next(it), obj)
#
#
# # INPUT DATA:
#
# # TEST_1:
# numbers = [1, 2, 3, 4, 5]
#
# print(*stop_on(numbers, 4))
#
# # TEST_2:
# iterator = iter('beegeek')
#
# print(*stop_on(iterator, 'a'))
#
# # TEST_3:
# data = map(abs, range(-100, 100))
#
# iterator = stop_on(data, 76)
#
# print(*iterator)
#
# # TEST_4:
# data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')
#
# iterator = stop_on(data, 'o')
#
# print(*iterator)
#
# # TEST_5:
# data = 'JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'
#
# iterator = stop_on(data, 'e')
#
# print(*iterator)
#
# # TEST_6:
# data = 'g'
#
# iterator = stop_on(data, 'g')
#
# print(*iterator)
#
# # TEST_7:
# data = 'eeeeeeeeeeeeee'
#
# iterator = stop_on(data, 'e')
#
# print(*iterator)
#
# # TEST_8:
# data = iter('qweretqwewerqweqwerewr')
#
# iterator = stop_on(data, 'H')
#
# print(*iterator)
#
# # TEST_9:
# data = iter('beegeek')
#
# iterator = stop_on(data, 'g')
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
# try:
#     print(next(iterator))
# except StopIteration:
#     print('Error')
#
# # TEST_10:
# data = ['bee', 'geek', 'stepik', 'python']
#
# print(*stop_on(data, 'stepik'))
#
# # TEST_11:
# data = []
#
# print(list(stop_on(data, 'stepik')))


# from copy import deepcopy
#
# def with_previous(iterable, prev=None):
#     it_prev = [prev] + list(deepcopy(iterable))
#     return (i for i in zip(iterable, it_prev))
#
#
# def with_previous(iterable):
#     prev_elem = None
#     for elem in iterable:
#         yield elem, prev_elem
#         prev_elem = elem
#
#
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# numbers = [1, 2, 3, 4, 5]
#
# print(*with_previous(numbers))
#
# # TEST_2:
# iterator = iter('stepik')
#
# print(*with_previous(iterator))
#
# # TEST_3:
# print(*with_previous(map(abs, range(-100, 100))))
#
# # TEST_4:
# print(*with_previous(map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')))
#
# # TEST_5:
# print(*with_previous('JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'))
#
# # TEST_6:
# print(*with_previous('A'))
#
# # TEST_7:
# print(*with_previous('AB'))
#
# # TEST_8:
# gen = with_previous(['bee', 'geek', 'stepik', 'python'])
#
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# # TEST_9:
# print(list(with_previous('')))

# from copy import deepcopy
#
# def pairwise(iterable, last=None):
#     it_prev = list(deepcopy(iterable))[1:] + [last]
#     return (i for i in zip(iterable, it_prev))


# def pairwise(iterable):
#     it = iter(iterable)
#     i = next(it, None)
#     while i != None:
#         i, prev = next(it, None), i
#         yield prev, i



# INPUT DATA:

# TEST_1:
# numbers = [1, 2, 3, 4, 5]
#
# print(*pairwise(numbers))
#
# # TEST_2:
# iterator = iter('stepik')
#
# print(*pairwise(iterator))
#
# # TEST_3:
# print(list(pairwise([])))
#
# # TEST_4:
# data = map(abs, range(-100, 100))
#
# print(*pairwise(data))
#
# # TEST_5:
# data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')
#
# print(*pairwise(data))
#
# # TEST_6:
# data = 'JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'
#
# print(*pairwise(data))
#
# # TEST_7:
# iterator = pairwise('A')
#
# print(next(iterator))
#
# # TEST_8:
# data = ['bee', 'geek', 'stepik', 'python']
#
# print(*pairwise(data))

# def with_previous(iterable):
#     prev_elem = None
#     for elem in iterable:
#         yield elem, prev_elem
#         prev_elem = elem

# def pairwise(iterable):
#     it = iter(iterable)
#     i = next(it, None)
#     while i != None:
#         i, prev = next(it, None), i
#         yield prev, i

# def around(iterable):
#     prev_elem = None
#     it = iter(iterable)
#     i = next(it, None)
#     while i != None:
#         i, elem = next(it, None), i
#         yield prev_elem, elem, i
#         prev_elem = elem
#
#
# def around(iterable):
#     it = iter(iterable)
#     a = None
#     b = next(it, None)
#     c = next(it, None)
#     while b != None:
#         yield a, b, c
#         a, b, c = b, c, next(it, None)
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# numbers = [1, 2, 3, 4, 5]
#
# print(*around(numbers))
#
# # TEST_2:
# iterator = iter('hey')
#
# print(*around(iterator))
#
# # TEST_3:
# iterator = around(iter('beegeek'))
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
# # TEST_4:
# data = map(abs, range(-100, 100))
#
# print(*around(data))
#
# # TEST_5:
# data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')
#
# print(*around(data))
#
# # TEST_6:
# data = map(str.upper, 'y')
#
# iterator = around(data)
#
# print(next(iterator))
#
# # TEST_7:
# data = map(str.upper, 'yt')
#
# print(*around(data))
#
# # TEST_8:
# data = map(str.upper, 'ytu')
#
# print(*around(data))
#
# # TEST_9:
# data = ['bee', 'geek', 'stepik', 'python']
#
# print(*around(data))
#
# # TEST_10:
# print(list(around([])))



