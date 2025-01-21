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

# import sys
# import re
#
# bee = geek = 0
#
# for line in sys.stdin:
#     if re.search(r'bee.*bee', line):
#         bee += 1
#     if re.search(r'\bgeek\b', line):
#         geek += 1
#
# print(bee)
# print(geek)

# import re
#
# message = input()
# pattern = r"^Здравствуйте|^Доброе утро|^Добрый (день|вечер).*"
#
# match = re.match(pattern, message, re.I)
# print(bool(match))
#
#
# import sys
# from re import search, IGNORECASE, MULTILINE
#
#
#
# for line in sys.stdin:
#     match = search('^Здравствуйте.*|^Доброе утро.*|^Добрый день.*|Добрый вечер.*', line, flags=IGNORECASE|MULTILINE)
#     print(bool(match))

# import sys
# import re
#
# pattern = r'beegeek'
# counter = 0
#
# for line in sys.stdin:
#     match = re.search(pattern, line, re.I)
#     if match:
#         counter += 1
#
# print(counter)
#
#
# import sys
# import re
# counter = 0
# for line in sys.stdin:
#     counter += bool(re.search('beegeek', line, re.I))
#
# print(counter)


# from re import findall, finditer
#
# result1 = findall(r'\w', 'beegeek')
# result2 = finditer(r'\w', 'beegeek')
#
# print(result1)
# print(list(result2))
#
#
# match1, *_ = result1
# # match2, *_ = result2
#
# print(match1)
# print(_)
# print(match2)


# print(type(match1))
# print(type(match2))

# from re import finditer
#
# result = finditer(r'(\d\d):(\d\d)', 'You can call me from 10:00 to 12:00')
#
# for match_obj in result:
#     print(match_obj.groups())


# import re
# article = '''Stepik (до августа 2016 года Stepic) — это образовательная платформа и конструктор онлайн-курсов!

# Первые образовательные материалы были выпущены на Stepik 3 сентября 2013 года.
# В январе 2016 года Stepik выпустил мобильные приложения под iOS и Android. В 2017 году разработаны мобильные приложения для изучения ПДД в адаптивном режиме для iOS и Android...

# На октябрь 2020 года на платформе зарегистрировано 5 миллионов пользователей!
# Stepik позволяет любому зарегистрированному пользователю создавать интерактивные обучающие уроки и онлайн-курсы, используя видео, тексты и разнообразные задачи с автоматической проверкой и моментальной обратной связью.

# Проект сотрудничает как с образовательными учреждениями, так и c индивидуальными преподавателями и авторами.
# Stepik сегодня предлагает онлайн-курсы от образовательных организаций, а также индивидуальных авторов!

# Система автоматизированной проверки задач Stepik была использована в ряде курсов на платформе Coursera, включая курсы по биоинформатике от Калифорнийского университета в Сан-Диего и курс по анализу данных от НИУ «Высшая школа экономики»...

# Stepik также может функционировать как площадка для проведения конкурсов и олимпиад, среди проведённых мероприятий — отборочный этап Олимпиады НТИ (2016—2020) (всероссийской инженерной олимпиады школьников, в рамках программы Национальная технологическая инициатива), онлайн-этап акции Тотальный диктант в 2017 году, соревнования по информационной безопасности StepCTF-2015...'''

# pattern_b = r'^(stepik)'
# pattern_d = r'.*(\.\.\.)$|.*(!)$'
#
# begin = re.findall(pattern_b, article, re.I|re.M)
# dots = re.findall(pattern_d, article, re.I|re.M)
#
# print(len(begin))
# print(len(dots))

# result1 = re.findall(r'^stepik.*', article, re.I|re.M)
# result2 = re.findall(r'.*\.\.\.$|.*!$', article, re.I|re.M)
# print(len(result1), len(result2), sep='\n')


# import re
#
# text = 'thdbakru rubabadjso babadirnid iehedba  ibebibeb duabafbf'
# word = 'ba'
# # text, word = input(), input()
#
# pattern = '\B' + '(' + word + ')' + '\B'
#
# print(len(re.findall(pattern, text, re.I)))



# import re
#
# s = input()
#
# if s.endswith('se'):
#     eng, br = s, s[:-2] + 'ze'
# else:
#     br, eng = s, s[:-2] + 'se'
#
#
#
#
# pattern = fr'\b({eng}|{br})\b'
#
# text = input()
#
# print(len(list(re.finditer(pattern, text, re.I))))
#
#
# import re
#
# w, s = input()[:-2], input()
#
# print(len(re.findall(fr'\b{w}(ze|se)\b', s, re.I)))


# import re
#
# w, s = input()[:-2], input()
#
# a = re.findall(fr'{w}(our|or)\b', s, re.I)
#
# print(len(re.findall(fr'\b{w}u?r\b', s, re.I)))


#
# uour
# ghour uuour uourr uour uorik uor uuor uorr Uor Uour

import re

# def abbreviate(phrase):
#     pattern = rf'\b[a-zA-Z|]|[A-Z]'
#     s = re.findall(pattern, phrase)
#     return ''.join(s).upper()
#
# print(abbreviate('javaScript object notation'))
#
# import re
#
# def abbreviate(phrase):
#     return ''.join(re.findall(r'[A-Z]|\b\w',phrase)).upper()