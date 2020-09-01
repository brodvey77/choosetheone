
def customs_fee_tarif(customs_value_ru):
    customs_fee = 0
    if customs_value_ru in range(0, 200001):
        customs_fee = 775
        print(f'Таможенный сбор - {str(customs_fee)} рублей')
    elif customs_value_ru in range(200001, 450001):
        customs_fee = 1550
        print(f'Таможенный сбор - {str(customs_fee)} рублей')
    elif customs_value_ru in range(450001, 1000201):
        customs_fee = 3100
        print(f'Таможенный сбор - {str(customs_fee)} рублей')
    elif customs_value_ru in range(1000201, 2700001):
        customs_fee = 8530
        print(f'Таможенный сбор - {str(customs_fee)} рублей')
    elif customs_value_ru in range(2700001, 4200001):
        customs_fee = 12000
        print(f'Таможенный сбор - {str(customs_fee)} рублей')
    elif customs_value_ru in range(4200001, 5500001):
        customs_fee = 15500
        print(f'Таможенный сбор - {str(customs_fee)} рублей')
    elif customs_value_ru in range(5500001, 7000001):
        customs_fee = 20000
        print(f'Таможенный сбор - {str(customs_fee)} рублей')
    elif customs_value_ru in range(7000001, 8000001):
        customs_fee = 23000
        print(f'Таможенный сбор - {str(customs_fee)} рублей')
    elif customs_value_ru in range(8000001, 9000001):
        customs_fee = 25000
        print(f'Таможенный сбор - {str(customs_fee)} рублей')
    elif customs_value_ru in range(9000001, 10000001):
        customs_fee = 27000
        print(f'Таможенный сбор - {str(customs_fee)} рублей')
    elif customs_value_ru > 10000000:
        customs_fee = 30000
        print(f'Таможенный сбор - {str(customs_fee)} рублей')
  

customs_fee_tarif(98536455)