
class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode


    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, hexcode):
        self._hexcode = hexcode
        self.r = int(hexcode[0:2], 16)
        self.g = int(hexcode[2:4], 16)
        self.b = int(hexcode[4:], 16)






# INPUT DATA:

# TEST_1:
print('test1')
color = Color('0000FF')

print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

print('---------------------------------------------------------')

# TEST_2:
print('test2')
color = Color('0000FF')

color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

print('---------------------------------------------------------')
# TEST_3:
print('test3')
color = Color('0000FF')

print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

print()

color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

print('---------------------------------------------------------')
# TEST_4:
print('test4')
hexcodes = ['FC5A5E', '13AABE', '851149', 'AAAAAA', 'FFFFFF', 'B6A1D8', 'ABCDEF', 'FEDCBA', '123456', '999999']
count = 1
for hc in hexcodes:
    color = Color(hc)
    print(f'Цвет № {count}')
    print(color.hexcode)
    print(color.r, color.g, color.b, sep='\n')
    print()
    count += 1