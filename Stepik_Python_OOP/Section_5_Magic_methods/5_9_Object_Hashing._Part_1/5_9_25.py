def limited_hash(left, right, hash_function=hash):
    size = right - left + 1
    
    def wrapper(obj):
        h = hash_function(obj)
        # Циклическое преобразование в диапазон [left, right]
        offset = (h - left) % size
        return left + offset
    
    return wrapper



    def limited_hash(left, right, hash_function=hash):
    def inner_hash_function(x):
        return left + (hash_function(x) - left) % (right - left + 1)
    return inner_hash_function
    