# iterate

# iterable objects

number_list = [1, 2, 3, 4, 5]

# for number in number_list:
#     print(number)
#
# for letter in 'my string':
#         print(letter)

# iterators

number_list_iterator = iter(number_list)
print(type(number_list_iterator))

string_iterator = iter('my string')
print(type(string_iterator))

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

def my_for_loop(iterable):
    iterator = iter(iterable)

    while True:
        try:
            print(iterator.__next__())
        except StopIteration:
            print('iteration is finished')
            break

my_for_loop('bugagaga')
my_for_loop([1, 2, 3, 4, 5])





