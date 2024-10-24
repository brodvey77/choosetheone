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



from datetime import date, time

day, month, year = input('Введите дату в формате ДД.ММ.ГГГГ').split('.')
hour, minute, second = input('Введите время в формате ЧЧ:ММ:СС').split(':')

my_date = date(int(year), int(month), int(day))        # создаем объект типа date
my_time = time(int(hour), int(minute), int(second))    # создаем объект типа time

print(my_date)
print(my_time)



from datetime import date, time

while True:
    try:
        day, month, year = input('Введите дату в формате ДД.ММ.ГГГГ').split('.')

        my_date = date(int(year), int(month), int(day))

        print('Введена корректная дата:', my_date)
        break
    except:      # перехватываем любую ошибку
        print('Введенная дата не является корректной, попробуйте еще раз')



При создании новой даты-времени (тип datetime) нужно указать год, месяц, день, часы, минуты, секунды и микросекунды. При этом год, месяц и день являются обязательными, а часы, минуты, секунды и микросекунды необязательными.

Приведенный ниже код:

from datetime import datetime

my_datetime = datetime(1992, 10, 6, 9, 40, 23, 51204)    # создаем полную дату-время
only_date = datetime(2021, 12, 31)                       # создаем дату-время с нулевой временной информацией

print(my_datetime)
print(only_date)
print(type(my_datetime))


Конструктор типа datetime сначала принимает год, месяц, день, часы, минуты, секунды, а уже потом микросекунды. Мы также можем использовать именованные аргументы, нарушая указанный порядок datetime(day=6, month=10, year=1992, second=23, minute=40, microsecond=51204, hour=9).

Так же, как и при работе с типами date и time, пользуясь типом datetime, можно получать доступ к отдельным значениям созданной даты-времени: годам, месяцам, дням, часам, минутам, секундам и микросекундам. Получить доступ к ним можно с помощью атрибутов:

year — год
month — месяц
day — день
hour — час
minute — минуты
second — секунды
microsecond — микросекунды
Приведенный ниже код:

from datetime import datetime

my_datetime = datetime(1992, 10, 6, 9, 40, 23, 51204)

print('Год =', my_datetime.year)
print('Месяц =', my_datetime.month)
print('День =', my_datetime.day)
print('Часы =', my_datetime.hour)
print('Минуты =', my_datetime.minute)
print('Секунды =', my_datetime.second)
print('Микросекунды =', my_datetime.microsecond)


Методы combine(), date(), time()
Сформировать новый объект типа datetime можно с помощью двух разных объектов, представляющих дату и время (date и time). Для этого используется метод combine().

Приведенный ниже код:

from datetime import date, time, datetime

my_date = date(1992, 10, 6)
my_time = time(10, 45, 17)
my_datetime = datetime.combine(my_date, my_time)

print(my_datetime)


Если, наоборот, нужно получить из даты-времени (тип datetime) по отдельности дату (тип date) и время (тип time), то используются методы date() и time() соответственно.

Приведенный ниже код:

from datetime import date, time, datetime

my_datetime = datetime(2022, 10, 7, 14, 15, 45)
my_date = my_datetime.date()                     # получаем только дату (тип date)
my_time = my_datetime.time()                     # получаем только время (тип time)

print(my_datetime, type(my_datetime))
print(my_date, type(my_date))
print(my_time, type(my_time))



Методы now(), utcnow(), today()
Для того, что получить текущее время на момент исполнения программы, используются методы now() и utcnow() для локального и UTC времени соответственно.

Приведенный ниже код:

from datetime import datetime

datetime_now = datetime.now()
datetime_utcnow = datetime.utcnow()

print(datetime_now)           # текущее локальное время (московское) на момент запуска программы
print(datetime_utcnow)        # текущее UTC время на момент запуска программы


Метод timestamp()
Метод timestamp() позволяет преобразовать объект типа datetime в количество секунд, прошедших с момента начала эпохи. Данный метод возвращает значение типа float.
from datetime import datetime

my_datetime = datetime(2021, 10, 13, 8, 10, 23)

print(my_datetime.timestamp())
выводит:

1634101823.0


Метод fromtimestamp()
Метод fromtimestamp() позволяет преобразовать количество секунд, прошедших с момента начала эпохи, в объект типа datetime. Данный метод является обратным по отношению к методу timestamp().

Приведенный ниже код:

from datetime import datetime

my_datetime = datetime.fromtimestamp(1634101823.0)

print(my_datetime)
выводит:

2021-10-13 08:10:23
Обратите внимание на то, что метод fromtimestamp() по умолчанию возвращает объект datetime в вашем часовом поясе.

Форматирование даты-времени
По умолчанию объекты типа datetime (как и объекты типа date и time) выводятся в специальном формате, который называется ISO 8601. Данное представление не всегда удовлетворяет нашим запросам.

