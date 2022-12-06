# файловая_переменная = open(имя_файла, режим_доступа)
#
# файловая переменная – имя переменной, которая ссылается на файловый объект;
# имя_файла – строковый литерал, задающий имя файла;
# режим_доступа – строковый литерал, задающий режим доступа (чтение, запись, и т.д.), в котором файл будет открыт.

# 'r' Read (чтение) Открыть файл только для чтения. Такой файл не может быть изменен.
# 'w'	Write (запись)	Открыть файл для записи. Если файл уже существует, стереть его содержимое. Если файл не существует, он будет создан.
# 'a'	Append (добавление)	Открыть файл для записи. Данные будут добавлены в конец файла. Если файл не существует, он будет создан.
# 'r+'	Read + Write	Открыть файл для чтения и записи. В этом режиме происходит частичная перезапись содержимого файла.
# 'x'	Create (создание)	Создать новый файл. Если файл существует, произойдет ошибка.

# При работе с текстом на русском языке нужно указать кодировку, для этого служит параметр encoding:
# file = open('info.txt', 'r', encoding='utf-8')

# file1 = open('students.txt', 'w')
# file2 = open('customers.txt', 'w', encoding='utf-8')
#
# print(file1.encoding)
# print(file2.encoding)
#
# file1.close()
# file2.close()

# file = open('info.txt', 'r')    # открываем файл с именем info.txt для чтения
#
#                                 # работаем с содержимым файла info.txt
#
# file.close()                    # закрываем файл после окончания работы

# Для чтения содержимого открытого для чтения файла используются три файловых метода:
#
# read() – читает все содержимое файла;
# readline() – читает одну строку из файла;
# readlines() – читает все содержимое файла и возвращает список строк.


# С помощью цикла while:
#
# file = open('languages.txt', 'r', encoding='utf-8')
#
# line = file.readline()         # считываем первую строку
#
# while line != '':              # пока не конец файла
#     print(line.strip())        # обрабатываем считанную строку
#     line = file.readline()     # читаем новую строку
#
# file.close()

# С помощью цикла for (предпочтительный вариант):
#
# file = open('languages.txt', 'r', encoding='utf-8')
#
# for line in file:
#     print(line.strip())
#
# file.close()

# import random
# file = open('lines.txt', 'r', encoding='utf-8')
# d = file.readlines()
# print(d[random.choice(range(0, len(d)))])
# file.close()

# import random
# content = open('lines.txt', 'r', encoding='utf-8')
# print(random.choice(content.readlines()))


# text = open('numbers.txt', 'r', encoding='utf-8')
# a = 0
# for line in text:
#     a += int(line.rstrip())
# print(a)

# file = open('nums.txt')
#
# print(sum(map(int, file)))
#
# file.close()

# text = open('nums.txt', 'r', encoding='utf-8').readlines()
# a = 0
#
# for line in text:
#     if line.strip().isdigit():
#         a += int(line.strip())
#
# print(a)
#
# text.close()

# file = open('nums.txt')
#
# print(sum(map(int, file.read().split())))
#
# file.close()

# file = open('prices.txt', encoding='utf-8')
# line = file.readline()
# x = 0
# while line != '':
#     z = line.strip().split()
#     x += int(z[1]) * int(z[2])
#     line = file.readline()
# print(x)
# file.close()

# file = open('prices.txt')
# lines = map(str.split, file)
# print(sum(map(lambda line: int(line[1]) * int(line[2]), lines)))
# file.close()


# with open('languages.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         print(line)
#                           # автоматическое закрытие файла
# print('Файл закрыт')


# with open('test.txt', encoding='utf-8') as file:
#     print('Repeat after me:', file.readline().strip())
#     for line in file:
#         print(line.strip() + '!')


# with open('text.txt', encoding='utf-8') as file:
#     print(file.read()[::-1])


# with open('data.txt', encoding='utf-8') as file:
#     l = file.readlines()
#     for line in l[::-1]:
#         print(line.strip())

# with open('lines.txt', encoding='utf-8') as file:
#     l = list(map(lambda x: x.strip(), file.readlines()))
#     maximuim = len(max(l, key=len))
#     for line in l:
#         if len(line) == maximuim:
#             print(line)


# with open('numbers.txt') as file:
#     line = file.readline().split()
#     while line != []:
#         print(sum(map(int, line)))
#         line = file.readline().split()




# with open('numbers.txt') as f:
#     for line in f:
#         print(sum(map(int, line.split())))


# with open('nums.txt', encoding='utf-8') as file:
#     l = []
#     for line in file.read():
#         if line.isdigit():
#             l.append(line)
#         else:
#             l.append(line.replace(line, ' '))
#     s = ''.join(l)
#     print(sum(map(int, s.split())))


# with open('nums.txt') as file:
#     number = '0'
#     total = 0
#     for char in file.read():
#         if char.isdigit():
#             number += char
#         else:
#             total += int(number)
#             number = '0'
#     print(total)


# Input file contains:
# 108 letters
# 20 words
# 4 lines


# with open('file.txt', encoding='utf-8') as file:
#     l = file.read().split()
#     c_words = len(l)
#     file.seek(0)
#     c_lines = 0
#     for i in file:
#         c_lines += 1
#     c_digits = 0
#     for i in l:
#         for j in i:
#             if j.isalpha():
#                 c_digits += 1
#     print(f'Input file contains:\n{c_digits} letters\n{c_words} words\n{c_lines} lines ')

# import random
# with open('first_names.txt', encoding='utf-8') as first, open('last_names.txt', encoding='utf-8') as last:
#     a = first.read().strip().split()
#     b = last.read().strip().split()
#
#     for i in range(3):
#         print(f'{random.choice(a)} {random.choice(b)}')



# with open('population.txt', encoding='utf-8') as file:
#     l = []
#     line = file.readline().split()
#     while line != []:
#         l.append(line)
#         line = file.readline().split()
#
#
#     for i in list(filter(lambda x: x[0][0] == 'G' and int(x[-1]) > 500000, l)):
#         print(i[0])


# with open('population.txt') as f:
#     for line in f:
#         n, p = line.split('\t')
#         if n.startswith('G') and int(p) > 500000:
#             print(n)


# def read_csv(data):
#     import csv
#     with open(data, newline='') as csvfile:
#         reader = list(csv.DictReader(csvfile))
#         return reader
#
# print(read_csv('data.csv'))


# with open('data.csv') as file:
#     name_table = file.readline()


# with open('test.txt', 'a') as file:
#     file.write('\n')
#     file.write('Michael\n')
#     file.write('Alexander')

# with open('test.txt', 'r+') as file:
#     file.write('Mick Jagger\n')
#     file.write('Ace Canon\n')

# with open('test.txt', 'w') as output:
#     print('stepik', 'beegeek', 'iq-option', sep='*', end='+\n', file=output)
#     print('python', file=output)

# with open('test.txt', 'w', encoding='utf-8') as file:
#     file.writelines(['Добро пожаловать в Beegeek!\n', 'Наши курсы самые лучшие! '])
#     file.write('Позвоните нам: (916) 928-92xx')

# s = input()
# with open('test.txt', 'w', encoding='utf-8') as file:
#     file.write(s)


# with open('test.txt', 'w', encoding='utf-8') as output:
#     import random
#     for i in range(25):
#         print(random.randrange(111, 778), file=output)


# with open('test.txt', 'w', encoding='utf-8') as file:
#     import random
#     for i in range(25):
#         file.write(str(random.randrange(111, 778)) + '\n')


# with open('input.txt', 'r', encoding='utf-8') as file1:
#     l = file1.readlines()
#     with open('output.txt', 'w', encoding='utf-8') as file2:
#         for num, line in enumerate(l, start=1):
#             file2.write(str(num) + ')' + ' ' + line)


# with open('input.txt') as inp, open('output.txt', 'w') as out:
#     for i, j in enumerate(inp, start=1):
#         print(f'{i}) {j}', end='', file=out)

# with open('test.txt', encoding='utf-8') as data, open('new_scores.txt', 'w', encoding='utf-8') as output:
#     line = data.readline().split()
#     while line != []:
#         x = int(line[1]) + 5
#         if x > 100:
#             x = 100
#         print(f'{line[0]} {x}', file=output)
#         line = data.readline().split()
#
#
# with open('class_scores.txt') as class_scores, open('new_scores.txt', 'w') as new_scores:
#     for line in class_scores:
#         name, score = line.split()
#         score = int(score) + 5
#         if score > 100:
#             score = 100
#         print(name, score, file=new_scores)

#

# with open('goats.txt', encoding='utf-8') as data, open('answer.txt', 'w', encoding='utf-8') as new_data:
#     colors = []
#     line = data.readline()
#     while line != 'GOATS\n':
#         colors.append(line)
#         line = data.readline()
#     colors.remove('COLOURS\n')
#     colors = list(map(lambda x: x.replace('\n', ''), colors))
#     goats = list(map(lambda x: x.replace('\n', ''), data.readlines()))
#     pcs = len(goats)
#
#     d = {}
#     for i in goats:
#         d[i] = d.get(i, 0) + 1
#
#     for k, v in sorted(d.items()):
#         if v > pcs*0.07:
#             print(k, end='\n', file=new_data)
#

# with open('goats.txt') as f1, open('answer.txt', 'w') as f2:
#     cont = f1.read().split('\n')
#     colors, goats = cont[1:cont.index('GOATS')], cont[cont.index('GOATS')+1:]
#     print(*sorted(filter(lambda x: goats.count(x) / len(goats) > 0.07, colors)), sep='\n', file=f2)


# n = 4
# l = ['test.txt', 'text.txt', 'prices.txt', 'population.txt']
# s = []
# for i in l:
#     with open(i, encoding='utf-8') as file:
#         s.append(file.read())
#
#
# with open('output.txt', 'w', encoding='utf-8') as output:
#     output.writelines(s)

# def minutes(x):
#     res=[int(i) for i in x.split(':')]
#     return res[0]*60+res[1]
#
# with open('logfile.txt', encoding='utf-8') as file, open('output.txt', 'w', encoding='utf-8') as output:
#     log = file.readline().split(',')
#     while log != ['']:
#         if minutes(log[2]) - minutes(log[1]) >= 60:
#             print(log[0], file=output)
#         log = file.readline().split(',')




# with open('output.txt', 'w') as out:
#     for i in range(int(input())):
#         with open(input()) as f:
#             out.write(f.read())


# with open('logfile.txt',encoding='utf-8') as fr, open('output.txt','a',encoding='utf-8') as fw:
#     for line in fr:
#          name, st, en = line.split(', ')
#          if int(en.replace(':','')) - int(st.replace(':','')) >= 100:
#             print(name,file = fw)



# text = 'file_0.txt'
#
# with open(text, encoding='utf-8')  as file:
#     line = file.readlines()
#     print(len(line))

# counter = 0
# with open('data.txt', encoding='utf-8') as file:
#     text = file.readlines()
#     for i in text:
#         counter += int(i.strip('$\n'))
#     print(f'${counter}')


# with open('data.txt', encoding='utf-8') as file:
#     counter = 0
#     text = file.readlines()
#     for word in text:
#         if int(word.split()[1]) >= 65 and int(word.split()[2]) >= 65 and int(word.split()[3]) >= 65:
#             counter+=1
#         else:
#             continue
# print(counter)
#
# with open('grades.txt') as f:
#     n = 0
#
#     for line in f:
#         n += 1 if all(int(x) >= 65 for x in line.strip().split()[1:]) else 0
#
#     print(n)

# with open('data.txt', encoding='utf-8') as file:
#     d = {}
#     for i in file.read().split():
#         d[i] = len(i)
#     maximum = max(d.values())
#     print(filter(d, maximum))

# with open('data.txt', encoding='utf-8') as file:
#     l = file.read().split()
#     maximuim = len(max(l, key=len))
#     for line in l:
#         if len(line) == maximuim:
#             print(line)

# with open('data.txt', encoding='utf-8') as file:
#     text = file.readlines()
#     if len(text) >= 10:
#         for i in range(len(text)-10, len(text)):
#             print(text[i].strip('\n'))
#     else:
#         for i in text:
#             print(i.strip())
#
# with open(input()) as file:
#     print(*file.readlines()[-10:], sep='')


# my_dict = {
#     'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
#     'ё': 'jo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k',
#     'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
#     'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c',
#     'ч': 'ch', 'ш': 'sh', 'щ': 'shh', 'ъ': '*', 'ы': 'y', 'ь': '\'',
#     'э': 'je', 'ю': 'ju', 'я': 'ya',
#
#     'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E',
#     'Ё': 'Jo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'J', 'К': 'K',
#     'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
#     'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C',
#     'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shh', 'Ъ': '*', 'Ы': 'y', 'Ь': '\'',
#     'Э': 'Je', 'Ю': 'Ju', 'Я': 'Ya'
# }
#
# with open('data.txt', 'r', encoding='utf-8') as file, open('cyrillic.txt', 'w', encoding='utf-8') as output:
#     text = file.read()
#     for i in text:
#         if i in my_dict:
#             text = text.replace(i, my_dict[i])
#     print(text, file=output)

# import re
# with open('data.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     match_1 = re.findall(r'# .+\ndef (\w+_?\w+)\(+', text)
#     match_all = re.findall(r'def (\w+_?\w+)\(+', text)
#     if len(match_1) == len(match_all):
#         print('Best Programming Team')
#     else:
#         for i in match_all:
#             if i not in match_1:
#                 print(i)
#
# with open(input(), encoding='utf-8') as inf:
# 	not_commented_funcs, preline = [], ''
# 	for line in inf:
# 		if not preline.startswith('#') and line.startswith('def '):
# 			not_commented_funcs.append(line[4:line.find('(')])
# 		preline = line
# 	print('\n'.join(not_commented_funcs) if not_commented_funcs else 'Best Programming Team')


# import re
#
# with open('forbidden_words.txt', encoding='utf-8') as fw:
#     forbidden_words = fw.read().split(' ')
#
# with open(input(), encoding='utf-8') as rw:
#     my_string = rw.read()
#
#
# def change(forbidden_words, text):
#     out = text
#     for w in forbidden_words:
#         out = re.sub(w, "*" * len(w), out, flags=re.I | re.M)
#     return out
#
#
# print(change(forbidden_words, my_string))


# with open("forbidden_words.txt", encoding="utf-8") as file, open(input()) as infile:
#     text = infile.read()
#     for f in file.read().strip("\n").split():
#         pos = text.lower().find(f)
#         while pos > -1:
#             text = text[:pos] + "*" * len(f) + text[pos+len(f):]
#             pos = text.lower().find(f)
# print(text)

