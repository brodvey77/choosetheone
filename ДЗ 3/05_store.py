# -*- coding: utf-8 -*-

# Есть словарь кодов товаров


goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}



for element in goods:
    good = element
    good_code = goods[good]
    good_qty = 0
    good_price = 0
    for i in store[good_code]:
        good_qty = i['quantity']
        good_price = i['price'] * good_qty
        print(good, 'Количество', good_qty, 'шт. Стоимость', good_price, 'руб')









