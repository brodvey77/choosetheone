from enum import Enum

class Seasons(Enum):
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    FALL = 4


    def text_value(self, code):
        translations = {
            'ru': {
                1: 'зима',
                2: 'весна',
                3: 'лето',
                4: 'осень'
            },
            'en': {
                1: 'winter',
                2: 'spring',
                3: 'summer',
                4: 'fall'
            }
        }
        if code == 'ru':
            return translations['ru'][self.value]
        if code == 'en':
            return translations['en'][self.value]

print(Seasons.FALL.text_value('ru'))
print(Seasons.FALL.text_value('en'))

from enum import Enum


class Seasons(Enum):
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    FALL = 4

    def text_value(self, country_code):
        if country_code == 'en':
            return self.name.lower()
        else:
            return ['зима', 'весна', 'лето', 'осень'][self.value - 1]



from enum import Enum, auto


class Seasons(Enum):
    WINTER = auto()
    SPRING = auto()
    SUMMER = auto()
    FALL = auto()

    def text_value(self, country_code):
        seasons_translate = {
            'en': {
                self.WINTER: 'winter',
                self.SPRING: 'spring',
                self.SUMMER: 'summer',
                self.FALL: 'fall'
            },
            'ru': {
                self.WINTER: 'зима',
                self.SPRING: 'весна',
                self.SUMMER: 'лето',
                self.FALL: 'осень'
            },
        }
        return seasons_translate[country_code][self]






