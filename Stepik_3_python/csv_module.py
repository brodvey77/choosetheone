# import csv
#
# with open('products.csv', encoding='UTF-8') as file:
#     rows = csv.reader(file)    # Создаём reader объект
#     for keyword, price, product_name in rows:
#         print(f'Ключевые слова: {keyword}, Цена: {price}, Наименование: {product_name}')

# import csv
#
# with open('products.csv', encoding='UTF-8') as file:
#     print(file)
#     rows = csv.DictReader(file, delimiter=';', quotechar='"')
#     for row in rows:
#         print(row)

# import csv
#
# with open('products.csv', encoding='utf-8') as file:
#     rows = csv.DictReader(file, delimiter=';', quotechar='"')
#     expensive = sorted(rows, key=lambda x: int(x['price']), reverse=True)
#     for record in expensive[:5]:
#         print(record)


# import csv
#
# columns = ['first_name', 'second_name', 'class_number', 'class_letter']
# data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Артур', 'Харисов', 10, 'В']]
#
# with open('students.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(columns)
#     for row in data:
#         writer.writerow(row)

# import csv
#
# columns = ['first_name', 'second_name', 'class_number', 'class_letter']
# data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Роман', 'Белых', 10, 'В']]
#
# with open('students.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerow(columns)
#     for row in data:
#         writer.writerow(row)

# import csv
#
# columns = ['first_name', 'second_name', 'class_number', 'class_letter']
# data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Роман', 'Белых', 10, 'В']]
#
# with open('students.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerow(columns)
#     writer.writerows(data)



# import csv
#
# data = [{'first_name': 'Тимур', 'second_name': 'Гуев', 'class_number': 11, 'class_letter': 'А'},
#         {'first_name': 'Руслан', 'second_name': 'Чаниев', 'class_number': 9, 'class_letter': 'Б'},
#         {'first_name': 'Роман', 'second_name': 'Белых', 'class_number': 10, 'class_letter': 'В'}]
#
# columns = ['first_name', 'second_name', 'class_number', 'class_letter']
#
# with open('students.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=columns, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
#     writer.writeheader()
#     for row in data:
#         writer.writerow(row)


# import csv
#
# with open('products.csv', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     for line in reader:
#         print(line)
#         break
#
# import csv
#
# with open('products.csv', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for line in reader:
#         print(type(line))
#         break

# import csv
#
# with open('products.csv', encoding='UTF-8') as csv_file:
#     # Считываем содержимое файла
#     # text = csv_file.read()
#     # Создаем ридер объект и указываем в качестве разделителя символ - ;
#     rows = csv.reader(csv_file, delimiter=';')
#     # Выводим каждую строку
#     for row in rows:
#         print(row)


# import csv
#
# with open('writing_test.csv', 'w', encoding='utf-8', newline='') as csv_file:
#     # создаем writer объект и указываем названия столбцов
#     writer = csv.DictWriter(csv_file, fieldnames=['first_col', 'second_col'])
#     # записываем первую строку с названиями столбцов
#     writer.writeheader()
#     # записываем строку с данными
#     writer.writerow({'first_col': 'value1', 'second_col': 'value2'})

# import csv
#
# with open('products.csv', encoding='UTF-8') as file:
#     # создаем writer объект и указываем названия столбцов
#     reader = csv.reader(file, delimiter=';')
#     table = [i for i in reader]
#     del(table[0])
#     for line in table:
#         if int(line[1]) > int(line[2]):
#             print(line[0])


# import csv
# from statistics import mean
#
# with open('products.csv', encoding='UTF-*') as file:
#     # create dict-reader object
#     reader = csv.DictReader(file, fieldnames=['company_name', 'salary'], delimiter=';')
#     my_dict = {}
#     for i in reader:
#         my_dict.setdefault(i['company_name'], []).append(i['salary'])
#     del my_dict['company_name']
#     for k,v in my_dict.items():
#         # print(k, list(map(lambda x: int(x), v)))
#         my_dict[k] = list(map(lambda x: int(x), v))
#
#
#     my_dict = dict(sorted(my_dict.items(), key=lambda x:(mean(x[1]), x[0])))
#     for k in my_dict.keys():
#         print(k)


