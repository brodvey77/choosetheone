# from datetime import date
#
# dates = [date(2000, 12, 31), date(1999, 3, 8), date(1999, 2, 22)]
#
# max_date = max(dates)
# min_date = min(dates)
#
# print(max_date.year + min_date.day)
import datetime
# from datetime import date
#
# dates = [date(2023, 1, 1), date(2020, 7, 20), date(2021, 9, 17), date(2022, 6, 10)]
#
# print(*sorted(dates, key=lambda d: d.day), sep=', ')


# # импортируем тип date из модуля datetime
# from datetime import date
#
# # выводим текущую дату
# print(date.today())


# # импортируем тип date из модуля datetime
# from datetime import date
#
# # создаем объект, соответсвующий дате урагана
# hurricane_andrew = date(1992,8,24)
#
# # выводим день недели
# print(hurricane_andrew.weekday())


# from datetime import date
# florida_hurricane_dates = [date(1987, 11, 15), date(1988, 3, 12), date(1976, 5, 12)]
#
# # счетчик для нужного количества ураганов
# early_hurricanes = 0
#
# # цикл по датам в которые был ураган
# for hurricane in florida_hurricane_dates:
#     # если месяц урагана меньше чем июнь (порядковый номер 6)
#     if hurricane.month < 6:
#         early_hurricanes += 1
#
# print(early_hurricanes)


# from datetime import date
#
# dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11),
#          date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21),
#          date(1666, 6, 6), date(1968, 5, 26)]
#
# for i in dates:
#     print(f'{i.year}-Q{(i.month+2)//3}')


# from datetime import date
#
# def get_min_max(d):
#     if len(d) > 0:
#         return min(d), max(d)
#     else:
#         return ()
#
#
#
# dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
#
# print(get_min_max(dates))
# print(get_min_max([]))


# from datetime import date
# def get_date_range(start, end):
#     c = date.toordinal(end) - date.toordinal(start)
#     l = []
#     for i in range(c + 1):
#         a = date.toordinal(start)
#         a += i
#         l.append(date.fromordinal(a))
#     return l
#
#
#
#
#
# date1 = date(2019, 6, 7)
# date2 = date(2019, 6, 5)
#
# print(get_date_range(date1, date2))
#
#
#
# def get_date_range(start, end):
#     return [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]

# from datetime import date
#
# def saturdays_between_two_dates(a, b):
#     if a > b:
#         a, b = b, a
#     l = [date.weekday(date.fromordinal(i)) for i in range(a.toordinal(), b.toordinal() + 1)]
#     return l.count(5)
#
#
# date1 = date(2021, 11, 1)
# date2 = date(2021, 11, 22)
#
# print(saturdays_between_two_dates(date1, date2))

# from datetime import date
#
# my_date = date(2019, 2, 4)
#
# print(my_date)

# from datetime import time
#
# my_time = time(8, 20, 15)
#
# print(my_time)

# from datetime import date
#
# my_date = date(2021, 12, 31)
#
# print(my_date.strftime('%d %B %Y'))


# from datetime import time
#
# alarm = time(7, 30, 25)
#
# print('Часы:', alarm.strftime('%H'))
# print('Минуты:', alarm.strftime('%M'))
# print('Секунды:', alarm.strftime('%S'))


# from datetime import date
#
# birthday = date(1992, 10, 6)
#
# print('Название месяца:', birthday.strftime('%B'))
# print('Название дня недели:', birthday.strftime('%A'))
# print('Год:', birthday.strftime('%Y'))
# print('Месяц:', birthday.strftime('%m'))
# print('День:', birthday.strftime('%d'))


# from datetime import date
# # присваиваем самую раннюю дату урагана в переменную first_date
# first_date = date(2022, 12, 5)
#
# # конвертируем дату в ISO и RU формат
# iso = 'Дата первого урагана в ISO формате: ' + first_date.isoformat()
# ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%d.%m.%Y')
# us = 'Дата первого урагана в US формате: ' + first_date.strftime('%m/%d/%Y')
#
# print(iso)
# print(ru)
# print(us)


