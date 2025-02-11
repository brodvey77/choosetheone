
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


# # объявление функции
# def is_correct_bracket(text):
#     while '()' in text:
#         text = text.replace('()', '')
#     return not text

# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_correct_bracket(txt))


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

# class Figure:
#     type_fig = 'ellipse'
#     color = 'red'


# fig1 = Figure()

# fig1.start_pt = (10, 5)
# fig1.end_pt = (100, 20)
# fig1.color = 'blue'

# del fig1.color

# for k,v in fig1.__dict__.items():
#     print(k, end=' ')


# class Person:
#     name = 'Сергей Балакирев'
#     job = 'Программист'
#     city = 'Москва'


# p1 = Person()

# print('job' in p1.__dict__)

# if 'job' in p1.__dict__:
#     print(True)
# else:
#     print(False)


# class Person:
#     name = 'Сергей Балакирев'
#     job = 'Программист'
#     city = 'Москва'
# p1 = Person()
# print(hasattr(p1, p1.job)


# import sys

# pokemons = [pokemon.strip() for pokemon in sys.stdin]
# print(len(pokemons) - len(set(pokemons)))

# import json
# import functools


# def jsonify(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         json_data = json.dumps(func(*args, **kwargs))
#         return json_data
#     return wrapper




# # TEST_1:
# @jsonify
# def make_user(id, live, options):
#     return {'id': id, 'live': live, 'options': options}

# print(make_user(4, False, None))

# # TEST_2:
# @jsonify
# def make_list(n):
#     return list(range(1, n + 1))

# print(make_list(10))

# # TEST_3:
# @jsonify
# def make_str(s1, s2):
#     return (s1 + s2) * 5

# print(make_str('bee', 'geek'))

# # TEST_4:
# @jsonify
# def make_square(num):
#     return num**2

# print(make_square(10))
# print(make_square(10.5))

# # TEST_5:
# @jsonify
# def make_bool(flag):
#     return not flag

# print(make_bool(True))
# print(make_bool(False))

# # TEST_6:
# @jsonify
# def make_None():
#     return None

# print(make_None())

# # TEST_7:
# @jsonify
# def make_tuple():
#     """JSON-Tuple object"""
#     return (1, '2', 3.0, None, False, {'1': True})


# print(make_tuple())
# print(make_tuple.__name__)
# print(make_tuple.__doc__)

# import sys


# data = [i.strip('()\n').split(',') for i in sys.stdin]

# for val in data:
#     if -90 <= eval(val[0]) <= 90 and -180 <= eval(val[1]) <= 180:
#         print(True)
#     else:
#         print(False)

# import sys

# axis = [eval(line.strip()) for line in sys.stdin]
# for x, y in axis:
#     print(-90 <= x <= 90 and -180 <= y <= 180)



# for coords in open(0):
#     latitude, longitude = map(float, coords.strip('\n()').split(', '))
#     print(-90 <= latitude <= 90 and -180 <= longitude <= 180)




# def filterfalse(predicate, iterable):
#     return itertools.filterfalse(predicate, iterable)

# import itertools

# def quantify(iterable, predicate):
#     return len(list(filter(predicate, iterable)))




# # INPUT DATA:

# # TEST_1:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(quantify(numbers, lambda x: x > 1))

# # TEST_2:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(quantify(numbers, lambda x: x % 2 == 0))

# # TEST_3:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(quantify(numbers, lambda x: x < 0))

# # TEST_4:
# iterable = ['dddddd', 'a', 'aa', 'aaa', 'bbbb', 'ccccc']

# print(quantify(iterable, lambda elem: len(elem) > 3))

# # TEST_5:
# iterable = iter(['cdddddd', 'ca', 'caa', 'caaa', 'cbbbb', 'ccccc', 'c'])

# print(quantify(iterable, lambda elem: elem.startswith('c')))

# # TEST_6:
# iterable = iter(['cdddddd', 'ca', 'caa', 'caaa', 'cbbbb', 'ccccc', 'c'])

# print(quantify(iterable, lambda elem: elem.endswith('A')))

# # TEST_7:
# iterable = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# print(quantify(iterable, lambda elem: elem == 1))

# # TEST_8:
# iterable = iter([2, 3, 4, 5, 6, 7, 8, 9, 1])

# print(quantify(iterable, lambda elem: elem == 1))

# # TEST_9:
# iterable = iter([2, 3, 4, 1, 5, 6, 7, 8, 9, 10])

# print(quantify(iterable, lambda elem: elem == 1))

# # TEST_10:
# iterable = iter(['', 1, 0, (), [[]], [], {1: 2}])

# print(quantify(iterable, None))

# import re

# def is_integer(string: str):
#     match = re.fullmatch(r'-?\d+', string)
#     if match:
#         return True
#     else:
#         return False







# # INPUT DATA:

# # TEST_1:
# print(is_integer('199'))

# # TEST_2:
# print(is_integer('-43'))

# # TEST_3:
# print(is_integer('5f'))

# # TEST_4:
# print(is_integer('5.0'))

# # TEST_5:
# print(is_integer('1.1'))

# # TEST_6:
# print(is_integer('1-1'))

# # TEST_7:
# print(is_integer('58593485349483423'))

# # TEST_8:
# print(is_integer('585934853t49483423'))

# # TEST_9:
# print(is_integer('1-2-3'))

# # TEST_10:
# print(is_integer('5-'))

# # TEST_11:
# print(is_integer('-p'))

# # TEST_12:
# print(is_integer('1111111111'))

# # TEST_13:
# print(is_integer('--9'))

# # TEST_14:
# print(is_integer('-0001'))
# print(is_integer('0001'))


