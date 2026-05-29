import os

with os.scandir('.') as enries:
    for entry in enries:
        print(entry.name, '--->', entry.stat().st_size, 'bytes')



from tempfile import TemporaryFile

with TemporaryFile(mode='r+') as file:
    file.write('Python generation!')
    file.seek(0)
    content = file.read()
    print(content)