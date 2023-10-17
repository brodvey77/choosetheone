# import json
#
# colors = ['black', 'white']
#
# colors_json = json.dumps(colors, indent='-> ')
#
# print(colors_json)
import csv
# import json
#
# weekdays = {i: day for i, day in enumerate(['Sunday', 'Monday', 'Tuesday'])}
#
# weekdays_json = json.dumps(weekdays, separators=('; ', '-'))
#
# print(weekdays_json)

# import json
#
# numbers = {2: 'two', 1: 'one', 4: 'four', 3: 'three'}
#
# numbers_json = json.dumps(numbers, sort_keys=True)
#
# print(numbers_json)


# import json
#
# data = {('Timur', 'Guev'): 'BEEGEEK', ('Roman', 'Belyh'): 'IQ-option'}
#
# data_json = json.dumps(data)
#
# print(data_json)

#
# import json
#
# data = {('Timur', 'Guev'): 'BEEGEEK', 'BEEGEEK': ('Arthur', 'Kharisov'), ('Roman', 'Belyh'): 'IQ-option'}
#
# data_json = json.dumps(data, skipkeys=True)
#
# print(data_json)


# import json

# countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
#              'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
#              'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
#              'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}

# countries_json = json.dumps(countries, indent='   ', sort_keys=True, separators=(', ', ' - '))

# print(countries_json)


# import json

# words = {
#          frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
#          "travel": "trævl",
#          ("hello", "world"): ("həˈləʊ", "wɜːld"),
#          "moonlight": "muːn.laɪt",
#          "sunshine": "ˈsʌn.ʃaɪn",
#          ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
#          "adventure": "ədˈventʃər",
#          "beautiful": "ˈbjuːtɪfl",
#          frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
#          "bicycle": "baisikl",
#          ("pilot", "fly"): ("pailət", "flai")
#         }


# data_json = json.dumps(words, skipkeys=True)



# import json

# club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
#          "trainer": "Julian Nagelsmann", "goalkeeper": "M. Neuer", "league_position": 1}

# club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
#          "trainer": "Xavier Creus", "goalkeeper": "M. Ter Stegen", "league_position": 7}

# club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
#          "trainer": "Michael Carrick", "goalkeeper": "D. De Gea", "league_position": 8}

# my_list = [club1, club2, club3]

# with open('data.json', 'w') as file:
#     json.dump(my_list, file, indent='   ')


# import json

# specs = {
#          'Модель': 'AMD Ryzen 5 5600G',
#          'Год релиза': 2021,
#          'Сокет': 'AM4',
#          'Техпроцесс': '7 нм',
#          'Ядро': 'Cezanne',
#          'Объем кэша L2': '3 МБ',
#          'Объем кэша L3': '16 МБ',
#          'Базовая частота': '3900 МГц'
#         }

# specs_json = json.dumps(specs, ensure_ascii=False, indent='   ')

# print(specs_json)



# import json
#
# def is_correct_json(string):
#         try:
#                 json.dumps(string)
#                 return True
#         except:
#                 return False
#
#
#
# a = input()
#
#
#
# print(is_correct_json(a))



# import  sys
# import json
#
# s = json.loads(sys.stdin.read())
#
# for k,v in s.items():
#     if isinstance(v, list):
#         print(f'{k}: {", ".join(map(str,v))}')
#     else:
#         print(f'{k}: {v}')


# import json
#
# def change_bool(b):
#     if b == True:
#         return False
#     else:
#         return True
#
# my_list = []
# with open('data.json', encoding='utf-8') as file:
#     data = json.load(file)
#     for i in data:
#         if isinstance(i, str):
#             my_list.append(i + "!")
#         elif type(i) == int or type(i) == float:
#             my_list.append(i + 1)
#         elif type(i) == bool:
#             my_list.append(change_bool(i))
#         elif isinstance(i, list):
#             my_list.append(i * 2)
#         elif type(i) == dict:
#             i.update({"newkey": None})
#             my_list.append(i)
#
# with open('updated_data.json', 'w', encoding='utf-8') as f:
#     json.dump(my_list, f, indent=3)



# import json
#
# opers = {'str': lambda x: x + '!',
#          'int': lambda x: x + 1,
#          'float': lambda x: x + 1,
#          'bool': lambda x: not x,
#          'list': lambda x: x * 2,
#          'dict': lambda x: x | {'newkey': None}}
#
# with open('data.json', encoding='utf8') as fi, open('updated_data.json', 'w', encoding='utf8') as fo:
# 	json.dump([opers[type(i).__name__](i) for i in json.load(fi) if type(i).__name__ in opers], fo, indent=3)



# import json
#
# my_list = []
# with open('data1.json', encoding='utf-8') as f1, open('data2.json', encoding='utf-8') as f2:
#     a = json.load(f1)
#     b = json.load(f2)
#     my_dict = a | b
#
#
# with open('data_merge.json', 'w', encoding='utf-8') as file:
#     json.dump(my_dict, file, indent=3)


