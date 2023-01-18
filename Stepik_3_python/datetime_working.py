# from datetime import date
#
# dates = [date(2000, 12, 31), date(1999, 3, 8), date(1999, 2, 22)]
#
# max_date = max(dates)
# min_date = min(dates)
#
# print(max_date.year + min_date.day)

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