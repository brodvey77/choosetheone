
def print_file_content(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print('Файл не найден')



class HandlerFileNotFoundError:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            return self.func(*args, **kwargs)
        except:
            print("Файл не найден")


@HandlerFileNotFoundError
def print_file_content(filename):
    with open(filename, encoding="utf-8") as f1:
        print(f1.read())