# import csv
#
# n = int(input())
# with open('products.csv', encoding='UTF-8') as file:
#     reader = list(csv.reader(file))
#     f_r = list(map(lambda x: [x[0], int(x[1]), int(x[2])], reader))
#     s_f_r = sorted(f_r, key=lambda x: x[n-1])
#     for i in s_f_r:
#         print(*i, sep=',')
#
#
# import csv
#
# i = int(input()) - 1
#
# with open('deniro.csv', 'r', encoding='utf-8') as file:
#     data = list(csv.reader(file))
#
# data.sort(key=lambda x: int(x[i]) if x[i].isdigit() else x[i])
# for lst in data:
#     print(*lst, sep=',')







# import csv
# d = {}
# with open('salary_data.csv', encoding='utf-8') as file:
#     rows = list(csv.reader(file, delimiter=';'))
#     for key, value in rows[1:]:
#         d[key] = d.get(key, []) + [int(value)]
#
#     d_sort = sorted(d, key=lambda x: (sum(d[x]) / len(d[x]), x))
#     print(*d_sort, sep='\n')


# import pandas as pd
#
# file = pd.read_csv(r'salary_data.csv', sep=';', encoding='utf-8')
# file = file.groupby(['company_name']).mean().reset_index()
# sorted_file = file.sort_values(['salary', 'company_name'], ascending=[True, True])
# print(*sorted_file['company_name'], sep='\n')

# import csv
# def csv_columns(filename: str) -> dict:
#     with open(filename, encoding='UTF-8') as file:
#         reader = csv.DictReader(file)
#         d = {}
#         for row in reader:
#            for i in row:
#                d.setdefault(i, []). append(row[i])
#         return d
#
#
# print(csv_columns('products.csv'))




# import csv
#
# def csv_columns(filename):
#
#     with open(filename, encoding="utf-8") as file_in:
#         rows = list(csv.reader(file_in))
#         return {key: value for key, *value in zip(*rows)}



# import csv
#
#
# def csv_columns(filename):
#     with open(filename, 'r', encoding='utf-8') as file:
#         reader = csv.DictReader(file, delimiter=',')
#         d = {}
#         for row in reader:
#             for key, value in row.items():
#                 d[key] = d.get(key, []) + [value]
#         return d


# import csv
# import re
#
# with open('products.csv', encoding='UTF-8') as file_in:
#     reader = list(csv.reader(file_in))
#     del reader[0]
#     reader_f = list(map(lambda x: [x[2], x[0] + ' ' + x[1]], reader))
#     reader_f2 = list(map(lambda x: x[0], reader_f))
#     reader_f3 = list(map(lambda x: x[x.index('@') + 1:], reader_f2))
#     d = {}
#     for adres in reader_f3:
#         d[adres] = d.get(adres, 0) + 1
#     sorted_d = list(sorted(d.items(), key=lambda x: (x[1], x[0])))
#
# columns = ['domain', 'count']
# with open('domain_usage.csv', 'w', encoding='UTF-8', newline='') as file_out:
#     writer = csv.writer(file_out)
#     writer.writerow(columns)
#     for row in sorted_d:
#         writer.writerow(row)

# import csv
#
# domens = dict()
#
# with open('data.csv', encoding='utf-8') as f:
#     for *n, d in csv.reader(f):
#         key = d.split('@')[-1]
#         domens[key] = domens.get(key, 0) + 1
#
# del domens['email']
#
# with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['domain', 'count'])
#     for row in sorted(domens.items(), key=lambda x: (x[1], x[0])):
#         writer.writerow(row)


# import csv
#
# with open('products.csv', encoding='UTF-8') as file:
#     reader = list(csv.reader(file, delimiter=';'))
#     f_reader = list(map(lambda x: [x[1], int(x[3])], reader[1:]))
#     d = {}
#     for row in f_reader:
#         d.setdefault(row[0], []).append(row[1])
#     d = {k: sum(v) for k,v in d.items()}
#     sorted_d = dict(sorted(d.items(), key=lambda x: (-x[1], x[0])))
#     for k,v in sorted_d.items():
#         print(f'{k}: {v}')


# import csv
#
# with open('wifi.csv', encoding='UTF-8') as f:
#     d = {}
#     for r in [*csv.reader(f, delimiter=';')][1:]:
#         d[r[1]] = d.get(r[1], 0) + int(r[3])
#
# for i in sorted(d, key=lambda x:(-d[x], x)):
#     print(f'{i}: {d[i]}')


