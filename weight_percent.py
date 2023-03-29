# import math
#
# total_weight = input('Введите общий вес: ')
# total_weight_transport = input('Введите общую стоимость транспорта: ')
# sum_transport_to_board  = (int(total_weight_transport) * 50) / 100
# weight_of_one_track = input('Введите вес одной ДТ: ')
# # print(transport_to_board)
#
# percent = (int(weight_of_one_track) * 100) / int(total_weight)
# print(percent)
#
# sum_of_one_truck = (sum_transport_to_board * percent) / 100
# print(sum_of_one_truck)
# print(math.ceil(sum_of_one_truck))

import os


print(os.getenv('BOT_TOKEN'))