# import calendar, datetime
#
# year, mounth = 2012, 3
#
# # start_date = date(year=year, month=mounth, day=1)
# counter = 0
# for i in calendar.monthcalendar(year, mounth):
#     if i[3] != 0:
#         counter += 1
#         if counter == 4:
#             x = datetime.date(day=i[3], month=mounth, year=year)
#
# print(x.strftime('%d.%m.%Y'))


# def is_decimal(string):
#     try:
#         float(string)
#         return True
#     except ValueError:
#         return False
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# print(is_decimal('100'))
#
# # TEST_2:
# print(is_decimal('199.1'))
#
# # TEST_3:
# print(is_decimal('-0.2'))
#
# # TEST_4:
# print(is_decimal('.-95'))
#
# # TEST_5:
# print(is_decimal('-.95'))
#
# # TEST_6:
# print(is_decimal('.10'))
#
# # TEST_7:
# print(is_decimal('.'))
#
# # TEST_8:
# print(is_decimal(''))
#
# # TEST_9:
# print(is_decimal('10..1'))
#
# # TEST_10:
# print(is_decimal('--10.1'))
#
# # TEST_11:
# print(is_decimal('---1.1'))
#
# # TEST_12:
# print(is_decimal('1-.1'))
#
# # TEST_13:
# print(is_decimal('1.-1'))
#
# # TEST_14:
# print(is_decimal('1.1-'))
#
# # TEST_15:
# print(is_decimal('1.1.1'))
#
# # TEST_16:
# print(is_decimal('a.a'))
#
# # TEST_17:
# print(is_decimal('a'))
#
# # TEST_18:
# print(is_decimal('348209348203758348635465'))
#
# # TEST_19:
# print(is_decimal('3482093.48203758348635465'))
#
# # TEST_20:
# print(is_decimal('1-1'))
#
# # TEST_21:
# print(is_decimal('1-1-1'))
#
# # TEST_22:
# strings = ['100.', '349..', '-425.', '-1248..']
# for string in strings:
#     print(is_decimal(string))
#
# # TEST_23:
# print(is_decimal('-0001'))
# print(is_decimal('0001'))
#
# # TEST_24:
# print(is_decimal('0.99.'))
# print(is_decimal('-0.99.'))
# print(is_decimal('.99.'))
# print(is_decimal('-.99.'))

# import re
#
# def is_fraction(string: str) -> bool:
#     if re.fullmatch(r'-?\d+/0*[1-9]\d*', string):
#         return True
#     else:
#         return False
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# print(is_fraction('1000/1'))
#
# # TEST_2:
# print(is_fraction('-54/9'))
#
# # TEST_3:
# print(is_fraction('71'))
#
# # TEST_4:
# print(is_fraction('1/0'))
#
# # TEST_5:
# print(is_fraction(''))
#
# # TEST_6:
# print(is_fraction('/4'))
#
# # TEST_7:
# print(is_fraction('1000'))
#
# # TEST_8:
# print(is_fraction('-987/1'))
#
# # TEST_9:
# print(is_fraction('0/1'))
#
# # TEST_10:
# print(is_fraction('-/56'))
#
# # TEST_11:
# print(is_fraction('1/1234'))
#
# # TEST_12:
# print(is_fraction('2-/4'))
#
# # TEST_13:
# print(is_fraction('3/-7'))
#
# # TEST_14:
# print(is_fraction('5/8-'))
#
# # TEST_15:
# print(is_fraction('--1/2'))
#
# # TEST_16:
# print(is_fraction('-7/3-'))
#
# # TEST_17:
# print(is_fraction('-7-/-3-'))
#
# # TEST_18:
# print(is_fraction('/4/5'))
#
# # TEST_19:
# print(is_fraction('4/5/'))
#
# # TEST_20:
# print(is_fraction('54365486548645/472342935648904709456'))
#
# # TEST_21:
# print(is_fraction('5/2/4'))
#
# # TEST_22:
# print(is_fraction('5/2/4/2'))
#
# # TEST_23:
# print(is_fraction('1000/10'))
#
# # TEST_24:
# print(is_fraction('1000/00001'))
# print(is_fraction('-1000/00001'))
#
# # TEST_25:
# print(is_fraction('1000/00004123'))
# print(is_fraction('1000/0000'))
# print(is_fraction('1000/00000008000'))

# def intersperse(iterable, delimiter):
#     it = iter(iterable)  # Получаем итератор из итерируемого объекта
#     try:
#         yield next(it)  # Первый элемент без разделителя
#     except StopIteration:
#         return  # Если итерируемый объект пуст, завершаем генератор
#
#     for item in it:
#         yield delimiter  # Вставляем разделитель
#         yield item  # Вставляем следующий элемент
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# print(*intersperse([1, 2, 3], 0))
#
# # TEST_2:
# inter = intersperse('beegeek', '!')
# print(next(inter))
# print(next(inter))
# print(*inter)
#
# # TEST_3:
# print(*intersperse('A', '...'))
#
# # TEST_4:
# print(*intersperse(range(5), '>'))
#
# # TEST_5:
# iterable = iter('Beegeek')
#
# print(*intersperse(iterable, '+'))
#
# # TEST_6:
# iterable = iter('Be')
#
# print(*intersperse(iterable, '---'))
#
# # TEST_7:
# print(*intersperse([], 100))
#
# # TEST_8:
# print(*intersperse('beegeek', '   '))
#
# # TEST_9:
# data = intersperse(range(5), -1)
# print(list(data))
#
# # TEST_10:
# data = intersperse(range(5), '!!!')
# print(list(data))
#
# # TEST_11:
# data = intersperse(['John Warner Backus', 5, 'Niklaus Emil Wirth', True, 'Lawrence Gordon Tesler', None, {1, 2, 3}, {'hello': 'world'}], '—')
# print(list(data))
