
class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r', encoding='utf-8')
        return (i.strip('\n') for i in self.file.readlines())


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()



with open('poem.txt', 'w', encoding='utf-8') as file:
    print('Я кашлянул в звенящей тишине,', file=file)
    print('И от шального эха стало жутко…', file=file)
    print('Расскажет ли утятам обо мне', file=file)
    print('под утро мной испуганная утка?', file=file)

with ReadableTextFile('poem.txt') as file:
    for line in file:
        print(line)


class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.obj = open(self.filename, 'r', encoding='utf-8')
        return (line.strip() for line in self.obj)

    def __exit__(self, *exc_info):
        self.obj.close()