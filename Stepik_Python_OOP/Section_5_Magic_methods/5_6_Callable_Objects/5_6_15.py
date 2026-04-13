from datetime import  date

class DateFormatter:
    def __init__(self, country_code ):
        self.country_code = country_code

    def __call__(self, d):
        match self.country_code:
            case 'ru'|'fr':
                return date.strftime(d, '%d.%m.%Y')
            case 'us':
                return date.strftime(d, '%m-%d-%Y')
            case 'ca':
                return date.strftime(d, '%Y-%m-%d')
            case 'br':
                return date.strftime(d, '%d/%m/%Y')
            case 'pt':
                return date.strftime(d, '%d-%m-%Y')



ca_format = DateFormatter('ca')

print(ca_format(date(2022, 11, 7)))


from datetime import date


class DateFormatter:
    __COUNTRY_CODES = {
        'ru': '%d.%m.%Y',
        'fr': '%d.%m.%Y',
        'us': '%m-%d-%Y',
        'ca': '%Y-%m-%d',
        'br': '%d/%m/%Y',
        'pt': '%d-%m-%Y'
    }

    def __init__(self, country_code):
        self.country_code = country_code

    def __call__(self, d):
        return d.strftime(self.__COUNTRY_CODES[self.country_code])