Чтобы преобразовать дату-время в строку нужного формата, следует воспользоваться методом strftime(), указав ему в качестве аргумента параметры форматирования.

from datetime import datetime

my_datetime = datetime(2021, 8, 10, 18, 20, 34)

print(my_datetime)                                            # вывод в ISO формате
print(my_datetime.strftime('%d.%m.%y --- %H::%M::%S'))
print(my_datetime.strftime('%d/%m/%y'))
print(my_datetime.strftime('%A %d, %B %Y'))
print(my_datetime.strftime('%H:%M:%S'))
выводит

2021-08-10 18:20:34
10.08.21 --- 18::20::34
10/08/21
Tuesday 10, August 2021
18:20:34
Для форматированного вывода объектов типов date, time, datetime используется один и тот же метод strftime()


Преобразование строки в дату-время
Как уже было сказано в прошлом уроке, преобразовать данные из строки в объект типа datetime можно двумя способами:

ручным преобразованием
с помощью метода strptime()
Ручной подход основан на использовании метода split():

from datetime import datetime

datetime_str = input('Введите дату/время в формате ДД.ММ.ГГГГ ЧЧ:ММ:СС')

date_str, time_str = datetime_str.split(' ')

date_info = [int(i) for i in date_str.split('.')]
time_info = [int(i) for i in time_str.split(':')]

my_datetime = datetime(date_info[2], date_info[1], date_info[0], time_info[0], time_info[1], time_info[2])

print(my_datetime)
На практике для преобразования строки в объект datetime редко используется ручной подход. Вместо него используется метод strptime(), который преобразует строку (первый аргумент) в объект datetime согласно переданному формату (второй аргумент).


Приведенный ниже код работает аналогично коду выше:

from datetime import datetime

datetime_str = input('Введите дату/время в формате ДД.ММ.ГГГГ ЧЧ:ММ:СС')

my_datetime = datetime.strptime(datetime_str, '%d.%m.%Y %H:%M:%S')

print(my_datetime)
Рассмотрим примеры работы данного метода.

Приведенный ниже код:

from datetime import datetime

datetime0 = datetime.strptime('10.08.2034 13:55:59', '%d.%m.%Y %H:%M:%S')
datetime1 = datetime.strptime('10/08/21', '%d/%m/%y')
datetime2 = datetime.strptime('Tuesday 10, August 2021', '%A %d, %B %Y')
datetime3 = datetime.strptime('18.20.34', '%H.%M.%S')
datetime4 = datetime.strptime('2021/08/10', '%Y/%m/%d')
datetime5 = datetime.strptime('10.08.2021 (Tuesday, August)', '%d.%m.%Y (%A, %B)')
datetime6 = datetime.strptime('Year: 2021, Month: 08, Day: 10, Hour: 18.', 'Year: %Y, Month: %m, Day: %d, Hour: %H.')

print(datetime0, datetime1, datetime2, datetime3, datetime4, datetime5, datetime6, sep='\n')
выводит:

2034-08-10 13:55:59
2021-08-10 00:00:00
2021-08-10 00:00:00
1900-01-01 18:20:34
2021-08-10 00:00:00
2021-08-10 00:00:00
2021-08-10 18:00:00


Обратите внимание на то, что первый аргумент должен соответствовать формату второго аргумента. Если он не соответствует, то возникает исключение ValueError.

В результате выполнения кода:

from datetime import datetime

my_datetime = datetime.strptime('10/08/2034 13:55:59', '%d.%m.%Y %H:%M:%S')

print(my_datetime)
мы получим:

ValueError: time data '10/08/2034 13:55:59' does not match format '%d.%m.%Y %H:%M:%S'


Примечание 7. Для того, чтобы использовать конкретную локализацию (перевод на язык), нужно использовать модуль locale. Приведенный ниже код устанавливает русскую локализацию:

from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

my_datetime = datetime(2021, 8, 10, 12, 34, 15)

print(my_datetime.strftime('%A %d, %B %Y, %H:%M:%S'))
и выводит:

вторник 10, Август 2021, 12:34:15
Для установки английской локализации используется код:

import locale

locale.setlocale(locale.LC_ALL, 'en_EN.UTF-8')
Почитать подробнее о модуле locale можно в официальной документации тут (английский язык) или тут (русский язык).


strptime - это парсер, который превращает произвольную строку в объект типа datetime

strftime - это форматтер, который превращает объект datetime в строку произвольного (заданного) формата


Тип данных timedelta
Тип данных timedelta представляет из себя временной интервал (разница между двумя объектами datetime или date) и используется для удобного выполнения различных манипуляций над типами datetime или date.

При создании объекта timedelta можно указать следующие аргументы:

