

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except:
        return False


def is_iterator(obj):
    if hasattr(obj, '__next__'):
        return True
    else:
        return False


print(is_iterator(123))
print(is_iterator([1, 2, 3]))
print(is_iterator((1, 2, 3)))
print(is_iterator('123'))
print(is_iterator(iter('123')))
print(is_iterator(map(int, '123')))


from collections.abc import Iterator, Iterable


def is_iterable(obj):
    return isinstance(obj, Iterable)


def is_iterator(obj):
    return isinstance(obj, Iterator)