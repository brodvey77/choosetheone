

# def hide_card(card_number):
#     card_number = card_number.replace(' ', '')
#     return '*'*8+card_number[12:]
#
# card = '3456 9012 5678 1234'
#
# print(hide_card(card))
#
#
# def hide_card(card):
#     return '*' * 12 + card.replace(' ', '')[-4:]



# def same_parity(numbers):
#     if numbers == []:
#         new_numbers = []
#     if numbers[0] % 2 == 0:
#         new_numbers = filter(lambda x: x % 2 == 0, numbers)
#     else:
#         new_numbers = filter(lambda x: x % 2 != 0, numbers)
#     return list(new_numbers)

# print(same_parity([6, 0, 67, -7, 10, -20]))



# def print_given(*args, **kwargs):
#     for i in args:
#         print(i, type(i))
#     for k,v in sorted(kwargs.items()):
#         print(k, v, type(v))

# print_given()

# def convert(string):
#     c1 = 0
#     c2 = 0
#     for i in string:
#         if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#             c1 += 1
#         if i in 'abcdefghijklmnopqrstuvwxyz':
#             c2 += 1
#     if c2 > c1:
#         return string.lower()
#     if c1 > c2:
#         return string.upper()
#     else:
#         return string.lower()


# def convert(text):
#     lower_count = len(list(filter(str.islower, text)))
#     upper_count = len(list(filter(str.isupper, text)))
#     if lower_count >= upper_count:
#         return text.lower()
#     return text.upper()


# def convert(string):
#     if sum(1 if c.isupper() else -1 for c in string if c.isalpha()) > 0:
#         return string.upper()
#     return string.lower()

# print(convert('BEEgeek'))
# print(convert('pyTHON'))
# print(convert('pi31415!'))



# def filter_anagrams(word,words):
#     fl = []
#     for i in words:
#         if sorted(list(i)) == sorted(list(word)):
#             fl.append(i)
#     return(fl)


# def filter_anagrams(word, anagrams):
#     return(list(filter(lambda x: sorted(x) == sorted(word), anagrams))) 


# print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))



# def likes(names):
#     if len(names) == 0:
#         return 'Никто не оценил данную запись'
#     if len(names) == 1:
#         return names[0] + ' оценил(а) данную запись'
#     if len(names) == 2:
#         return names[0]+ ', ' + names[1] + ' оценили данную запись'
#     if len(names) == 3:
#         return names[0]+ ', ' + names[1]+ ' и ' + names[2] + ' оценили данную запись'
#     if len(names) > 3:
#         c = len(names) - 2
#         return f'{names[0]}, {names[1]} и {c} других оценили данную запись'

        




# print(likes([]))
# print(likes(['Тимур']))
# print(likes(['Тимур', 'Артур']))
# print(likes(['Тимур', 'Артур', 'Руслан']))
# print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
# print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
# print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))


def index_of_nearest(numbers, number):
    if len(numbers) < 1:
        return -1
    return numbers.index(min(numbers, key=lambda x: abs(x - number)))


print(index_of_nearest([], 17)) #-1
print(index_of_nearest([7, 13, 3, 5, 18], 0)) #2
print(index_of_nearest([9, 5, 3, 2, 11], 4)) #1
print(index_of_nearest([7, 5, 4, 4, 3], 4)) #2
print(index_of_nearest([6, 100, 101, 2], 4)) #0
print(index_of_nearest([734234423423423, 5343423423546463423, 934234423423423423, -1], 0)) #3
print(index_of_nearest([1, 14, 100, 65, 6], 5)) #4
print(index_of_nearest([10, 164, 100, 265, 16], 8)) #0
print(index_of_nearest([10, 99, 0, -12, 16], -9)) #3
print(index_of_nearest([1, 1, 1, 1, 1], 1)) #0