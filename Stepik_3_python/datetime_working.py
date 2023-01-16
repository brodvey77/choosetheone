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



