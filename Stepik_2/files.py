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


# with open('output.txt', 'w') as out:
#     for i in range(int(input())):
#         with open(input()) as f:
#             out.write(f.read())
