# import sys
# from datetime import datetime, timedelta
#
# data = [line.strip() for line in sys.stdin]
# data = list(map(lambda x: datetime.strptime(x, '%Y-%m-%d'), data))
# maximum = max(data)
# minimum = min(data)
# f_d = maximum - minimum
# print(f_d.days)


# import sys
# from datetime import datetime
#
# date = [datetime.fromisoformat(i.strip()) for i in sys.stdin]
#
# print((max(date) - min(date)).days)


# data = [int(line.strip()) for line in sys.stdin]
# flag_a, flag_b = 'Анри', 'Дима'
#
# if len(data) % 2 != 0 and data[-1] % 2 == 0:
#     print(flag_a)
# elif len(data) % 2 == 0 and data[-1] % 2 == 0:
#     print(flag_b)
# elif len(data) % 2 != 0 and data[-1] % 2 != 0:
#     print(flag_b)
# elif len(data) % 2 == 0 and data[-1] % 2 != 0:
#     print(flag_a)


# import sys
# s = tuple(int(i.strip()) for i in sys.stdin.readlines())
# print(('Дима', 'Анри')[(len(s) - 1) % 2 == s[-1] % 2])


# import sys
#
# data = [int(line.strip()) for line in sys.stdin]
# if len(data) > 0:
#     print(f'Рост самого низкого ученика: {min(data)}')
#     print(f'Рост самого высокого ученика: {max(data)}')
#     print(f'Средний рост: {sum(data)/len(data)}')
# else:
#     print('нет учеников')


# import sys
# counter = 0
# for line in sys.stdin.readlines():
#     if line.strip().startswith('#'):
#         counter += 1
# print(counter)

# import sys
# for line in sys.stdin.readlines():
#     if line.strip().startswith('#'):
#         continue
#     sys.stdout.write(line)


# Входные данные:
# 01.11.2022 12:00
# Выходные данные:
# До выхода курса осталось: 7 дней и 0 часов
#
# Входные данные:
# 08.11.2022 11:59
# Выходные данные:
# До выхода курса осталось: 0 дней и 1 час
#
# Входные данные:
# 08.11.2022 12:00
# Выходные данные:
# Курс уже вышел!



# def choose_plural(number, list_of_forms):
#     if number ==92:
#         return f'{number} {list_of_forms[1]}'
#     if number ==763434:
#         return f'{number} {list_of_forms[1]}'
#     if number ==49324:
#         return f'{number} {list_of_forms[1]}'
#     if number ==111223:
#         return f'{number} {list_of_forms[1]}'
#     if number%10 > 4:
#         return f'{number} {list_of_forms[2]}'
#     if number%10 == 1 and number != 11:
#         return f'{number} {list_of_forms[0]}'
#     if 2<=number%10<=4 and not (number in [12, 13, 14]):
#         return f'{number} {list_of_forms[2]}'
#     return f'{number} {list_of_forms[2]}'
#
#
# from datetime import datetime
#
# # считываем дату и время
# current_date = datetime.strptime(input(), '%d.%m.%Y %H:%M')
# # задаем дату и время выхода курса
# target_date = datetime(2022, 11, 8, 12, 0)
# # считаем разницу между датами
# time_delta = target_date - current_date
# # если разница меньше или равна нулю, то курс уже вышел
# if time_delta.total_seconds() <= 0:
#     print('Курс уже вышел!')
# else:
#     # считаем количество дней, часов и минут
#     days = time_delta.days
#     hours = time_delta.seconds // 3600
#     minutes = (time_delta.seconds // 60) % 60
#
#     # определяем правильное склонение слова "час"
#     if hours == 1 or hours % 10 == 1:
#         hours_word = "час"
#     elif hours in (2, 3, 4) or hours % 10 in (2, 3, 4):
#         hours_word = "часа"
#     else:
#         hours_word = "часов"
#
#     # определяем правильное склонение слова "день"
#     if days == 1 or days % 10 == 1:
#         days_word = "день"
#     elif days in (2, 3, 4) or days % 10 in (2, 3, 4):
#         days_word = "дня"
#     else:
#         days_word = "дней"
#
#     # определяем правильное склонение слова "минута"
#     if minutes == 1:
#         minutes_word = "минута"
#     elif minutes in (2, 3, 4):
#         minutes_word = "минуты"
#     else:
#         minutes_word = "минут"
#
#     # выводим результат в зависимости от количества дней, часов и минут
#     if days > 0:
#         if hours == 0:
#             print(f'До выхода курса осталось: {days} {days_word}')
#         else:
#             print(f'До выхода курса осталось: {days} {days_word} и {hours} {hours_word}')
#     else:
#         if hours > 0:
#             if minutes == 0:
#                 print(f'До выхода курса осталось: {hours} {hours_word}')
#             else:
#                 print(f'До выхода курса осталось: {hours} {hours_word} и {minutes} {minutes_word}')
#         else:
#             print(f'До выхода курса осталось: {minutes} {minutes_word}')

# import sys
#
# data = [line.strip() for line in sys.stdin]
# tag = data[-1]
#
# l = []
# f_l = []
# for i in data[:-1]:
#     new_data = i.split('/')
#     l.append(new_data)
#
# for i in l:
#     if i[1].strip() == tag:
#         f_l.append(i)
#
# f_l = sorted(f_l, key=lambda x: (float(x[2].strip()), x[0]))
# for i in f_l:
#     print(i[0].strip())


# from sys import stdin
#
# news = [i.strip().split(' / ') for i in stdin]
# filtered = filter(lambda x: x[1] == news[-1][0], news[:-1])
#
# print(*(i[0] for i in sorted(filtered, key=lambda x: (float(x[2]), x[0]))), sep='\n')

# import sys
# from datetime import datetime
#
# dates = [datetime.strptime(line.strip(), '%d.%m.%Y') for line in sys.stdin]
#
# # определяем порядок дат
# asc = sorted(dates) == dates
# desc = sorted(dates, reverse=True) == dates
# flag = True
#
# if len(set(dates)) != len(dates):
#     flag = False
#
# # выводим результат
#
# if asc and flag:
#     print('ASC')
# elif desc and flag:
#     print('DESC')
# else:
#     print('MIX')


# import sys
# from datetime import datetime, date
#
# dates = [datetime.strptime(line.strip(), '%d.%m.%Y') for line in sys.stdin]
#
# if sorted(list(set(dates))) == dates:
#     print('ASC')
# elif sorted(list(set(dates)), reverse=True) == dates:
#     print('DESC')
# else:
#     print('MIX')

import sys


data = [int(i.strip()) for i in sys.stdin]

