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

from functools import reduce
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



