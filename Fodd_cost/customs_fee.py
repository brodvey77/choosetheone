def customs_fee_tariff(customs_value_ru):
    if customs_value_ru in range(0, 200001):
        return 775
    elif customs_value_ru in range(200001, 450001):
        return 1550
    elif customs_value_ru in range(450001, 1000201):
        return 3100
    elif customs_value_ru in range(1000201, 2700001):
        return 8530
    elif customs_value_ru in range(2700001, 4200001):
        return 12000
    elif customs_value_ru in range(4200001, 5500001):
        return 15500
    elif customs_value_ru in range(5500001, 7000001):
        return 20000
    elif customs_value_ru in range(7000001, 8000001):
        return 23000
    elif customs_value_ru in range(8000001, 9000001):
        return 25000
    elif customs_value_ru in range(9000001, 10000001):
        return 27000
    elif customs_value_ru > 10000000:
        return 30000