# sentence = 'In the face of ambiguity refuse the temptation to guess'
#
# filter_iterator = filter(lambda word: len(word) > 4, sentence.split())   # фильтруем
# map_iterator = map(lambda word: word.upper(), filter_iterator)           # преобразовываем
# enumerate_iterator = enumerate(map_iterator, 1)                          # нумеруем
#
# for index, value in enumerate_iterator:                                  # выводим
#     print(f'{index}. {value}')