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


