import math
from pprint import pprint
from api_cbr import cource_of_eur

# Ввод данных
sum_of_specification = input('Введите сумму предложения(евро): ')

# создать функцию выбора по количеству м2

weight_of_specification = input('Введите вес по спецификации(кг): ')
sum_of_transport = input('Введите сумму транспорта за одно авто(евро): ')
# вставка курса евро
exchange_rates = int(cource_of_eur)
sum_of_customs_clearance_ruble = input('Введите стоимость таможенного оформления(в рублях): ')
sum_of_customs_clearance = math.ceil(int(sum_of_customs_clearance_ruble) / exchange_rates)
# print(f'Курс евро по ЦБ с округлением - {exchange_rates} рублей')

# проверка
# print('сумма предложения - ' + sum_of_specification + ' евро')
# print('сумма транспорта - ' + sum_of_transport + ' евро')
# print('Вес по спецификации - ' + weight_of_specification + ' кг')
# print('Стоимость таможенного оформления - ' + sum_of_customs_clearance + ' евро')

# расчет на одно авто
sum_of_trucks = math.ceil(int(weight_of_specification) / 22000)
print(f'Количество авто - {int(sum_of_trucks)} машин')
cost_invoice = math.ceil(int(sum_of_specification) / sum_of_trucks)
print(f'Сумма инвойса - {str(cost_invoice)} евро')
sum_of_insurance = math.ceil(int(cost_invoice) * 0.2 / 100)
print(f'Сумма страховки - {str(sum_of_insurance)} евро')


def print_delimetr():   # функция разделителя
    print('=' * 55)

#  создать функцию выбора процентной ставки

transport_to_board = math.ceil(int(sum_of_transport) * 42 / 100)
print(f'Сумма транспорта до границы с ТС - {str(transport_to_board)} евро')
print_delimetr()

# Расчет таможенной стоимости
customs_value = cost_invoice + transport_to_board + sum_of_insurance
print(f'Таможенная стоимость - {str(customs_value)} евро')
print_delimetr()

# Расчет таможенных платежей
custom_duty = math.ceil(customs_value * 14 / 100)
print(f'Пошлина - {str(custom_duty)}')
vat = math.ceil((customs_value + custom_duty) * 20 / 100)
print(f'НДС - {str(vat)}')


# Расчет таможенного сбора
customs_value_ru = math.ceil(customs_value * exchange_rates)
# print('Таможенная стоимость в рублях - ' + str(customs_value_ru) + ' рублей')
customs_fee = 0
if customs_value_ru in range(0, 200001):
    customs_fee = 775
    print(f'Таможенный сбор - {str(customs_fee)} рублей')
elif customs_value_ru in range(200001, 450001):
    customs_fee = 1550
    print(f'Таможенный сбор - {str(customs_fee)} рублей')
elif customs_value_ru in range(450001, 1200001):
    customs_fee = 3100
    print(f'Таможенный сбор - {str(customs_fee)} рублей')
elif customs_value_ru in range(1200001, 2700001):
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
print_delimetr()

# Сумма таможенных платежей
customs_fee_eur = math.ceil(customs_fee / exchange_rates)
sum_of_customs_payments = custom_duty + vat + customs_fee_eur
# print(sum_of_customs_payments)

# Вывод данных
print('Расчет на одно авто:')

sum_of_one_track = cost_invoice + int(sum_of_transport) + sum_of_insurance + sum_of_customs_payments + \
                   int(sum_of_customs_clearance)
print_delimetr()
pprint(f'Сумма инвойса - {str(cost_invoice)} евро')
pprint(f'сумма транспорта - {sum_of_transport} евро')
pprint(f'Сумма страховки - {str(sum_of_insurance)} евро')
pprint(f'Сумма таможенных платежей - {str(sum_of_customs_payments)}')
pprint(f'Стоимость таможенного оформления - {sum_of_customs_clearance} евро')
pprint(f'Итого на одно авто - {str(sum_of_one_track)} евро')

pprint('Общий расчет:')
pprint(f'Итого - {str(sum_of_one_track * sum_of_trucks)} евро')
print_delimetr()



# with open('D:/хрень рабочая/Downloads/sample.txt', 'w') as test:
#     print(f'Итого - {str(sum_of_one_track * sum_of_trucks)} евро', file=test)
