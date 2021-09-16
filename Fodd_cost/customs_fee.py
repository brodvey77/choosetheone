from start import cost_of_invoice, cost_of_transport_to_board,cource_of_eur
from insurance import insurance

customs_value_ru = cost_of_invoice + cost_of_transport_to_board


def customs_fee_tariff():
    if customs_value_ru in range(0, 200001):
        customs_fee = 775
        return customs_fee
    elif customs_value_ru in range(200001, 450001):
        customs_fee = 1550
        return customs_fee
    elif customs_value_ru in range(450001, 1000201):
        customs_fee = 3100
        return customs_fee
    elif customs_value_ru in range(1000201, 2700001):
        customs_fee = 8530
        return customs_fee
    elif customs_value_ru in range(2700001, 4200001):
        customs_fee = 12000
        return customs_fee
    elif customs_value_ru in range(4200001, 5500001):
        customs_fee = 15500
        return customs_fee
    elif customs_value_ru in range(5500001, 7000001):
        customs_fee = 20000
        return customs_fee
    elif customs_value_ru in range(7000001, 8000001):
        customs_fee = 23000
        return customs_fee
    elif customs_value_ru in range(8000001, 9000001):
        customs_fee = 25000
        return customs_fee
    elif customs_value_ru in range(9000001, 10000001):
        customs_fee = 27000
        return customs_fee
    elif customs_value_ru > 10000000:
        customs_fee = 30000
        return customs_fee


customs_fee_tariff()
