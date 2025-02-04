
# n = int(input())

# for i in range(n):
#     for j in range(n):
#         print(min(i + 1, j + 1, n - i, n - j), end=' ')
#     print()



# def is_correct_bracket_sequence(sequence):
#     count = 0
#     for char in sequence:
#         count = count + 1 if char == '(' else count - 1
#         if count < 0:
#             return False
#     return count == 0

# print(is_correct_bracket_sequence(input()))


# def inversions(sequence):
#     counter = 0
#     ind = 1
#     for i in sequence:
#         for j in sequence[ind:]:
#             if i > j:
#                 counter += 1
#         ind += 1
#     return counter


# # INPUT DATA:

# # TEST_1:
# sequence = [3, 1, 4, 2]

# print(inversions(sequence))

# # TEST_2:
# sequence = [1, 2, 3, 4, 5]

# print(inversions(sequence))

# # TEST_3:
# sequence = [4, 3, 2, 1]

# print(inversions(sequence))

# # TEST_4:
# sequence = [1, 1, 1, 1, 1, 1]

# print(inversions(sequence))

# # TEST_5:
# sequence = [10, 20, 30, 40, 50, 60, 70, 60]

# print(inversions(sequence))

# # TEST_6:
# sequence = [2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(inversions(sequence))

# # TEST_7:
# sequence = [5, 59, 580, 5701]

# print(inversions(sequence))

# # TEST_8:
# sequence = [1, 2, 5, 3, 4]

# print(inversions(sequence))

# # TEST_9:
# sequence = [1, 2, 10, 3, 4, 9, 5, 6, 8, 7]

# print(inversions(sequence))

