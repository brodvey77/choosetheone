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



