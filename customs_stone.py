import math

sum_of_specification = input('Введите сумму предложения: ')
weight_of_specification = input('Введите вес по спецификации: ')
sum_of_transport = input('Введите общую сумму транспорта: ')
sum_of_customs_clearance = input('Введите стоимость таможенного оформления: ')
exchange_rates = input('Введите курс евро в рублях: ')

print('сумма предложения - ' + sum_of_specification)
print('сумма транспорта - ' + sum_of_transport)
print('Вес по спецификации - ' + weight_of_specification)
print('Стоимость таможенного оформления - ' + sum_of_customs_clearance)

# расчет на одно авто
sum_of_trucks = math.ceil(int(weight_of_specification) / 22000)
print('Колличество авто - {}'.format(int(sum_of_trucks)))
cost_invoice = math.ceil(int(sum_of_specification) / sum_of_trucks)
print('Сумма инвойса - ' + str(cost_invoice) + 'евро')
# sum_of_insurance = int(cost_invoice) * 0.2 / 100
# print(sum_of_insurance)

