import pandas as pd
import openpyxl

# Загрузка данных из файла Excel
df = pd.read_excel('datasheet_chemical.xlsx')

# Преобразование данных в словарь
dictionary = df.to_dict()

# Вывод словаря
for k,v in dictionary.items():
    print(k, v)