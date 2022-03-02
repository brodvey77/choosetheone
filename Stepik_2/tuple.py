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


# poets = [
#     ('Есенин', 13),
#     ('Тургенев', 14),
#     ('Маяковский', 28),
#     ('Лермонтов', 20),
#     ('Фет', 15)]
#
# for i in range(len(poets)):
#     for j in range(i+1, len(poets)):
#         if poets[i][1] > poets[j][1]:
#             poets[i], poets[j] = poets[j], poets[i]
#
# print(poets[0])
# print(poets[-1])

# poets = [
#     ('Тургенев', 14),
#     ('Есенин', 13),
#     ('Маяковский', 28),
#     ('Фет', 15),
#     ('Лермонтов', 20)]
#
# for i in range(len(poets)):
#     for j in range(i+1, len(poets)):
#         print(poets[i], 'vs', poets[j])
#         if poets[i] > poets[j]:
#             poets[i], poets[j] = poets[j], poets[i]
#
# print(poets[0])
# print(poets[-1])


# numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
#
# temp_num = numbers[0]
#
# for i in range(len(numbers) - 1):
#     temp_num *= numbers[i + 1]
#
# print(temp_num)


# data = 'Python для продвинутых!'
# a = tuple(data)
# print(a)


# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# city = list(poet_data)
# city[2] = 'Москва'
# poet_data = tuple(city)
# print(poet_data)


# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# list_of_numbers = [sum(i) / len(i) for i in numbers]
# print(list_of_numbers)

# a, b, c = int(input()), int(input()), int(input())
#
#
# def get_x(a, b):
#     x = -b / (2 * a)
#     return x
#
#
# def get_y(a, b, c, x):
#     y = a * (x ** 2) + b * x + c
#     return round(y, 2)
#
#
# x = get_x(a, b)
# y = get_y(a, b, c, x)
#
# point = [x, y]
# point = tuple(point)
#
# print(point)

# def parabola_vertex(a, b, c):
#     x = -(b / (2 * a))
#     y = (4 * a * c - b**2) / (4 * a)
#     return x, y
#
#
# print(parabola_vertex(int(input()), int(input()), int(input())))

#      Конкурсный отбор

# n = int(input())
# students = []
#
# for i in range(n):
#     students.append(input().split())
#
# for row in students:
#     print(*row)
#
# print()
#
# for i in students:
#     if i[-1] == '4':
#         print(*i)
#     if i[-1] == '5':
#         print(*i)

# students = [tuple(input().split()) for _ in range(int(input()))]
#
# for student in students:
#     print(*student)
#
# print()
#
# for name, grade in students:
#     if int(grade) > 3:
#         print(name, grade)

# tuple1 = 1,
# tuple2 = 1, 2, 4
#
# print(type(tuple1))
# print(type(tuple2))

# n = int(input())
# f1, f2 = 1, 1
# for i in range(n):
#     print(f1)
#     f1, f2 = f2, f1 + f2

# points = [('матан', 100), ('линал', 98), ('ангем', 90)]
#
# subject, value = points[1]
#
# print(subject, value)


# notes = ('Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si')
#
# do, re, mi, *tail = notes
#
# print(tail)


# notes = ('Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si')
#
# do, re, *tail, si = notes
#
# print(tail)


# n = int(input())
# f1, f2, f3 = 1, 1, 1
#
# for i in range(n):
#     print(f2, end=' ')
#     f1, f2, f3 = f3, f1, f1 + f2 + f3


# tpl = (100, 200, 300, 400, 500)
# print(tpl[-2])
# print(tpl[-4:-1])

# a, *b, c = 'No bees', 'no honey'
# print(b)
