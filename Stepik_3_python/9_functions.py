# print(round(3.5))
# print(round(4.5))

# print(bool(['']))
# print(bool([None]))
#
# print(int(2.7))
# print(round(2.7))

# for i in range(ord('a'), ord('z') + 1):
#     print(chr(i))

# def convert(n):
#     a = format(n, 'b')
#     b = format(n, 'o')
#     c = format(n, 'X')
#     return a, b, c
#
#
#
# number = int(input())
#
# print(convert(number))




films = {'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
         'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},
         'Encanto': {'imdb': 7.3, 'kinopoisk': 7.4},
         'The Witcher': {'imdb': 8.2, 'kinopoisk': 7.3},
         'Ghostbusters: Afterlife': {'imdb': 7.3, 'kinopoisk': 8},
         'Harry Potter 20th Anniversary: Return to Hogwarts': {'imdb': 8.1, 'kinopoisk': 8.2},
         'Shingeki no Kyojin': {'imdb': 9.0, 'kinopoisk': 8.3},
         'The Matrix': {'imdb': 8.7, 'kinopoisk': 8.5},
         'The Dark Knight': {'imdb': 9.0, 'kinopoisk': 8.5},
         'The Shawshank Redemption': {'imdb': 9.3, 'kinopoisk': 9.1},
         'Avengers: Endgame': {'imdb': 8.4, 'kinopoisk': 7.7}}

# d = {}
# for k, v in films.items():
#     d[k] = sum(v.values()) / 2
#
# a = min(d.values())
#
# for k, v in d.items():
#     if v == a:
#         print(k)

# result = min(films, key=lambda x: sum(films[x].values()))
# print(result)

# def non_negative_even(numbers):
#     return all(map(lambda x: x >= 0 and x % 2 == 0, numbers))
#
# print(non_negative_even([0, 2, 4, 8, 16]))


# def is_greater(lists, number):
#     return any(map(lambda x: sum(x) > number, lists))
#
#
# data = [[0, 1, 2], [0, 3], [1, 1, 1], [3]]
#
# print(is_greater(data, 3))


# circle_areas = [3.56773, 5.57668, 4.31914, 6.20241, 91.01344, 32.01213]
#
# result1 = list(map(round, circle_areas, [1]*6))         # округляем числа до 1 знака после запятой
# result2 = list(map(round, circle_areas, range(1, 7)))   # округляем числа до 1,2,...,6 знаков после запятой
#
# print(circle_areas)
# print(result1)
# print(result2)