# iterate

# iterable objects

# number_list = [1, 2, 3, 4, 5]

# for number in number_list:
#     print(number)
#
# for letter in 'my string':
#         print(letter)

# iterators

# number_list_iterator = iter(number_list)
# print(type(number_list_iterator))
#
# string_iterator = iter('my string')
# print(type(string_iterator))

# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())

# print(string_iterator.__next__())
# print(string_iterator.__next__())
# print(string_iterator.__next__())
# print(string_iterator.__next__())
# print(string_iterator.__next__())

# print(next(number_list_iterator))
# print(next(number_list_iterator))
# print(next(number_list_iterator))

# def my_for_loop(iterable):
#     iterator = iter(iterable)
#
#     while True:
#         try:
#             print(iterator.__next__())
#         except StopIteration:
#             print('iteration is finished')
#             break
#
# my_for_loop('bugagaga')
# my_for_loop([1, 2, 3, 4, 5])

# custom iterable

# for number in range(1, 10):
#     print(number)

# class MyRange:
#     def __init__(self, start, end):
#         self.strat = start
#         self.end = end
#         self.current = start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current < self.end:
#             number = self.current
#             self.current += 1
#             return number
#         raise StopIteration
#
#
# first_range = MyRange(20, 30)
# for number in first_range:
#     print(number)

# Generators functions

# def my_function(x):
#     return x
#
# print(my_function(4))

# def count_up_to(x):
#     count = 1
#     while count <= x:
#         yield count
#         count += 1
#
#
# print(count_up_to(4))
# counter = count_up_to(4)
# print(counter.__next__())
# print(next(counter))
# print(next(counter))
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())

# counter = count_up_to(10)
# print(list(count_up_to(7)))
#
# # for number in count_up_to(10):
# #     print(number)
# counter.__next__()
# counter.__next__()
# counter.__next__()
#
# for number in counter:
#     print(number)

# Infinite process

# def create_patterns():
#     max_patterns = 100
#     patterns = ('first', 'second', 'third', 'forth')
#     i = 0
#     result_list = []
#     while len(result_list) < max_patterns:
#         if i >= len(patterns):
#             i = 0
#         result_list.append(patterns[i])
#         i += 1
#     return result_list
#
# print(create_patterns())

# def get_current_pattern():
#     patterns = ('first', 'second', 'third', 'forth')
#     i = 0
#     while True:
#         if i >= len(patterns):
#             i = 0
#         yield patterns[i]
#         i += 1
#
# current_pattern = get_current_pattern()
# print(next(current_pattern))
# print(next(current_pattern))
# print(next(current_pattern))
# print(next(current_pattern))
# print(next(current_pattern))
# print(next(current_pattern))
# print(next(current_pattern))

# def get_number_from_range():
#     for number in range(10):
#         yield  number
#
# counter = get_number_from_range()
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# counter1 = (number for number in range(10))
#
# print(next(counter1))
# print(next(counter1))
# print(next(counter1))
# print(next(counter1))
# print(next(counter1))
# print([number for number in range(10)])

# print(sum([number for number in range(10)]))
# print(sum(number for number in range(10)))
# import time
#
# list_start_time = time.time()
# print(sum([number for number in range(10000000)]))
# list_processing_time = time.time() - list_start_time
#
# gen_start_time = time.time()
# print(sum(number for number in range(10000000)))
# gen_processing_time = time.time() - gen_start_time
#
# print(f'Processing with list is {list_processing_time}')
# print(f'Processing with generator is {gen_processing_time}')

# def get_week_day():
#     days_of_week =['Sunday', 'Monday', 'Tuesday', 'Wednesday',
#                    'Thursday', 'Friday', 'Saturday']
#     i = 0
#     while True:
#         if i >= len(days_of_week):
#             i = 0
#         yield days_of_week[i]
#         i += 1
#
# current_day = get_week_day()
# print(next(current_day))
# print(next(current_day))
# print(next(current_day))
# print(next(current_day))
# print(next(current_day))
# print(next(current_day))
# print(next(current_day))

# def get_week_day():
#     days_of_week =['Sunday', 'Monday', 'Tuesday', 'Wednesday',
#                    'Thursday', 'Friday', 'Saturday']
#     for day in days_of_week:
#         yield day


# def even_odd():
#     value = 'even'
#     while True:
#         yield value
#         if value == 'even':
#             value = 'odd'
#         else:
#             value = 'even'
#
#
# even_odd_generator = even_odd()
# print(next(even_odd_generator))
# print(next(even_odd_generator))
# print(next(even_odd_generator))
# print(next(even_odd_generator))
# print(next(even_odd_generator))
# print(next(even_odd_generator))
# print(next(even_odd_generator))


def get_infinite_square_generator():
    number = 1
    while True:
        yield number * number
        number += 1

infinite_square_generator = get_infinite_square_generator()
print(infinite_square_generator.__next__())
print(infinite_square_generator.__next__())
print(infinite_square_generator.__next__())
print(infinite_square_generator.__next__())
print(infinite_square_generator.__next__())
print(infinite_square_generator.__next__())
print(infinite_square_generator.__next__())
print(infinite_square_generator.__next__())
print(infinite_square_generator.__next__())
print(infinite_square_generator.__next__())
print(infinite_square_generator.__next__())

