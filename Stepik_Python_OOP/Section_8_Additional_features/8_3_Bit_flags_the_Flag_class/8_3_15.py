from enum import Flag, auto

class MovieGenres(Flag):
    ACTION = auto()
    COMEDY = auto()
    DRAMA = auto()
    FANTASY = auto()
    HORROR = auto()


class Movie:
    def __init__(self, name, genres):
        self.name = name
        self.genres = genres

    def in_genre(self, ganr):
        if ganr in self.genres:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.name}'



# movie = Movie('The Lord of the Rings', MovieGenres.ACTION | MovieGenres.FANTASY)
#
# print(movie)


# movie = Movie('The Lord of the Rings', MovieGenres.ACTION | MovieGenres.FANTASY)
#
# print(movie.in_genre(MovieGenres.FANTASY))
# print(movie.in_genre(MovieGenres.COMEDY))
# print(movie.in_genre(MovieGenres.ACTION | MovieGenres.FANTASY))

# movie = Movie('Scary movie', MovieGenres.COMEDY | MovieGenres.HORROR)
#
# print(movie.in_genre(MovieGenres.FANTASY))
# print(movie.in_genre(MovieGenres.COMEDY))
# print(movie.in_genre(MovieGenres.COMEDY | MovieGenres.HORROR)


# movie = Movie('Avengers', MovieGenres.FANTASY | MovieGenres.ACTION)
#
# print(movie.in_genre(MovieGenres.DRAMA))
# print(movie.in_genre(MovieGenres.ACTION))
# print(movie.in_genre(MovieGenres.FANTASY | MovieGenres.ACTION))
# print(movie)

# movie = Movie('Любовь и голуби', MovieGenres.DRAMA | MovieGenres.COMEDY)
#
# print(movie.in_genre(MovieGenres.DRAMA))
# print(movie.in_genre(MovieGenres.ACTION))
# print(movie.in_genre(MovieGenres.DRAMA | MovieGenres.COMEDY))
# print(movie)


movie = Movie('Scary movie', MovieGenres.COMEDY | MovieGenres.HORROR)

print(movie.in_genre(MovieGenres.FANTASY))
print(movie.in_genre(MovieGenres.COMEDY))
print(movie.in_genre(MovieGenres.COMEDY | MovieGenres.HORROR))


from enum import Flag, auto


class MovieGenres(Flag):
    ACTION = auto()
    COMEDY = auto()
    DRAMA = auto()
    FANTASY = auto()
    HORROR = auto()


class Movie:
    def __init__(self, movie, genres):
        self.movie = movie
        self.genres = genres

    def in_genre(self, genre):
        return genre in self.genres

    def __str__(self):
        return self.movie
