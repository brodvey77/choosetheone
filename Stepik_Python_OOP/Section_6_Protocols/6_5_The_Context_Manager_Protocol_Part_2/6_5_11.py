
class WriteSpy:
    def __init__(self, file1, file2, to_close=False):
        self.file1 = file1
        self.file2 = file2
        self.to_close = to_close

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.to_close:
            self.close()

    def close(self):
        self.file1.close()
        self.file2.close()

    def writable(self):
        try:
            w1 = self.file1.writable()
        except Exception:
            return False
        try:
            w2 = self.file2.writable()
        except Exception:
            return False
        return w1 and w2

    def closed(self):
        return self.file1.closed and self.file2.closed

    def write(self, text):
        if not self.writable():
            raise ValueError("Файл закрыт или недоступен для записи")
        self.file1.write(text)
        self.file2.write(text)



f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')
f1.close()

try:
    with WriteSpy(f1, f2, to_close=True) as combined:
        combined.write('No cost too great')
except ValueError as error:
    print(error)