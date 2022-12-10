

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



def same_parity(numbers):
    if numbers == []:
        new_numbers = []
    if numbers[0] % 2 == 0:
        new_numbers = filter(lambda x: x % 2 == 0, numbers)
    else:
        new_numbers = filter(lambda x: x % 2 != 0, numbers)
    return list(new_numbers)

print(same_parity([6, 0, 67, -7, 10, -20]))

