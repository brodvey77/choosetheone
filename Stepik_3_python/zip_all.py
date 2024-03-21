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


# import os
# import json
#
# def is_correct_json(file_path):
#     try:
#         with open(file_path) as f:
#             json.load(f)
#         return True
#     except:
#         return False
#
# def get_players(file_path):
#     with open(file_path) as f:
#         data = json.load(f)
#     if data.get('team') == 'Arsenal':
#         return data.get('first_name'), data.get('last_name')
#     return None
#
# def main():
#     players = []
#     for root, dirs, files in os.walk('data'):
#         for file in files:
#             if file.endswith('.json'):
#                 file_path = os.path.join(root, file)
#                 if is_correct_json(file_path):
#                     player = get_players(file_path)
#                     if player is not None:
#                         players.append(player)
#     players.sort()
#     for player in players:
#         print(player[0], player[1])
#
# if __name__ == '__main__':
#     main()


# from zipfile import ZipFile
# import json
#
# def is_correct_json(string):
#     try:
#         json.load(string)
#         return True
#     except:
#         return False
#
# players = []
# with ZipFile('data.zip') as zip_file:
#     info = zip_file.namelist()
#     for i in info:
#         if i[-4:] == 'json':
#             with zip_file.open(i) as file:
#                 if is_correct_json(file):
#                     with open(zip_file.extract(i)) as f:
#                         data = json.load(f)
#                         if data.get('team') == 'Arsenal':
#                             players.append((data.get('first_name'), data.get('last_name')))
#
# for i in sorted(players):
#     print(*i)

import zipfile
# import os
#
# def print_file_structure(zip_file, indent=''):
#     with zipfile.ZipFile(zip_file, 'r') as archive:
#         for item in archive.infolist():
#             if item.is_dir():
#                 print(f'{indent}{item.filename}/')
#                 print_file_structure(item.filename, indent + '  ')
#             else:
#                 file_size = item.file_size
#                 if file_size >= 1024 * 1024:
#                     file_size = f'{file_size // (1024 * 1024)} MB'
#                 elif file_size >= 1024:
#                     file_size = f'{file_size // 1024} KB'
#                 else:
#                     file_size = f'{file_size} B'
#                 print(f'{indent}{item.filename} {file_size}')
#
# zip_file = 'desktop.zip'
# print_file_structure(zip_file)

# from zipfile import ZipFile
#
#
# def convert_bytes(size):
#     """Конвертер байт в большие единицы"""
#     if size < 1000:
#         return f'{size} B'
#     elif 1000 <= size < 1000000:
#         return f'{round(size / 1024)} KB'
#     elif 1000000 <= size < 1000000000:
#         return f'{round(size / 1048576)} MB'
#     else:
#         return f'{round(size / 1073741824)} GB'
#
# with ZipFile('desktop.zip') as zip_file:
#     info = zip_file.infolist()
#     indent = ''
#     for item in info:
#         name = item.filename
#         size = convert_bytes(item.file_size)
#         items = name.rstrip("/").split("/")
#         if item.is_dir():
#             print("  " * (len(items) - 1) + items[-1])
#         else:
#             print("  " * (len(items) - 1) + items[-1] + ' ' + size)


# import  sys
# import pickle
#
# file_name, *data = list(map(str.strip, sys.stdin))
#
# with open(file_name, 'rb') as pickle_file:
#     a_f = pickle.load(pickle_file)
#     print(a_f(*data))
#
#
# import pickle
# import sys
#
# name, *args = [line.strip() for line in sys.stdin]
#
# with open(name, 'rb') as f:
#     func = pickle.load(f)
#
# print(func(*args))
#
# import pickle
# def filter_dump(filename, object: list, typename:type):
#     with open(filename, 'wb') as pickle_file:
#         pickle.dump([i for i in object if type(i) == typename], pickle_file)
#
#
#
#
# t_m = int
# obj = [2,3,4,"d", 8, 12]
# file_name = "some_file"
#
# filter_dump(file_name, obj, t_m)

