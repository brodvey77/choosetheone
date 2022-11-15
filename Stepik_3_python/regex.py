# import re
#
# text = input()
#
# pattern1 = re.compile('7-\d{3}-\d{3}-\d{2}-\d{2}|8-\d{3}-\d{4}-\d{4}')
#
# for i in pattern1.findall(text):
#     print(i)
#
# s = 'Beegek beegeek BEEGEEK bEeGeEk beegeek'
#
# regex = r'beegeek'
#
# print(regex)
# import re
# s = 'Order 1: B938274, Order 2: T8372, Order 3: g883929'
# pattern1 = re.compile('[A-Za-z]\d{4}')
# for i in pattern1.findall(s):
#     print(i)

# import re
# s = 'Stood u1pPP'
# pattern1 = re.compile('[a-z]\d[a-z][A-Z]{2}')
# for i in pattern1.findall(s):
#     print(i)

# import re
# s = 'What password do you prefer: 9ython or 4uTUMN?'
# pattern1 = re.compile('\d[aeiouy][^bcDF]\S[^AEIOUY][^.,]')
# for i in pattern1.findall(s):
#     print(i)

# import re
# s = 'Home: +7 927 991 13 31 Work: +7(917)-634-81-19 Alice: +89119873582 Arthur: +7(987)6639481 Timur: +79176879054'
# pattern1 = re.compile('\+7\d{10}|\+7\(\d{3}\)\d{7}|\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}|\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}')
# for i in pattern1.findall(s):
#     print(i)


# import re
# s = 'a4:44, ba:oa, 13-33, 18:57, 181:57, 18:571'
# pattern1 = re.compile('[0-1]\d:[0-5]\d|2[0-3]:[0-5]\d')
# for i in pattern1.findall(s):
#     print(i)

# regex = r'[0-1]\d:[0-5]\d|2[0-3]:[0-5]\d'


# \b(?:[01][0-9]|2[0-3]):[0-5][0-9]\b

# \b - граница слова
# (?:[01][0-9]|2[0-3]) - 0 или 1 и любая цифра или 2 и цифра от одного до трёх
# : - символ :
# [0-5][0-9] - цифра от нуля до пяти и любая цифра
# \b - граница слова


import re
s = 'a4:44, ba:oa, 13-33, 18:57, 181:57, 18:571'
pattern1 = re.compile('[0-1]\d:[0-5]\d|2[0-3]:[0-5]\d')
for i in pattern1.findall(s):
    print(i)
