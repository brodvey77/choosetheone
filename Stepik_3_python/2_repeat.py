

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



def filter_anagrams(word,words):
    fl = []
    for i in words:
        if sorted(list(i)) == sorted(list(word)):
            fl.append(i)
    return(fl)





print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))