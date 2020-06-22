# from random import randint
#
# class Lemming:
#     pass
#
# total_lemmigs = 0
#
# lemming_1 = Lemming()
# total_lemmigs += 1
# lemming_2 = Lemming()
# total_lemmigs += 1
# lemming_3 = Lemming()
# total_lemmigs += 1
#
# family = []
# family_size = randint(16, 32)
# while len(family) < family_size:
#     new_lemmig = Lemming()
#     family.append(new_lemmig)
#     total_lemmigs += 1
#
# print(total_lemmigs)
from random import randint


class Lemming:
    total = 0

    def __init__(self):
        Lemming.total += 1


burrow = []
burrow_depth = randint(90, 100)
while len(burrow) < burrow_depth:
    family = []
    family_size = randint(16, 32)
    while len(family) < family_size:
        new_lemmig = Lemming()
        family.append(new_lemmig)
    burrow.append(family)

print(Lemming.total)