# from datetime import date
#
# andrew = date(1992, 8, 24)
#
# print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
# print(andrew.strftime('%B(%Y)'))   # выводим дату в формате month_name (YYYY)
# print(andrew.strftime('%Y-%j'))   # выводим дату в формате YYYY-day_number


# n = 'python'
#
# try:
#     n = int(n)
#     print(n * 2)
# except ValueError:
#     print('Произошла ошибка')

# try:
#     names = ['Tim', 'Tom', 'Jerry', 'Alvin', 'Wall-e']
#     print(names[-5])
#     print(names[5])
# except:
#     print('IndexError')

# from datetime import date
#
# a, b = date.fromisoformat(input()), date.fromisoformat(input())
# print(min(a, b).strftime('%d-%m (%Y)'))

from datetime import date

# from datetime import date
# l = list(map(lambda x: x.strftime('%d/%m/%Y'),sorted([date.fromisoformat(input()) for i in range(int(input()))])))
# print(*l)


from datetime import date


# определяем функцию, печатающую красивую дату
# def print_good_dates(dates):
#     l = []
#     for i in dates:
#         if i.strftime('%Y') == '1992' and int(i.strftime('%d')) + int(i.strftime('%m')) == 29:
#             l.append(i)
#     s = sorted(l)
#     for i in s:
#         print(i.strftime('%B %d, %Y'))
#
#
# dates = []
# print_good_dates(dates)
#
#
# def print_good_dates(dates):
#     for d in sorted(filter(lambda d: d.year == 1992 and d.month + d.day == 29, dates)):
#         print(d.strftime('%B %d, %Y'))

# from datetime import date
#
# def is_correct(d, m, y):
#     try:
#         if date(day=d, month=m, year=y):
#             return True
#     except:
#         return False
#
#
#
# def is_correct(day, month, year):
#     try:
#         date(year, month, day)
#         return True
#     except:
#         return False


# print(is_correct(31, 13, 2021))


# from datetime import date
#
# def is_correct(year, month, day):
#     try:
#         date(int(year), int(month), int(day))
#         return True
#     except:
#         return False
#
#
# text = input()
# counter = 0
# while text != 'end':
#     day, month, year = text.split('.')
#     if is_correct(year, month, day):
#         print('Корректная')
#         counter += 1
#     else:
#         print('Некорректная')
#     text = input()
# print(counter)


# from datetime import datetime
#
# birthday = datetime(1992, 10, 6, 9, 48, 17)
#
# birthday.replace(year=9999, month=11)
#
# print(birthday)


# from datetime import datetime
#
# datetimes = [datetime(2022, 6, 11, 13, 26),
#              datetime(2000, 12, 31, 23, 59),
#              datetime(2077, 1, 1, 12),
#              datetime(2042, 7, 29)]
#
# print(min(datetimes, key=lambda dt: dt.hour))
# print(max(datetimes, key=lambda dt: dt.year))


# from datetime import date, time, datetime
#
# dt = datetime.combine(date(2022, 6, 10), time(13, 50, 59))
#
# print(dt.day + dt.second)


# from datetime import datetime
#
# text = 'Experiment Date 01/28/2005; Time 23::50::13'
#
# dt = datetime.strptime(text, 'Experiment Date %m/%d/%Y, Time %H:%M:%S')
#
# print(dt)

# from datetime import datetime
#
# text = 'Дорогой дневник, 11.02.2021 произошло нечто невероятное. На часах было 18:09..'
# pattern = 'Дорогой дневник, %d.%m.%Y произошло нечто невероятное. На часах было %H:%M..'
#
# dt = datetime.strptime(text, pattern)
#
# print(dt)

# from datetime import datetime
#
# text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'
#
# dt = datetime.strptime(text, 'Уважаемый пациент, доктор готов принять Вас %d.%m.%Y в %H:%M')
#
# print(dt)


# from datetime import datetime
#
# seconds = 2483228800
# dt = datetime(2011, 11, 4)
#
# print(datetime.fromtimestamp(seconds))
# print(dt.timestamp())