недели (weeks)
дни (days)
часы (hours)
минуты (minutes)
секунды (seconds)
микросекунды (microseconds)
миллисекунды (milliseconds)
Мы можем выбрать любые их сочетания для задания временного интервала, при этом все аргументы являются необязательными и по умолчанию равны 0.


from datetime import timedelta

delta = timedelta(days=7, hours=20, minutes=7, seconds=17)

print(delta)
print(type(delta))

Аргументы могут быть целыми числами или числами с плавающей запятой, а также могут быть как положительными, так и
отрицательными. Используйте именованные аргументы, вместо позиционных, чтобы избежать ошибок.

Тип timedelta внутренне хранит только сочетание days, seconds, microseconds, а остальные переданные в конструктор аргументы конвертируются в эти единицы:

millisecond преобразуется в
1000
1000 microseconds
minutes преобразуется в
60
60 seconds
hours преобразуется в
3600
3600 seconds
weeks преобразуется в
7
7 days
Атрибуты days, seconds и microseconds затем нормализуются так, чтобы представление было уникальным:

0 <= microseconds < 1000000
0 <= seconds < 3600*24 (количество секунд в одном дне)
-999999999 <= days <= 999999999

В следующем примере показано, как любые аргументы, кроме days, seconds, microseconds, объединяются и нормализуются в три результирующих сочетания.

Приведенный ниже код:

from datetime import timedelta

delta1 = timedelta(days=50, seconds=27, microseconds=10, milliseconds=29000, minutes=5, hours=8, weeks=2)
delta2 = timedelta(weeks=1, hours=23, minutes=61)
delta3 = timedelta(hours=25)
delta4 = timedelta(minutes=300)

print(delta1, delta2, delta3, delta4, sep='\n')
выводит:

64 days, 8:05:56.000010
8 days, 0:01:00
1 day, 1:00:00
5:00:00


Атрибуты days, seconds, microseconds и метод total_seconds()
Как уже было сказано, тип timedelta внутренне хранит только сочетание days, seconds, microseconds, которые можно получить с помощью одноименных атрибутов.

Приведенный ниже код:

from datetime import timedelta

delta = timedelta(days=50, seconds=27, microseconds=10, milliseconds=29000, minutes=5, hours=8, weeks=2)

print('Количество дней =', delta.days)
print('Количество секунд =', delta.seconds)
print('Количество микросекунд =', delta.microseconds)

print('Общее количество секунд =', delta.total_seconds())
выводит:

Количество дней = 64
Количество секунд = 29156
Количество микросекунд = 10
Общее количество секунд = 5558756.00001
Метод total_seconds() возвращает общее количество секунд, содержащееся во временном интервалеtimedelta.

Обратите внимание на то, что у типа timedelta нет атрибутов hours и minutes, позволяющих получить количество часов и минут соответственно. Достать часы и минуты можно так:

def hours_minutes(td):
    return td.seconds // 3600, (td.seconds // 60) % 60
Приведенный ниже код:

from datetime import timedelta

def hours_minutes(td):
    return td.seconds // 3600, (td.seconds // 60) % 60

delta = timedelta(days=7, seconds=125, minutes=10, hours=8, weeks=2)

hours, minutes = hours_minutes(delta)

print(delta)
print(hours)
print(minutes)
выводит:

21 days, 8:12:05
8
12


Операции над временными интервалами timedelta
Тип данных timedelta поддерживает многие математические операции. Допустимо:

сложение временных интервалов
вычитание временных интервалов
умножение временного интервала на число
деление временного интервала на число
деление временного интервала на временной интервал
Сумма и разность временных интервалов
С помощью операторов + и - мы можем находить сумму и разность временных интервалов (тип timedelta).

Приведенный ниже код:

from datetime import timedelta

delta1 = timedelta(days=5) + timedelta(seconds=3600)  # 5 дней + 1 час
delta2 = timedelta(days=5) - timedelta(seconds=3600)  # 5 дней - 1 час

print(delta1)
print(delta2)
выводит:

5 days, 1:00:00
4 days, 23:00:00
Умножение временного интервала на число
С помощью оператора * мы можем умножать временной интервал (тип timedelta) на целое или вещественное число (типы int и float).

Приведенный ниже код:

from datetime import timedelta

delta1 = 48 * timedelta(hours=1)
delta2 = timedelta(weeks=1) * (3/7)

print(delta1)
print(delta2)
выводит:

2 days, 0:00:00
3 days, 0:00:00
Будьте осторожны с умножением временного интервала на вещественное число (тип float), так как может возникнуть округление.

Деление временных интервалов на число
С помощью операторов / и // мы можем делить временной интервал (тип timedelta) на целое или вещественное число (типы int и float).

