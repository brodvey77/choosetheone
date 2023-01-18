from datetime import date

my_date = date(1992, 10, 6)    # тип date: год + месяц + день

print(my_date)
print(type(my_date))


from datetime import date

my_date = date(1992, 10, 6)

print('Год =', my_date.year)
print('Месяц =', my_date.month)
print('День =', my_date.day)

import datetime
d = datetime.date.today()
print(f'{d.day}-{d.month}-{d.year}')

from datetime import date

date1 = date(2022, 10, 15)
date2 = date(1983, 6, 4)

print(date1.weekday())
print(date2.weekday())


from datetime import date

date1 = date(2022, 10, 15)
date2 = date(1999, 12, 26)

print(date1.isoweekday())
print(date2.isoweekday())


from datetime import date

print(date.min)
print(date.max)

Методы fromordinal() и toordinal() позволяют создать дату из номера дня, начиная с 0001-01-01, и наоборот, преобразовать дату в номер дня.

from datetime import date

date1 = date.fromordinal(365)     # дата, соответствуюшая номеру дня 365
date2 = date(1999, 12, 26)

print(date1)
print(date2.toordinal())          # номер дня, соответствующий дате 1999-12-26


Микросекунда (мкс) — единица времени, равная одной миллионной доле секунды
При создании времени (тип данных time) нужно указать часы, минуты, секунды и микросекунды.

from datetime import time

my_time = time(11, 20, 54, 1234)    # тип time: часы + минуты + секунды + микросекунды

print(my_time)
print(type(my_time))


from datetime import time

time1 = time(11, 20, 54, 1234)
time2 = time(11, 20, 54)
time3 = time(11, 20)
time4 = time(11)
time5 = time()
time6 = time(minute=23, second=56)

print(time1, time2, time3, time4, time5, sep='\n')
print(time6)

hour — часы времени
minute — минуты времени
second — секунды времени
microsecond — микросекунды времени


from datetime import time

my_time = time(11, 20, 54, 1234)

print('Часы =', my_time.hour)
print('Минуты =', my_time.minute)
print('Секунды =', my_time.second)
print('Микросекунды =', my_time.microsecond)

from datetime import date, time

date1 = date(2022, 10, 15)
date2 = date(1999, 12, 26)

time1 = time(13, 10, 5)
time2 = time(21, 32, 59)

print(date1 < date2)
print(time1 < time2)


Встроенная функция str() возвращает объект в неформальном (понятном человеку) строковом представлении.
Встроенная функция repr() возвращает объект в формальном (понятном интерпретатору) строковом представлении.

from datetime import date, time

my_date = date(2021, 12, 31)
my_time = time(11, 20, 54)

print(my_date)
print(my_time)


from datetime import date, time

my_date = date(2021, 12, 31)
my_time = time(11, 20, 54)

print(str(my_date))
print(str(my_time))

from datetime import date, time

my_date = date(2021, 12, 31)
my_time = time(11, 20, 54)

print(repr(my_date))
print(repr(my_time))

from datetime import date

dates = [date(2021, 12, 31), date(2019, 10, 6), date(2022, 11, 8)]   # список дат

print(dates)

from datetime import date

dates = [date(2021, 12, 31), date(2019, 10, 6), date(2022, 11, 8)]

print(*dates, sep='\n')

from datetime import date

my_set = {date(2021, 12, 31), date(2019, 3, 19), date(2022, 5, 25)}                # множество
my_dict = {date(2021, 12, 31): 'Новый год', date(2030, 10, 6): 'День рождения'}    # словарь

print(my_set)
print(my_dict)

Мы можем использовать встроенные функции min(), max(), sorted() и т.д. при работе с типами данных date и time

from datetime import date, time

dates = [date(2021, 12, 31), date(2025, 3, 19), date(2017, 5, 25)]

print(min(dates))
print(max(dates))
print(sorted(dates))

Для создания новой даты на основании уже существующей можно использовать встроенный метод replace(). Он возвращает новую дату с переданными измененными значениями свойств year, month, day

from datetime import date

date1 = date(1992, 10, 6)
date2 = date1.replace(year=1995)            # заменяем год
date3 = date1.replace(month=12, day=17)     # заменяем месяц и число

print(date1)
print(date2)
print(date3)

from datetime import time

time1 = time(17, 10, 6)
time2 = time1.replace(hour=21)                  # заменяем час
time3 = time1.replace(minute=48, second=59)     # заменяем минуты и секунды

print(time1)
print(time2)
print(time3)

В качестве ограничений по годам в типе date используются значения MINYEAR=1 и MAXYEAR=9999

Помните про ограничения на атрибуты (year, month, day, hour, minute, second, microsecond), которые используете для создания объектов типов date и time. В случае использования неверного значения возникнет ошибка (исключение) ValueError

from datetime import date

my_date = date(2021, 19, 7)     # несуществующий месяц

print(my_date)

По умолчанию объекты типов date и time выводятся в ISO 8601 формате:

дата в формате ISO 8601 имеет вид: YYYY-MM-DD
время в формате ISO 8601 имеет вид: HH:MM:SS или HH:MM:SS.ffffff




Для форматированного вывода даты и времени используется метод strftime() (для обоих типов date и time).

from datetime import date, time

my_date = date(2021, 8, 10)
my_time = time(7, 18, 34)

print(my_date)                             # вывод в ISO формате
print(my_time)                             # вывод в ISO формате

print(my_date.strftime('%d/%m/%y'))        # форматированный вывод даты
print(my_date.strftime('%A %d, %B %Y'))    # форматированный вывод даты
print(my_time.strftime('%H.%M.%S'))        # форматированный вывод времени

выводит:

2021-08-10
07:18:34
10/08/21
Tuesday 10, August 2021
07.18.34

Приведенный ниже код:

from datetime import date, time

my_date = date(2021, 8, 10)
my_time = time(7, 18, 34)

print(my_date.strftime('%a %A %w %d %b %B %m %y %Y %H %I %p %M %S %f %z %Z %j %U %W %c %x %X'))
print(my_time.strftime('%a %A %w %d %b %B %m %y %Y %H %I %p %M %S %f %z %Z %j %U %W %c %x %X'))
выводит:

Tue Tuesday 2 10 Aug August 08 21 2021 00 12 AM 00 00 000000   222 32 32 Tue Aug 10 00:00:00 2021 08/10/21 00:00:00
Mon Monday 1 01 Jan January 01 00 1900 07 07 AM 18 34 000000   001 00 01 Mon Jan  1 07:18:34 1900 01/01/00 07:18:34



Использование локализации
Для того чтобы использовать конкретную локализацию (перевод на язык), нужно использовать модуль locale.

Приведенный ниже код устанавливает русскую локализацию:

from datetime import date
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

my_date = date(2021, 8, 10)
print(my_date.strftime("%A %d, %B %Y"))    # форматированный вывод даты в русской локализации
и выводит:

вторник 10, Август 2021
Для установки английской локализации используется код:

import locale

locale.setlocale(locale.LC_ALL, 'en_EN.UTF-8')
Почитать подробнее о модуле locale можно в официальной документации тут (английский язык) или тут (русский язык).