# from datetime import datetime
#
# times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
#                       datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59),
#                       datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53),
#                       datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3),
#                       datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5),
#                       datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54),
#                       datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45),
#                       datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57),
#                       datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42),
#                       datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12),
#                       datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27),
#                       datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41),
#                       datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44),
#                       datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]

# pm = 0
# am = 0
# for i in times_of_purchases:
#     a = i.time().strftime(('%H'))
#     if int(a) >= 12:
#         pm += 1
#     else:
#         am += 1
# if am > pm:
#     print('До полудня')
# else:
#     print('После полудня')


# for i in times_of_purchases:
#     print(i.strftime('%p'))

# dts = [d.strftime('%p') for d in times_of_purchases]
# print(['До полудня', 'После полудня'][dts.count('PM')>dts.count('AM')])

# from datetime import date, time, datetime
#
# dates = [date(2020, 11, 12), date(2021, 7, 2), date(2020, 9, 25)]
# times = [time(12, 50, 22), time(12, 19, 1), time(7, 30, 1)]
#
# l = list(zip(dates, times))
#
# s = list(map(lambda x: datetime.combine(x[0], x[1]), l))
# a = sorted(s, key=lambda x: x.second)
# for i in a:
#     print(i)

# from datetime import date, time, datetime
#
# dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
#          date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24),
#          date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]
#
# times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59),
#          time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2),
#          time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]
#
# a = sorted(list(map(lambda x: datetime.combine(x[0], x[1]), list(zip(dates, times)))), key=lambda x: x.second)
# for i in a:
#     print(i)
#
#
# datetimes = [datetime.combine(d, t) for d, t in zip(dates, times)]
#
# print(*sorted(datetimes, key=lambda dt: dt.second), sep='\n')


# from datetime import datetime
#
# data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
#         'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
#         'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
#         'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
#         'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
#         'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
#         'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
#         'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
#         'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
#         'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
#         'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}
#
# d = {}
# for k, v in data.items():
#     s = datetime.timestamp(datetime.strptime(v[1], '%d.%m.%Y %H:%M:%S')) - datetime.timestamp(datetime.strptime(v[0], '%d.%m.%Y %H:%M:%S'))
#     d[s] = k
#
# print(d[min(d.keys())])
#
# for key, value in data.items():
#     dt1 = datetime.strptime(value[0], '%d.%m.%Y %H:%M:%S').timestamp()
#     dt2 = datetime.strptime(value[1], '%d.%m.%Y %H:%M:%S').timestamp()
#     data[key] = dt2 - dt1
#
# print(min(data, key=data.get))

# from datetime import datetime
#
# with open('diary.txt', encoding='utf-8') as file, open('test_1.txt', 'w', encoding='utf-8') as output:
#     line = file.read().split('\n\n')
#     d = {}
#     for text in line:
#         s = datetime.strptime(text[:17], '%d.%m.%Y; %H:%M')
#         d[s] = text[18:]
#     c = []
#     for k, v in sorted(d.items()):
#         print(k.strftime('%d.%m.%Y; %H:%M'))
#         if sorted(d.keys())[-1] != k:
#             print(v+'\n')
#         else:
#             print(v)

# from datetime import datetime
# import pandas as pd
#
#
# def is_available_date(dates, booking):
#     booked_dates = set()
#     for date in dates:
#         date_range = date.split("-")
#         start_date = datetime.strptime(date_range[0], "%d.%m.%Y")
#         end_date = start_date if len(date_range) == 1 else datetime.strptime(date_range[1], "%d.%m.%Y")
#         booked_dates.update(
#             pd.date_range(min(start_date, end_date), max(start_date, end_date)).strftime("%d.%m.%Y").to_list())
#
#     booking_list = booking.split("-")
#     start_date = datetime.strptime(booking_list[0], "%d.%m.%Y")
#     end_date = start_date if len(booking_list) == 1 else datetime.strptime(booking_list[1], "%d.%m.%Y")
#     check_in_dates = set(
#         pd.date_range(min(start_date, end_date), max(start_date, end_date)).strftime("%d.%m.%Y").to_list())
#
#     if booked_dates.intersection(check_in_dates):
#         return False
#     else:
#         return True

