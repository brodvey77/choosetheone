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

