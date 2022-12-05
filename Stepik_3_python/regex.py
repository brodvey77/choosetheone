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


# import re
# s = 'a4:44, ba:oa, 13-33, 18:57, 181:57, 18:571'
# pattern1 = re.compile('[0-1]\d:[0-5]\d|2[0-3]:[0-5]\d')
# for i in pattern1.findall(s):
#     print(i)

# from re import search
#
# match1 = search(r'\w+', 'Hello, Timur')
#
# print(match1.group() if match1 else None)

# from re import match
#
# match1 = match(r'[Hh]\w+', 'hello, Timur')
# match2 = match(r'[Tt]\w+', 'hello, Timur')
#
# print(match1.group() if match1 else None)
# print(match2.group() if match2 else None)


# from re import fullmatch
#
# match1 = fullmatch(r'[Hh]\w+ [Tt]\w+', 'Hello, Timur')
# match2 = fullmatch(r'[Hh]\w+, [Tt]\w+', 'Hello, Timur')
#
# print(match1.group() if match1 else None)
# print(match2.group() if match2 else None)


# from re import fullmatch
#
# match1 = fullmatch(r'(-)?(\d+)', '2077')
# match2 = fullmatch(r'(-)?(\d+)', '-1337')
#
# print(match1.group(1))
# print(match1.group(2))
# print(match2.group(1, 2))

# import sys
#
# for line in sys.stdin:
#     print(line.strip('\n'))

# import sys
#
# print('Python')
#
# sys.stdout = open('file.txt', 'w')
#
# print('is')
# print('Power')

# import sys
#
# for line in sys.stdin:
#     print(line[::-1].strip('\n'))

# import sys
# from re import search
#
#
# # text = sys.stdin.readline().strip('\n')
# #
# match_1 = search(r'(?P<Country>\w+),(?P<City>\w+),(?P<number>\w+)', 'asd,asdasd,asdasd')
#
# print(match_1.groupdict())

# import sys
# from re import fullmatch
#
# flag = ' '
# for text in sys.stdin:
#     text = text.strip('\n')
#     if ' ' not in text:
#         flag = '-'
#
#     regex = r'\d{1,3}-\d{1,3}-\d{4,10}|\d{1,3} \d{1,3} \d{4,10}'
#
#     match_1 = fullmatch(regex, text)
#     # print(match_1.group())
#     if match_1:
#         text = text.split(flag)
#         print(f'Код страны: {text[0]} Код города: {text[1]}, Номер: {text[2]}')
#     else:
#         print('нет совпадения')
# flag = ' '


# from re import match
# from sys import stdin
#
# regex = r'(?P<A>\d+)[ -](?P<B>\d+)[ -](?P<C>\d+)'
#
# for line in stdin:
#     a, b, c = match(regex, line).groupdict().values()
#     print(f'Код страны: {a}, Код города: {b}, Номер: {c}')

# import sys
# from re import search, fullmatch
#
# for line in sys.stdin:
#     match = search("(\d{1,3})[ -](\d{1,3})[ -](\d{4,10})", line)
#     print(f"Код страны: {match.group(1)}, Код города: {match.group(2)}, Номер: {match.group(3)}")



# import sys
# from re import search
#
# for line in sys.stdin:
#     match = search('(\d{1,3})[ -](\d{1,3})[ -](\d{4,10})', line)
#     print(f'Код страны: {match.group(1)}, Код города: {match.group(2)}, Номер: {match.group(3)}')

# import sys
# from re import fullmatch
#
# for line in sys.stdin:
#     match = fullmatch('_\d+[a-zA-Z]*_?', line.strip('\n'))
#     print(bool(match))

# import sys
# from re import fullmatch
#
# for line in sys.stdin:
#     match = fullmatch(r'(\w+)\1', line.strip('\n'))
#     if match:
#         print(match.group())
#     else:
#         continue
#
# import sys
# from re import search
#
# for line in sys.stdin:
#     print(line)
#     match = search(r'\b(geek)\b', line)
#     print(match)


# import sys
# from re import search
# c1 = 00
# c2 = 0

# for line in sys.stdin:
#     match_1 = search(r'.*bee.*bee.*', line.strip('\n'))
#     if match_1:
#         c1 += 1
#     match_2 = search(r'\bgeek\b', line.strip('\n'))
#     if match_2:
#         c2 += 1
# print(c1, c2, sep='\n')

# import sys
# from re import fullmatch, search
#
# counter = 0
#
# for line in sys.stdin:
#     match1 = fullmatch(r"^(beegeek).*\1$", line.strip('\n'))
#     match2 = search(r"^(beegeek).+[^k]$|^[^b].+(beegeek)$", line.strip('\n'))
#     match3 = search(r"^[^b].+beegeek.", line.strip('\n'))
#     match5 = fullmatch(r"^beegeek$", line.strip('\n'))
#     if match1:
#         counter += 3
#     if match2:
#         counter += 2
#     if match3:
#         counter += 1
#     if match5:
#         counter += 2
#     print(counter)
#
# print(counter)
#
# patterns = [
#     r"^beegeek.*beegeek$",
#     r"^beegeek.*|.*beegeek$",
#     r".*beegeek.*"
# ]



# from re import fullmatch, IGNORECASE
#
# match1 = fullmatch('beegeek', 'BeeGeek', flags=IGNORECASE)
#
# print(match1.group() if match1 else None)

# from re import fullmatch, DOTALL
#
# match1 = fullmatch('.+', 'beegeek\npython\nstepik', flags=DOTALL)
#
# print(match1.group() if match1 else None)