# dates = ['04.11.2021', '05.11.2021-09.11.2021']
# some_date = '06.11.2021'
# print(is_available_date(dates, some_date))


# from datetime import datetime
# def is_available_date(booked_dates, date_for_booking):
#     ord_booked_dates = []
#     for d in booked_dates:
#         dates = [datetime.strptime(i, '%d.%m.%Y').toordinal() for i in d.split('-')]
#         ord_booked_dates.extend(range(dates[0], dates[-1] + 1))
#     dt = [datetime.strptime(i, '%d.%m.%Y').toordinal() for i in date_for_booking.split('-')]
#     date_f_b = range(dt[0], dt[-1] + 1)
#     return(all([i not in ord_booked_dates for i in date_f_b]))


# from datetime import datetime
# def sd(s): # функция превращает строку в дату
#     return datetime.strptime(s, '%d.%m.%Y')
# def dk(spd): # функция превращает строку c датой или интервалом дат в кортеж из 2 дат
#     return (sd(spd[:10]), sd(spd[11:])) if '-' in spd else (sd(spd), sd(spd))
# def is_available_date(sp, d):
#     for x in sp: # проверяем, пересекаются ли кортежи дат гостя и отеля
#         if not(dk(x)[1] < dk(d)[0] or dk(x)[0] > dk(d)[1]):
#             return False # если пересекаются, то выводим False
#     return True  # а если нет, то True


# from datetime import date, datetime as dt
#
# def is_available_date(dates, some_date):
#     def setGen(dateRange):
#         d=list(map(lambda d: dt.strptime(d, '%d.%m.%Y').date().toordinal(), dateRange.split('-')))
#         if len(d)>1: return set([x for x in range(d[0], d[1]+1)])
#         else: return set(d)
#     return not any([bool(setGen(some_date).intersection(setGen(day))) for day in dates])

# from datetime import timedelta
#
# def hours_minutes(td):
#     return td.seconds // 3600, (td.seconds // 60) % 60
#
# delta = timedelta(days=7, seconds=125, minutes=10, hours=8, weeks=2)
#
# hours, minutes = hours_minutes(delta)
#
# print(delta)
# print(hours)
# print(minutes)

# from datetime import timedelta
#
# td = timedelta(minutes=61)
#
# print(td.hours)


# from datetime import timedelta
#
# td = timedelta(weeks=-3, hours=-12)
#
# print(td)


# from datetime import timedelta
#
# td1 = timedelta(days=2, hours=1, minutes=1)
# td2 = timedelta(hours=49, seconds=60)
#
# print(td1 == td2)
# print(td1 > td2)


# from datetime import timedelta
#
# td1 = timedelta(days=2, hours=1, minutes=1)
# td2 = timedelta(hours=49, seconds=60)
# print(td1)
# print(td2)
# print(td1 == td2)
# print(td1 > td2)


# from datetime import datetime
#
# release = datetime(2022, 7, 15)
# today = datetime(2022, 11, 6)
#
# print(type(release - today))


# from datetime import timedelta
#
# td = timedelta(weeks=-1, hours=-20, minutes=-120)
# abs_td = abs(td)
#
# print(td)
# print(abs_td)


# from datetime import datetime, timedelta
#
# dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)
# print(dt.strftime('%d.%m.%Y %H:%M:%S'))


# from datetime import date, timedelta
#
# today = date(2021, 11, 4)
# birthday = date(2022, 10, 6)
#
# days = (birthday - today).days
#
# print(days)


# from datetime import timedelta, datetime, date
#
# a = '04.11.2021'
# def t_a(x):
#     return datetime.strptime(x, '%d.%m.%Y')
#
# def d_d(x):
#     return date.strftime(x, '%d.%m.%Y')
#
# p_d = t_a(a) - timedelta(days=1)
# n_d = t_a(a) + timedelta(days=1)
#
# print(d_d(p_d), d_d(n_d), sep='\n')

