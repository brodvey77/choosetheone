word = 'bottles'
for beer_num in range(99, 0, -1):
    print(beer_num, word)
    print('take one down')
    print('pass it around')
    if beer_num == 1:
        print('no more bottles of beer')
    else:
        beer_num -= 1
        if beer_num == 1:
            word = 'bottle'
        print(beer_num, word, 'of beer' )

