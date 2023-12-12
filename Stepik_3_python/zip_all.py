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


# from zipfile import ZipFile
#
# counter_custom = 0
# counter_arch = 0
#
# with ZipFile('workbook_1.zip') as zip_file:
#     l = zip_file.infolist()
#     for i in l:
#         counter_custom += i.file_size
#         counter_arch += i.compress_size
#
#     print(f'Объем исходных файлов: {counter_custom} байт(а)')
#     print(f'Объем сжатых файлов: {counter_arch} байт(а)')
#
#
#
# from zipfile import ZipFile
#
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#     print(f'Объем исходных файлов: {sum(f.file_size for f in info)} байт(а)')
#     print(f'Объем сжатых файлов: {sum(f.compress_size for f in info)} байт(а)')

# from zipfile import ZipFile
#
# a = []
# with ZipFile('workbook_16.zip') as zip_file:
#     l = zip_file.infolist()
#     for i in l:
#         if not i.is_dir():
#             size = 100-(i.compress_size/i.file_size) * 100
#             a.append((i.filename.split('/')[-1], size))
#
#     a = sorted(a,key=lambda x: x[1], reverse=True)
#     print(a[0][0])


# from zipfile import ZipFile
#
# with ZipFile("workbook.zip") as zip_file:
#     filelist = zip_file.infolist()
#     t = ((f.filename, f.compress_size/f.file_size) for f in filelist
#          if f.file_size != 0)
#     print(min(t, key=lambda x: x[1])[0].split("/")[-1])


# from zipfile import ZipFile
# from datetime import datetime
#
# d = '2021-11-30 14:22:00'
# pattern = '%Y-%m-%d %H:%M:%S'
# l_f = []
# with ZipFile('workbook_17.zip') as zip_file:
#     l = zip_file.infolist()
#     for i in l:
#         if not i.is_dir():
#             name = i.filename.split('/')[-1]
#             i_d = datetime(*i.date_time)
#             if i_d > datetime.strptime(d, pattern):
#                 l_f.append((name))
#
#     for i in sorted(l_f):
#         print(i)


# from zipfile import ZipFile
# from datetime import datetime
#
# d = {}
# counter = 0
# with ZipFile('workbook_18.zip') as zip_file:
#     l = zip_file.infolist()
#     for i in l:
#         if not i.is_dir():
#             tt = datetime(*i.date_time)
#             d[i.filename.split('/')[-1]] = {'date_file': tt, 'size_start': i.file_size, 'size_finish': i.compress_size}
#
#     for k,v in sorted(d.items()):
#         print(k)
#         print(f'  Дата модификации файла: {v["date_file"]}')
#         print(f'  Объем исходного файла: {v["size_start"]} байт(а)')
#         print(f'  Объем сжатого файла: {v["size_finish"]} байт(а)')
#         counter +=1
#         if counter < len(d):
#             print()


# from zipfile import ZipFile
# import os
# import datetime
#
# with ZipFile('workbook.zip') as zip_file:
#     info = [i for i in zip_file.infolist() if not i.is_dir()]
#
#     for i in sorted(info, key=lambda x: os.path.basename(x.filename).lower()):
#         print(f"""{os.path.basename(i.filename)}
#   Дата модификации файла: {datetime.datetime(*i.date_time)}
#   Объем исходного файла: {i.file_size} байт(а)
#   Объем сжатого файла: {i.compress_size} байт(а)
# """)

# from zipfile import ZipFile
#
# file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
#               'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
#               'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

# from zipfile import ZipFile
#
# file_names = ['del_1.txt', 'del_2.txt']
# with ZipFile('files.zip', mode='w') as zip_file:
#     for i in file_names:
#         zip_file.write(i)
#     print(zip_file.namelist()
#
#
#
# with ZipFile('files.zip', mode='w') as zip_file:
#     [zip_file.write(file) for file in file_names]

#
# import zipfile
# import os
#
# def extract_this(zip_name, *args):
#     with zipfile.ZipFile(zip_name, 'r') as zip_ref:
#         if len(args) == 0:
#             zip_ref.extractall()
#         else:
#             for file in args:
#                 zip_ref.extract(file)


import os
import json

def is_correct_json(file_path):
    try:
        with open(file_path) as f:
            json.load(f)
        return True
    except:
        return False

def get_players(file_path):
    with open(file_path) as f:
        data = json.load(f)
    if data.get('team') == 'Arsenal':
        return data.get('first_name'), data.get('last_name')
    return None

def main():
    players = []
    for root, dirs, files in os.walk('data'):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                if is_correct_json(file_path):
                    player = get_players(file_path)
                    if player is not None:
                        players.append(player)
    players.sort()
    for player in players:
        print(player[0], player[1])

if __name__ == '__main__':
    main()