# from datetime import timedelta
#
# x = input()
# begin = timedelta(hours=0, minutes=0, seconds=0)
# last = timedelta(hours=int(x[0:2]), minutes=int(x[3:5]), seconds=int(x[6:]))
# result = int(timedelta.total_seconds(last - begin))
# print(result)
#
# from datetime import datetime, timedelta
# h, m, s = map(int, input().split(':'))
# td = timedelta(hours=h, minutes=m, seconds=s)
# print(int(td.total_seconds()))

# from datetime import timedelta, datetime
#
# def hours_minutes(td):
#     return td.seconds // 3600
#
#
# h, m, s = map(int, input().split(':'))
# time_now = timedelta(hours=h, minutes=m, seconds=s)
# alarm = timedelta(seconds=int(input()))
#
# wake_up = time_now + alarm
#
# if len(str(wake_up)) >= 8:
#     hh = str(hours_minutes(wake_up))
#     if len(hh) == 1:
#         hh = '0' + hh
#     wake_up = str(wake_up)
#     print(f'{hh}:{str(wake_up[-5:])}')
# else:
#     wake = str(wake_up)
#     if len(wake) < 8:
#         print('0' + wake)
#     else:
#         print(wake)


# from datetime import datetime, timedelta
#
# pattern = '%H:%M:%S'
# dt = datetime.strptime(input(), pattern) + timedelta(seconds=int(input()))
#
# print(dt.strftime(pattern))


# from datetime import date, datetime
# def saturdays_between_two_dates(a, b):
#     if a < b:
#         l = [date.weekday(date.fromordinal(i)) for i in range(a.toordinal(), b.toordinal() + 1)]
#     else:
#         l = [date.weekday(date.fromordinal(i)) for i in range(b.toordinal(), a.toordinal() + 1)]
#     return l.count(5)

# def num_of_sundays(y):
#     first_date = datetime(year=y, month=1, day=1)
#     last_date = datetime(year=y, month=12, day=31)
#     l = [date.weekday(date.fromordinal(i)) for i in range(first_date.toordinal(), last_date.toordinal() + 1)]
#     return l.count(6)
#
# print(num_of_sundays(2021))

# from datetime import datetime
#
# def num_of_sundays(year):
#     dt = datetime(year, 12, 31)
#     return int(dt.strftime('%U'))


# from datetime import date, time, datetime, timedelta
#
# d, m, y = map(int, input().split('.'))
# f_d = datetime(year=y, month=m, day=d)
#
# for i in range(1, 11):
#     print(f_d.strftime('%d.%m.%Y'))
#     f_d += timedelta(days=1 + i)


# from datetime import datetime, timedelta

# pattern = '%d.%m.%Y'
# dt = datetime.strptime(input(), pattern) - timedelta(days=1)
#
# for i in range(1, 11):
#     dt += timedelta(days=i)
#     print(dt.strftime(pattern))


# from datetime import datetime, date, timedelta
#
# pattern = '%d.%m.%Y'
# l = [datetime.strptime(i, pattern) for i in input().split(' ')]
#
# result = []
# for i in range(len(l)-1):
#     a = abs(l[i] - l[i+1])
#     result.append(a.days)
#
# print(result)

# from datetime import date, time, timedelta, datetime
#
# dates = [datetime.strptime(dt, '%d.%m.%Y') for dt in input().split()]
#
# diffs = [abs(dates[i] - dates[i - 1]).days for i in range(1, len(dates))]
#
# print(diffs)

# from datetime import datetime, timedelta
#
# def fill_up_missing_dates(dates):
#     new_dates = []
#     pattern = '%d.%m.%Y'
#     d = [datetime.strptime(dt, pattern) for dt in dates]
#     minimum, maximum = min(d), max(d)
#     for i in range(datetime.toordinal(minimum), datetime.toordinal(maximum)):
#         x = datetime.fromordinal(i)
#         new_dates.append(datetime.strftime(x, pattern))
#     new_dates.append(datetime.strftime(maximum, pattern))
#     return new_dates
#
#
#
#
# dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
#
# print(fill_up_missing_dates(dates))

