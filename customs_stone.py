
sum_of_specification = input('Введите сумму предложения: ')
weight_of_specification = input('Введите вес по спецификации: ')
sum_of_transport = input('Введите общую сумму транспорта: ')
sum_of_customs_clearance = input('Введите стоимость таможенного оформления: ')
exchange_rates = input('Введите курс евро в рублях: ')

print(sum_of_specification)
print(sum_of_transport)
print(weight_of_specification)
print(sum_of_customs_clearance)

# расчет на одно авто
sum_of_trucks = int(weight_of_specification) / 22000
print('Колличество авто {}'.format(sum_of_trucks))
# cost_invoice = int(sum_of_specification) / int(sum_of_trucks)
# print(cost_invoice)
# sum_of_insurance = int(cost_invoice) * 0.2 / 100
# print(sum_of_insurance)

