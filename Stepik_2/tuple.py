# my_tuple = (3,5,4,6,1,2,7)
#
# my_tuple_1 = tuple(sorted(my_tuple))
#
# my_tuple_2 = tuple(reversed(my_tuple_1))

# numbers = ((0, (9, 2)), (1, (4, 6, 3), (5, 2, 3), 8, 3))
# print(numbers[0][1][1])
#
# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
# last = countries[-1]
# print(last)

# numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
# minimal = min(numbers)
# maximal = max(numbers)
# print(minimal + maximal)

# (1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13).

# numbers1 = (1, 2, 3)
# numbers2 = (6,)
# numbers3 = (7, 8, 9, 10, 11, 12, 13)
#
# print((numbers1 * 2) + (numbers2 * 9) + numbers3)

# city_name = input()
# city_year = int(input())
# city = city_name, city_year
# print(city)

# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# non_empty_tuples = [i for i in tuples if len(i) > 0]
#
# print(non_empty_tuples)

# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
# new_tuples = [i[-1] for i in tuples]
# print(new_tuples)


# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
#
# new_tuples = [i[:-1] + (100,) for i in tuples]
#
# print(new_tuples)



