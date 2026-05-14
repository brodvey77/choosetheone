from random import shuffle
class RandomLooper:
    def __init__(self, *args):
        self.collection = iter([i for arg in args for i in arg])

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.collection)




randomlooper = RandomLooper(['red', 'blue', 'green', 'purple'])

answer = [next(randomlooper) for _ in range(4)]
print(answer)


import itertools as it
import random


class RandomLooper:
    def __init__(self, *args):
        self.iterables = list(it.chain(*args))
        self.length = len(self.iterables)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.length:
            raise StopIteration
        self.length -= 1
        ind = random.randint(0, self.length)
        return self.iterables.pop(ind)



from random import shuffle

class RandomLooper:
    def __init__(self, *args):
        self.data = [el for obj in args for el in obj]
        shuffle(self.data)
        self.iterable = iter(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterable)