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


# import sys
# import re
#
# text = sys.stdin.read()
# pattern = r'<a href="(.+)">(.+)</a>'
#
# for address, pointer in re.findall(pattern, text):
#     print(f'{address}, {pointer}')
#
# # put your python code here
# import re, sys
#
# pattern = r'<a href="(?P<adress>.+)">(?P<index>.*)</a>'
#
# for line in sys.stdin:
#     match = re.search(pattern, line.strip('\n'))
#     if match:
#         print(f'{match.groupdict()["adress"]}, {match.groupdict()["index"]}')
#
#

# from re import sub

# result = sub(r'\w+', lambda m: m.group().capitalize(), 'ThiS WORLD doesNT need A HeRo')

# print(result)

# from re import sub

# def convert(match_obj):
#     year, month, day = match_obj.group().split('-')
#     return f'{day}.{month}.{year}'

# result = sub(r'(\d{4}-\d{2}-\d{2})', convert, 'Gvido was born on 1956-01-31')

# print(result)

# import re


# def normalize_jpeg(filename):
#     s = re.sub(r'(jpe?g)$', 'jpg', filename, flags=re.I)
#     return s



# # INPUT DATA:

# # TEST_1:
# print(normalize_jpeg('stepik.jPeG'))

# # TEST_2:
# print(normalize_jpeg('mountains.JPG'))

# # TEST_3:
# print(normalize_jpeg('windows11.jpg'))

# # TEST_4:
# print(normalize_jpeg('jepg_file.jPG'))

# # TEST_5:
# print(normalize_jpeg('file_jepg.jPeG'))

# # TEST_6:
# print(normalize_jpeg('file.jepg.JPEG'))

# # TEST_7:
# print(normalize_jpeg('filename.jpg.jpg'))

# # TEST_8:
# print(normalize_jpeg('stepik.jpeg.jpeg'))

# # TEST_9:
# print(normalize_jpeg('stepik.jpg.jpeg'))

# # TEST_10:
# print(normalize_jpeg('stepik.jpeg.jpg'))

# # TEST_11:
# print(normalize_jpeg('beegeek.JPg'))

# # TEST_12:
# print(normalize_jpeg('нарусском.JPg'))

# # TEST_13:
# print(normalize_jpeg('на русском языке.JPG'))

# # TEST_14:
# print(normalize_jpeg('jpg.jPg.Jpg.JPG'))

# # TEST_15:
# print(normalize_jpeg('Это тест.JpEg'))


# import re

# def normalize_whitespace(string):
#     s = re.sub(r'\s{2,}', ' ', string)
#     return s



# # INPUT DATA:

# # TEST_1:
# print(normalize_whitespace('AAAA                A                AAAA'))

# # TEST_2:
# print(normalize_whitespace('Тут нет лишних пробелов'))

# # TEST_3:
# print(normalize_whitespace('Тут   н   е   т     л   и     шних пробелов     '))

# # TEST_4:
# print(normalize_whitespace('K L  L    O    I!  !  I OP    PPPppdj O   P'))

# # TEST_5:
# print(normalize_whitespace('               '))

# # TEST_6:
# print(normalize_whitespace('aaaaaaaaaaaaaaaaaaaaaaaaaa'))

# # TEST_7:
# print(normalize_whitespace('Раз два  три   четыре    пять      шесть      '))

# # TEST_8:
# print(normalize_whitespace('      Шесть-----пять    четыре***три  два+один'))

# # TEST_9:
# print(normalize_whitespace('1 9  2  8   3   7    6    5'))

# # TEST_10:
# print(normalize_whitespace('Проб.елов,нетв-этом:очень\длинно*мслове'))

# # TEST_11:
# print(normalize_whitespace(''))

# # TEST_12:
# print(normalize_whitespace(' '))

# # TEST_13:
# print(normalize_whitespace('There are no unnecessary gaps.'))

# # TEST_14:
# print(normalize_whitespace('. ,  ;   :    "     (       )      '))

# # TEST_15:
# print(normalize_whitespace('111111111111 2222222222222 333333333333'))

import re
import keyword

kwl = keyword.kwlist

kwl_s = '\\b|\\b'.join(kwl)

print(kwl_s)

def change_kw(string):
    s = re.sub(kwl_s, '<kw>', string, flags=re.I)
    print(s)



change_kw('False, True, assert, as, ,None, false, or, Import')
