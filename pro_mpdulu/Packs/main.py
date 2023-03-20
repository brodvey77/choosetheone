print('Это основной файл main.py, его имя в процессе выполнения программы:', __name__)

import pack_1
import pack_2
from pack_2 import pack_21

print(dir())
print(dir(pack_1))
print(dir(pack_2))
print(dir(pack_21))