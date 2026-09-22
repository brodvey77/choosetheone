from datetime import date

class WeatherWarning:
    def rain(self):
        print('Ожидаются сильные дожди и ливни с грозой')

    def snow(self):
        print('Ожидается снег и усиление ветра')

    def low_temperature(self):
        print('Ожидается сильное понижение температуры')


class WeatherWarningWithDate(WeatherWarning):
    def rain(self, d):
        print(f'{date.strftime(d, "%d.%m.%Y")}\nОжидаются сильные дожди и ливни с грозой')

    def snow(self, d):
        print(f'{date.strftime(d, "%d.%m.%Y")}\nОжидается снег и усиление ветра')

    def low_temperature(self, d):
        print(f'{date.strftime(d, "%d.%m.%Y")}\nОжидается сильное понижение температуры')










from datetime import date

weatherwarning = WeatherWarningWithDate()
dt = date(2022, 12, 12)

weatherwarning.rain(dt)
weatherwarning.snow(dt)
weatherwarning.low_temperature(dt)

from datetime import date


class WeatherWarning:
    def _generic_warning(self, message, d):
        if d is not None:
            print(d.strftime('%d.%m.%Y'))
        print(message)

    def rain(self, d=None):
        self._generic_warning('Ожидаются сильные дожди и ливни с грозой', d)

    def snow(self, d=None):
        self._generic_warning('Ожидается снег и усиление ветра', d)

    def low_temperature(self, d=None):
        self._generic_warning('Ожидается сильное понижение температуры', d)


class WeatherWarningWithDate(WeatherWarning):
    pass