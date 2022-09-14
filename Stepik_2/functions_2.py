# def matrix(n=1, m=None, value=0):
#     if m == None:
#         m = n
#     return [[value for i in range(m)] for j in range(n)]


# def f(n=3):
#     return n + 7
#
#
# print(f(f(f())))

# def func(*args):
#     return max(args) + min(args)
#
#
# print(func(10, 15, *[31, 42, 5, 1], *(17, 28, 19, 100), 13, 12))

# def count_args(*args):
# #     return len(args)
# #
# # print(count_args([], (''), 'a', 12, False))

import math
# def sq_sum(*args):
#     return sum([i**2 for i in args])
#
# print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def mean(*args):
    l = [i for i in args if type(i) == int or type(i) == float]
    if len(l) == 0:
        return 0.0
    else:
        return sum(l)/len(l)



print(mean())