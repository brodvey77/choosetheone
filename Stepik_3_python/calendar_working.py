# import calendar, locale
#
# for name in calendar.day_name:
#     print(name)
#
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
#
# for name in calendar.day_abbr:
#     print(name)


# import calendar, locale
#
# english_names = list(calendar.month_name)
# print(english_names)
#
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
#
# russian_names = list(calendar.month_name)
# print(russian_names)



# import calendar, locale
#
# english_names = list(calendar.month_abbr)
# print(english_names)
#
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
#
# russian_names = list(calendar.month_abbr)
# print(russian_names)

# import calendar
#
# print(calendar.MONDAY)
# print(calendar.TUESDAY)



# import calendar
#
# calendar.setfirstweekday(calendar.SUNDAY)
# calendar.setfirstweekday(6)


# import calendar
#
# print(calendar.firstweekday())
# calendar.setfirstweekday(calendar.SUNDAY)
# print(calendar.firstweekday())


# import calendar
#
# print(calendar.isleap(2020))
# print(calendar.isleap(2021))



# import calendar
#
# print(calendar.leapdays(2020, 2025))


# import calendar
#
# print(calendar.weekday(1983, 6, 4))


# import calendar
#
# print(calendar.monthrange(2023, 3))
# print(calendar.monthrange(2022, 2))


# import calendar
#
# print(*calendar.monthcalendar(2023, 3), sep='\n')


# Функция month()
# Функция month(year, month, w=0, l=0) возвращает календарь на месяц в многострочной строке. Аргументами функции являются: year (год), month (месяц), w (ширина столбца даты) и l (количество строк, отводимые на неделю).
# import calendar
#
# print(calendar.month(2023, 3))
# print(calendar.month(2023, 3, w=5, l=1))

# Функция calendar()
# Функция calendar(year, w=2, l=1, c=6, m=3) возвращает календарь на весь год в виде многострочной строки. Аргументами функции являются: year (год),  w (ширина столбца даты) и l (количество строк, отводимые на неделю), c (количество пробелов между столбцом месяца),  m (количество столбцов).
#
#     Аргументы w, l, c, m имеют значения по умолчанию, поэтому их можно не передавать явно при вызове функции.


# import calendar
# print(calendar.calendar(2023))

# import calendar, locale
#
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# print(calendar.calendar(2023))


# import calendar
#
# calendar.prmonth(2021, 9)
# calendar.prcal(2021)
#
# эквивалентен коду:

# import calendar
#
# print(calendar.month(2021, 9))
# print(calendar.calendar(2021))

# import calendar
# month = calendar.month_name[1]
# print(month)

# import calendar
#
# day = calendar.day_name[1]

# import calendar
# y = [int(input()) for i in range(int(input()))]
#
# for i in y:
#     print(calendar.isleap(i))
#
#
# from calendar import isleap
#
# for _ in range(int(input())):
#     print(isleap(int(input())))

# from calendar import month, month_abbr
#
# d = dict(zip(month_abbr, [i for i in range(13)]))
# a = '2021 Dec'
# y, m = a.split(' ')
#
# print(month(int(y), d[m]))
#
#
# from calendar import prmonth
# from datetime import datetime
#
# dt = datetime.strptime(input(), '%Y %b')
#
# prmonth(dt.year, dt.month)

# import calendar
# from datetime import datetime
#
# a = datetime.strptime(input(), '%Y-%m-%d').weekday()
#
# print(calendar.day_name[a])

# import calendar
# a = input()
# y, m = a.split(' ')
#
# l = calendar.monthcalendar(int(y), int(m))
# counter = 0
# for row in l:
#     for j in row:
#         if j != 0:
#             counter += 1
# print(counter)


# import calendar
#
# year, number = map(int, input().split())
# days = calendar.monthrange(year, number)[1]
#
# print(days)


# import calendar
#
# year, m = input().split(' ')
# d = dict(zip(calendar.month_abbr, [i for i in range(13)]))
#
# days = calendar.monthrange(int(year), d[m])[1]
#
# print(days)



# import calendar
#
# year, month = input().split()
# month = list(calendar.month_name).index(month)
# print(month)
#
# print(calendar.monthrange(int(year), int(month))[1])


# import calendar
# from datetime import date
# def get_days_in_month(god: int, mesyac: str) -> list:
#     d = dict(zip(calendar.month_name, [i for i in range(13)]))
#     l = calendar.monthcalendar(god, d[mesyac])
#     n_l = []
#     for row in l:
#         for c in row:
#             if c != 0:
#                 n_l.append(c)
#     n_l = list(map(lambda x: date(year=god, month=d[mesyac], day=x), n_l))
#     return n_l
#
#
#
#
# print(get_days_in_month(2021, 'December'))



# def get_days_in_month(year, month):
#     month = list(calendar.month_name).index(month)
#     return [date(year, month, day) for day in range(1, calendar.monthrange(year, month)[1] + 1)]


# import calendar
# from datetime import date
#
# l: list = []
# def get_all_mondays(god: int) -> list:
#     for i in range(date.toordinal(date(year=god, month=1, day=1)), date.toordinal(date(year=god, month=12, day=31)) + 1):
#         l.append(date.fromordinal(i))
#     s = list(filter(lambda x: x.weekday() == 0, l))
#     return s
#
#
# print(get_all_mondays(2001))

# def get_all_mondays(year):
#     mondays = []
#     for month in range(1, 13):
#         for week in calendar.monthcalendar(year, month):
#             monday = week[0]
#             if monday:
#                 mondays.append(date(year, month, monday))
#     return mondays


# import calendar
# from datetime import date
# def get_all_mondays(year):
#     tuesdays = []
#     f_tuesdays = []
#     for month in range(1, 13):
#         counter = 0
#         for week in calendar.monthcalendar(year, month):
#             tuesday = week[3]
#             if tuesday:
#                 tuesdays.append(date(year, month, tuesday))
#                 counter += 1
#             if counter == 3:
#                 f_tuesdays.append(date(year, month, tuesday))
#     f_tuesdays = map(lambda x: date.strftime(x, '%d.%m.%Y'), f_tuesdays)
#     print() f_tuesdays
#
#
# print(*get_all_mondays(2021), sep='\n')



# from calendar import weekday, THURSDAY
# from datetime import datetime
#
# year = int(input())
# for month in range(1, 13):
#     for day in range(15, 22):
#         if weekday(year, month, day) == THURSDAY:
#             thursday = datetime(year, month, day)
#             print(thursday.strftime('%d.%m.%Y'))
#             break


# import calendar
# from datetime import datetime
#
# free_days = []
# year = int(input())
#
# for i in range(1, 13):
#     c = calendar.monthcalendar(year, i)
#     first_week = c[0]
#     third_week = c[2]
#     fourth_week = c[3]
#     if first_week[calendar.THURSDAY]:
#         free_day = third_week[calendar.THURSDAY]
#     else:
#         free_day = fourth_week[calendar.THURSDAY]
#     free_days.append(datetime(year, i, free_day))
#
# for day in free_days:
#     print(day.strftime('%d.%m.%Y'))






