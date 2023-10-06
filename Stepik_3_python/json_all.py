# import json
#
# colors = ['black', 'white']
#
# colors_json = json.dumps(colors, indent='-> ')
#
# print(colors_json)


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


import json

words = {
         frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
         "travel": "trævl",
         ("hello", "world"): ("həˈləʊ", "wɜːld"),
         "moonlight": "muːn.laɪt",
         "sunshine": "ˈsʌn.ʃaɪn",
         ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
         "adventure": "ədˈventʃər",
         "beautiful": "ˈbjuːtɪfl",
         frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
         "bicycle": "baisikl",
         ("pilot", "fly"): ("pailət", "flai")
        }


data_json = json.dumps(words, skipkeys=True)
print(data_json)