# from datetime import datetime, timedelta
#
# pattern = '%H:%M'
# start, end = datetime.strptime(input(), pattern), datetime.strptime(input(), pattern)
# lesson, pause = timedelta(minutes=45), timedelta(minutes=10)
# l = []
# while (end - start) >= lesson:
#     print(f'{datetime.strftime(start, pattern)} - {datetime.strftime(start + lesson, pattern)}')
#     start = start+lesson+pause
#
#
#
# from datetime import datetime, timedelta
# f = '%H:%M'
# start, stop = (datetime.strptime(input(), f) for i in '__')
# while start <= (stop - timedelta(minutes=45)):
#     print(start.strftime(f), '-', (start + timedelta(minutes=45)).strftime(f))
#     start += timedelta(minutes=55)


# from datetime import date, time, datetime, timedelta
# from functools import reduce
#
#
# data = [('07:14', '08:46'),
#         ('09:01', '09:37'),
#         ('10:00', '11:43'),
#         ('12:13', '13:49'),
#         ('15:00', '15:19'),
#         ('15:58', '17:24'),
#         ('17:57', '19:21'),
#         ('19:30', '19:59')]
#
# pattern = '%H:%M'
# data = list(map(lambda x: datetime.strptime(x[1], pattern) - datetime.strptime(x[0], pattern), data))
# s = int(timedelta.total_seconds(reduce(lambda x, y: x + y, data)))
# print(s//60)


# from datetime import date, time, datetime, timedelta
#
# data = [('07:14', '08:46'),
#         ('09:01', '09:37'),
#         ('10:00', '11:43'),
#         ('12:13', '13:49'),
#         ('15:00', '15:19'),
#         ('15:58', '17:24'),
#         ('17:57', '19:21'),
#         ('19:30', '19:59')]
#
# seconds = 0
#
# for tup in data:
#     start, end = [datetime.strptime(x, '%H:%M') for x in tup]
#     seconds += (end - start).total_seconds()
#
# print(int(seconds // 60))``

# from datetime import datetime, timedelta, date
#
# d = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
# for y in range(1, 10000):
#     for m in range(1, 13):
#         third_day = date(y, m, 13)
#         key = third_day.weekday()
#         if key in d.keys():
#             d[key] = d[key] + 1
#         else:
#             d[key] = 0
#
#
# print(*d.values(), sep='\n')

# def get_string(string: str, times: int, sep: str='') -> str:
#     return sep.join([string] * times)
#
#
# print(get_string('hi', 5))


# def say_something(number: int, word: str) -> str:
#     word = word.capitalize()
#     return word * number

# from datetime import timedelta, datetime, time
#
# now = '01.11.2021 20:45'  # ответ 15
# pattern = '%d.%m.%Y %H:%M'
# date_now = datetime.strptime(now, pattern)
#
# schedule = {
#     0: {'start': datetime.combine(date_now.date(), time(9, 0, 0)),
#         'end': datetime.combine(date_now.date(), time(21, 0, 0))},
#     1: {'start': datetime.combine(date_now.date(), time(9, 0, 0)),
#         'end': datetime.combine(date_now.date(), time(21, 0, 0))},
#     2: {'start': datetime.combine(date_now.date(), time(9, 0, 0)),
#         'end': datetime.combine(date_now.date(), time(21, 0, 0))},
#     3: {'start': datetime.combine(date_now.date(), time(9, 0, 0)),
#         'end': datetime.combine(date_now.date(), time(21, 0, 0))},
#     4: {'start': datetime.combine(date_now.date(), time(9, 0, 0)),
#         'end': datetime.combine(date_now.date(), time(21, 0, 0))},
#     5: {'start': datetime.combine(date_now.date(), time(10, 0, 0)),
#         'end': datetime.combine(date_now.date(), time(18, 0, 0))},
#     6: {'start': datetime.combine(date_now.date(), time(10, 0, 0)),
#         'end': datetime.combine(date_now.date(), time(18, 0, 0))}
# }
#
#
# if schedule[date_now.weekday()]['end'] >= date_now >= schedule[date_now.weekday()]['start']:
#     m = (schedule[date_now.weekday()]['end'] - date_now).seconds // 60
#     print(m)
# else:
#     print("Магазин не работает")



