# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     zip_file.printdir()


# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.infolist()
#     print(info[6].file_size)                # размер начального файла в байтах
#     print(info[6].compress_size)            # размер сжатого файла в байтах
#     print(info[6].filename)                 # имя файла
#     print(info[6].date_time)                # дата изменения файла


# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.infolist()
#     print(info[0].is_dir())
#     print(info[6].is_dir())


# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.namelist()
#     print(*info, sep='\n')
#     print(info)


# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     with zip_file.open('test/Разные файлы/astros.json') as file:
#         print(file.read())

# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     with zip_file.open('test/Разные файлы/astros.json') as file:
#         print(file.read().decode('utf-8'))


# from zipfile import ZipFile
#
# with ZipFile('archive.zip', mode='w') as zip_file:
#     zip_file.write('program.py')
#     zip_file.write('lse.jpeg')
#     print(zip_file.namelist())

# from zipfile import ZipFile
#
# with ZipFile('archive.zip', mode='w') as zip_file:
#     zip_file.write('program.py', 'new_program.py')  # первый аргумент - это имя файла
#     zip_file.write('lse.jpeg', 'lse1.jpeg')         # второй аргумент - это имя файла в архиве
#     print(zip_file.namelist())


# from zipfile import ZipFile
#
# with ZipFile('test.zip', mode='a') as zip_file:
#     zip_file.write('data.csv', 'test/program.py')
#     zip_file.write('diary.txt')
#     print(*zip_file.namelist(), sep='\n')

# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     zip_file.extract('test/Картинки/avatar.png')
#     zip_file.extract('test/Программы/image_util.py')
#     zip_file.extract('lse.jpeg')



# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     zip_file.extractall()

#
# Примечания
# Примечание 1. Подробнее о формате zip можно прочитать на википедии.
#
# Примечание 2. Подробнее прочитать про архивирование в Python можно по ссылке.
#
# Примечание 3. Отличная статья на хабре "Zip-файлы: история, объяснение и реализация".
#
# Примечание 4. При создании объекта ZipFile мы также можем передать еще два необязательных аргумента:
#
# compression, который определяет метод сжатия, который должен использоваться при записи в архив. Он принимает одно из
# значений: ZIP_STORED, ZIP_DEFLATED, ZIP_BZIP2, ZIP_LZMA. По умолчанию используется значение compression=ZIP_STORED
#
# allowZip64, который позволяет разрешить использование расширений zip64, которые дают возможность создавать архивы
# размером больше 4 гигабайт. По умолчанию равен allowZip64=True
#
# Примечание 5. Для того чтобы проверить является ли некоторый файл zip архивом, используется функция zipfile.is_zipfile()
# которая принимает на вход путь к файлу (или сам файловый объект) и возвращает значение True, если указанный файл
# является zip архивом, или False в противном случае.


# from zipfile import ZipFile
#
# zip_file = open('test.zip')


# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     pass


# from zipfile import ZipFile
#
# zip_file = ZipFile('test.zip')


# from zipfile import ZipFile
#
# with open('test.zip') as zip_file:
#     pass


# from zipfile import ZipFile
# counter = 0
# with ZipFile('workbook.zip') as zip_file:
#     l = zip_file.infolist()
#     for i in l:
#         if i.is_dir() == False:
#             counter += 1
#     print(counter)


