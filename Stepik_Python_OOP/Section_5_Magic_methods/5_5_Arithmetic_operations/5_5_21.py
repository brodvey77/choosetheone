class Path:
    def __init__(self, *paths):
        components = []
        for path in paths:
            if isinstance(path, Path):
                components.extend(path.components)
            elif isinstance(path, str):
                if path:
                    components.extend(path.split('/'))
            else:
                return NotImplemented

        self.components = [comp for comp in components if comp]

    def __str__(self):
        return '/'.join(self.components)

    def __repr__(self):
        return f"Path('{self}')"

    def __truediv__(self, other):
        if isinstance(other, Path):
            return Path(str(self), str(other))
        elif isinstance(other, str):
            return Path(str(self), other)
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, str):
            return Path(other, str(self))
        elif isinstance(other, Path):
            return Path(str(other), str(self))
        else:
            return NotImplemented

    def __itruediv__(self, other):
        if isinstance(other, Path):
            self.components.extend(other.components)
            return self
        elif isinstance(other, str):
            if other:
                self.components.extend(other.split('/'))
            return self
        else:
            return NotImplemented



# INPUT DATA:

# TEST_1:
path = Path('home', 'user', 'docs')

print(str(path))
print(repr(path))

# TEST_2:
path = Path(Path('home'), 'user', Path('docs'))

print(path)

# TEST_3:
path = Path('home', 'user') / Path('docs')

print(path)

# TEST_4:
path1 = Path('home')
path2 = Path('user/docs')
path3 = path1 / path2

print(path1)
print(path2)
print(path3)

# TEST_5:
path = Path('home')
path /= 'user'

print(path)

# TEST_6:
path1 = Path('home') / Path('user')
path2 = Path('docs')
path1 /= path2

print(path1)

# TEST_7:
path = Path('home')

print(path.__truediv__(2))
print(path.__itruediv__(5))

# TEST_8:
path1 = Path('home')
path2 = Path('user/docs', Path('books/book.pdf'))
path3 = path1 / path2

print(path3)

# TEST_9:
path = Path('home/user', Path('docs'))
path /= Path('book.pdf')

print(path)

# TEST_10:
print(Path('home') / Path('user') / Path('docs') / Path('book.pdf'))

# TEST_11:
path1 = Path('home', 'user')
path2 = Path('projects', 'python')
path3 = Path('docs', '2025')
path4 = Path('book.pdf')


path_a = path1 / path2
print(path_a)

path_b = path_a / path3
print(path_b)

path_c = path_b / path4
print(path_c)

path_d = Path('var', 'log') / 'system'
print(path_d)

path_d /= Path('kernel')
print(path_d)

combined = Path('tmp', 'files') / '2025' / Path('reports/omg') / 'report.pdf'
print(combined)

seq_path = Path('home', 'user')
seq_path /= Path('downloads', 'photos')
print(seq_path)

seq_path /= 'vacation'
print(seq_path)

seq_path /= Path('2025', 'summer', 'trip.jpg')
print(seq_path)

# TEST_12:
path = Path('home')
id1 = id(path)

path /= 'user'
id2 = id(path)

print(id1 == id2)



!s - вызывает str() (по умолчанию)

!r - вызывает repr()

!a - вызывает ascii()


class Path:
    def __init__(self, *parts):
        parts = (str(part) for part in parts)
        self._path = '/'.join(parts)

    def __str__(self):
        return self._path

    def __repr__(self):
        return f'{self.__class__.__name__}({self._path!r})'

    def __truediv__(self, other):
        if isinstance(other, self.__class__ | str):
            return self.__class__(self._path, other)

        return NotImplemented

    def __itruediv__(self, other):
        if isinstance(other, self.__class__ | str):
            self._path += '/' + str(other)
            return self

        return NotImplemented