# import pickle
#
# data = ['9', 83.1, 637, 907, 465, '785', 271.2, 223, 755, 29, 215, 5, 433, 897, 729, 645, 437, 427, 347, 237, 827, 731,
#         11, [139, 581], 473, 579, [483, 113, 923, 273, 615], 31.3, 63, 675, 787, 277, 441, 207, 819.5, 337, 641, 239,
#         27, 743, 703, '535', 117, 193, 515, 843, 887, 227, 485, 905, 655, 419, 209, [553, 933, 499], 185, 351, 951.3,
#         741, 115, 279, 33, 365, 205, 359, 289, 91, 19, 161, 81, 825, 263, '817', 739, 935, 413, 221, 501, 247, '775',
#         367, 25, 543, '89', 445, 697, 931, 3, 745, 233, 35, 125, 717, 157, 453, 653, 617, 355, 829, 929, '719', 143,
#         529, 527, 373, '821', 965, 797, 683, 857, 709.3, 307, 15, 779, 565.8, 327, 89.1, 867.7, 689, 605,
#         (783, 639, 847, 927), 135, 257, 771, 311, 201, 303.5, 165, 127, 235, 141, (699, 959, 937, 947), 64.7, 649, 411,
#         777, 57, 561, 421, 559, 599, 687, 563, {331, 197, 513}, 59, 73, 835, 459, {231, 1, 189, 855, 725}, 567, 103,
#         261, 943, 577, 813, 913, 479, 597, 575, 511, 971, 285]
# data2 = {'30': 900, 7.7: 5929, '7.1': 5041, 11: 121, 7.8: 6084, 6: '36', 49: 2401, 51: 2601, 96: 9216, 80: 6400,
#          (53, 21): 441, 68: 4624, 3: 9, 42: 1764, 20: 400, 87: 7569, 39: 1521, 1: 1, 4: 16, 31: 961, 29: 841, 28: 784,
#          (45, 16, 37): 1369, 18: '324', '26': 676, 15: 225, 36: 1296, 22: 484, 27: 729, 47: 2209, 95: 9025, 32: 1024,
#          8.2: 6724, 2.3: 529, 7.5: 5625, 40: 1600, 84: 7056, 91: 8281, '43': 1849, 8.9: 79.21, 5: 25, 12: '144', 7: 49,
#          25: 625, 67: 4489, 94: 8836, 88: 7744, 93: 8649, '85': '7225', 90: 8100, 7.9: 6241, 24: 576, 81: 6561,
#          83: 6889, 2: 4, 34: 1156, 1.3: 169, '62': '3844', 9: 81, 14: 196, 7.3: 5.329, 63: [3969, 4096, 9604], 55: 3025,
#          44: 1936, 5.6: 3136, '74': 5476, 97: 9409, 46: 2116, 65: 4225, 92: 8464, 99: 9801, 38: 1444, 58: 3364, 0: 0,
#          59: 3481, 8: 64, 35: 1225, '57': '3249', 52: '2704', 19: 361, 76: 5776, 41: 1681, 72: 5184, 50: 2500, 61: 3721,
#          66: 4356, 17: 289, 60: 3600, 33: 1089, '86': 7396, '48': 2304, 10: 100, 54: 2916, '70': 4900, 69: 4761}
# data3 = ['a', 'c', 'c', [1, 2, '3'], 'f', (1, 2, 4, 5, 7), {'a', 'f', 'h', 1}]
#
# with open('data.pkl', 'wb') as file:
#     pickle.dump(data, file)
#
# with open('data2.pkl', 'wb') as file:
#     pickle.dump(data2, file)
#
# with open('data3.pkl', 'wb') as file:
#     pickle.dump(data3, file)

# import pickle
#
#
# p_f = input()
# c_s = int(input())
#
# with open(p_f, 'rb') as file:
#     data = pickle.load(file)
#     s = 0
#     if type(data) == list:
#         s = max(filter(lambda x: type(x) == int, data), default=0) * min(filter(lambda x: type(x) == int, data), default=0)
#     if type(data) == dict:
#         for i in data.keys():
#             if type(i) == int:
#                 s += i
#     elif len(data) == 0:
#         s = 0
#
# if c_s == s:
#     print('Контрольные суммы совпадают')
# else:
#     print('Контрольные суммы не совпадают')