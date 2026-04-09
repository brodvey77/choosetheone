
class Filter:
    def __init__(self, predicate):
        self.predicate = predicate

    def __call__(self, iterable):
        return list(filter(self.predicate, iterable))


more_than_five = Filter(lambda x: x > 5)
numbers = [13, 1, 4, 10, 10, 7]

print(more_than_five(numbers))


