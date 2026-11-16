from abc import ABC, abstractmethod
from datetime import datetime as dt, date


class Dates(ABC):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def to_date(self):
        return date(self.year, self.month, self.day)

    @abstractmethod
    def format(self):
        pass

    @abstractmethod
    def iso_format(self):
        pass


class USADate (Dates):


    def format(self):
        return self.to_date().strftime('%m-%d-%Y')

    def iso_format(self):
        return self.to_date().strftime('%Y-%m-%d')


class ItalianDate(Dates):


    def format(self):
        return self.to_date().strftime('%d/%m/%Y')

    def iso_format(self):
        return self.to_date().strftime('%Y-%m-%d')



usadate = USADate(2023, 4, 6)

print(usadate.format())
print(usadate.iso_format())


italiandate = ItalianDate(2023, 4, 6)

print(italiandate.format())
print(italiandate.iso_format())



from abc import ABC, abstractmethod
from datetime import date


class DateFormat(ABC):
    def __init__(self, year, month, day):
        self._date = date(year, month, day)

    def iso_format(self):
        return self._date.isoformat()

    @abstractmethod
    def format(self):
        pass


class USADate(DateFormat):
    def format(self):
        return self._date.strftime('%m-%d-%Y')


class ItalianDate(DateFormat):
    def format(self):
        return self._date.strftime('%d/%m/%Y')