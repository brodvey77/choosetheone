
class StrExtension:

    @classmethod
    def remove_vowels(cls, string):
        return ''.join(filter(lambda x: x not in 'aAeEiIoOuUyY', string))

    @classmethod
    def leave_alpha(cls, string):
        return ''.join(char for char in string if 'a' <= char <= 'z' or 'A' <= char <= 'Z')

    @classmethod
    def replace_all(cls, string, chars, char):
        return ''.join(char if i in chars else i for i in string)




print(StrExtension.remove_vowels('Python'))
print(StrExtension.remove_vowels('Stepik'))
print(StrExtension.leave_alpha('Python111'))
print(StrExtension.leave_alpha('__Stepik__()'))
print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))



import re


class StrExtension:
    __VOWELS = re.compile(r'[aeiouy]', flags=re.I)
    __ALPHABET = re.compile(r'[^a-zA-Z]')

    @staticmethod
    def remove_vowels(string):
        return StrExtension.__VOWELS.sub('', string)

    @staticmethod
    def leave_alpha(string):
        return StrExtension.__ALPHABET.sub('', string)

    @staticmethod
    def replace_all(string, chars, char):
        return re.sub(fr'[{chars}]', char, string)