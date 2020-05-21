import math
# Ввод данных

sum_of_specification = input('Введите сумму предложения: ')
weight_of_specification = input('Введите вес по спецификации: ')
sum_of_transport = input('Введите общую сумму транспорта: ')
sum_of_customs_clearance = input('Введите стоимость таможенного оформления: ')
exchange_rates = input('Введите курс евро в рублях: ')

# проверка
print('сумма предложения - ' + sum_of_specification + ' евро')
print('сумма транспорта - ' + sum_of_transport + ' евро')
print('Вес по спецификации - ' + weight_of_specification + ' кг')
print('Стоимость таможенного оформления - ' + sum_of_customs_clearance + ' евро')

# расчет на одно авто
sum_of_trucks = math.ceil(int(weight_of_specification) / 22000)
print('Колличество авто - {} машин'.format(int(sum_of_trucks)))
cost_invoice = math.ceil(int(sum_of_specification) / sum_of_trucks)
print('Сумма инвойса - ' + str(cost_invoice) + ' евро')
sum_of_insurance = math.ceil(int(cost_invoice) * 0.2 / 100)
print('Сумма страховки - ' + str(sum_of_insurance) + ' евро')
transport_to_board = math.ceil(int(sum_of_transport) * 55 / 100)
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
print('Таможенная стоимость в рублях - ' + str(customs_value_ru) + ' рублей')

if customs_value_ru in range(0, 200001):
    print('Таможенный сбор - 375 рублей')
elif customs_value_ru in range(200001, 450001):
    print('Таможенный сбор - 750 рублей')
elif customs_value_ru in range(450001, 1000201):
    print('Таможенный сбор - 1500 рублей')
elif customs_value_ru in range(1000201, 2500001):
    print('Таможенный сбор - 4125 рублей')
elif customs_value_ru in range(2500001, 5000001):
    print('Таможенный сбор - 5625 рублей')
elif customs_value_ru in range(5000001, 10000001):
    print('Таможенный сбор - 15000 рублей')
elif customs_value_ru in range(10000001, 99999999999999999999999):
    print('Таможенный сбор - 22500 рублей')