# from re import search, MULTILINE, IGNORECASE
#
# text = '''Flat is better than nested.
# Now is better than never.
# Readability counts.'''
#
# match1 = search('^read', text, flags=MULTILINE | IGNORECASE)
#
# print(match1.group() if match1 else None)

#
# from re import escape
#
# print(escape(r'\\'))
# print(escape('\\'))
# import sys
# import re
#
# kind_words = ['^Здравствуйте.*', '^Доброе утро.*', '^Добрый день.*', '^Добрый вечер.*']
#
# for line in sys.stdin:
#     match = re.search('^Здравствуйте.*', line)

# from re import findall, finditer
#
# result1 = findall(r'\w', 'beegeek')
# result2 = finditer(r'\w', 'beegeek')
#
# match1, *_ = result1
# match2, *_ = result2
#
# print(type(match1))
# print(type(match2))

# from re import findall
#
# result = findall(r'[Bb]\w+', 'But that bee can only bite once')
#
# print(result)

#
# from re import findall
#
# result = findall(r'__(\w+)__', 'They are surrounded by double underscores: __init__ or __add__')
#
# print(result)


# from re import findall
#
# result = findall(r'(\w+)-(\w+)', 'ex-wife, self-made, twenty-six')
#
# print(result)


# from re import finditer
#
# result = finditer(r'[Pp]\w+', 'Purse men of genuine python skin (the dorsal part)')
#
# for match_obj in result:
#     print(match_obj.group())


# from re import finditer
#
# result = finditer(r'A(\w+)', 'Timur, Arthur, Dima, Anri, Ruslan')
#
# for match_obj in result:
#     print(match_obj.group())


# from re import finditer
#
# result = finditer(r'(\d\d):(\d\d)', 'You can call me from 10:00 to 12:00')
#
# for match_obj in result:
#     print(match_obj.groups())

# import re
# article = '''Stepik (до августа 2016 года Stepic) — это образовательная платформа и конструктор онлайн-курсов!
#
# Первые образовательные материалы были выпущены на Stepik 3 сентября 2013 года.
# В январе 2016 года Stepik выпустил мобильные приложения под iOS и Android. В 2017 году разработаны мобильные приложения для изучения ПДД в адаптивном режиме для iOS и Android...
#
# На октябрь 2020 года на платформе зарегистрировано 5 миллионов пользователей!
# Stepik позволяет любому зарегистрированному пользователю создавать интерактивные обучающие уроки и онлайн-курсы, используя видео, тексты и разнообразные задачи с автоматической проверкой и моментальной обратной связью.
#
# Проект сотрудничает как с образовательными учреждениями, так и c индивидуальными преподавателями и авторами.
# Stepik сегодня предлагает онлайн-курсы от образовательных организаций, а также индивидуальных авторов!
#
# Система автоматизированной проверки задач Stepik была использована в ряде курсов на платформе Coursera, включая курсы по биоинформатике от Калифорнийского университета в Сан-Диего и курс по анализу данных от НИУ «Высшая школа экономики»...
#
# Stepik также может функционировать как площадка для проведения конкурсов и олимпиад, среди проведённых мероприятий — отборочный этап Олимпиады НТИ (2016—2020) (всероссийской инженерной олимпиады школьников, в рамках программы Национальная технологическая инициатива), онлайн-этап акции Тотальный диктант в 2017 году, соревнования по информационной безопасности StepCTF-2015...'''
#
# result1 = re.findall(r'^stepik.*', article, re.I|re.M)
# result2 = re.findall(r'.*\.\.\.$|.*!$', article, re.I|re.M)
# print(len(result1), len(result2), sep='\n')

# import re
# text = input()
# podtext = f'\B{input()}\B'
#
# result = re.finditer(podtext, text)
#
# print(len(list(result)))


# import re
# text = input()
# word = rf'\b{input()}\b'
# print(word)
#
# print(len(re.findall(word, text)))

# import re
#
# s, word = input(), input()
# print(len(re.findall(r'\b'+word+r'\b', s)))

# import re
#
# word = input()
# word = rf'\b+{word[:-2]}+[zs]+e'
# text = input()
#
# print(word[:-2])
# result = re.findall(word, text)
#
# print(len(result))

# gthese
# gthsese Gthese gthese ggthese ggtheze gtheze

#
# import re
#
# word = input()
# word = rf'\b{word[:-2]}u?r\b'
# text = input()
#
# result = re.findall(word, text)
# print(len(result))

# import re
# def abbreviate(phrase):
#     abv = re.findall(r'\b\w|[A-Z]', str(phrase))
#     return ''.join(abv).upper()
#
# text = input()
# print(abbreviate(re.findall(r'\'([A-Za-z\s]+)\'', text)))
#
#
# import re
#
# def abbreviate(phrase):
#     return ''.join(re.findall(r'[A-Z]|\b\w',phrase)).upper()


# import re
# import sys
#
# for text in sys.stdin:
#     l1 = []
#     l2 = []
#     a = re.findall(r'<a>?(.+)</a>', text)
#     for i in a:
#         link1 = re.findall(r'\"(.+)\"', i)
#         l1.append(*link1)
#
#     for i in a:
#         link2 = re.findall(r'>(.+)$', i)
#         l2.append(*link2)
#
#     result = [f'{i}, {j}' for i, j in zip(l1, l2)]
#
#     for i in result:
#         print(i)
#


# import sys
# import re
#
# text = sys.stdin.read()
# pattern = r'<a href="(.+)">(.+)</a>'
#
# for address, pointer in re.findall(pattern, text):
#     print(f'{address}, {pointer}')