# import json
#
# with open('people.json', encoding='utf-8') as file:
#     obj_json = json.load(file)
#     l = []
#     for i in obj_json:
#         for j in i:
#             if j not in l:
#                 l.append(j)
#     s = [{key: obj.get(key, None) for key in l} for obj in obj_json ]
#
# with open('updated_people.json', 'w', encoding='utf-8') as f:
#     json.dump(s, f, indent=3)

# import json
#
#
# with open('people.json', encoding='utf-8') as js:
#     content = json.load(js)
#
# keys = set()
# for data in content:
#     keys |= data.keys()
#
# for data in content:
#     data |= dict.fromkeys(keys - data.keys())
#
# with open('updated_people.json', 'w') as js:
#     json.dump(content, js, indent=3)




# import json
#
# my_dict = {}
# with open('countries.json', encoding='utf-8') as file:
#     data = json.load(file)
#     for i in data:
#         my_dict.setdefault(i['religion'], []).append(i['country'])
#
#
# with open('religion.json', 'w', encoding='utf-8') as fr:
#     json.dump(my_dict, fr, indent=3)




# import json
#
# with open("countries.json") as file_in, open("religion.json", "w") as file_out:
#
#     d = {}
#     datas = json.load(file_in)
#     for data in datas:
#         d[data['religion']] = d.get(data['religion'], []) + [data['country']]
#
#     json.dump(d, file_out)



# import pandas as pd
# import json
#
# # Load the CSV file into a pandas DataFrame
# df = pd.read_csv('playgrounds.csv', delimiter=';', encoding='utf-8')
#
# # Create an empty dictionary to store the results
# results = {}
#
# # Loop over each row in the DataFrame
# for index, row in df.iterrows():
#     # Extract the administrative area and district from the row
#     adm_area = row['AdmArea']
#     district = row['District']
#     address = row['Address']
#
#     # Check if the administrative area is already in the results dictionary
#     if adm_area not in results:
#         # If not, add it with an empty dictionary as the value
#         results[adm_area] = {}
#
#     # Check if the district is already in the administrative area's dictionary
#     if district not in results[adm_area]:
#         # If not, add it with an empty list as the value
#         results[adm_area][district] = []
#
#     # Add the address to the district's list of addresses
#     results[adm_area][district].append(address)
#
# # Write the results to a JSON file
# with open('addresses.json', 'w', encoding='utf-8') as f:
#     json.dump(results, f, ensure_ascii=False, indent=3)


# import json
# import csv
# with open('playgrounds.csv', encoding='utf-8') as file:
#     s = list(csv.reader(file, delimiter=';'))
#
# my_dict = {}
# for i in s[1:]:
#     my_dict.setdefault(i[1], {}).setdefault(i[2], []).append(i[3])
#
#
# with open('addresses.json', 'w', encoding='utf-8') as f:
#     json.dump(my_dict, f, ensure_ascii=False, indent=3)


# import json, csv
#
# with open('playgrounds.csv', encoding='utf-8') as fin, \
#     open('addresses.json', 'w', encoding='utf-8') as fout:
#     pgs = list(csv.reader(fin, delimiter=';'))[1:]
#
#     districts = {}
#     for name, area, district, addr in pgs:
#         districts.setdefault(area, {}).setdefault(district,[]).append(addr)
#
#     json.dump(districts, fout, indent=3, ensure_ascii=False)

#
#
# import json
# import csv
#
# d = {}
# my_list = []
# with open('students.json', encoding='utf-8') as file:
#     data = json.load(file)
#     for i in data:
#         if i['age'] >= 18 and i['progress'] >= 75:
#             d[i['name']] = i.setdefault('phone')
#
#
#
# with open('data.csv', 'w', encoding='utf-8', newline='') as f:
#     writer = csv.writer(f, delimiter=',')
#     writer.writerow(('name', 'phone'))
#     for k, v in sorted(d.items()):
#         writer.writerow((k, v))


# import  json
# import datetime
# from datetime import datetime
#
# my_list = []
#
# with open('pools.json', encoding='utf-8') as file:
#     d = json.load(file)
#     for i in d:
#         time_data = (i['WorkingHoursSummer']['Понедельник']).split('-')
#         if datetime.strptime(time_data[0], '%H:%M') <= datetime.strptime('10:00', '%H:%M') and \
#             datetime.strptime(time_data[1], '%H:%M') >= datetime.strptime('12:00', '%H:%M'):
#             my_list.append(i)
#         else:
#             continue
#
#     f_l = sorted(sorted(my_list, key=lambda x: x["DimensionsSummer"]['Width']), key=lambda x: x["DimensionsSummer"]['Length'])[-1]
#
#     print(f"{f_l['DimensionsSummer']['Length']}x{f_l['DimensionsSummer']['Width']}\n{f_l['Address']}")