# from datetime import datetime, timedelta
#
# dt = datetime.strptime(input(), '%d.%m.%Y %H:%M')
# td = timedelta(hours=dt.hour, minutes=dt.minute)
#
# if dt.weekday() < 5 and timedelta(hours=9) <= td < timedelta(hours=21):
#     print(int((timedelta(hours=21) - td).total_seconds() // 60))
# elif dt.weekday() > 4 and timedelta(hours=10) <= td < timedelta(hours=18):
#     print(int((timedelta(hours=18) - td).total_seconds() // 60))
# else:
#     print('Магазин не работает')
#
#
#
#
# from datetime import datetime
# date = datetime.strptime(input(), '%d.%m.%Y %H:%M')
#
# start, end = (date.replace(hour=i, minute=0) for i in ((9, 21), (10, 18))[date.weekday() > 4])
#
# if start <= date < end:
#     print((end - date).seconds // 60)
# else:
#     print('Магазин не работает')

# from datetime import date, datetime
#
# a, b = '30.04.2021', '10.05.2021'
#
# l = []
#
# for d in range(datetime.toordinal(datetime.strptime(a, '%d.%m.%Y')),
#                datetime.toordinal(datetime.strptime(b, '%d.%m.%Y')) + 1):
#     l.append(date.fromordinal(d))
#
# def check_first(d: list) -> list:
#     counter = 0
#     nl = []
#     fd = date.strftime(d[0], '%d.%m.%Y').split('.')
#     while (int(fd[0]) + int(fd[1])) % 2 == 0:
#         counter += 1
#         fd = date.strftime(d[counter], '%d.%m.%Y').split('.')
#     l = d[counter:]
#     return l
#
#
#
# for i in range(0, len(check_first(l)) + 1, 3):
#     if i < len(check_first(l)):
#         if check_first(l)[i].weekday() not in [0, 3]:
#             print(date.strftime(check_first(l)[i], '%d.%m.%Y'))
#     else:
#         break



# from datetime import datetime, date, timedelta
# pattern = '%d.%m.%Y'
# start, end = [datetime.strptime(input(), pattern) for _ in range(2)]
# while (start.day + start.month) % 2 == 0:
#     start += timedelta(days=1)
#
# while start <= end:
#     if start.weekday() not in [0, 3]:
#         print(start.strftime(pattern))
#     start += timedelta(days=3)


# from datetime import datetime, date
#
# data = [i for i in range(datetime.strptime(input(), '%d.%m.%Y').toordinal(),
#                          datetime.strptime(input(), '%d.%m.%Y').toordinal() + 1)]
# start = list(filter(lambda x: (date.fromordinal(x).day + date.fromordinal(x).month) % 2 != 0, data))[0]
# for j in range(start, max(data)+1, 3):
#     if date.fromordinal(j).strftime('%w') != '1' and date.fromordinal(j).strftime('%w') != '4':
#         print(date.fromordinal(j).strftime('%d.%m.%Y'))


# from datetime import datetime
#
# n: int = int(input())
# staff = [tuple(input().split()) for i in range(n)]
# my_dict = {}
#
# for s in staff:
#     my_dict.setdefault(datetime.strptime(s[-1], '%d.%m.%Y'), []).append(s[0] + ' ' + s[1])
# s_d = sorted(my_dict.items(), reverse=True)
#
# for k, v in dict(s_d).items():
#     if len(v) <= 1:
#         print(k, v)
#     else:
#         print(k, len(v))
#     break


# from datetime import datetime, timedelta
#
# data = {}
# youngest = datetime.max
# pattern = '%d.%m.%Y'
#
# for _ in range(int(input())):
#     *name, birthday = input().split()
#     name, birthday = ' '.join(name), datetime.strptime(birthday, pattern)
#     if birthday < youngest:
#         youngest = birthday
#     data[name] = birthday
#
# oldest = [name for name, bd in data.items() if bd == youngest]
#
# if len(oldest) > 1:
#     print(youngest.strftime(pattern), len(oldest))
# else:
#     print(youngest.strftime(pattern), oldest[0])



