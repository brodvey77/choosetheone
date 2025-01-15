# import sys
# from re import search, match, fullmatch
# pattern = r'(?P<country>\d{1,3})[ -](?P<city>\d{1,3})[ -](?P<number>\d{4,10})'
#
# for i in sys.stdin:
#     match1 = fullmatch(pattern, i.strip())
#     print(f'Код страны: {match1.group("country")}, Код города: {match1.group("city")}, Номер: {match1.group("number")}')


# import sys
# from re import search, fullmatch
#
# pattern = r'_\d+[A-Za-z]*_?$'
#
# for login in sys.stdin:
#     match1 = fullmatch(pattern, login.strip())
#     if match1:
#         print(True)

# import sys
# from re import search, match, fullmatch
#
# pattern = r'^(\w+)\1$'
#
# for word in sys.stdin:
#     match1 = fullmatch(pattern, word.strip('\n'))
#     if match1:
#         print(f'{match1.group()}')
#
#
#
# import sys
# import re
#
# for line in map(str.rstrip, sys.stdin):
#     if re.fullmatch(r'(\w+)\1', line):
#         print(line)