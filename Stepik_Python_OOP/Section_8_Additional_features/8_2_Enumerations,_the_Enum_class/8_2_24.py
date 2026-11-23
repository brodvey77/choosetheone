from enum import Enum
from datetime import date, datetime, timedelta


class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class NextDate:
    def __init__(self, today, weekday=Weekday, considering_today=False):
        self.today = today
        self.weekday = weekday
        self.considering_today = considering_today


    def date(self):
        current = self.today.weekday()
        target = self.weekday.value

        diff = (target - current) % 7

        if diff == 0:
            if self.considering_today:
                return self.today
            else:
                return self.today + timedelta(days=7)
        return self.today + timedelta(days=diff)

    def days_until(self):
        return (self.date() - self.today).days




# from datetime import date
#
# today = date(2023, 4, 17)                              # понедельник
# next_friday = NextDate(today, Weekday.FRIDAY)          # следующая пятница
#
# print(next_friday.date())
# print(next_friday.days_until())


# from datetime import date
#
# today = date(2023, 4, 17)                              # понедельник
# next_monday = NextDate(today, Weekday.MONDAY)          # следующий понедельник без учета текущего
#
# print(next_monday.date())
# print(next_monday.days_until())


from datetime import date

today = date(2023, 4, 17)                              # понедельник
next_monday = NextDate(today, Weekday.MONDAY, True)    # следующий понедельник с учетом текущего

print(next_monday.date())
print(next_monday.days_until())


from datetime import timedelta
from enum import IntEnum

Weekday = IntEnum('Weekday', ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'], start=0)


class NextDate:
    def __init__(self, today, weekday, after_today=False):
        self.today = today
        self.weekday = weekday
        self.after_today = after_today

    def date(self):
        next_date = self.today + timedelta((self.weekday - self.today.weekday()) % 7)
        if not self.after_today and next_date == self.today:
            next_date += timedelta(7)
        return next_date

    def days_until(self):
        return (self.date() - self.today).days



