

# print(1, 2, 3, sep=":", end=' ')
# print(1, 2, 3, sep=",")

# loren = open('/home/choosetheone/Documents/[infobiza.net] 1.2 sample.txt', 'r')
# for line in loren:
#     print(line, end='')
# loren.close()

# loren = open('/home/choosetheone/Documents/[infobiza.net] 1.2 sample.txt', 'r')
# for line in loren:
#     if 'let' in line.lower():
#         print(line, end='')
# loren.close()

# with open('/home/choosetheone/Documents/[infobiza.net] 1.2 sample.txt', 'r') as loren:
#     for line in loren:
#         if 'let' in line.lower():
#             print(line, end='')

# with open('/home/choosetheone/Documents/[infobiza.net] 1.2 sample.txt', 'r') as loren:
#     line = loren.readline()
#     while line:
#         print(line, end='')
#         line = loren.readline()

# with open('/home/choosetheone/Documents/[infobiza.net] 1.2 sample.txt', 'r') as loren:
#     lines = loren.readlines()
# print(lines)
#
# for line in lines[::-1]:
#     print(line)

# with open('/home/choosetheone/Documents/[infobiza.net] 1.2 sample.txt', 'r') as loren:
#     text = loren.read()
# print(text)

# color_list = ['red', 'orange', 'yellow', 'green', 'blue',
#               'indigo', 'violet', 'dark green']
# with open('/home/choosetheone/Documents/sample.txt', 'w') as rainbow_colors:
#     for color in color_list:
#         print(color, file=rainbow_colors)

colors_list = []
with open('/home/choosetheone/Documents/sample.txt', 'r') as rainbow_colors:
    for color in rainbow_colors:
        colors_list.append(color.strip('\n'))

print(colors_list)

with open('/home/choosetheone/Documents/sample.txt', 'a') as rainbow_colors:
    print('dark black', file=rainbow_colors)
    print('dark red', file=rainbow_colors)







