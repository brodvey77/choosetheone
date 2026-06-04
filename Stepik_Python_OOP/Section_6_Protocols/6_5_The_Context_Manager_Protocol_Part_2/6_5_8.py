
class Reloopable:
    def __init__(self, file):
        self.file = file


    def __enter__(self):
        return self.file.readlines()


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def __iter__(self):
        return iter(self.file)


with open('file.txt', 'w') as file:
    pass

file = open('file.txt')
print(file.closed)

with Reloopable(file) as reloopable:
    pass

print(file.closed)


class Reloopable:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.file.close()

    def __iter__(self):
        self.file.seek(0)
        yield from self.file
