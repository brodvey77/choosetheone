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

import re
s = 'Order 1: B938274, Order 2: T8372, Order 3: g883929'
pattern1 = re.compile('[A-Za-z]\d{4}')
for i in pattern1.findall(s):
    print(i)