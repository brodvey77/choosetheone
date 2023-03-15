# import sys
# from datetime import datetime, timedelta
#
# data = [line.strip() for line in sys.stdin]
# data = list(map(lambda x: datetime.strptime(x, '%Y-%m-%d'), data))
# maximum = max(data)
# minimum = min(data)
# f_d = maximum - minimum
# print(f_d.days)
import sys

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



