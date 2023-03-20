print('Это основной файл main.py, его имя в процессе выполнения программы:', __name__)

import Pack_1
import Pack_2
from Pack_2 import pack_21

print(dir())
print(dir(Pack_1))
print(dir(Pack_2))
print(dir(pack_21))