# # TEST_10:
# sequence = [39, 955, 78, -732, -870, 496, -959, 642, -848, -666, 737, -348, -220, -575, 434, 281, 447, 104, -189, -549, 724, 687, -969, -913, -797, 1000, -798, 278, -943, 642, -837, 91, -701, -909, 692, 176, -281, 879, -841, -326, -324, -704, -667, -562, 93, -648, -355, -504, 295, 287, -121, 373, 962, 900, 932, -191, -18, 79, 448, 817, 506, 220, 397, 188, -566, 771, 275, 385, 317, 563, 908, 506, 1000, 91, -526, 302, -865, 452, 235, 501, 982, -281, -446, 173, -889, -474, 376, 711, -338, 10, -461, -371, 627, -148, 665, 282, -999, 961, 639, -349, -876, 18, 737, 719, 661, 442, 536, 395, 214, 849, 164, 1, 647, -448, 95, -693, -422, -995, 761, -343, -269, 827, -186, 290, 243, -223, 916, -862, -759, 336, 944, 370, 25, 433, -660, 169, -546, -62, -124, -553, -248, 933, 907, 707, -151, 710, -223, 324, -707, -331, 62, -859, 571, -925, 263, 879, -844, 38, 705, 684, -50, 164, 354, -763, 130, -519, -178, -59, -311, 664, 717, 826, 772, 983, 817, -197, -829, -249, -777, -792, 302, -59, -702, 943, 639, -844, 188, 533, 241, 935, 606, -701, -326, -368, 995, -937, -41, -470, -883, -608, 230, 425, -355, 54, 769, 774, -980, -981, 866, -910, 668, 140, -781, 483, -155, 845, 602, -126, -391, 776, -739, 578, 841, 435, 736, 665, 139, -296, 700, 247, 935, 963, 587, 681, -404, -394, -333, -637, -88, -696, 401, -598, -690, 590, -388, -895, -954, 467, 921, 965, -481, -176, 153, -816, 735, 126, 671, -632, 218, -802, 102, -120, 369, 927, 792, -739, 381, 167, 991, 472, -226, -437, -579, -329, 970, 561, -576, -487, 392, 113, 443, -218, -7, 251, 759, -409, 935, -201, -198, -278, 426, -62, -557, 299, 851, -999, 586, -783, -952, 355, -610, 318, -842, -417, 20, -810, 96, 929, -393, 237, -703, 346, -925, 301, -902, -342, -506, -546, -333, -791, 513, -432, -791, 76, -312, -754, 958, 459, -540, -372, 634, 548, 382, 574, -7, -484, -610, 63, -616, -827, -679, -761, 506, -267, -136, -72, -971, -716, -340, -860, 3, -518, 536, 433, -843, -487, -500, -328, -171, 880, -449, 201, -359, -594, -76, -866, -143, 64, -37, -97, 112, -776, 255, 394, 956, 222, 967, -769, 826, 631, -401, 433, 145, 248, -274, 227, -38, 302, -902, -994, -72, -247, 437, 936, 385, -412, 189, 185, -168, 379, -308, -159, 529, 619, 199, -361, -34, 528, -257, -548, -495, -55, -599, -39, -641, -814, 733, -167, 540, 156, -837, -589, 642, 791, 84, -830, 901, -359, 367, -374, -257, -502, -276, -199, -876, -429, 326, 631, 241, -633, -620, -853, 521, -550, 488, -803, 639, -27, 928, -621, -472, 74, 957, 183, 327, 193, 236, -862, 408, 276, -346, 518, -777, 108, 329, 175, -752, -292, 616, -421, 854, -945, 508, -19, 224, -815, 937, -983, -584, -573, -852, 141, -693, -627, 650, 543, 612, 553, -956, -98, -376, 997, -640, -895, -170, -534, -501, -287, 120, -163, 261, -987, -744, 625, 205, 46, -986, -493, -272, 859, -382, 729, 376, 814, -204, 527, -943, 117, -384, 897, -818, -766, 10, -426, 691, 317, -705, 424, -113, -795, -1, -22, -921, -172, -336, -610, 691, 962, 869, 494, 72, -4, 555, 336, 161, -649, -626, 263, 762, 642, 978, 250, -637, -635, 443, -918, -328, -653, -157, 942, 416, 335, -303, 874, -219, -769, 518, 219, -194, -200, -799, 944, -274, 262, -609, 626, -75, 404, 736, -552, 688, -962, 898, -893, 152, -255, 399, 830, -999, -867, 772, -539, -897, -778, -211, 904, -52, -969, 27, -713, -595, 43, -749, 435, -120, -578, 807, -787, -548, 828, -759, 860, -840, 983, 732, -240, 400, -844, -414, -826, 545, -848, 15, 210, 486, -21, -721, -217, -30, 687, 426, -125, -140, 670, 960, -441, 957, -278, 61, 680, 605, 967, -159, -12, -169, 58, -782, -972, 658, 879, 311, 355, 265, -632, -666, -14, -606, -582, 793, 797, 100, 385, 299, -215, -461, -572, 726, 509, -461, 162, 708, -16, -180, -757, -55, 936, -832, 845, 715, 214, -291, -331, 631, 136, -276, -167, -867, -440, -395, -877, -497, 295, -504, 236, -326, 706, 503, 57, 971, -407, 263, -384, 547, -495, 995, -481, -204, 106, -341, 955, -324, -90, -744, -898, 814, -161, 907, -711, 583, 37, 548, 377, -301, 42, -182, 281, -758, -625, 241, -170, 268, 23, -37, -613, -679, 718, -737, 791, -577, -268, 126, 69, -752, 918, 668, 334, -566, -828, -806, -320, 79, -256, 822, -37, 915, -91, -506, 570, 259, 812, 925, -556, -271, 727, 644, 822, -832, 56, 744, 885, 857, -2, 493, 493, -301, 90, 500, 895, -492, -303, -531, -382, -141, 652, 920, 833, -849, -79, 931, 357, 835, 691, -420, 593, -45, 173, 460, -770, -949, -958, -484, -563, -204, 30, 40, -105, 900, 452, -583, 152, 446, -430, 41, -297, -618, -826, -569, -179, 269, 685, 163, -865, 389, -71, 342, 752, -213, 771, 229, 834, 712, 4, 717, 543, 950, -917, -228, 559, 849, 202, -746, -727, -55, 546, 311, -317, -200, 476, 841, -579, -43, 768, 852, -564, -109, -883, -752, -762, 243, 497, 100, -276, 188, -61, 63, 92, 877, 609, -105, 510, 916, 734, 939, -412, -282, -804, -899, -973, -179, -283, 395, 260, -487, 872, -861, -926, -731, -6, -274, 269, 112, 881, -570, -500, -129, -306, -591, -907, 692, 132, -490, 856, 124, -932, 330, 305, -660, -237, -164, 204, -596, 195, 882, 885, 850, 30, 411, -852, 529, -392, 558, -782, 699, -859, 577, -606, -58, 871, -976, 944, -88, 613, 197, -118, -925, 739, -857, -630, 470, 701, 389, -13, -243, -291, 165, -403, -865, -39, -829, 648, 427, -213, -670, 804, -344, 35, -66, 3, 156, 727, -260, -24, -500, -23, 584, -798, -499, 700, 621, 668, -543, -366, 546, -286, 836, -602, 590, 555, -830, 22, 705, 747, 230, -277, -433, -413, -537, 870, 394, 481, 938, 885, -457, -830, 267, -851, -791, -454, -528, -914]

# print(inversions(sequence))


# class Car:
#     pass



# setattr(Car, 'model', 'Тойота')
# setattr(Car, 'color', 'Розовый')
# setattr(Car, 'number', 'П111УУ77')

# print(Car.__dict__['color'])



# class Car:
#     pass
# d = {
#     'model': "Тойота",
#     'color': "Розовый",
#     'number': "О111АА77"
# }
# [setattr(Car,k,v) for k,v in d.items()]

# print(Car.__dict__['color'])



# class Notes:
#     uid = 1005435
#     title = "Шутка"
#     author = "И.С. Бах"
#     pages = 2


# print(getattr(Notes, 'author'))


# class Dictionary:
#     rus = "Питон"
#     eng = "Python"


# print(getattr(Dictionary, 'rus_word', False))


# class TravelBlog:
#     total_blogs = 0


# tb1 = TravelBlog()

# setattr(tb1, 'name', 'Франция')
# setattr(tb1, 'days', 6)


# setattr(TravelBlog, 'total_blogs', 2)


# tb2 = TravelBlog()
# setattr(tb2, 'name', 'Италия')
# setattr(tb2, 'days', 5)

# setattr(TravelBlog, 'total_blogs', 3)

# print(tb1.__dict__)
# print(tb2.__dict__)
# print(TravelBlog.__dict__)

class Figure:
    type_fig = 'ellipse'
    color = 'red'


fig1 = Figure()

fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'

del fig1.color

for k,v in fig1.__dict__.items():
    print(k, end=' ')