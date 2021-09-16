# получение данных от пользователя по стоимости инвойса и транспортных расходов до границы
from api_cbr import cource_of_eur
from isurance import cost_of_insurance
from math import ceil
from customs_fee import customs_fee_tariff
from duty import duty
from NDS import nds

cost_of_invoice, cost_of_transport_to_board = int(input()), int(input())
customs_value_ru = ceil((cost_of_invoice + cost_of_transport_to_board +
                        cost_of_insurance(cost_of_invoice)) * cource_of_eur)
customs_value = ceil(cost_of_invoice + cost_of_transport_to_board + cost_of_insurance(cost_of_invoice))

print(f'Сбор в евро {ceil(customs_fee_tariff(customs_value_ru) / cource_of_eur)}')
print(f'Пошлина в евро {duty(customs_value)}')
print(f'НДС в евро {nds(customs_value)}')