Приведенный ниже код:

from datetime import timedelta

delta = timedelta(hours=1, minutes=6)
delta1 = delta / 2
delta2 = delta // 5

print(delta1)
print(delta2)
выводит:

0:33:00
0:13:12
Деление временного интервала на временной интервал
С помощью операторов / и // мы также можем делить один временной интервал (тип timedelta) на другой. По сути происходит деление общей длительности одного интервала на общую длительность другого интервала.

Приведенный ниже код:

from datetime import timedelta

delta1 = timedelta(weeks=1) / timedelta(hours=5)       # обычное деление, результат float
delta2 = timedelta(weeks=1) // timedelta(hours=5)      # целочисленное деление, результат int

print(delta1)
print(delta2)
выводит:

33.6
33
   Общая длительность временного интервала вычисляется с помощью метода total_seconds().

Мы также можем использовать оператор нахождения остатка от деления %, при этом остаток вычисляется как объект timedelta.

Приведенный ниже код:

from datetime import timedelta

delta1 = timedelta(weeks=1) % timedelta(hours=5)         # 3 часа
delta2 = timedelta(hours=1) % timedelta(minutes=7)       # 4 минуты

print(delta1)
print(delta2)
выводит:

3:00:00
0:04:00
Рассмотрим следующую задачу: рабочая смена длится
7
7 часов
30
30 минут, сколько полных смен в
3
3-х сутках?

Решение. Приведенный ниже код решает поставленную задачу:

from datetime import timedelta

all_time = timedelta(days=3)
smena = timedelta(hours=7, minutes=30)

print(all_time // smena)
print(all_time % smena)
и выводит:

9
4:30:00
Таким образом, в
3
3-х сутках помещается
9
9 полных смен и еще останется
4
4 часа
30
30 минут.

Операции над datetime и date


Операции над datetime и date
К объектам типа datetime и date можно прибавлять (вычитать) временные интервалы (тип timedelta), тем самым формируя новые объекты.

Приведенный ниже код:

from datetime import datetime, date, timedelta

my_datetime1 = datetime(2021, 1, 1, 12, 15, 20) + timedelta(weeks=1, hours=25)
my_datetime2 = datetime(2021, 1, 1, 12, 15, 20) - timedelta(weeks=1, hours=25)

my_date1 = date(2021, 1, 1) + timedelta(hours=49)
my_date2 = date(2021, 1, 1) - timedelta(hours=49)

print(my_datetime1, my_datetime2, my_date1, my_date2, sep='\n')
выводит:

2021-01-09 13:15:20
2020-12-24 11:15:20
2021-01-03
2020-12-30
   Обратите внимание на то, что при прибавлении временного интервала к дате (тип date) неполные сутки отбрасываются.

Объект типа timedelta также возникает при вычитании двух дат (тип date) или дат-времён (тип datetime).

Приведенный ниже код:

from datetime import datetime, date, timedelta

delta1 = datetime(2021, 1, 1, 12, 15, 20) - datetime(2020, 5, 1, 10, 5, 10)
delta2 = date(2020, 2, 29) - date(2019, 9, 1)
delta3 = date(2019, 9, 1) - date(2020, 2, 29)

print(delta1)
print(delta2)
print(delta3)
выводит:

245 days, 2:10:10
181 days, 0:00:00
-181 days, 0:00:00
Примечания
Примечание 1. Мы можем использовать встроенные функции str() и repr() для преобразования объектов типа timedelta к строковому типу.

Приведенный ниже код:

from datetime import timedelta

delta1 = timedelta(weeks=1, hours=23, minutes=61)
delta2 = timedelta(minutes=-300)

print(str(delta1), str(delta2), sep='\n')
print(repr(delta1), repr(delta2), sep='\n')
выводит:

8 days, 0:01:00
-1 day, 19:00:00
datetime.timedelta(days=8, seconds=60)
datetime.timedelta(days=-1, seconds=68400)
Обратите внимание на то, что при печати значения объекта timedelta с помощью функции print() функция str() вызывается автоматически.

Примечание 2. При работе с типом timedelta мы можем использовать встроенную функцию abs(). Функция возвращает объект timedelta с положительным значением всех атрибутов.

 Приведенный ниже код:

from datetime import timedelta

delta = timedelta(days=-2, minutes=-300)
abs_delta = abs(delta)

print('Исходная:', delta.days, delta.seconds, delta, sep='\n')
print('С модулем:', abs_delta.days, abs_delta.seconds, abs_delta, sep='\n')
выводит:

Исходная:
-3
68400
-3 days, 19:00:00
С модулем:
2
18000
2 days, 5:00:00
Примечание 3. Тип данных timedelta является неизменяемым.

Примечание 4. Документация по модулю datetime доступна по ссылке.








