
from api_cbr import cource_of_eur
from isurance import cost_of_insurance
from math import ceil
from customs_fee import customs_fee_tariff
from duty import duty
from NDS import nds
from colorama import init, Fore, Back, Style
init(autoreset=True)


cost_of_invoice, cost_of_transport_to_board = int(input('Введите стоимость инвойса: ')), \
                                              int(input('Введите стоимость транспортда до границы: '))

customs_value_ru = ceil((cost_of_invoice + cost_of_transport_to_board +
                        cost_of_insurance(cost_of_invoice)) * cource_of_eur)      # расчет таможенной стоимости в руб

customs_value = ceil(cost_of_invoice + cost_of_transport_to_board +
                     cost_of_insurance(cost_of_invoice))                          # расчет таможенной стоимости в евро

tax_ru = customs_fee_tariff(customs_value_ru)
tax = ceil(customs_fee_tariff(customs_value_ru) / cource_of_eur)
customs_duty = duty(customs_value)
customs_vat = nds(customs_value)

print(f'Сбор - {tax} евро')
print(f'Пошлина - {customs_duty} евро')
print(f'НДС - {customs_vat} евро')
print(Style.BRIGHT + Fore.RED + f'Итого - {tax + customs_duty + customs_vat} евро')