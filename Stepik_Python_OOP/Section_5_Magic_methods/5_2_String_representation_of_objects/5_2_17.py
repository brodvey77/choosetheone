
class PhoneNumber:
    def __init__(self, phone_number):
        self.phone_number = phone_number.replace(' ', '')

    def __str__(self):
        return f"({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}"

    def __repr__(self):
        return f"PhoneNumber('{self.phone_number}')"

phone = PhoneNumber('9173963385')

print(str(phone))
print(repr(phone))

print('=' * 40)

phone = PhoneNumber('918 396 3389')

print(str(phone))
print(repr(phone))

print('=' * 40)

phone1 = PhoneNumber('9173963385')
phone2 = PhoneNumber('918 396 3389')
phone3 = PhoneNumber('919 333 3344')

print(phone1, phone2, phone3, sep=', ')
print([phone1, phone2, phone3])

import re


class PhoneNumber:
    def __init__(self, phone_number):
        if PhoneNumber.is_correct(phone_number):
            self.phone_number = phone_number.replace(' ', '')

    @staticmethod
    def is_correct(string):
        if re.fullmatch(r"\d{10}|\d{3} \d{3} \d{4}", string):
            return True
        else:
            return False

    def __str__(self):
        return f"({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.phone_number}')"