# import csv
#
# with open('products.csv', 'r', encoding='UTF-8') as file:
#     reader = [i for i in csv.reader(file, delimiter=';')]
#     f_reader = list(map(lambda x: [int(x[0]), x[1], x[2], int(float(x[3]))], reader[1:]))
#     l_m = list(filter(lambda x: x[0] == 1 and x[2] == 'male' and x[3] < 18, f_reader))
#     f_m = list(filter(lambda x: x[0] == 1 and x[2] == 'female' and x[3] < 18, f_reader))
#     f_l = l_m + f_m
#     for i in f_l:
#         print(i[1])

# import csv
# from datetime import datetime
#
# with open('products.csv', 'r', encoding='UTF-8') as file_in:
#     reader = list(csv.reader(file_in))[1:]
#     f_reader = list(map(lambda x: [x[0], x[1], datetime.strptime(x[2], '%d/%m/%Y %H:%M')], reader))
#     sorted_reader_date = list(sorted(f_reader, key=lambda x: x[2], reverse=True))
#     d = {}
#     for row in sorted_reader_date:
#         d[row[1]] = d.setdefault(row[1], [row[0], row[2]])
#     sorted_d = dict(sorted(d.items()))
#     # williamwilson@list.ru ['nice~william7', datetime.datetime(2021, 11, 28, 4, 28)]
#     l = []
#     for k, v in sorted_d.items():
#         l.append([v[0], k, datetime.strftime(v[1], '%d/%m/%Y %H:%M')])
#
#
# with open('new_name_log.csv', 'w', encoding='UTF-8', newline='') as file_out:
#     writer = csv.writer(file_out)
#     writer.writerow(['username', 'email', 'dtime'])
#     for row in l:
#         writer.writerow(row)

# import csv
# from datetime import datetime
#
# with open('name_log.csv', encoding='UTF-8') as f:
# 	header, *rows = csv.reader(f)
#
# d = {i[1]:i for i in sorted(rows, key=lambda x: datetime.strptime(x[2], '%d/%m/%Y %H:%M'))}
#
# with open('new_name_log.csv', 'w', encoding='UTF-8', newline='') as f:
# 	w = csv.writer(f)
# 	w.writerow(header)
# 	w.writerows(sorted(d.values(), key=lambda x: x[1]))

# import csv
#
# def condense_csv(filename, id_name):
#   # open the input file and read it as a list of lists
#   with open(filename) as input_file:
#     data = list(csv.reader(input_file))
#
#   # create a dictionary to store the properties and values for each object
#   objects = {}
#   for row in data:
#     # get the object name, property name and value from each row
#     object_name = row[0]
#     property_name = row[1]
#     value = row[2]
#
#     # if the object name is not in the dictionary, create a new entry with an empty list
#     if object_name not in objects:
#       objects[object_name] = []
#
#     # append the property name and value to the list of the object
#     objects[object_name].append((property_name, value))
#
#   # open the output file and write it with the desired format
#   with open('condensed.csv', 'w', newline='') as output_file:
#     writer = csv.writer(output_file)
#
#     # write the header row with id_name and all property names
#     header = [id_name]
#     properties = [p for p, v in objects[next(iter(objects))]]
#     header.extend(properties)
#     writer.writerow(header)
#
#     # write each object row with its name and values
#     for object_name, values in objects.items():
#       row = [object_name]
#       values = [v for p, v in values]
#       row.extend(values)
#       writer.writerow(row)
#
#
#
# text = '''01,Title,Ran So Hard the Sun Went Down
# 02,Title,Honky Tonk Heroes (Like Me)'''
#
# with open('data.csv', 'w', encoding='utf-8') as file:
#     file.write(text)
#
# condense_csv('data.csv', id_name='ID')
#
# with open('condensed.csv', encoding='utf-8') as file:
#     print(file.read().strip())



import csv

with open('products.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    data = [row for row in reader]

# Sort the columns by class number and letter
class_order = sorted(header[1:], key=lambda x: (int(x.split('-')[0]), x.split('-')[1]))
header_sorted = [header[0]] + class_order
data_sorted = [[row[0]] + [row[header.index(col)] for col in class_order] for row in data]

# Write the sorted data to a new file
with open('sorted_student_counts.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header_sorted)
    writer.writerows(data_sorted)
