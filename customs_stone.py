import math
# Ввод данных
from pprint import pprint

sum_of_specification = input('Введите сумму предложения(евро): ')
weight_of_specification = input('Введите вес по спецификации(кг): ')
sum_of_transport = input('Введите сумму транспорта за одно авто(евро): ')
sum_of_customs_clearance = input('Введите стоимость таможенного оформления(евро): ')
exchange_rates = input('Введите курс евро в рублях: ')

# проверка
# print('сумма предложения - ' + sum_of_specification + ' евро')
# print('сумма транспорта - ' + sum_of_transport + ' евро')
# print('Вес по спецификации - ' + weight_of_specification + ' кг')
# print('Стоимость таможенного оформления - ' + sum_of_customs_clearance + ' евро')

# расчет на одно авто
sum_of_trucks = math.ceil(int(weight_of_specification) / 22000)
print('Количество авто - {} машин'.format(int(sum_of_trucks)))
cost_invoice = math.ceil(int(sum_of_specification) / sum_of_trucks)
print('Сумма инвойса - ' + str(cost_invoice) + ' евро')
sum_of_insurance = math.ceil(int(cost_invoice) * 0.2 / 100)
print('Сумма страховки - ' + str(sum_of_insurance) + ' евро')
transport_to_board = math.ceil(int(sum_of_transport) * 44 / 100)
print('Сумма транспорта до границы с ТС - ' + str(transport_to_board) + ' евро')

# Расчет таможенной стоимости
customs_value = cost_invoice + transport_to_board + sum_of_insurance
print('Таможенная стоимость - ' + str(customs_value) + ' евро')

# Расчет таможенных платежей
custom_duty = math.ceil(customs_value * 14 / 100)
print('Пошлина - ' + str(custom_duty))
vat = math.ceil((customs_value + custom_duty) * 20 / 100)
print('НДС - ' + str(vat))


# Расчет таможенного сбора
customs_value_ru = math.ceil(customs_value * int(exchange_rates))
# print('Таможенная стоимость в рублях - ' + str(customs_value_ru) + ' рублей')
customs_fee = 0
if customs_value_ru in range(0, 200001):
    customs_fee = 375
    print('Таможенный сбор - ' + str(customs_fee) + ' рублей')
elif customs_value_ru in range(200001, 450001):
    customs_fee = 750
    print('Таможенный сбор - ' + str(customs_fee) + ' рублей')
elif customs_value_ru in range(450001, 1000201):
    customs_fee = 1500
    print('Таможенный сбор - ' + str(customs_fee) + ' рублей')
elif customs_value_ru in range(1000201, 2500001):
    customs_fee = 4125
    print('Таможенный сбор - ' + str(customs_fee) + ' рублей')
elif customs_value_ru in range(2500001, 5000001):
    customs_fee = 5625
    print('Таможенный сбор - ' + str(customs_fee) + ' рублей')
elif customs_value_ru in range(5000001, 10000001):
    customs_fee = 15000
    print('Таможенный сбор - ' + str(customs_fee) + ' рублей')
elif customs_value_ru > 10000001:
    customs_fee = 22500
    print('Таможенный сбор - ' + str(customs_fee) + ' рублей')


# Сумма таможенных платежей
customs_fee_eur = math.ceil(customs_fee / int(exchange_rates))
sum_of_customs_payments = custom_duty + vat + customs_fee_eur
# print(sum_of_customs_payments)


# Вывод данных
print('Расчет на одно авто:')

sum_of_one_track = cost_invoice + int(sum_of_transport) + sum_of_insurance + sum_of_customs_payments + int(sum_of_customs_clearance)

pprint('Сумма инвойса - ' + str(cost_invoice) + ' евро')
pprint('сумма транспорта - ' + sum_of_transport + ' евро')
pprint('Сумма страховки - ' + str(sum_of_insurance) + ' евро')
pprint('Сумма таможенных платежей - ' + str(sum_of_customs_payments))
pprint('Стоимость таможенного оформления - ' + sum_of_customs_clearance + ' евро')
pprint('Итого на одно авто - ' + str(sum_of_one_track) + ' евро')

pprint('Общий расчет:')
pprint('Итого - ' + str(sum_of_one_track * sum_of_trucks) + ' евро')




